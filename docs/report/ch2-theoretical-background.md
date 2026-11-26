# Chapter 2. Model-driven DSS Theoretical Background

Author: Hồ Ngọc An · Draft: 2026-11-26

This chapter introduces the concepts that the system is built on: decision support systems (DSS), the model-driven DSS category, the decision-making process, and multi-criteria decision making (MCDM). It ends by explaining why TOPSIS was chosen. The full mathematical procedure of TOPSIS is given in Chapter 4.

## 2.1 Decision Support Systems

A **decision support system** is an interactive computer-based information system that helps decision makers use data and models to solve semi-structured or unstructured problems [Sprague & Carlson, 1982; Turban et al., 2011]. A DSS does not replace the decision maker. It improves the quality and consistency of a decision by organising information, applying analytical models, and presenting results in a form the user can understand and question.

### 2.1.1 Structured, semi-structured, and unstructured decisions

Gorry and Scott Morton (1971) classify decisions by how well their solution procedure can be defined:

| Type | Description | Example in housing |
| --- | --- | --- |
| Structured | Routine; a fixed procedure gives the answer | Removing rooms above the budget |
| Semi-structured | Part of the problem can be modelled, part needs human judgement | Ranking rooms by several weighted criteria |
| Unstructured | No agreed procedure; depends on intuition | Deciding whether a landlord seems trustworthy |

Student housing selection is a **semi-structured** decision. The criteria and data can be modelled, but the importance of each criterion is personal, and the final choice usually follows a visit. This is the type of problem a DSS is designed for.

### 2.1.2 The decision-making process

Simon (1960) describes decision making in phases. The table maps each phase to the proposed system.

| Phase | Meaning | Support provided by the system |
| --- | --- | --- |
| Intelligence | Recognise the problem and collect information | A dataset of rooms with standardised criteria |
| Design | Build alternatives and a model to evaluate them | Five criteria, cost/benefit directions, budget filter, TOPSIS model |
| Choice | Evaluate alternatives and select one | Ranked list, top three rooms, calculation details |
| Implementation | Act on the decision | Outside the system (visiting and renting the room) |

### 2.1.3 Components of a DSS

A classic DSS architecture has three main subsystems [Sprague & Carlson, 1982]:

1. **Data management subsystem** – stores and validates the data used in decisions. In this project: `data/rooms_sample.csv` and the validator `load_rooms` in `src/housing_dss/data.py`.
2. **Model management subsystem** – contains the analytical models. In this project: the TOPSIS algorithm in `src/housing_dss/topsis.py` and the criterion definitions in `src/housing_dss/criteria.py`.
3. **User interface (dialogue) subsystem** – lets the user enter preferences and see results. In this project: the Streamlit application (`app.py` and `src/housing_dss/ui/`).

The user, who supplies the budget and weights and interprets the results, is often treated as a fourth component.

## 2.2 Model-driven DSS

Power (2002) classifies DSS by the main component that drives the support:

| Category | Driving component | Typical example |
| --- | --- | --- |
| Data-driven | Access to and manipulation of large data sets | Dashboards, OLAP reports |
| **Model-driven** | **Quantitative models (optimisation, simulation, decision analysis)** | **Scoring and ranking tools, scheduling models** |
| Knowledge-driven | Expert rules and knowledge bases | Diagnostic expert systems |
| Document-driven | Retrieval of unstructured documents | Policy and contract search |
| Communication-driven | Collaboration among several decision makers | Group decision tools |

A **model-driven DSS** uses relatively small amounts of data and focuses on a decision model that the user manipulates through parameters. Its key characteristics are:

- the value comes from the model, not from the volume of data;
- users change parameters (here, the budget and criterion weights) and observe how the result changes ("what-if" analysis);
- the model should be transparent enough for users to trust and explain the output.

The Student Housing DSS fits this category. It works with a small dataset (30 rooms), its core is a decision-analysis model (TOPSIS), and its main interaction is changing weights to see how the ranking responds.

## 2.3 Multi-criteria Decision Making

**Multi-criteria decision making (MCDM)** is a field of operations research that supports decisions involving several, often conflicting, criteria. MCDM problems are usually divided into:

- **Multi-objective decision making (MODM):** the alternatives are not listed in advance and are defined by constraints over continuous variables (for example, optimisation models).
- **Multi-attribute decision making (MADM):** a finite set of alternatives is evaluated on a finite set of attributes.

Housing selection is a **MADM** problem: there is a finite list of rooms (alternatives) and five attributes (criteria).

### 2.3.1 Elements of a MADM problem

| Element | Notation | In this project |
| --- | --- | --- |
| Alternatives | $A_1, \dots, A_m$ | Rooms that pass the budget filter |
| Criteria | $C_1, \dots, C_n$ | Cost, distance, area, security, amenities ($n = 5$) |
| Decision matrix | $X = [x_{ij}]$ | Value of room $i$ on criterion $j$ |
| Weights | $w_1, \dots, w_n$ | Importance set by the student, normalised to sum to 1 |
| Criterion type | Cost or benefit | Cost: lower is better; Benefit: higher is better |

Two technical issues are common to MADM methods:

- **Different units.** Criteria are measured in VND, km, m², and score points. Values must be **normalised** to a common, unit-free scale before they can be combined.
- **Different directions.** Cost criteria must be treated so that smaller values are preferred, and benefit criteria so that larger values are preferred.

### 2.3.2 Common MADM methods

| Method | Main idea | Strengths | Weaknesses for this project |
| --- | --- | --- | --- |
| Simple Additive Weighting (SAW) | Weighted sum of normalised values | Very simple, easy to explain | Fully compensatory; does not consider distance to the best and worst options |
| AHP [Saaty, 1980] | Pairwise comparisons build weights and scores | Structured way to derive weights | Many pairwise questions; heavy for students; consistency checks needed |
| TOPSIS [Hwang & Yoon, 1981] | Rank by closeness to an ideal and distance from an anti-ideal solution | Simple computation, intuitive geometric meaning, handles cost and benefit criteria directly | Results depend on the current set of alternatives (rank reversal) |
| VIKOR [Opricovic & Tzeng, 2004] | Compromise ranking based on group utility and individual regret | Good for compromise solutions | Extra parameter and more complex explanation |
| ELECTRE / PROMETHEE | Outranking relations between pairs of alternatives | Handles partial non-compensation | More parameters (thresholds, preference functions); harder to explain to end users |

## 2.4 TOPSIS

**TOPSIS** (Technique for Order of Preference by Similarity to Ideal Solution) was introduced by Hwang and Yoon (1981). Its principle is that the best alternative should be **closest to the positive ideal solution** and **farthest from the negative ideal solution**.

- The **positive ideal solution** $A^+$ takes the best value on each criterion: the lowest cost and distance, and the highest area, security, and amenities among the eligible rooms.
- The **negative ideal solution** $A^-$ takes the worst value on each criterion.
- Each room receives a **relative closeness score** $C_i \in [0, 1]$; the closer to 1, the better the room relative to the others.

The main steps are: build the decision matrix, normalise it (vector normalisation in this project), apply the weights, determine $A^+$ and $A^-$, compute the Euclidean distances $D_i^+$ and $D_i^-$, and calculate

$$C_i = \frac{D_i^-}{D_i^+ + D_i^-}.$$

The detailed formulas and a manually calculated three-room example are presented in Chapter 4.

TOPSIS is one of the most widely applied MADM methods, with applications in supplier selection, location selection, and many other ranking problems [Behzadian et al., 2012].

## 2.5 Why TOPSIS for Student Housing Selection

TOPSIS was chosen for the following reasons:

1. **Matches the problem type.** Housing selection has a finite set of rooms and a small number of quantitative criteria, which is the standard MADM setting for TOPSIS.
2. **Handles cost and benefit criteria naturally.** Cost and distance (lower is better) and area, security, and amenities (higher is better) are treated directly when building $A^+$ and $A^-$.
3. **Easy for students to use.** The user only sets five weights. There is no long list of pairwise comparisons as in AHP or thresholds as in outranking methods.
4. **Explainable.** The idea "closest to the best, farthest from the worst" is intuitive, and the intermediate values ($D^+$, $D^-$, $C$) can be shown in the interface. This supports the transparency expected from a model-driven DSS [see also Explainable TOPSIS, 2023].
5. **Supports sensitivity analysis.** The calculation is fast, so the ranking can be recomputed instantly whenever the student changes the weights or budget.
6. **Verifiable.** With only a few rooms, the full calculation can be done by hand and compared with the software output (Chapter 4 and Chapter 6).

### Known limitations of TOPSIS

- **Rank reversal.** Adding or removing an alternative changes $A^+$ and $A^-$, which can change the order of other rooms. The system therefore presents the score as relative to the current eligible set.
- **Full compensation.** A very poor value on one criterion can be offset by good values on others. The budget is applied as a hard filter before TOPSIS to prevent unaffordable rooms from being ranked.
- **Weights are subjective.** Results depend on the weights chosen. Preset profiles and live sensitivity analysis help users see this effect.
- **Equal score intervals.** The 1–5 scores for security and amenities are treated as equally spaced numerical values.

## 2.6 Summary

Student housing selection is a semi-structured, multi-attribute decision. A model-driven DSS suits it because the value lies in a transparent decision model that the student can adjust, not in large data volumes. Among MADM methods, TOPSIS offers a good balance between simplicity, explainability, and correct handling of cost and benefit criteria. Chapter 3 defines the requirements and data used by the model, and Chapter 4 presents the TOPSIS calculation in detail.

## References

<!-- Check every reference against the original source and apply the citation style required by the course before final submission. -->

- Behzadian, M., Khanmohammadi Otaghsara, S., Yazdani, M., & Ignatius, J. (2012). A state-of the-art survey of TOPSIS applications. *Expert Systems with Applications, 39*(17), 13051–13069.
- Gorry, G. A., & Scott Morton, M. S. (1971). A framework for management information systems. *Sloan Management Review, 13*(1), 55–70.
- Hwang, C. L., & Yoon, K. (1981). *Multiple Attribute Decision Making: Methods and Applications*. Springer.
- Opricovic, S., & Tzeng, G. H. (2004). Compromise solution by MCDM methods: A comparative analysis of VIKOR and TOPSIS. *European Journal of Operational Research, 156*(2), 445–455.
- Power, D. J. (2002). *Decision Support Systems: Concepts and Resources for Managers*. Quorum Books.
- Saaty, T. L. (1980). *The Analytic Hierarchy Process*. McGraw-Hill.
- Simon, H. A. (1960). *The New Science of Management Decision*. Harper & Row.
- Sprague, R. H., & Carlson, E. D. (1982). *Building Effective Decision Support Systems*. Prentice-Hall.
- Turban, E., Sharda, R., & Delen, D. (2011). *Decision Support and Business Intelligence Systems* (9th ed.). Pearson.
- Towards Explainable TOPSIS (2023). arXiv:2306.07706. https://arxiv.org/abs/2306.07706
