"""Evidence-bounded English content for the anonymous Adap manuscript."""

from __future__ import annotations


TITLE = (
    "Failure-Complete Evaluation of Semantic Rescue in Few-Shot Tabular "
    "Self-Training"
)

ABSTRACT = (
    "Semantic representations are increasingly proposed as side information for "
    "few-shot tabular learning, yet a representation-level signal is useful only if "
    "it improves the downstream predictor under a fair information boundary. We test "
    "a falsifiable data-mining question: can strictly out-of-fold semantic evidence "
    "rescue unlabeled rows rejected by a matched tree self-training system without "
    "consulting candidate or evaluation labels? ProtoOOF-Tree-v1 builds "
    "leave-one-pair-out class prototypes from a fixed T0-3B representation, activates "
    "rescue only through support-only evidence, and otherwise returns the tree "
    "endpoint exactly. A frozen development kill-screen covers two OpenML datasets, "
    "three shot counts, and three seeds: 18 episodes and 72 ordered method rows for "
    "the tree anchor, semantic route, no-semantics control, and row-permuted control. "
    "The main route matches the tree anchor in all 18 episodes, giving an overall "
    "paired ROC-AUC difference of 0.0000; both dataset means and medians are 0.0000, "
    "and no shot level has a positive mean. Separation from the no-semantics and "
    "permuted controls is +0.0010 and -0.0005, below the registered thresholds. The "
    "decision is NO_GO. This result does not imply that semantic tabular "
    "representations are universally ineffective. It establishes a reproducible "
    "boundary for this leakage-controlled gate and transfer path, and demonstrates "
    "how failure-complete evaluation prevents intermediate activity or exact fallback "
    "from being misreported as predictive value."
)

KEYWORDS = (
    "few-shot tabular learning; data mining; self-training; pseudo-labeling; "
    "semantic representations; trustworthy machine learning; negative results"
)


BODY = [
    {"type": "section", "title": "I. INTRODUCTION"},
    {
        "type": "p",
        "text": (
            "Low-label tabular classification invites two different forms of prior "
            "knowledge. Tree ensembles supply an effective structural bias for mixed, "
            "non-smooth features and remain strong comparators even when neural models "
            "are available [1], [2]. Pretrained language models supply another kind of "
            "prior: feature names, categorical values, and row descriptions can be "
            "serialized as text and mapped to a semantic space. Work such as TabLLM, "
            "TransTab, and FeatLLM demonstrates that this route can be useful in selected "
            "few-shot settings [3]-[5]. The fixed semantic asset tested here comes from "
            "the T0 multitask prompted-training family [6]. The unresolved issue in a "
            "hybrid system is not "
            "whether semantic scores can be computed. It is whether those scores add "
            "information beyond a competitive tabular endpoint under the same labeled "
            "support."
        ),
    },
    {
        "type": "p",
        "text": (
            "That distinction matters operationally. An organization may be willing to "
            "use a language model once to construct features but still require a small "
            "tree for latency, portability, or governance. In that setting, a semantic "
            "component earns its place only if the information survives transfer to the "
            "tree. A high semantic similarity, an accepted gate, or a nonzero auxiliary "
            "weight is merely evidence that a mechanism ran. None of these observations "
            "alone establishes that the final predictor improved."
        ),
    },
    {
        "type": "p",
        "text": (
            "Pseudo-label rescue makes the attribution problem sharper. Self-training "
            "can expand a small support set, yet the same feedback loop can reinforce "
            "mistakes [7]. Confidence thresholds control which pseudo-labels are used, "
            "but confidence may be miscalibrated, and changing a threshold changes both "
            "label quality and quantity [8]. A semantic rescue rule can therefore appear "
            "promising for three incompatible reasons: it may capture useful external "
            "knowledge, repeat the tree's own ordering in another coordinate system, or "
            "exploit leaked or unstable information. A fair experiment must distinguish "
            "these possibilities before inspecting the final metric."
        ),
    },
    {
        "type": "p",
        "text": (
            "We evaluate ProtoOOF-Tree-v1, a deliberately bounded route from a fixed "
            "semantic representation to a tree self-training endpoint. The method "
            "constructs semantic class prototypes in leave-one-pair-out folds, compares "
            "semantic and tree-native support evidence, and can append only candidates "
            "that the tree route rejected. Candidate and evaluation labels are absent "
            "from representation construction, gating, thresholding, and rescue. When "
            "support evidence is insufficient, the complete training arrays and final "
            "predictions must equal the tree anchor exactly."
        ),
    },
    {
        "type": "p",
        "text": (
            "The study asks three research questions. RQ1: does the semantic route "
            "improve the all-episode mean ROC-AUC over the matched TreeSelfTrain-S "
            "anchor? RQ2: does any apparent effect depend on semantic content rather "
            "than a feature-only nonsemantic route or a fixed row permutation? RQ3: "
            "does the mechanism meet its registered reliability conditions, including "
            "exact fallback, absence of collapse, positive behavior across datasets and "
            "shot levels, and actual rescue on both datasets? These questions are "
            "answered by one frozen conjunctive decision, not by choosing favorable "
            "episodes after execution."
        ),
    },
    {
        "type": "p",
        "text": (
            "The answer is negative. Across 18 registered episodes, ProtoOOF-Tree-v1 "
            "never activates rescue and equals TreeSelfTrain-S exactly. The principal "
            "paired effect is 0.0000 ROC-AUC, the required separation from both controls "
            "is absent, and the frozen verdict is NO_GO. Rather than hide this result, "
            "we use it to bound the method claim and expose what a future semantic "
            "rescue mechanism must change."
        ),
    },
    {
        "type": "p",
        "text": "The paper makes four falsifiable contributions:",
    },
    {
        "type": "bullets",
        "items": [
            (
                "a falsifiable incremental estimand for whether semantic side "
                "information changes a matched downstream tree, rather than merely "
                "producing an active representation or gate;"
            ),
            (
                "a leakage-controlled transfer and exact-fallback contract: semantic "
                "evidence is constructed and judged out of fold, no candidate or "
                "evaluation label reaches the method, and a rejected rescue cannot "
                "silently change the anchor endpoint;"
            ),
            (
                "matched no-semantics and row-permutation controls that test whether "
                "semantic content, rather than generic routing, supports the effect; and"
            ),
            (
                "a failure-complete 18-episode, 72-row report whose stop rule retains "
                "every episode and converts the null endpoint into an auditable NO_GO "
                "decision."
            ),
        ],
    },
    {"type": "section", "title": "II. RELATED WORK"},
    {"type": "subsection", "title": "A. Strong Tabular Baselines and Few-Shot Priors"},
    {
        "type": "p",
        "text": (
            "Gradient-boosted decision trees remain a central reference point for "
            "tabular prediction. XGBoost combines additive tree boosting with a "
            "regularized scalable implementation [1]. Controlled comparisons of deep "
            "tabular models show that results depend strongly on tuning and protocol, "
            "and that no deep architecture is universally superior to boosted trees "
            "[2]. This literature motivates treating the tree route as the primary "
            "endpoint rather than as an intentionally weak ablation."
        ),
    },
    {
        "type": "p",
        "text": (
            "Tabular foundation models offer a different prior. TabPFN learns a "
            "synthetic-data prior and performs prediction through in-context inference "
            "on small classification tasks [9]. TabICL extends this family toward larger "
            "datasets while documenting costs and fairness differences in ensembling, "
            "subsampling, and validation use [10]. These models demonstrate that a prior "
            "can replace or augment task-specific fitting. They do not, however, answer "
            "whether a language-derived semantic score can improve a separately "
            "deployed tree through pseudo-label selection."
        ),
    },
    {"type": "subsection", "title": "B. Language Models as Tabular Representations"},
    {
        "type": "p",
        "text": (
            "TabLLM serializes rows into natural-language strings and uses a language "
            "model for zero- or few-shot classification [3]. TransTab combines column "
            "descriptions and cell values to construct transferable row representations "
            "across tables [4]. FeatLLM assigns the language model a feature-engineering "
            "role: generated rules are converted into binary features for a simpler "
            "downstream model [5]. Together, these studies justify testing semantic "
            "transfer while also showing why its boundary must be explicit: performance "
            "depends on serialization, model access, prompt length, parsing, dataset, "
            "and comparator. Our experiment freezes one T0-3B representation and asks "
            "only whether it adds value to one tree-rescue path."
        ),
    },
    {"type": "subsection", "title": "C. Pseudo-Label Selection and the Missing Negative Test"},
    {
        "type": "p",
        "text": (
            "Pseudo-labeling augments labeled examples with predictions on unlabeled "
            "data [7]. Its central risk is confirmation bias: early errors can become "
            "training targets. Recent work reframes confidence and threshold choice as "
            "an explicit coverage-versus-error decision rather than a heuristic [8]. "
            "VIME likewise shows that semi-supervised assumptions and augmentations "
            "must be valid for heterogeneous tabular features [11]. These observations "
            "suggest a stronger evaluation standard for semantic rescue. The gate must "
            "be support-only, controls must test semantic dependence, the final tree "
            "must be the endpoint, and rejected or failed episodes must remain visible. "
            "The present work supplies that missing negative test; no individual "
            "component is claimed as novel in isolation."
        ),
    },
    {"type": "subsection", "title": "D. From Plausible Mechanism to Decision Evidence"},
    {
        "type": "p",
        "text": (
            "The reviewed literature also suggests a useful claim hierarchy. A model may "
            "encode semantic structure; an auxiliary score may correlate with labels; a "
            "gate may select candidates; selected pseudo-labels may be individually "
            "accurate; and the final learner may improve. These claims are not "
            "interchangeable. FeatLLM, for example, evaluates both generated rules and "
            "their downstream use [5], while confidence-control work ties selection to "
            "an explicit error objective [8]. For a semantic-to-tree system, the last "
            "link remains decisive because the tree can already encode much of the "
            "useful ordering or can be harmed by a small number of redundant rows."
        ),
    },
    {
        "type": "p",
        "text": (
            "Our evidence ladder therefore has four levels. Representation evidence asks "
            "whether the semantic cache is well formed and label-free. Mechanism evidence "
            "asks whether out-of-fold support comparisons and gates behave as specified. "
            "Attribution evidence asks whether behavior disappears when semantic content "
            "is removed or permuted. Endpoint evidence asks whether the final tree gains "
            "under the complete registered denominator. ProtoOOF-Tree-v1 reaches the "
            "first two levels as an implemented pathway, fails the control-separation "
            "requirement at the third, and produces no gain at the fourth. This ordering "
            "keeps a technically functioning module from being described as a validated "
            "learning contribution."
        ),
    },
    {
        "type": "p",
        "text": (
            "Broader tabular benchmarks reinforce the need for this restraint. Across "
            "45 typical tabular datasets, tree ensembles remain difficult to displace "
            "even after extensive neural-model tuning [12]. LightGBM and CatBoost also "
            "show that the phrase 'tree baseline' covers materially different inductive "
            "biases and treatments of efficiency, sampling, and categorical leakage "
            "[13], [14]. The present endpoint is specifically the registered XGBoost-"
            "based TreeSelfTrain-S route; the result is not a ranking of all tree "
            "learners. This distinction both strengthens the internal comparison and "
            "limits external claims."
        ),
    },
    {
        "type": "p",
        "text": (
            "Confidence-thresholded pseudo-labeling is also used in deep SSL systems "
            "such as FixMatch [15], where a weakly augmented view supplies a label for a "
            "strongly augmented view. That construction depends on valid image "
            "augmentations and a shared neural model. Our setting has neither assumption: "
            "heterogeneous tabular features are not perturbed, and the semantic proposer "
            "and tree consumer are different models. The common lesson is narrower: "
            "confidence determines data inclusion and must therefore be evaluated as "
            "part of the final learning system."
        ),
    },
    {"type": "section", "title": "III. QUESTION, ESTIMAND, AND LEAKAGE BOUNDARY"},
    {"type": "subsection", "title": "A. Registered Episode"},
    {
        "type": "p",
        "text": (
            "An episode is indexed by dataset d, shot count K, and seed s. Let S(d,K,s) "
            "be the labeled support, U(d,K,s) the unlabeled candidate pool, and T(d,K,s) "
            "the held-out evaluation set. The tree anchor and all ProtoOOF variants use "
            "the same episode identity. The protocol permits transductive access to "
            "candidate features, including their cached semantic representations, but "
            "candidate labels and evaluation labels are unavailable to every fit, "
            "prototype, gate, threshold, sign, candidate decision, and weight."
        ),
    },
    {
        "type": "p",
        "text": (
            "The primary contrast for one episode is δ(d,K,s) = AUC(main) − "
            "AUC(tree). The registered development estimand averages this paired "
            "difference over all 18 episodes. A failed method row remains part of the "
            "inventory and forces the failure conjunct to reject. Consequently, the "
            "estimand is neither a complete-case average nor a best-seed summary."
        ),
    },
    {
        "type": "equation",
        "text": "Δ = (1/18) Σ [AUC(main; d,K,s) − AUC(tree; d,K,s)].    (1)",
    },
    {"type": "subsection", "title": "B. Claims the Design Can and Cannot Support"},
    {
        "type": "p",
        "text": (
            "A positive result would authorize only a separately frozen independent "
            "confirmation. It would not establish a universal language-model advantage, "
            "the superiority of semantic features on all tables, or the causal effect of "
            "an individual ProtoOOF component. A NO_GO is also bounded: it rejects the "
            "registered gate-and-rescue path under the fixed datasets, shots, seeds, "
            "representation, serialization, and tree endpoint. It does not prove that "
            "other semantic models, selection rules, or downstream learners cannot "
            "benefit. This asymmetry is intentional. The design is powerful enough to "
            "stop an unsupported promotion but not to generalize beyond its evidence."
        ),
    },
    {"type": "subsection", "title": "C. Why the Estimand Is Failure-Complete"},
    {
        "type": "p",
        "text": (
            "A selective denominator would answer a different and easier question. If "
            "the mean were computed only where the semantic gate accepted, the method "
            "could improve its reported score by declining difficult episodes. If "
            "failed executions were removed, numerical instability could also improve "
            "the apparent result. The all-episode estimand instead evaluates the complete "
            "decision system: representation, support comparison, activation, rescue, "
            "fallback, and final refit. A gate that never activates may be safe, but it "
            "cannot satisfy a claim of incremental predictive value."
        ),
    },
    {
        "type": "p",
        "text": (
            "The conjunctive rule also prevents compensation among incompatible "
            "properties. A large gain on one dataset cannot cancel a negative mean on "
            "the other; an average gain cannot compensate for failure to distinguish "
            "semantic content from its controls; and exact fallback cannot compensate "
            "for zero rescue. The registered thresholds should be read as engineering "
            "promotion criteria for this development screen, not as universal effect "
            "sizes or post-hoc significance levels."
        ),
    },
    {"type": "section", "title": "IV. PROTOOOF-TREE-V1"},
    {"type": "subsection", "title": "A. Immutable Tree Anchor"},
    {
        "type": "p",
        "text": (
            "TreeSelfTrain-S is the deployment anchor. It consumes the registered "
            "support, selects its own pseudo-labeled candidate rows, assigns targets and "
            "reliability weights, and fits the final tree. ProtoOOF-Tree-v1 is not "
            "allowed to replace the anchor's accepted pseudo-labeled rows or reorder the anchor "
            "training prefix. It may append only a rescue set A(d,K,s) drawn from rows "
            "that the tree rejected. This constraint turns the comparison into an "
            "incremental-information test: any endpoint difference must enter through "
            "the appended semantic rescue."
        ),
    },
    {"type": "subsection", "title": "B. Feature-Only Semantic Representation"},
    {
        "type": "p",
        "text": (
            "Each row is serialized without a label token, label name, metric, or "
            "downstream result and embedded by a sealed T0-3B revision. The semantic "
            "cache is fixed before the report is opened. Main and control routes share "
            "the episode split, support pairs, cache identity, and numerical pipeline. "
            "The experiment therefore tests the information carried by the selected "
            "feature representation, not adaptive prompting after metric inspection."
        ),
    },
    {"type": "subsection", "title": "C. Leave-One-Pair-Out Prototype Evidence"},
    {
        "type": "p",
        "text": (
            "Support examples are paired across the two classes. For each held-out pair, "
            "the remaining support representations define two class prototypes. A "
            "signed score records the relative similarity of the held-out row to these "
            "prototypes. Repeating the procedure produces an out-of-fold semantic score "
            "for every support row. The same held-out rows receive matched evidence from "
            "the immutable tree route. No fold, prototype orientation, or score sign is "
            "chosen from candidate or test performance."
        ),
    },
    {"type": "subsection", "title": "D. Support-Only Gate, Candidate Rescue, and Fallback"},
    {
        "type": "p",
        "text": (
            "The activation gate compares semantic and tree-native evidence using only "
            "the held-out support scores. The candidate confidence threshold is the "
            "median absolute support prototype score. There is no threshold search, "
            "dataset-specific adjustment, or performance-driven sign flip. If the gate "
            "accepts, a rejected tree candidate is eligible only when the semantic and "
            "tree predictions disagree in the prespecified direction and the semantic "
            "magnitude meets the support-derived threshold. An eligible row receives "
            "the registered semantic target and a reliability weight capped by the "
            "frozen alpha rule."
        ),
    },
    {
        "type": "p",
        "text": (
            "Gate rejection, an empty rescue set, or a registered numerical failure "
            "cannot be relabeled as a success. With no rescue, every training row, "
            "target, weight, ordering decision, and prediction must be array-exact to "
            "TreeSelfTrain-S. Alpha zero must reproduce the anchor as a separate receipt. "
            "These conditions make no-harm auditable rather than rhetorical. They also "
            "explain why a zero endpoint is meaningful: it is a verified fallback state, "
            "not a missing or silently skipped computation. Fig. 1 summarizes this "
            "information boundary."
        ),
    },
    {
        "type": "figure",
        "key": "pipeline",
        "caption": (
            "Fig. 1. Registered information flow. Candidate features may enter the "
            "semantic cache, but candidate/evaluation labels never enter prototypes, "
            "gating, thresholding, or rescue. The final tree changes only through an "
            "accepted appended rescue set."
        ),
    },
    {"type": "subsection", "title": "E. Causal Controls"},
    {
        "type": "p",
        "text": (
            "ProtoOOF-NoSemantics replaces the semantic representation with a "
            "feature-only nonsemantic representation while preserving folds, gate, "
            "threshold logic, and downstream fitting. ProtoOOF-Permuted applies a fixed "
            "row permutation while preserving the representation shape and computation. "
            "The ordered four-method inventory is therefore TreeSelfTrain-S, "
            "ProtoOOF-Tree-v1, ProtoOOF-NoSemantics, and ProtoOOF-Permuted. The controls "
            "do not prove a complete causal decomposition, but they provide necessary "
            "tests: an effect that does not separate from either control cannot be "
            "attributed to the intended semantic alignment."
        ),
    },
    {"type": "subsection", "title": "F. Episode Execution Contract"},
    {
        "type": "p",
        "text": (
            "Algorithm 1 summarizes one episode. The ordering is part of the method. "
            "The anchor is completed first, before any semantic candidate is appended. "
            "Out-of-fold scores are then constructed from support only; the gate and "
            "threshold are frozen from those scores; and candidate features are queried "
            "only after activation has been decided. This order rules out an otherwise "
            "subtle leakage path in which the distribution of candidate scores influences "
            "whether the semantic route is considered reliable."
        ),
    },
    {
        "type": "table",
        "caption": "ALGORITHM 1. FROZEN EXECUTION FOR ONE (DATASET, SHOT, SEED) EPISODE",
        "headers": ["Step", "Operation and invariant"],
        "rows": [
            ["1", "Build immutable TreeSelfTrain-S arrays and endpoint."],
            ["2", "Pair support classes; hold out one pair at a time."],
            ["3", "Form prototypes without the held-out support pair."],
            ["4", "Compare semantic and tree evidence on held-out support only."],
            ["5", "Freeze gate and median-absolute support threshold."],
            ["6", "If rejected, return array-exact anchor output."],
            ["7", "If accepted, inspect rejected candidate features only."],
            ["8", "Append eligible rescue rows after the anchor prefix."],
            ["9", "Refit the same tree family; emit all four method rows."],
        ],
    },
    {
        "type": "p",
        "text": (
            "The four method rows are emitted even if one route encounters a registered "
            "failure. This fixed cardinality allows inventory checks to distinguish an "
            "actual zero effect from a missing output. It also makes method identity "
            "auditable: an episode cannot be silently renamed, reordered, or replaced "
            "after its metric is observed."
        ),
    },
    {"type": "section", "title": "V. EXPERIMENTAL PROTOCOL"},
    {"type": "subsection", "title": "A. Data, Shots, Seeds, and Method Grid"},
    {
        "type": "p",
        "text": (
            "The formal development scope contains two binary OpenML datasets: credit-g "
            "(OpenML 31) and spambase (OpenML 44). The source audit records 1,000 rows "
            "and 20 features for credit-g, including 13 categorical and seven continuous "
            "features, with class counts 700/300. Spambase contains 4,601 rows, 57 "
            "continuous features, and class counts 2,788/1,813. These differences make "
            "the pair a small but useful contrast between mixed-type financial data and "
            "dense continuous frequency features. They do not constitute broad task "
            "coverage."
        ),
    },
    {
        "type": "p",
        "text": (
            "Registered shot counts are 5, 10, and 20; registered seeds are 0, 9, and "
            "19. Their Cartesian product gives 18 episodes. Each episode emits one "
            "ordered record for each of four methods, for 72 method rows. Dataset bytes, "
            "normalized manifests, label audits, split identities, study source, "
            "execution protocol, and report builder are content-addressed. The released "
            "report records zero execution failures. Table I records the complete study "
            "grid and evidence boundary."
        ),
    },
    {
        "type": "table",
        "caption": "TABLE I. FROZEN STUDY GRID AND EVIDENCE BOUNDARY",
        "headers": ["Item", "Registered value"],
        "rows": [
            ["Datasets", "credit-g (31); spambase (44)"],
            ["Rows", "1,000; 4,601"],
            ["Features", "20 mixed; 57 continuous"],
            ["Class counts", "700/300; 2,788/1,813"],
            ["Shots", "5, 10, 20"],
            ["Seeds", "0, 9, 19"],
            ["Episodes", "2 x 3 x 3 = 18"],
            ["Methods/episode", "4 ordered routes"],
            ["Total method rows", "72; failures retained"],
            ["Primary metric", "Held-out ROC-AUC"],
            ["Candidate access", "Features yes; labels no"],
            ["Representation", "Fixed feature-only T0-3B cache"],
        ],
    },
    {"type": "subsection", "title": "B. Fairness Matrix"},
    {
        "type": "p",
        "text": (
            "Fairness is defined by common episode identity and a bounded method-only "
            "difference. All four routes share the support and candidate pools, split, "
            "final tree family, output metric, row-order contract, and failure policy. "
            "The ProtoOOF variants additionally share fold construction, support-only "
            "gate, candidate threshold rule, and numerical pipeline. Only the "
            "representation/control transformation differs. TreeSelfTrain-S remains "
            "immutable; it is not retuned to counter the semantic route, and the "
            "semantic route is not tuned per dataset or seed. Table II makes these "
            "controlled differences explicit."
        ),
    },
    {
        "type": "p",
        "text": (
            "The comparison answers an incremental question, not a leaderboard question. "
            "LightGBM, CatBoost, TabPFN, TabICL, and end-to-end LLM predictors are not "
            "additional arms in the frozen 72-row grid. Adding them after opening the "
            "results would change the method inventory, tuning budget, and estimand. The "
            "registered XGBoost-based tree is sufficient for the stated claim because "
            "ProtoOOF-Tree-v1 returns that exact endpoint when rescue is absent and "
            "differs only through appended candidates when rescue is active. A broader "
            "benchmark would be valuable for a new study, but it is neither needed nor "
            "authorized to reinterpret the current main-minus-tree effect."
        ),
    },
    {
        "type": "table",
        "caption": "TABLE II. CONTROLLED DIFFERENCES AMONG THE FOUR ROUTES",
        "headers": ["Property", "Tree", "Main", "NoSem.", "Perm."],
        "rows": [
            ["Same episode/split", "yes", "yes", "yes", "yes"],
            ["Same final tree family", "yes", "yes", "yes", "yes"],
            ["Anchor pseudo rows retained", "base", "yes", "yes", "yes"],
            ["Support-only OOF gate", "--", "yes", "yes", "yes"],
            ["Semantic alignment intact", "--", "yes", "no", "no"],
            ["Fixed row permutation", "no", "no", "no", "yes"],
            ["Exact fallback required", "ref.", "yes", "yes", "yes"],
        ],
    },
    {"type": "subsection", "title": "C. Frozen Conjunctive Decision"},
    {
        "type": "p",
        "text": (
            "The development screen returns only GO_TO_INDEPENDENT_CONFIRMATION or "
            "NO_GO. GO requires every registered conjunct: no failed method row; an "
            "overall main-minus-tree mean of at least 0.02 ROC-AUC; nonnegative mean and "
            "median on both datasets; at least 0.01 mean separation from each control; "
            "a positive main-minus-tree mean for at least two shot levels; exact "
            "fallback and alpha-zero equivalence; nonempty rescue evidence on both "
            "datasets; and zero pseudo-label collapse. The use of a conjunction matters. "
            "Passing no-harm while failing incremental benefit is a safe implementation "
            "result, not a successful learning result. Table III pairs every condition "
            "with its frozen outcome."
        ),
    },
    {
        "type": "table",
        "caption": "TABLE III. REGISTERED GO CONDITIONS AND FROZEN OUTCOMES",
        "headers": ["Condition", "Threshold", "Observed", "Pass"],
        "rows": [
            ["No failed rows", "all 72", "72 success", "yes"],
            ["Overall main - tree", ">= 0.0200", "0.0000", "no"],
            ["Both dataset mean/median", ">= 0", "all 0.0000", "yes"],
            ["Main - no-semantics", ">= 0.0100", "+0.0010", "no"],
            ["Main - permuted", ">= 0.0100", "-0.0005", "no"],
            ["Positive shot means", ">= 2", "0", "no"],
            ["Exact fallback/alpha zero", "all exact", "all exact", "yes"],
            ["Rescue on both datasets", "required", "none in main", "no"],
            ["Pseudo-label collapse", "zero", "zero", "yes"],
        ],
    },
    {"type": "subsection", "title": "D. Evidence Integrity"},
    {
        "type": "p",
        "text": (
            "The execution ledger binds study, source, model, data, protocol, and runtime "
            "identities. Primary and mirror transactions contain identical result bytes "
            "and a manifest written after the result artifacts. A result-blind inventory "
            "review verifies that all 18 episodes and 72 ordered records exist before "
            "the report builder is authorized. The report is generated from the bound "
            "rows and exposes every failed conjunct. These controls do not improve the "
            "model; they constrain post hoc reinterpretation after the metrics are known."
        ),
    },
    {"type": "subsection", "title": "E. Metric, Aggregation, and Failure Semantics"},
    {
        "type": "p",
        "text": (
            "Held-out ROC-AUC is the episode endpoint. It evaluates ranking without "
            "selecting a test threshold and is well defined for the registered binary "
            "tasks, but it does not measure probability calibration or a deployment "
            "cost function. The same evaluation rows and metric implementation are used "
            "for every method within an episode. Paired differences are formed before "
            "aggregation, preserving the dataset/shot/seed match. Means by dataset and "
            "shot are secondary components of the registered gate rather than separately "
            "optimized endpoints."
        ),
    },
    {
        "type": "p",
        "text": (
            "A method-row failure is not imputed with a favorable value and is not "
            "dropped. Instead, the row remains in the 72-record inventory with its error "
            "code, and the no-failure conjunct fails. Numerical failure, gate rejection, "
            "and empty rescue are deliberately different states: failure invalidates the "
            "episode for promotion, whereas rejection or empty rescue invokes an exact, "
            "testable anchor fallback. The formal run contains the latter state for all "
            "18 main-route episodes and no execution failure."
        ),
    },
    {"type": "subsection", "title": "F. Result Opening and Audit Trail"},
    {
        "type": "p",
        "text": (
            "The authorized report builder exposes no option for changing scientific fields. The "
            "authorized builder opens the complete bound inventory once and emits the "
            "method table, paired episode differences, aggregate summary, conjunct "
            "outcomes, and verdict. The study, runner, execution protocol, review "
            "inventory, and report artifacts are joined by SHA-256 identities. This "
            "content addressing does not guarantee that every scientific design choice "
            "is correct, but it does establish which bytes produced the reported "
            "decision and whether the primary and mirror copies agree."
        ),
    },
    {"type": "subsection", "title": "G. Leakage and Equivalence Audits"},
    {
        "type": "p",
        "text": (
            "Leakage prevention is checked at several interfaces. The representation "
            "cache persists feature-only text and embeddings, with no label token, label "
            "name, evaluation metric, or downstream result. A held-out support pair does "
            "not contribute to the prototypes used to score that pair. Candidate "
            "features are unavailable to the support activation decision, and candidate "
            "labels are unavailable throughout. Evaluation labels are opened only by the "
            "common endpoint evaluator. These controls do not rule out prior knowledge "
            "of a public dataset inside a pretrained model; they rule out direct use of "
            "the registered episode labels by the transfer pipeline."
        ),
    },
    {
        "type": "p",
        "text": (
            "Fallback equivalence is stronger than comparing two rounded metrics. The "
            "receipts require the training rows, targets, reliability weights, ordering, "
            "and predictions to be array-exact to TreeSelfTrain-S when rescue is absent. "
            "A separate alpha-zero route verifies that the semantic append path reduces "
            "to the same anchor when its weight is disabled. The formal report records "
            "both equivalence requirements as satisfied in every applicable row. This "
            "allows the observed main-tree zero to be traced to a specific invariant "
            "rather than to rounding or insufficient metric precision."
        ),
    },
    {
        "type": "p",
        "text": (
            "The audit boundary is still finite. Hashes establish artifact identity but "
            "do not prove that a pretrained model never encountered the public table in "
            "pretraining. Likewise, deterministic split identities prevent accidental "
            "reshuffling across methods, but they do not convert two public datasets "
            "into a representative population. These residual risks are carried into "
            "the limitations rather than treated as solved by provenance tooling."
        ),
    },
    {"type": "section", "title": "VI. RESULTS"},
    {"type": "subsection", "title": "A. RQ1: Does Semantic Rescue Improve the Tree?"},
    {
        "type": "p",
        "text": (
            "No. ProtoOOF-Tree-v1 and TreeSelfTrain-S have identical ROC-AUC in every "
            "registered episode. The paired difference is exactly zero for 18 of 18 "
            "episodes, so the overall mean is 0.0000. The credit-g mean and median are "
            "both 0.0000; the spambase mean and median are also 0.0000. Aggregating by "
            "shot count produces zero at 5, 10, and 20 shots, so the number of positive "
            "shot-level means is zero. This is an endpoint statement, not a claim of "
            "statistical equivalence. The experiment was designed around a practical "
            "promotion threshold, and the observed effect is below it."
        ),
    },
    {"type": "subsection", "title": "B. RQ2: Does the Route Separate from the Controls?"},
    {
        "type": "p",
        "text": (
            "No. The mean main-minus-NoSemantics contrast is +0.0009668, displayed as "
            "+0.0010, below the registered +0.0100 threshold. The mean main-minus-"
            "Permuted contrast is -0.0005258, displayed as -0.0005, and therefore has "
            "the wrong sign as well as insufficient magnitude. These aggregates arise "
            "from a small number of control activations: NoSemantics accepts one gate "
            "and rescues 50 candidates; Permuted accepts two gates and rescues 100 "
            "candidates in total. The main semantic route accepts no gate and rescues "
            "no candidate. Control activity is not evidence that the controls are "
            "better methods; it shows that the gate can activate without the intended "
            "semantic alignment, which defeats the attribution required for GO. Table IV "
            "and Fig. 2 summarize the frozen effects and activity."
        ),
    },
    {
        "type": "table",
        "caption": "TABLE IV. COMPLETE FROZEN EFFECT SUMMARY",
        "headers": ["Statistic", "Value"],
        "rows": [
            ["Episodes / method rows / failures", "18 / 72 / 0"],
            ["Main - tree mean", "+0.0000"],
            ["credit-g mean / median", "+0.0000 / +0.0000"],
            ["spambase mean / median", "+0.0000 / +0.0000"],
            ["Main - no-semantics mean", "+0.0010"],
            ["Main - permuted mean", "-0.0005"],
            ["Positive shot-level means", "0 of 3"],
            ["Main gate accepts / rescues", "0 / 0"],
            ["Frozen verdict", "NO_GO"],
        ],
    },
    {
        "type": "figure",
        "key": "effects",
        "caption": (
            "Fig. 2. Frozen per-episode paired differences. The main-minus-tree effect "
            "is zero for every dataset, shot, and seed; only control contrasts depart "
            "from zero in three low-shot control activations."
        ),
    },
    {"type": "subsection", "title": "C. RQ3: Does the Mechanism Meet the Reliability Gate?"},
    {
        "type": "p",
        "text": (
            "It meets the implementation-safety conditions but not the learning-value "
            "conditions. All 72 rows complete successfully, fallback and alpha-zero "
            "equivalence are exact, both dataset summaries are nonnegative, and no "
            "pseudo-label collapse occurs. Five conjuncts nevertheless fail: minimum "
            "overall gain, separation from NoSemantics, separation from Permuted, the "
            "number of positive shot means, and rescue on both datasets. Because the "
            "rule is conjunctive, the correct decision is NO_GO and no independent "
            "confirmation is authorized by this study."
        ),
    },
    {"type": "subsection", "title": "D. Episode-Level Control Departures"},
    {
        "type": "p",
        "text": (
            "Only three control contrasts depart from zero. On credit-g at five shots, "
            "the main-minus-Permuted differences are +0.0020833 for seed 0 and "
            "-0.0115476 for seed 9. On spambase at five shots and seed 9, the "
            "main-minus-NoSemantics difference is +0.0174028. Every other main-control "
            "contrast is zero. Because one permuted control is better than the main "
            "route and another is worse, and because all departures occur at five shots, "
            "the pattern is consistent with an unstable low-support gate. It does not "
            "identify instability as the unique cause; three departures are too few for "
            "a reliable distributional conclusion."
        ),
    },
    {
        "type": "p",
        "text": (
            "The exact main-tree zeros require a different interpretation from small "
            "paired estimates near zero. Here the main route does not add a candidate "
            "and the fallback contract forces identical arrays and predictions. The "
            "endpoint equality is therefore explained by the observed execution path. "
            "It should not be converted into a confidence interval for equivalence, and "
            "it provides no estimate of what would happen if the main gate accepted."
        ),
    },
    {"type": "subsection", "title": "E. Interpreting the Deterministic Zero"},
    {
        "type": "p",
        "text": (
            "The result is stronger than a claim that the mean is merely close to zero "
            "and weaker than a claim that all semantic rescue effects are zero. It is "
            "stronger because all 18 paired outcomes are generated by a verified exact "
            "fallback, not by cancellation of positive and negative estimates. It is "
            "weaker because the registered main gate never exposes the final tree to a "
            "main-route rescue. The experiment therefore falsifies the complete "
            "proposal as a usable promotion candidate: a mechanism that cannot activate "
            "under its own safety rule delivers no incremental benefit. It does not "
            "estimate the effect of forcibly bypassing that rule."
        ),
    },
    {
        "type": "p",
        "text": (
            "For the same reason, conventional significance language would be misleading. "
            "There is no sampled distribution of nonzero main effects to test, and no "
            "equivalence margin was registered. The correct inferential statement is "
            "decision-based: the observed execution path fails the minimum 0.02 "
            "promotion effect and four additional necessary conjuncts. This is enough "
            "to stop independent confirmation under the registered protocol."
        ),
    },
    {"type": "section", "title": "VII. FAILURE ANALYSIS AND DECISION VALUE"},
    {"type": "subsection", "title": "A. Directly Observed Boundary"},
    {
        "type": "p",
        "text": (
            "Three observations are supported directly. First, the semantic support "
            "comparison never satisfies the activation rule in the main route. Second, "
            "exact fallback works: a rejected rescue leaves the anchor endpoint "
            "unchanged in every episode. Third, the gate is not uniquely responsive to "
            "the intended semantic alignment because nonsemantic and permuted controls "
            "activate in three episodes. Together, these facts narrow the failure to the "
            "tested path from representation through support evidence to candidate "
            "selection. They do not show whether the fixed embedding contains useful "
            "label information under a different decoder."
        ),
    },
    {"type": "subsection", "title": "B. Plausible Mechanisms, Not Proven Causes"},
    {
        "type": "p",
        "text": (
            "The frozen results are diagnostic but not a factorial ablation. Several "
            "explanations remain plausible. With only 5, 10, or 20 labels, leave-one-"
            "pair-out prototypes may be too variable to dominate the tree-native "
            "ordering on support. The median absolute support score may be conservative "
            "when semantic margins are compressed. The serialized T0-3B geometry may "
            "encode broad feature meaning without aligning to the particular OpenML "
            "label boundary. Finally, the tree may reject few candidates that are both "
            "semantically clear and useful to refit. None of these explanations is "
            "identified causally by the present two-dataset grid, so they are hypotheses "
            "for new studies, not retroactive explanations of the zero effect."
        ),
    },
    {
        "type": "p",
        "text": (
            "The control pattern adds one sharper warning. A support-only gate can pass "
            "because of small-sample ordering noise even when semantic alignment has "
            "been removed or permuted. A future design should therefore estimate gate "
            "stability itself, for example through repeated support resampling, and "
            "should require the semantic route to beat control activation rates before "
            "candidate rescue is considered. This proposal is a design implication, not "
            "a result already tested here."
        ),
    },
    {"type": "subsection", "title": "C. Scientific and Practical Significance of NO_GO"},
    {
        "type": "p",
        "text": (
            "Negative evidence is useful when it changes a decision. A report limited to "
            "successful gates could have turned three control activations into an "
            "apparently active mechanism. A report limited to no-harm could have called "
            "the 18 exact fallbacks a safe semantic augmentation. Neither description "
            "would answer whether semantic information improved the endpoint. The "
            "registered rule instead stops the method before a larger confirmation and "
            "preserves compute and interpretive budget for designs that can demonstrate "
            "incremental information."
        ),
    },
    {
        "type": "p",
        "text": (
            "For practitioners, the present recommendation is simple: retain "
            "TreeSelfTrain-S under this protocol. The semantic route adds representation "
            "and gating machinery but produces the same final predictions. This is not "
            "a permanent rejection of language-derived features. It is a refusal to pay "
            "for an unvalidated pathway whose intended semantic control separation also "
            "fails."
        ),
    },
    {"type": "subsection", "title": "D. Falsification Map for the Next Study"},
    {
        "type": "p",
        "text": (
            "The frozen result suggests a sequence of new, separately registered tests. "
            "First measure whether prototype margins are reproducible under repeated "
            "support resampling; this tests gate stability without candidate labels. "
            "Then compare the semantic representation with no-semantics and permutation "
            "controls before rescue, using a threshold fixed independently of the "
            "development episodes. Only if semantic support evidence separates from both "
            "controls should candidate rescue be evaluated. Finally, an accepted rescue "
            "must be judged by its incremental final-tree effect, not by pseudo-label "
            "accuracy alone. Table V converts these diagnoses into separately falsifiable "
            "tests."
        ),
    },
    {
        "type": "table",
        "caption": "TABLE V. NEW HYPOTHESES IMPLIED BY THE NO_GO BOUNDARY",
        "headers": ["Open hypothesis", "Required new evidence"],
        "rows": [
            ["Prototype geometry is unstable", "Repeated support-resampling margins"],
            ["Semantic alignment is weak", "Pre-rescue separation from both controls"],
            ["Gate is overly conservative", "Independent threshold and activation study"],
            ["Useful disagreements are rare", "Blind audit of rejected-candidate strata"],
            ["Another decoder can use the cache", "New learner with frozen fair baseline"],
        ],
    },
    {
        "type": "p",
        "text": (
            "These tests must not reuse the present development outcomes to choose a "
            "favorable threshold and then be described as confirmation. The method, "
            "datasets, seed inventory, estimand, and stopping rule should be frozen as a "
            "new study. This separation preserves the value of the current negative "
            "result while allowing the research program to continue."
        ),
    },
    {"type": "subsection", "title": "E. Design Lessons for Reliable Adaptation"},
    {
        "type": "p",
        "text": (
            "The first lesson is to bind the claim to the consumer of the adaptation. "
            "If the deployed model is a tree, evidence about an embedding or pseudo-label "
            "selector is intermediate evidence. The final tree must change in the "
            "desired direction under a fair comparison. The second lesson is to make "
            "abstention visible. A conservative gate is desirable only when its "
            "abstentions do not inflate a success-only denominator and when the cost of "
            "running the unused pathway is acknowledged."
        ),
    },
    {
        "type": "p",
        "text": (
            "The third lesson concerns controls. A no-semantics route checks whether "
            "generic feature geometry or calibration is sufficient for activation; a "
            "permuted route checks whether row alignment matters. Both should traverse "
            "the same code path and should be judged by prespecified contrasts. If a "
            "control activates, the correct response is not to delete that episode but "
            "to weaken the semantic attribution. Finally, failure handling belongs in "
            "the estimand. A reliable method is a system that returns a scientifically "
            "interpretable record for every registered unit, including rejection and "
            "failure states."
        ),
    },
    {
        "type": "p",
        "text": (
            "These principles are transferable beyond this particular PLM or tree. They "
            "apply whenever a high-capacity representation proposes data, weights, or "
            "decisions to a smaller downstream learner. The semantic component must add "
            "information, the downstream endpoint must realize it, and the conclusion "
            "must survive controls that preserve computation while removing the intended "
            "content."
        ),
    },
    {"type": "section", "title": "VIII. LIMITATIONS AND THREATS TO VALIDITY"},
    {
        "type": "p",
        "text": (
            "External validity is narrow. The screen covers two binary OpenML datasets, "
            "three shot counts, and three seeds. It can reject the registered mechanism "
            "but cannot characterize performance on high-cardinality categorical data, "
            "multiclass tasks, regression, domain-specific tables, or larger support "
            "sets. Three seeds per condition are insufficient for a precise sampling "
            "distribution; the decision is therefore threshold-based and failure-"
            "complete, not a claim of statistical equivalence."
        ),
    },
    {
        "type": "p",
        "text": (
            "Construct validity is limited by one fixed T0-3B revision, one feature-only "
            "serialization, one prototype score, one support gate, and one tree family. "
            "The no-semantics and permuted controls test necessary dependence on the "
            "intended representation, but they do not identify all sources of "
            "calibration, row-order sensitivity, or prototype instability. Because the "
            "registered development route never rescues, the study cannot estimate the "
            "conditional quality of main-route rescued labels."
        ),
    },
    {
        "type": "p",
        "text": (
            "The protocol is transductive: unlabeled candidate features are available "
            "when the semantic cache and candidate scores are constructed. Deployments "
            "that require strictly inductive prediction have a different information "
            "boundary. The evidence package content-addresses the artifacts needed for "
            "the frozen result, but the manuscript does not infer unrecorded hardware, "
            "latency, energy, or full environment details. No efficiency claim is made."
        ),
    },
    {
        "type": "p",
        "text": (
            "Finally, this is a development kill-screen, not an independent confirmation. "
            "If thresholds, datasets, seeds, failure treatment, serialization, model "
            "revision, or estimand are changed, the result belongs to a new study. Such "
            "changes may be scientifically justified, but they cannot be used to "
            "reinterpret the frozen NO_GO."
        ),
    },
    {
        "type": "p",
        "text": (
            "Reporting validity also has limits. The artifact chain preserves the frozen "
            "result and exposes the stop rule, but an external reader does not receive a "
            "new independent rerun through this paper. Dataset names and OpenML "
            "identifiers are disclosed for reproducibility, while anonymous review "
            "requires that personal repository paths and local machine identities remain "
            "absent. A post-review release should provide the nonidentifying manifests, "
            "runner, and report builder needed to reproduce the tables without exposing "
            "private infrastructure."
        ),
    },
    {"type": "section", "title": "IX. REPRODUCIBILITY AND EVIDENCE CHECKLIST"},
    {
        "type": "p",
        "text": (
            "The evidential unit is the registered episode, not a selected successful "
            "run. A sufficient release links the frozen decision conditions, the 72-row "
            "ledger with explicit failure fields, episode contrasts, aggregate report, "
            "and a content-addressed manifest. A reviewer can then recompute every mean, "
            "median, activity count, control difference, and conjunctive decision without "
            "inferring missing rows from prose. Eighteen episode identities times four "
            "ordered methods must equal 72 rows, each registered unit must occur once, "
            "and every summary must be derivable from that ledger."
        ),
    },
    {
        "type": "p",
        "text": (
            "Reproduction and evidence audit are different claims. Reproduction reruns "
            "the frozen program from the registered data and feature cache; an evidence "
            "audit verifies that released rows entail the tables and verdict. This paper "
            "supports the latter directly. A post-review package should support both "
            "while keeping immutable the dataset identities, feature-only cache, seeds, "
            "split contract, method order, thresholds, and failure policy. Unrecorded "
            "environment facts remain unknown; changing a registered object creates a "
            "new experiment, manifest, and decision record."
        ),
    },
    {
        "type": "p",
        "text": (
            "The checklist also separates cache completion, gate eligibility, rescue "
            "activity, held-out endpoint change, and the derived promotion verdict. The "
            "first three cannot license a predictive claim. Reporting all five levels "
            "prevents exact fallback from being mistaken for useful adaptation and makes "
            "the negative boundary falsifiable."
        ),
    },
    {"type": "section", "title": "X. CONCLUSION"},
    {
        "type": "p",
        "text": (
            "This study evaluates one concrete semantic-rescue path as an incremental "
            "data-mining decision rather than a representation showcase. Under the "
            "frozen 18-episode protocol, ProtoOOF-Tree-v1 activates no rescue, matches "
            "the tree in every episode, fails both control-separation conditions, and "
            "receives a NO_GO verdict. Exact fallback establishes implementation safety, "
            "not predictive value. The evidence therefore supports a narrow action: "
            "retain the matched tree route and do not promote this semantic mechanism. "
            "It does not support a universal rejection of language-derived tabular "
            "representations. By retaining every registered episode and separating "
            "representation activity, gate activity, endpoint change, and promotion, "
            "the failure-complete protocol makes that boundary auditable and falsifiable "
            "for future mechanisms."
        ),
    },
]


REFERENCES = [
    (
        "[1] T. Chen and C. Guestrin, \"XGBoost: A scalable tree boosting system,\" "
        "in Proc. 22nd ACM SIGKDD Int. Conf. Knowledge Discovery and Data Mining, "
        "2016, pp. 785-794."
    ),
    (
        "[2] Y. Gorishniy, I. Rubachev, V. Khrulkov, and A. Babenko, \"Revisiting "
        "deep learning models for tabular data,\" in Advances in Neural Information "
        "Processing Systems, vol. 34, 2021."
    ),
    (
        "[3] S. Hegselmann, A. Buendia, H. Lang, M. Agrawal, X. Jiang, and D. "
        "Sontag, \"TabLLM: Few-shot classification of tabular data with large language "
        "models,\" in Proc. 26th Int. Conf. Artificial Intelligence and Statistics, "
        "PMLR 206, 2023, pp. 5549-5581."
    ),
    (
        "[4] Z. Wang and J. Sun, \"TransTab: Learning transferable tabular transformers "
        "across tables,\" in Advances in Neural Information Processing Systems, vol. "
        "35, 2022."
    ),
    (
        "[5] S. Han, J. Yoon, S. O. Arik, and T. Pfister, \"Large language models can "
        "automatically engineer features for few-shot tabular learning,\" in Proc. "
        "41st Int. Conf. Machine Learning, PMLR 235, 2024, pp. 17454-17479."
    ),
    (
        "[6] V. Sanh et al., \"Multitask prompted training enables zero-shot task "
        "generalization,\" in Proc. Int. Conf. Learning Representations, 2022."
    ),
    (
        "[7] D.-H. Lee, \"Pseudo-label: The simple and efficient semi-supervised "
        "learning method for deep neural networks,\" in ICML Workshop on Challenges "
        "in Representation Learning, 2013."
    ),
    (
        "[8] H. Vishwakarma, Y. Chen, S. S. S. Namburi Gnvv, S. J. Tay, R. K. "
        "Vinayak, and F. Sala, \"Rethinking confidence scores and thresholds in "
        "pseudolabeling-based SSL,\" in Proc. 42nd Int. Conf. Machine Learning, PMLR "
        "267, 2025, pp. 61582-61600."
    ),
    (
        "[9] N. Hollmann, S. M\u00fcller, K. Eggensperger, and F. Hutter, \"TabPFN: A "
        "transformer that solves small tabular classification problems in a second,\" "
        "in Proc. Int. Conf. Learning Representations, 2023."
    ),
    (
        "[10] J. Qu, D. Holzm\u00fcller, G. Varoquaux, and M. Le Morvan, \"TabICL: A "
        "tabular foundation model for in-context learning on large data,\" in Proc. "
        "42nd Int. Conf. Machine Learning, PMLR 267, 2025, pp. 50817-50847."
    ),
    (
        "[11] J. Yoon, Y. Zhang, J. Jordon, and M. van der Schaar, \"VIME: Extending "
        "the success of self- and semi-supervised learning to tabular domain,\" in "
        "Advances in Neural Information Processing Systems, vol. 33, 2020."
    ),
    (
        "[12] L. Grinsztajn, E. Oyallon, and G. Varoquaux, \"Why do tree-based models "
        "still outperform deep learning on typical tabular data?\" in Advances in "
        "Neural Information Processing Systems, vol. 35, 2022."
    ),
    (
        "[13] G. Ke, Q. Meng, T. Finley, T. Wang, W. Chen, W. Ma, Q. Ye, and T.-Y. "
        "Liu, \"LightGBM: A highly efficient gradient boosting decision tree,\" in "
        "Advances in Neural Information Processing Systems, vol. 30, 2017."
    ),
    (
        "[14] L. Prokhorenkova, G. Gusev, A. Vorobev, A. V. Dorogush, and A. Gulin, "
        "\"CatBoost: Unbiased boosting with categorical features,\" in Advances in "
        "Neural Information Processing Systems, vol. 31, 2018."
    ),
    (
        "[15] K. Sohn, D. Berthelot, N. Carlini, Z. Zhang, H. Zhang, C. Raffel, E. D. "
        "Cubuk, A. Kurakin, and C.-L. Li, \"FixMatch: Simplifying semi-supervised "
        "learning with consistency and confidence,\" in Advances in Neural Information "
        "Processing Systems, vol. 33, 2020."
    ),
]


def word_count() -> int:
    text = " ".join(
        [TITLE, ABSTRACT, KEYWORDS]
        + [
            item.get("text", "")
            + " "
            + " ".join(item.get("items", []))
            + " "
            + " ".join(" ".join(row) for row in item.get("rows", []))
            for item in BODY
        ]
        + REFERENCES
    )
    return len(text.split())


if __name__ == "__main__":
    print(word_count())
