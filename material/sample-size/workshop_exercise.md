# Exercise: Explore sample size and power

## Scenario

A research team is planning a hypothetical two-arm randomized trial. The primary outcome is a continuous score measured once after treatment. Participants will be allocated equally to an experimental treatment and a control group.

The team wants to understand how many participants are needed to detect a difference between the group means. It expects the outcome to have a standard deviation of 10 points in each group, but is uncertain about the treatment effect. Explore differences of 2, 3, and 4 points.

## 1. Generate a power graph

Start a new conversation with your AI assistant and try the following prompt:

> We are planning a two-arm randomized trial with equal group sizes and a continuous primary outcome. Assume independent, normally distributed outcomes and a standard deviation of 10 points in both groups. We plan to compare group means using a two-sided independent-samples t-test at a significance level of 0.05.
>
> Use simulation to estimate power for sample sizes from 20 to 500 participants per group and for true differences in group means of 2, 3, and 4 points. Create a graph with sample size per group on the x-axis and estimated power on the y-axis. Use a different color for each effect size and add a horizontal line at 80% power.
>
> Explain the assumptions, state how many simulated trials you used for each point, and provide the code and a downloadable graph.

Inspect the graph and the assistant's explanation:

- What does 80% power mean in this scenario?
- How does the required sample size change with the assumed effect size?
- Are the axes, effect sizes, and assumptions clearly labeled? Is sample size shown per group or for the entire trial?
- Are the simulation results smooth enough to interpret? What happens if you ask for more simulated trials?

## 2. Explore the assumptions

Choose one or more follow-up questions:

> Approximately how many participants **per group** are needed for 80% power for each effect size? Also give the total for the trial. Explain how you estimated the crossing point from the simulation.

> How does the graph change if the standard deviation is 12 rather than 10 points? Show the original and new results in a way that is easy to compare.

> If 15% of recruited participants are expected to drop out before the outcome is measured, how many should we recruit per group for each effect size? Show the calculation and round up to whole participants.

For the dropout question, distinguish the number of participants needed **with outcome data** from the number to recruit. The simple adjustment assumes dropout is 15% in each group and does not otherwise change the analysis.

## 3. Validate the result

Ask the assistant to check its simulation against an analytical power calculation:

> Check the simulated power for an effect of 3 points, a standard deviation of 10 points, and 175 participants per group against an analytical calculation for the same two-sided independent-samples t-test. Show both estimates, state the number of simulations, and give the simulation's approximate 95% Monte Carlo uncertainty interval. Explain whether any difference is consistent with simulation uncertainty.

The analytical power should be approximately **80%** for this example. It need not match the simulated estimate exactly: simulation itself introduces random variation. If the results differ beyond the expected simulation uncertainty, ask the assistant to investigate its code and assumptions. For example, check that it uses 175 participants **in each group**, the same significance level, and the same test in both calculations.

## 4. Discuss

- Which assumptions had the greatest influence on the sample size?
- Did the assistant make any choices you had to clarify or correct?
- Could another researcher reproduce and check the graph using the supplied code?
- What additional information would you need before using the result to plan a real study?

Optional: ask the assistant to improve the graph for a grant application or presentation, then check that the revised version still represents the calculations accurately.
