# Project Proposal: AI-Assisted Treatment Planning in Pleural Mesothelioma

**Grant Call:** National Oncology Foundation – AI in Healthcare Pilot
**Host Institution:** University Medical Center Groningen (UMCG)
**Principal Investigator:** Dr. A. J. de Vries (Department of Epidemiology / Medical Statistics)
**Clinical Co-Investigator:** Prof. Dr. E. B. Bakker (Department of Pulmonary Diseases)
**Project Duration:** 12 Months (01-10-2026 to 30-09-2027)

---

## 1. Background

Pleural mesothelioma (PM) is a rare, aggressive malignancy of the pleural lining with poor median survival (< 18 months). With the recent Dutch reimbursement approval for combined immune checkpoint inhibitors (nivolumab + ipilimumab), clinicians face a critical dilemma: determining which patients derive substantial benefit from expensive, potentially toxic immunotherapy versus conventional platinum-based chemotherapy.

This pilot project aims to develop an **interpretable AI-driven clinical decision-support tool** that pairs PM patients with the optimal treatment strategy. Leveraging routine clinical biobank data from the regional hospital oncology cohort and external validation data from an independent partner cancer center, we will construct a constrained Bayesian neural network capable of isolating true predictive treatment effects from underlying prognostic factors.

---

## 2. Research Objectives

1. **Feature Harmonization & Prior Elicitation:** Extract and harmonize multi-modal routine clinical care data (demographics, blood cell counts, inflammatory markers, liver/kidney profiles) and formalize prior clinical knowledge from published trials into Bayesian priors.
2. **Predictive Modeling:** Develop an interpretable neural network architecture with partitioned hidden units to distinguish prognostic factors from predictive biomarker–treatment interactions.
3. **Interactive Clinical Tool:** Deliver a prototype "What-If" decision-support interface that enables oncologists to simulate predicted survival under alternative treatment regimens.
4. **External Validation:** Evaluate model generalizability on an independent multi-center validation cohort (~300 cases).

---

## 3. Work Packages and Schedule

The 12-month pilot project is organized into four sequential and overlapping work packages:

### Work Package 1: Biobank Data Harmonization
* **Full Title:** Data Extraction, Quality Control & Biobank Harmonization
* **Period:** October 2026 – March 2027 (Q4 2026 – Q1 2027, Months 1–6)
* **Lead:** PhD Candidate (with Postdoc supervision)
* **Tasks:**
  * **Task 1.1: Extract EHR Data (Oct 2026 – Dec 2026 / Q4 2026):** Extract electronic health records and institutional biobank data for mesothelioma patients treated with chemotherapy or immunotherapy.
  * **Task 1.2: Curate Clinical Variables (Jan 2027 – Mar 2027 / Q1 2027):** Curate and time-align clinical variables, laboratory values (CRP, NLR, LDH, albumin), and survival outcomes.
* **Milestone M1 (End Mar 2027 / End Q1 2027):** Curated, quality-controlled cohort dataset frozen and documented.

---

### Work Package 2: Bayesian Baseline Modeling
* **Full Title:** Prior Elicitation & Baseline Bayesian Model
* **Period:** January 2027 – June 2027 (Q1 2027 – Q2 2027, Months 4–9)
* **Lead:** Postdoctoral Researcher (with PhD Candidate)
* **Tasks:**
  * **Task 2.1: Elicit Literature Priors (Jan 2027 – Mar 2027 / Q1 2027):** Extract hazard ratios and parameter distributions from international mesothelioma literature (CheckMate 743, ASCO guidelines) to construct informative Bayesian priors.
  * **Task 2.2: Train Baseline Model (Apr 2027 – Jun 2027 / Q2 2027):** Implement and train a linear Bayesian survival baseline model incorporating treatment interaction terms.
* **Milestone M2 (End Jun 2027 / End Q2 2027):** Baseline linear model validated; benchmark predictive performance established.

---

### Work Package 3: Interpretable Decision Tool
* **Full Title:** Interpretable Neural Network & "What-If" Decision Tool
* **Period:** April 2027 – September 2027 (Q2 2027 – Q3 2027, Months 7–12)
* **Lead:** Postdoctoral Researcher & AI Unit
* **Tasks:**
  * **Task 3.1: Bipartite Neural Network (Apr 2027 – Jun 2027 / Q2 2027):** Develop a sparse neural network with bipartite hidden layer structures to strictly separate prognostic markers from predictive treatment response.
  * **Task 3.2: Build Clinical Tool (Jul 2027 – Sep 2027 / Q3 2027):** Build an interactive clinical prototype allowing oncologists to simulate expected survival curves under chemotherapy vs. immunotherapy.
* **Milestone M3 (End Sep 2027 / End Q3 2027):** Interactive decision-support software prototype functional and tested locally.

---

### Work Package 4: Validation & Dissemination
* **Full Title:** External Cohort Validation & Scientific Dissemination
* **Period:** July 2027 – September 2027 (Q3 2027, Months 10–12)
* **Lead:** PhD Candidate & Postdoctoral Researcher
* **Tasks:**
  * **Task 4.1: Validate External Cohort (Jul 2027 – Sep 2027 / Q3 2027):** Apply the model to the external validation cohort (~300 cases) to evaluate out-of-distribution discrimination and calibration.
  * **Task 4.2: Manuscript & Final Report (Jul 2027 – Sep 2027 / Q3 2027):** Draft and submit peer-reviewed manuscript; present findings at a multidisciplinary thoracic oncology meeting.
* **Milestone M4 (End Sep 2027 / End Q3 2027):** Peer-reviewed manuscript submitted; final project report delivered to funding body.

---

## 4. Requested Personnel & Resource Budget

### Personnel Justification

#### 1. Postdoctoral Researcher (AI & Medical Statistics)
* **Appointment Period:** 01-10-2026 to 30-09-2027 (12 months)
* **Effort:** 0.8 FTE
* **Institutional Employer Surcharge (Opslag):** 18.05%

#### 2. PhD Candidate / Junior Researcher (Oncology & Data Science)
* **Appointment Period:** 01-10-2026 to 30-09-2027 (12 months)
* **Effort:** 1.0 FTE
* **Institutional Employer Surcharge (Opslag):** 18.05%

### Non-Personnel Budget
* **Compute & Secure Cloud Storage:** €2,500
* **Open Access Publication Costs:** €3,000
* **Dissemination / Conference Attendance:** €1,500
