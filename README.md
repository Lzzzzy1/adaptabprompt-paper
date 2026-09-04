# AdapTabPrompt ICCEIC 2026 Manuscript Archive

Private, self-contained archive for the AdapTabPrompt manuscript **“Failure-Complete Evaluation of Semantic Rescue in Few-Shot Tabular Self-Training.”** The repository preserves the audited ICCEIC 2026 candidate manuscripts, the frozen evidence used by their tables, and the source and verification code needed to reconstruct and check the DOCX files.

## Scientific status

The registered result is **NO_GO**, not a claimed performance improvement:

- 2 datasets (`credit-g`, `spambase`) × 3 shot levels (5, 10, 20) × 3 seeds (0, 9, 19) = **18 registered episodes**.
- Four method records per episode = **72 ordered method rows**, with **0 failed rows**.
- ProtoOOF-Tree-v1 and the tree anchor are identical in all 18 episodes; the overall Main-minus-Tree effect is **+0.0000000**.
- The matched control differences are Main-minus-NoSemantics **+0.0009668** and Main-minus-Permuted **-0.0005258**.
- Five of ten registered decision conditions fail, so the frozen verdict remains **NO_GO**.

The result establishes a reproducible boundary for this particular gate-and-transfer mechanism. It does not establish that semantic rescue is generally ineffective, and it must not be presented as an AP or accuracy gain.

## Manuscripts

- `manuscript/AdapTabPrompt_ICCEIC2026_Final_Anonymous.docx`
- `manuscript/AdapTabPrompt_ICCEIC2026_Final_Anonymous.pdf`
- `manuscript/AdapTabPrompt_ICCEIC2026_Final_Author_Copy.docx`
- `manuscript/AdapTabPrompt_ICCEIC2026_Final_Author_Copy.pdf`

Use the anonymous pair only when the receiving venue requests an anonymous review manuscript. The author pair is a named archival or camera-ready backup. Both pairs contain the same scientific content, tables, conclusions, and 15 references; only identity-bearing material differs.

## Repository map

- `manuscript/` — audited final candidate DOCX and PDF pairs.
- `source/evidence/` — frozen `report.json` and CSV ledgers that drive the numerical tables.
- `source/work/` — frozen scientific text, references, and evidence-contract code.
- `source/manuscript_content.py` — integrated manuscript prose and the authoritative Table IV wording.
- `source/build_manuscript.py` — portable DOCX generator; output goes to ignored `build/`.
- `source/audit_candidates.py` — structural, identity, table, citation, and frozen-data verifier.
- `source/template/` and `source/assets/` — retained conference template and pipeline figure.
- `audit/` — independent final audit in human- and machine-readable form.
- `MANIFEST.sha256` — SHA-256 inventory for every tracked archive payload except the manifest itself.

## Reproduce and verify

Python 3.12 was used for the archived run.

```powershell
python -m pip install -r source/requirements.txt
python source/work/paper_data.py
python source/audit_candidates.py --final --summary
python source/build_manuscript.py
```

The build command regenerates the anonymous and author DOCX files under `build/`; it does not overwrite the audited copies. PDF export requires a compatible Microsoft Word or LibreOffice installation and can introduce renderer-dependent pagination, so the audited PDFs are retained separately. `source/render_pdf_pages.py` can rasterize a PDF for visual comparison.

The private external editing source is intentionally excluded. Its accepted wording has already been frozen in `source/manuscript_content.py`; no external source file, editing report, chat attachment, local absolute path, or credential is required to run the archived build and checks.

## Scope and non-claims

This repository is an independent AdapTabPrompt archive and does not depend on any other manuscript or model repository. It is **not** evidence that the paper has been submitted, accepted, published, or indexed by ICCEIC, IEEE, EI Compendex, Scopus, or any other venue.

See `audit/Final_Independent_Audit.md` for the completed six-page layout and integrity review. Verify all payloads against `MANIFEST.sha256` before reuse.
