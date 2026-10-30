
## Implementing a published model

Agentic AI can read a paper, implement and run the statistical model it describes, and check the 
published results.  Provided that data are available, this makes "reproducible science" genuinely 
achievable.

This example shows this using a recently published paper.  The underlying data are freely available, 
and where reproducing the results is indeed possible.

The paper concerns a model that predicts the risk of all-cause mortality in a data set covering 
24,000 people followed for 8 years.  The data includes a large number of predictor variables.

Trying this out, it turned out that the paper did not describe a few choices about data preparation
and modeling, and the AI had to make a few guesses.  Nevertheless the results are very close to the
published numbers.

The AI also found that a few choices made by the authors were not optimal:

- different follow-up intervals were not taken into account
- no imputation was done; and missingness turned out to be informative for certain variables

Taking these aspects into account only has a very minor influence on the predictive value of the
model, but it does show markedly improved calibration.


## Practicalities

Copilot cannot access the paper as it's behind a paywall.  I have therefore attached the paper as a .pdf.

Copilot also cannot any data from the internet, so they have been added too, as a .zip file.  The interface
we use (Copilot 365) does not allow uploading .zip files (sigh), so I renamed it to data.zip.txt - Copilot
then handles it fine.

For convenience the task itself is explained in Task.md.  Copilot can be directed to this file and execute
the task.  It could of course be given in a prompt.


## Running it

Upload the 3 files "Agogo-et-al-2025.pdf", "data.zip.txt", "Task.md"

Then type as a prompt "Perform task 1", followed by "Perform task 2".

Ask it to compare these results to the published "super learner".


## How well does it work

I compared Copilot with Claude.  Claude can download the data itself, which is convenient, but not
a real practical difference.

Claude puts the data and intermediate results in folders on your own computer.  I find that pleasant
to work with; it makes it easy to access the data and results yourself.

Copilot makes more small mistakes, and gives less detail about the choices it makes.  For example,
missing data and "0" values are encoded in an unusual way; Claude handled this well, but with
Copilot this initially went wrong.

Copilot initially added the follow-up time as a predictor variable in a Cox model, causing 
convergence problems.  One time I asked Copilot to fix the convergence problem, and without further 
hints it found the problem itself and fixed it.  Another time I explicitly told it to remove the 
follow-up time from the predictors, but then it got confused and did not manage to fix the problem.

This was with Copilot in the "auto" setting.  I got better results straight away when I selected the
best model, currently "GPT 5.6 Sol Think Deeper".  Only then it found that Cox regression (without
the age^2 term) gave good results, and with best calibration.
