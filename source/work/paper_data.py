"""Frozen evidence contract for the Adap manuscript archive.

This module reads only the repository's frozen evidence snapshot. All
manuscript numbers must flow through this module.
"""

from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean, median


HERE = Path(__file__).resolve().parent
EVIDENCE_DIR = HERE.parent / "evidence"
REPORT_PATH = EVIDENCE_DIR / "report.json"
METHOD_ROWS_PATH = EVIDENCE_DIR / "method_rows.csv"
EPISODE_DIFFS_PATH = EVIDENCE_DIR / "episode_differences.csv"
SUMMARY_PATH = EVIDENCE_DIR / "summary.csv"

EXPECTED_METHODS = (
    "TreeSelfTrain-S",
    "ProtoOOF-Tree-v1",
    "ProtoOOF-NoSemantics",
    "ProtoOOF-Permuted",
)
EXPECTED_DATASETS = {"credit-g", "spambase"}
EXPECTED_SHOTS = {5, 10, 20}
EXPECTED_SEEDS = {0, 9, 19}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_report() -> dict:
    return json.loads(REPORT_PATH.read_text(encoding="utf-8"))


def load_method_rows() -> list[dict]:
    with METHOD_ROWS_PATH.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    for row in rows:
        row["shot"] = int(row["shot"])
        row["seed"] = int(row["seed"])
        row["roc_auc"] = float(row["roc_auc"])
        row["gate_accepted"] = int(row["gate_accepted"])
        row["rescued_count"] = int(row["rescued_count"])
        row["pseudo_label_collapse"] = int(row["pseudo_label_collapse"])
        row["exact_tree_fallback"] = row["exact_tree_fallback"].lower() == "true"
    return rows


def load_episode_differences() -> list[dict]:
    with EPISODE_DIFFS_PATH.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    for row in rows:
        row["shot"] = int(row["shot"])
        row["seed"] = int(row["seed"])
        for key in (
            "main_minus_tree",
            "main_minus_no_semantics",
            "main_minus_permuted",
        ):
            row[key] = float(row[key])
    return rows


def validate_contract() -> dict:
    report = load_report()
    method_rows = load_method_rows()
    episode_rows = load_episode_differences()

    assert report["schema"] == "proto-oof-tree-v1-development-report-v1"
    assert report["verdict"] == "NO_GO"
    assert report["episode_count"] == 18
    assert report["method_row_count"] == 72
    assert report["failure_row_count"] == 0
    assert len(method_rows) == 72
    assert len(episode_rows) == 18

    episodes = {
        (row["dataset"], row["shot"], row["seed"]) for row in method_rows
    }
    expected_episodes = {
        (dataset, shot, seed)
        for dataset in EXPECTED_DATASETS
        for shot in EXPECTED_SHOTS
        for seed in EXPECTED_SEEDS
    }
    assert episodes == expected_episodes

    method_counts = Counter(
        (row["dataset"], row["shot"], row["seed"]) for row in method_rows
    )
    assert set(method_counts.values()) == {4}
    assert {row["method"] for row in method_rows} == set(EXPECTED_METHODS)
    assert all(row["status"] == "success" for row in method_rows)
    assert all(row["pseudo_label_collapse"] == 0 for row in method_rows)
    assert all(row["exact_tree_fallback"] for row in method_rows)
    assert all(row["main_minus_tree"] == 0.0 for row in episode_rows)

    grouped: dict[tuple[str, int, int], dict[str, float]] = defaultdict(dict)
    for row in method_rows:
        key = (row["dataset"], row["shot"], row["seed"])
        grouped[key][row["method"]] = row["roc_auc"]
    for values in grouped.values():
        assert values["ProtoOOF-Tree-v1"] == values["TreeSelfTrain-S"]

    main_tree = [row["main_minus_tree"] for row in episode_rows]
    no_semantics = [row["main_minus_no_semantics"] for row in episode_rows]
    permuted = [row["main_minus_permuted"] for row in episode_rows]
    assert mean(main_tree) == report["statistics"]["overall_main_minus_tree_mean"]
    assert abs(mean(no_semantics) - report["statistics"]["main_minus_no_semantics_mean"]) < 1e-15
    assert abs(mean(permuted) - report["statistics"]["main_minus_permuted_mean"]) < 1e-15

    for dataset in EXPECTED_DATASETS:
        values = [
            row["main_minus_tree"]
            for row in episode_rows
            if row["dataset"] == dataset
        ]
        assert mean(values) == 0.0
        assert median(values) == 0.0

    shot_means = {
        shot: mean(
            row["main_minus_tree"]
            for row in episode_rows
            if row["shot"] == shot
        )
        for shot in EXPECTED_SHOTS
    }
    assert sum(value > 0 for value in shot_means.values()) == 0

    return {
        "report": report,
        "method_rows": method_rows,
        "episode_differences": episode_rows,
        "shot_means": shot_means,
        "source_hashes": {
            path.name: sha256(path)
            for path in (REPORT_PATH, METHOD_ROWS_PATH, EPISODE_DIFFS_PATH, SUMMARY_PATH)
        },
    }


if __name__ == "__main__":
    validated = validate_contract()
    print(
        json.dumps(
            {
                "verdict": validated["report"]["verdict"],
                "episodes": len(validated["episode_differences"]),
                "rows": len(validated["method_rows"]),
                "source_hashes": validated["source_hashes"],
            },
            indent=2,
        )
    )
