# AI Grant Writing Workshop: Hands-on Participant Guide

Welcome to the hands-on session! In this workshop, you will eliminate tedious administrative tasks in grant preparation.

---

## 1. Set up

Navigate to [Copilot](https://m365.cloud.microsoft/chat) and open the Agent Store by clicking
 *Agents*. Next, scroll down and click "New agent".

Send the following instruction to the Agent Builder:

> Your job is to help prepare grant applications.

A configuration panel will open where you can Edit the Instructions, Knowledge, Prompts and
Skills. We will focus on the latter: under "Skills" upload the following files:

- [make-gantt-chart.zip](https://github.com/luntergroup/health-in-context-agents-workshop/releases/latest/download/make-gantt-chart.zip)
- [salary-calculator.zip](https://github.com/luntergroup/health-in-context-agents-workshop/releases/latest/download/salary-calculator.zip)

Then click "Build", and start a chat after its creation.

## 2. Exercise: Salary & Personnel Budget Calculation in Copilot

Calculating personnel costs for grants can be tricky: it involves nation-wide CAO salary
scales, periodic step increments (periodiek), inflation bumps, and institutional surcharges.
Luckily, we've already added a Salary Calculator skill to our agent.

We will use the synthetic proposal text located in `[workshop/synthetic_grant_proposal.md](workshop/synthetic_grant_proposal.md)`.

Take a peek inside the file to see what is written, before you continue with the next steps.

> **Warm tip:** In Microsoft Copilot, you can attach or paste the text of the proposal into your chat, then run the prompts below.



### Step 1: Baseline Calculation

The proposal specifies the roles and FTEs, but **you** provide the salary scale and starting steps to Copilot.

Attach or paste the proposal text, and prompt Copilot:

> *"Based on the attached project proposal, calculate the personnel budget for both positions according to the UMCG CAO:*
> *- Postdoctoral Researcher: Scale A10, starting Step 11, annual step increment (periodiek) in August, 0.8 FTE*
> *- PhD Candidate: Scale PRO, starting Step 0, annual step increment in August, 1.0 FTE*
> *Please calculate the costs, accounting for the 18.05% employer surcharge, and provide the individual and combined totals."*

**What to look for:**

- Copilot executes the calculation for the supplied scales and steps across the 12-month appointment.
- It accounts for the August 1st step increments and applies the 18.05% surcharge.



### Step 2: "What-If" Exploration (Monkeying around)

Try asking a follow-up question in Copilot:

> *"What would the combined personnel budget be if we increase the postdoc from 0.8 FTE to 1.0 FTE?"*

or:

> *"If the funder provides a fixed total personnel budget of €150,000, how could we adjust the FTE of the postdoc to fit within this envelope?"*

---



## 3. Exercise: Project Schedule & Gantt Chart Generation

Grant reviewers expect clear visual timelines, but manually formatting Gantt charts in PowerPoint or Excel is time-consuming.

### Step 1: Generate the Project Schedule Table & Mermaid Gantt Chart

Prompt Copilot:

> *"Generate a Gantt chart in (plain text SVG format) from all work packages, tasks, and milestones using the skill. Do a quality assurance round, editing the SVG text as needed. Compress as zip file for download."*

**What to look for:**

- Copilot structures the four work packages (WP1 to WP4) cleanly into chronological phases.
- The generated Mermaid Gantt chart clearly lays out the quarters (Q4 2026 to Q3 2027) with tasks and milestones marked.



### Step 2: Customization & Formats

Test how Copilot adapts when you ask for adjustments:

> *"Can you also generate clean SVG code for this Gantt chart so I can insert it directly into a presentation or webpage?"*

or:

> *"How would the schedule shift if ethics approval for WP1 is delayed by 2 months?"*

---

