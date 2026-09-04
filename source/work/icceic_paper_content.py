"""ICCEIC 2026 manuscript content built around the frozen NO_GO evidence."""

from __future__ import annotations


TITLE = "Failure-Complete Evaluation of Semantic Rescue in Few-Shot Tabular Self-Training"

ABSTRACT = (
    "Semantic representations can provide side information for few-shot tabular learning, "
    "but an adaptive rescue mechanism is useful only if the signal improves its deployed "
    "predictor under a fair information boundary. We test whether strictly out-of-fold "
    "semantic evidence can rescue unlabeled rows rejected by a matched tree self-training "
    "system without using candidate or evaluation labels. ProtoOOF-Tree-v1 constructs "
    "leave-one-pair-out class prototypes from a fixed T0-3B representation, activates "
    "rescue through support-only evidence, and otherwise returns the tree endpoint exactly. "
    "A frozen kill-screen covers two OpenML datasets, three shot counts, and three seeds: "
    "18 episodes and 72 ordered method rows for the tree anchor, semantic route, no-semantics "
    "control, and row-permuted control. The main route equals the tree in all 18 episodes; "
    "the overall paired ROC-AUC difference, both dataset means and medians, and every shot "
    "mean are 0.0000. Mean separation from no-semantics and permuted controls is +0.0010 and "
    "-0.0005, below registered thresholds. The frozen decision is NO_GO. The result bounds "
    "this leakage-controlled gate and transfer path rather than semantic tabular learning in "
    "general, and shows why safe fallback must not be reported as predictive benefit."
)

KEYWORDS = (
    "adaptive decision-making, few-shot tabular learning, self-training, semantic "
    "representations, reliable artificial intelligence, negative results, data mining"
)


INTRO = [
    (
        "Few-shot tabular classification combines scarce labels with heterogeneous features. "
        "Tree ensembles remain difficult baselines to displace [1], [2], whereas language-model "
        "approaches use names, values, or row serializations as prior knowledge [3]-[6]. The "
        "engineering question is therefore incremental: does a semantic route change the final "
        "tree, not merely produce an active representation or plausible score? This distinction "
        "matters for an adaptive controller that must either append pseudo-labels or fall back "
        "safely under distribution shift."
    ),
    (
        "Pseudo-labeling can enlarge a small support set, but feedback can reinforce error [7]. "
        "Confidence selection also couples label quality and coverage [8]. A semantic rescue may "
        "appear useful because it adds information, repeats the tree ordering, or exploits an "
        "unfair information path. We therefore require support-only gating, matched controls, an "
        "immutable tree anchor, and retention of every failed episode. Related tabular foundation "
        "models [9], [10], semi-supervised tabular learning [11], and strong boosted-tree evidence "
        "[12]-[14] motivate these controls; FixMatch illustrates why confidence alone is not an "
        "endpoint claim [15]."
    ),
    (
        "We ask: (RQ1) does the semantic route improve mean ROC-AUC over the matched tree; (RQ2) "
        "does it separate from feature-only and permuted controls; and (RQ3) does it satisfy a "
        "registered reliability gate? The contributions are a leakage-controlled adaptive rescue "
        "contract, semantic-dependence controls, an exact-fallback invariant, and a complete "
        "NO_GO report. No component is claimed as novel in isolation, and no favorable episode "
        "is selected after execution."
    ),
]


METHOD = [
    (
        "Episode and endpoint. Each registered episode is a (dataset, shot, seed) triple. The "
        "binary datasets are OpenML credit-g (ID 31) and spambase (ID 44); shots are 5, 10, and "
        "20, and seeds are 0, 9, and 19. TreeSelfTrain-S is the fixed anchor. All four routes use "
        "the same labeled support, candidate pool, evaluation set, preprocessing, split, and "
        "ROC-AUC endpoint. Candidate and evaluation labels never enter representation construction, "
        "prototype formation, threshold selection, gating, or rescue."
    ),
    (
        "Semantic route. A fixed T0-3B row representation is computed from feature content. For "
        "each labeled support pair, class prototypes are rebuilt without that pair; held-out "
        "support scores thus provide leave-one-pair-out semantic evidence. A support-only gate "
        "compares semantic and tree-native evidence. If accepted, the route may append only "
        "candidates rejected by TreeSelfTrain-S. If the gate rejects or the eligible set is empty, "
        "training arrays, auxiliary weight, and final predictions must equal the anchor exactly. "
        "This invariant is implementation safety, not evidence of accuracy."
    ),
    (
        "Controls and decision. ProtoOOF-NoSemantics preserves feature-only routing while removing "
        "semantic content. ProtoOOF-Permuted applies one fixed row permutation to the semantic cache. "
        "The frozen verdict is conjunctive: overall improvement, control separation, consistency "
        "across datasets and shots, rescue activity on both datasets, no collapse or failed rows, "
        "and exact fallback must all hold. Any failed conjunct yields NO_GO."
    ),
]


RESULTS = [
    (
        "RQ1—endpoint. ProtoOOF-Tree-v1 matches TreeSelfTrain-S in every episode. The overall "
        "main-minus-tree mean is 0.0000; credit-g and spambase each have mean and median 0.0000; "
        "and the number of shot levels with a positive mean is 0. The main gate/rescue total is "
        "0/0, so the exact fallback invariant explains the deterministic endpoint equality."
    ),
    (
        "RQ2—controls. Mean main-minus-no-semantics is +0.000966820370534934 (reported as +0.0010), "
        "and mean main-minus-permuted is -0.0005257936507936532 (reported as -0.0005). Neither reaches "
        "the registered +0.01 separation. Only three episode-level control contrasts are nonzero: "
        "credit-g/5/0 main-minus-permuted = +0.002083333333333326; credit-g/5/9 = -0.011547619047619084; "
        "and spambase/5/9 main-minus-no-semantics = +0.01740276666962881. NoSemantics activates "
        "1 gate/50 rescues and Permuted 2/100, but this activity does not establish semantic benefit."
    ),
    (
        "RQ3—decision. Five conjuncts fail: overall_main_delta_min, main_minus_no_semantics_min, "
        "main_minus_permuted_min, positive_shot_means_min_count, and rescue_required_both_datasets. "
        "All 72 method rows execute successfully, no pseudo-label collapse occurs, and exact fallback "
        "passes, yet the registered verdict remains NO_GO."
    ),
]


BOUNDARY = [
    (
        "The directly observed boundary is narrow but useful: this fixed representation, prototype "
        "construction, support-only gate, and transfer rule did not alter the matched tree on the "
        "two datasets and 18 registered episodes. It does not show that semantic representations, "
        "other gates, or other distribution shifts are ineffective. The present grid is small; the "
        "kill-screen was designed to stop an unproductive route, not to estimate a population-wide "
        "effect or a p-value."
    ),
    (
        "The control activations suggest a falsifiable next step rather than a positive claim. A "
        "replacement should first demonstrate stable rescue coverage without label leakage, then "
        "semantic-content dependence against matched no-semantics and permutation controls, and only "
        "then a downstream gain across datasets and shot levels. Until those conditions are met, the "
        "safe action is to retain TreeSelfTrain-S and reject the semantic rescue route."
    ),
]


CONCLUSION = (
    "A failure-complete evaluation prevents mechanism activity from being confused with predictive "
    "value. ProtoOOF-Tree-v1 is leakage-controlled and safely falls back, but it supplies no final-tree "
    "gain and no registered control separation in the frozen study. The decision is therefore NO_GO. "
    "For reliable adaptive algorithms, exact fallback is a safety property; only a reproducible "
    "endpoint improvement under matched controls can justify deployment."
)


REPRODUCIBILITY = [
    (
        "The evidence contract fixes the two OpenML identifiers, three shot counts, three seeds, "
        "four ordered routes, and all failure semantics before interpretation. Reproduction begins "
        "from the registered split and fixed representation cache, executes TreeSelfTrain-S, Main, "
        "NoSemantics, and Permuted for every episode, and records both ROC-AUC and gate/rescue activity. "
        "A row is never discarded because a route fails; the failure count is part of the decision. "
        "The present ledger contains exactly 18 episodes and 72 successful method rows."
    ),
    (
        "Three invariants make the result auditable. First, the episode key (dataset, shot, seed) must "
        "be identical across routes. Second, candidate and evaluation labels are unavailable to all "
        "selection logic. Third, whenever Main rejects rescue, its appended arrays, auxiliary weight, "
        "and predictions must equal the anchor. The final report then recomputes paired effects from "
        "the ordered rows and checks them against the frozen aggregate statistics. These checks turn "
        "fallback equality into a testable implementation statement rather than an interpretive claim."
    ),
    (
        "A new study can challenge the current boundary, but it must be frozen independently. It should "
        "register the replacement representation or gate, the distribution-shift model, datasets, shots, "
        "seeds, controls, thresholds, and failure treatment before opening outcomes. Evidence for a new "
        "GO requires all three levels: stable rescue coverage, dependence on semantic content under the "
        "matched controls, and positive final-tree effects across datasets and shot levels. Passing only "
        "the first level would repeat the mechanism-versus-endpoint error exposed here."
    ),
    (
        "Operationally, reliability has two axes. Exact fallback limits harm when evidence is weak; the "
        "registered endpoint decides whether the added component is worth deploying. ProtoOOF-Tree-v1 "
        "passes the former and fails the latter. This separation supports a conservative controller: "
        "retain the established tree until a replacement passes the entire frozen decision rather than "
        "activating on an isolated low-shot episode."
    ),
]


FALSIFICATION_ROWS = (
    ("Support gate is underpowered", "Pre-registered stronger support evidence activates stably on both datasets without label access"),
    ("Semantic geometry misses tree errors", "A frozen alternative representation separates from both controls and improves the tree"),
    ("Transfer is the bottleneck", "Accepted rescues are accurate and yield positive paired endpoint effects under the same anchor"),
    ("Effect is distribution-specific", "A preselected broader grid passes dataset and shot consistency conditions"),
)


AI_DISCLOSURE = (
    "AI Tool Use Disclosure—OpenAI Codex (GPT-5 family, accessed September 2026) assisted with "
    "English-language editing, formatting, and venue-rule auditing. It did not generate or alter "
    "experimental data. The author retained and checked the research design, code, frozen results, "
    "citations, and interpretations."
)


EXTRA_COMPLETE = {
    "related": [
        (
            "Strong baselines and priors. XGBoost established a scalable regularized boosting system "
            "[1]. Controlled tabular benchmarks later showed that tuning and protocol can dominate "
            "architecture comparisons [2], [12], while LightGBM and CatBoost remain strong alternatives "
            "[13], [14]. TabPFN and TabICL instead learn priors that support in-context prediction [9], "
            "[10]. These studies support a strong comparator and disciplined information accounting."
        ),
        (
            "Language-derived tabular information. TabLLM serializes rows for language-model prediction "
            "[3]; TransTab learns transferable representations across tables [4]; and FeatLLM turns "
            "language-model rules into features for a simpler learner [5]. T0 supplies the fixed "
            "multitask prompted representation used here [6]. Our claim is not that these systems are "
            "interchangeable, but that any auxiliary semantics must be evaluated at the final deployed "
            "endpoint with matched access."
        ),
        (
            "Selection and negative tests. Classic pseudo-labeling uses model predictions as training "
            "targets [7]; later work treats confidence thresholds as explicit coverage-error decisions "
            "[8]. VIME [11] and FixMatch [15] show that semi-supervised gains depend on compatible "
            "assumptions and confidence behavior. Our negative controls ask whether semantic content, "
            "rather than generic routing or row order, carries the observed effect."
        ),
    ],
    "protocol": [
        (
            "The estimand is the paired episode difference between the main route and TreeSelfTrain-S. "
            "The same split and seed make this difference interpretable as an incremental endpoint "
            "effect. Every method row remains in the ledger, including failures; in this run all 72 "
            "rows succeeded. Aggregation is fixed before interpretation: all-episode mean, per-dataset "
            "mean and median, and shot-level means."
        ),
        (
            "The causal controls differ in one intended information source. NoSemantics tests whether "
            "feature-only routing or bookkeeping can explain activity. Permuted preserves the cache "
            "marginals while breaking the registered row correspondence. Because control activation "
            "alone can change the tree, the comparison is made at final ROC-AUC, not at gate counts."
        ),
        (
            "The implementation contract additionally verifies zero collapse and byte-level source/evidence "
            "hashes outside the paper. Main fallback requires identical appended arrays and predictions; "
            "it is stronger than similar aggregate performance. This prevents a rejected gate from "
            "silently perturbing the tree while also preventing equality from being marketed as a gain."
        ),
    ],
    "failure": [
        (
            "A plausible, unproven explanation is that leave-one-pair-out support evidence is too weak at "
            "these shot counts to approve main-route rescue. A second possibility is that the fixed T0-3B "
            "geometry does not align with the tree's error set. The present evidence cannot distinguish "
            "these mechanisms because the main gate never activates; they remain hypotheses, not findings."
        ),
        (
            "The nonzero controls occur only at five-shot episodes. Permutation activity therefore warns "
            "that a gate can respond to unstable low-shot geometry without demonstrating semantic content. "
            "The single NoSemantics activation similarly shows that route activity is insufficient. A future "
            "method must pass the endpoint and control-separation conjuncts together."
        ),
    ],
    "limitations": [
        (
            "External validity is limited to two binary OpenML datasets, three low-shot conditions, three "
            "seeds, one representation family, one tree anchor, and ROC-AUC. The study does not cover "
            "multiclass tasks, regression, missingness shifts, temporal drift, calibration, latency, or cost."
        ),
        (
            "The registered thresholds are decision thresholds, not estimates of a universal minimum effect. "
            "No significance test or p-value was registered or added after seeing the data. Eighteen episodes "
            "are enough for the planned kill-screen, not for broad equivalence or superiority claims."
        ),
        (
            "Because the main route always falls back, this study validates the safety invariant more directly "
            "than the intended rescue mechanism. Broader use would require new frozen experiments, stronger "
            "semantic dependence tests, calibration analysis, and datasets selected before outcome inspection."
        ),
    ],
}


REFERENCES = [
    '[1] T. Chen and C. Guestrin, "XGBoost: A scalable tree boosting system," in Proc. 22nd ACM SIGKDD Int. Conf. Knowledge Discovery and Data Mining, 2016, pp. 785-794. https://doi.org/10.1145/2939672.2939785',
    '[2] Y. Gorishniy, I. Rubachev, V. Khrulkov, and A. Babenko, "Revisiting deep learning models for tabular data," in Advances in Neural Information Processing Systems, vol. 34, 2021. https://proceedings.neurips.cc/paper_files/paper/2021/hash/9d86d83f925f2149e9edb0ac3b49229c-Abstract.html',
    '[3] S. Hegselmann, A. Buendia, H. Lang, M. Agrawal, X. Jiang, and D. Sontag, "TabLLM: Few-shot classification of tabular data with large language models," in Proc. AISTATS, PMLR 206, 2023, pp. 5549-5581. https://proceedings.mlr.press/v206/hegselmann23a.html',
    '[4] Z. Wang and J. Sun, "TransTab: Learning transferable tabular transformers across tables," in Advances in Neural Information Processing Systems, vol. 35, 2022. https://doi.org/10.52202/068431-0210',
    '[5] S. Han, J. Yoon, S. O. Arik, and T. Pfister, "Large language models can automatically engineer features for few-shot tabular learning," in Proc. ICML, PMLR 235, 2024, pp. 17454-17479. https://proceedings.mlr.press/v235/han24f.html',
    '[6] V. Sanh et al., "Multitask prompted training enables zero-shot task generalization," in Proc. ICLR, 2022. https://openreview.net/forum?id=9Vrb9D0WI4',
    '[7] D.-H. Lee, "Pseudo-label: The simple and efficient semi-supervised learning method for deep neural networks," ICML Workshop on Challenges in Representation Learning, 2013. https://openreview.net/pdf?id=3iGjh_NmoG',
    '[8] H. Vishwakarma, Y. Chen, S. S. S. Namburi Gnvv, S. J. Tay, R. K. Vinayak, and F. Sala, "Rethinking confidence scores and thresholds in pseudolabeling-based SSL," in Proc. ICML, PMLR 267, 2025, pp. 61582-61600. https://proceedings.mlr.press/v267/vishwakarma25a.html',
    '[9] N. Hollmann, S. Muller, K. Eggensperger, and F. Hutter, "TabPFN: A transformer that solves small tabular classification problems in a second," in Proc. ICLR, 2023. https://openreview.net/forum?id=cp5PvcI6w8_',
    '[10] J. Qu, D. Holzmuller, G. Varoquaux, and M. Le Morvan, "TabICL: A tabular foundation model for in-context learning on large data," in Proc. ICML, PMLR 267, 2025, pp. 50817-50847. https://proceedings.mlr.press/v267/qu25d.html',
    '[11] J. Yoon, Y. Zhang, J. Jordon, and M. van der Schaar, "VIME: Extending the success of self- and semi-supervised learning to tabular domain," in Advances in Neural Information Processing Systems, vol. 33, 2020. https://proceedings.neurips.cc/paper/2020/hash/7d97667a3e056acab9aaf653807b4a03-Abstract.html',
    '[12] L. Grinsztajn, E. Oyallon, and G. Varoquaux, "Why do tree-based models still outperform deep learning on typical tabular data?" in Advances in Neural Information Processing Systems, vol. 35, 2022. https://doi.org/10.52202/068431-0037',
    '[13] G. Ke et al., "LightGBM: A highly efficient gradient boosting decision tree," in Advances in Neural Information Processing Systems, vol. 30, 2017. https://proceedings.neurips.cc/paper/2017/hash/6449f44a102fde848669bdd9eb6b76fa-Abstract.html',
    '[14] L. Prokhorenkova, G. Gusev, A. Vorobev, A. V. Dorogush, and A. Gulin, "CatBoost: Unbiased boosting with categorical features," in Advances in Neural Information Processing Systems, vol. 31, 2018. https://proceedings.neurips.cc/paper/2018/hash/14491b756b3a51daac41c24863285549-Abstract.html',
    '[15] K. Sohn, D. Berthelot, N. Carlini, Z. Zhang, H. Zhang, C. A. Raffel, E. D. Cubuk, A. Kurakin, and C.-L. Li, "FixMatch: Simplifying semi-supervised learning with consistency and confidence," in Advances in Neural Information Processing Systems, vol. 33, 2020. https://proceedings.neurips.cc/paper/2020/hash/06964dce9addb1c5cb5d6e3d9838f733-Abstract.html',
]
