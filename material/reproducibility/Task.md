
## Re-analysis of a mortality prediction model

Paper: Agogo & Mwambi (2025), Ann Epidemiol 102:36–47, doi:10.1016/j.annepidem.2024.12.015
Data: NHANES 2009–2016 with linked public-use mortality files on ~24000 individuals.

NHANES data can be obtained from`https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/<year>/DataFiles/`.
However as Copilot cannot download files, the data are provided in data.zip.txt.  It has a
.txt extension so it can be uploaded, but it is a regular .zip file.

### 1. Reproduce

Re-implement only the paper's logistic regression, exactly as described (complete cases,
outcome "dead by 31 Dec 2019"). Where the description is ambiguous, choose the option that
reproduces the published sample sizes. Compare with Table 3, training and test, focusing 
only on AUC-ROC and AUC-PR, which do not involve thresholds.

### 2. Extend, step by step

Each step builds on the previous one:

a. **Observation window.** Follow-up to 2019 is much shorter for later survey cycles.
   Add the potential follow-up (months from exam to 31 Dec 2019) as predictor to the 
   logistic regression.  Do not use the recorded follow-up time: for decedents it is 
   time to death.

b. **Survival model.** Fit a Cox model on time since exam instead. Use it to predict each
   person's risk of death by 31 Dec 2019, and compare it with (a).

c. **Age.** Add a quadratic age term to both (a) and (b), and keep the better model.

d. **All participants.** Using the best model from (c), drop the complete-case restriction:
   - set marital status to "not married" for those under 20 (they were not asked);
   - drop household income;
   - impute all other missing values with MICE, without using the outcome;
   - add missingness indicators (except for marital status); variables that are always
     missing together share one indicator.

   Evaluate on the full test set.  In addition to the AUC metrics also report the log
   loss, and the mean predicted risk, and show this alongside the true event rate.

