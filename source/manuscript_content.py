"""Integrated language map for the ICCEIC Adap manuscript.

Scientific details are drawn from the frozen Adap evidence and the
already-audited manuscript source.
"""

from __future__ import annotations

from work.paper_content import BODY as VERIFIED_BODY


TITLE = "Failure-Complete Evaluation of Semantic Rescue in Few-Shot Tabular Self-Training"

ABSTRACT = (
    "Semantic representations can provide side information for few-shot tabular learning, "
    "but an adaptive rescue route is useful only when it improves the downstream predictor "
    "under a fair information boundary. We test whether strictly out-of-fold semantic evidence "
    "can rescue unlabeled rows rejected by a matched tree self-training system without using "
    "candidate or evaluation labels. ProtoOOF-Tree-v1 forms leave-one-pair-out class prototypes "
    "from a fixed T0-3B representation, makes every activation decision from labeled support "
    "alone, and otherwise returns the tree endpoint exactly. The frozen kill-screen covers two "
    "OpenML datasets, three shot counts, and three seeds: 18 episodes and 72 ordered method "
    "rows spanning the tree anchor, semantic route, no-semantics control, and row-permuted "
    "control. The semantic route matches the tree in all 18 episodes, so the overall paired "
    "ROC-AUC difference is +0.0000000. Mean separation from the no-semantics and permuted "
    "controls is +0.0009668 and -0.0005258, respectively, both below the registered +0.0100 "
    "threshold. The main route records 0 gate acceptances and 0 rescued rows; the two controls "
    "record 1/50 and 2/100. Five of ten promotion conditions fail, and the frozen decision is "
    "NO_GO. The result bounds this particular leakage-controlled gate and transfer path; it "
    "does not establish that semantic tabular learning is generally ineffective."
)

KEYWORDS = (
    "adaptive decision-making, few-shot tabular learning, self-training, semantic "
    "representations, reliable artificial intelligence, negative results, data mining"
)


def verified(index: int) -> str:
    item = VERIFIED_BODY[index]
    if item.get("type") not in {"p", "equation"}:
        raise ValueError(f"verified item {index} is not prose")
    return item["text"]


SECTIONS = [
    (
        "I. INTRODUCTION",
        [
            (
                "Few-shot tabular classification combines scarce labels with heterogeneous "
                "features. Tree ensembles remain difficult to displace under controlled tabular "
                "comparisons [1], [2], while language-model approaches use feature names, values, "
                "or row serializations as prior information [3]-[6]. The engineering question is "
                "therefore additive rather than cosmetic: does a semantic path improve the final "
                "tree, or does it merely produce plausible scores and an active-looking module?"
            ),
            (
                "Self-training can enlarge a small labeled support set, but feedback can also "
                "reinforce early mistakes [7]. Confidence selection couples pseudo-label quality "
                "with coverage [8]. A semantic rescue can appear successful because it contributes "
                "useful information, repeats the tree ordering in another space, or follows an "
                "unfair information path. We therefore require support-only gating, matched "
                "controls, an immutable tree anchor, and retention of every registered episode."
            ),
            (
                "We ask three questions. RQ1 asks whether the semantic route improves mean ROC-AUC "
                "over the matched tree. RQ2 asks whether it separates from feature-only and "
                "row-permuted controls. RQ3 asks whether it passes a registered reliability gate. "
                "The decision is conjunctive: an attractive intermediate score, one favorable "
                "episode, or exact no-harm fallback cannot substitute for downstream improvement."
            ),
            verified(4),
            (
                "The contribution is an evaluation contract rather than a claim that a single "
                "component is novel in isolation. The contract links an incremental endpoint "
                "estimand, out-of-fold evidence, two semantic-dependence controls, exact fallback, "
                "and a failure-complete stop rule. Its practical value is to make a negative "
                "development decision reproducible before a larger confirmation consumes more "
                "data, computation, or interpretation."
            ),
            (
                "The answer in the frozen study is negative. ProtoOOF-Tree-v1 never activates "
                "rescue and exactly matches TreeSelfTrain-S in all 18 episodes. The result is not "
                "presented as statistical equivalence or as a general rejection of semantic "
                "representations. It is evidence that this particular representation, gate, and "
                "transfer rule should not be promoted under the registered criteria."
            ),
        ],
    ),
    (
        "II. RELATED WORK",
        [
            (
                "Strong tabular baselines and priors. XGBoost established a scalable regularized "
                "boosting framework [1]. Tabular foundation models take a different route: TabPFN "
                "and TabICL learn priors for in-context prediction [9], [10]. These lines of work "
                "motivate both a competitive tree anchor and disciplined accounting of what "
                "information an auxiliary route receives."
            ),
            (
                "Language-derived tabular information. TabLLM serializes rows for language-model "
                "prediction [3]; TransTab learns representations transferable across tables [4]; "
                "and FeatLLM converts language-model rules into features for a simpler learner [5]. "
                "T0 supplies the fixed multitask-prompted representation used here [6]. Our claim "
                "is narrower: any auxiliary semantics must be evaluated at the final deployed "
                "endpoint with matched information access."
            ),
            (
                "Selection and negative tests. Classic pseudo-labeling uses model predictions as "
                "training targets [7], whereas later work treats confidence thresholds as explicit "
                "coverage-error decisions [8]. VIME shows how semi-supervised assumptions must suit "
                "heterogeneous tabular data [11]. These results motivate support-only selection, "
                "but they do not remove the need to test whether semantic content is responsible "
                "for an observed change."
            ),
            (
                "Broader benchmark evidence reinforces this caution. Tree-based models remain "
                "strong on many typical tables [12], and LightGBM and CatBoost embody distinct "
                "inductive and systems choices [13], [14]. FixMatch illustrates how confidence "
                "controls data inclusion in semi-supervised learning [15]. The common lesson is "
                "that a selection mechanism must be judged through its final learner, not through "
                "confidence or activity alone."
            ),
        ],
    ),
    (
        "III. METHOD AND FAIR INFORMATION PROTOCOL",
        [
            (
                "Episode and endpoint. Each registered episode is a (dataset, shot, seed) triple. "
                "The binary datasets are OpenML credit-g (ID 31) and spambase (ID 44); shots are "
                "5, 10, and 20, and seeds are 0, 9, and 19. TreeSelfTrain-S is the fixed anchor. "
                "All four routes share labeled support, candidate pool, evaluation set, "
                "preprocessing, split, and ROC-AUC endpoint."
            ),
            verified(34),
            (
                "Feature-only semantic representation. Every row is serialized without a label "
                "token, label name, metric, or downstream result and embedded with one sealed "
                "T0-3B revision. The semantic cache is fixed before the report is opened. Main and "
                "control routes share the episode split, support pairs, cache identity, and "
                "numerical pipeline; the study does not adapt prompts after seeing outcomes."
            ),
            (
                "Out-of-fold prototype evidence. Support examples are paired across the two "
                "classes. For each held-out pair, the remaining support representations define two "
                "class prototypes. Relative similarity supplies a signed score for the held-out "
                "row. Repeating this operation gives one semantic score per support row without "
                "allowing that row to define the prototypes used to score it."
            ),
            verified(40),
            (
                "Exact fallback. If the gate rejects, the eligible rescue set is empty, or a "
                "registered numerical failure occurs, the route cannot be relabeled as a success. "
                "With no accepted rescue, every training row, target, reliability weight, ordering "
                "decision, and final prediction must match TreeSelfTrain-S exactly. Alpha zero is "
                "checked separately. This is an implementation-safety invariant, not evidence of "
                "accuracy."
            ),
            verified(44),
            (
                "The primary estimand is the paired episode difference AUC(Main) - AUC(Tree). "
                "Because methods share the same split and seed, this quantity isolates the "
                "incremental endpoint effect of the complete rescue route. It is averaged across "
                "all 18 episodes. No success-only denominator, best seed, or complete-case filter "
                "is permitted."
            ),
        ],
    ),
    (
        "IV. FROZEN EXPERIMENTAL PROTOCOL",
        [
            verified(51),
            verified(52),
            (
                "Fairness is defined by common episode identity and a bounded method-only "
                "difference. All routes share support and candidate pools, final tree family, "
                "metric, row-order contract, and failure policy. ProtoOOF variants also share fold "
                "construction, support-only gate, threshold rule, and numerical pipeline. Only the "
                "representation or control transformation changes."
            ),
            verified(59),
            verified(64),
            verified(65),
            verified(69),
            verified(70),
            (
                "The hashes recorded in the evidence manifest identify the exact report, method "
                "ledger, episode-difference ledger, and summary used for this paper. Hashing does "
                "not prove that every scientific design choice is correct, but it prevents a "
                "different result file from being substituted after interpretation. The complete "
                "18-episode ledger is therefore reproduced in Table II rather than summarized by "
                "a favorable subset."
            ),
        ],
    ),
    (
        "V. FROZEN RESULTS",
        [
            (
                "RQ1 - endpoint. ProtoOOF-Tree-v1 matches TreeSelfTrain-S in every registered "
                "episode. The overall main-minus-tree mean is +0.0000000; credit-g and spambase "
                "each have mean and median 0.0000; and the number of shot levels with a positive "
                "mean is 0. Main records 0 gate acceptances and 0 rescued rows, so exact fallback "
                "explains the deterministic endpoint equality."
            ),
            (
                "RQ2 - controls. Mean Main-NoSemantics is +0.0009668, whereas mean "
                "Main-Permuted is -0.0005258. Neither reaches the registered +0.0100 separation, "
                "and the latter has the wrong sign. NoSemantics records 1 accepted gate and 50 "
                "rescued rows; Permuted records 2 and 100. Activity in these controls does not "
                "establish semantic benefit."
            ),
            verified(82),
            (
                "RQ3 - decision. Five of ten conjuncts fail: overall_main_delta_min, "
                "main_minus_no_semantics_min, main_minus_permuted_min, "
                "positive_shot_means_min_count, and rescue_required_both_datasets. All 72 method "
                "rows execute successfully, no pseudo-label collapse occurs, and exact fallback "
                "passes. Because all conditions are required, the frozen verdict remains NO_GO."
            ),
            verified(83),
            verified(85),
        ],
    ),
    (
        "VI. FAILURE ANALYSIS AND DECISION VALUE",
        [
            (
                "The directly observed boundary is narrow. The main semantic comparison never "
                "satisfies its activation rule; exact fallback leaves the tree unchanged; and "
                "matched controls activate in three low-shot episodes without establishing the "
                "intended semantic alignment. These observations locate the failure within the "
                "tested path from representation through support evidence to candidate rescue."
            ),
            (
                "Several explanations remain plausible but unverified. Leave-one-pair-out support "
                "evidence may be too variable at 5, 10, or 20 shots. The support-derived threshold "
                "may be conservative when semantic margins are compressed. The fixed T0-3B "
                "geometry may encode broad feature meaning without aligning with the tree error "
                "set. Because Main never activates, this study cannot distinguish these mechanisms."
            ),
            verified(92),
            (
                "Negative evidence is useful when it changes a decision. Counting only accepted "
                "gates could have turned the three control activations into an apparently active "
                "method. Reporting only no-harm could have described 18 exact fallbacks as a "
                "successful semantic augmentation. Neither statement answers whether semantics "
                "improved the endpoint. The registered rule prevents both interpretations."
            ),
            verified(95),
            verified(102),
        ],
    ),
    (
        "VII. LIMITATIONS AND THREATS TO VALIDITY",
        [
            verified(105),
            verified(106),
            verified(107),
            (
                "This is a development kill-screen, not an independent confirmation. Changing "
                "thresholds, datasets, seeds, failure treatment, serialization, model revision, "
                "or estimand creates a new study. The current zero effects arise from exact "
                "fallback, not from a sampled distribution of small nonzero effects; no p-value, "
                "significance test, or equivalence margin is added after seeing the outcomes."
            ),
            verified(109),
        ],
    ),
    (
        "VIII. REPRODUCIBILITY AND FALSIFICATION",
        [
            (
                "The evidence contract fixes two OpenML identifiers, three shot counts, three "
                "seeds, four ordered routes, and all failure semantics before interpretation. A "
                "reproduction begins from the registered split and fixed representation cache, "
                "runs TreeSelfTrain-S, Main, NoSemantics, and Permuted for each episode, and records "
                "ROC-AUC together with gate and rescue activity."
            ),
            verified(111),
            verified(113),
            (
                "A new study may challenge this boundary, but it should be frozen independently. "
                "It must specify a replacement representation or gate, distribution-shift model, "
                "datasets, shots, seeds, controls, thresholds, and failure treatment before opening "
                "outcomes. A new GO requires stable rescue coverage, dependence on semantic content "
                "under matched controls, and a positive final-tree effect across datasets and shot "
                "levels."
            ),
        ],
    ),
]

FALSIFICATION_ROWS = (
    ("Support gate is underpowered", "Pre-registered stronger support evidence activates stably on both datasets without label access"),
    ("Semantic geometry misses tree errors", "A frozen alternative representation separates from both controls and improves the tree"),
    ("Transfer is the bottleneck", "Accepted rescues are accurate and yield positive paired endpoint effects under the same anchor"),
    ("Effect is distribution-specific", "A preselected broader grid passes dataset and shot consistency conditions"),
)

CONCLUSION = (
    "A failure-complete evaluation prevents mechanism activity from being confused with predictive "
    "value. ProtoOOF-Tree-v1 is leakage-controlled and falls back exactly, but it supplies no "
    "final-tree gain and no registered control separation in the frozen study. The decision is "
    "therefore NO_GO. Exact fallback is a safety property; only a reproducible endpoint improvement "
    "under matched controls can justify deployment. The result retains a narrow interpretation: it "
    "rejects this gate-and-transfer route while leaving other semantic representations and adaptive "
    "designs open to independently frozen tests."
)

AI_DISCLOSURE = (
    "AI Tool Use Disclosure - External language editing and OpenAI Codex (GPT-5 family, accessed "
    "September 2026) assisted with English phrasing, formatting, and consistency checks. These "
    "tools did not generate or alter experimental data. The author retained and verified the "
    "research design, code, frozen results, references, and interpretations."
)
