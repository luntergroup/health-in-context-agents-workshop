# Putting AI to work: A hands-on workshop

Material for the Health in Context (HiC) workshop.

Participant pages: <https://luntergroup.github.io/health-in-context-agents-workshop/>

![QR code for https://luntergroup.github.io/health-in-context-agents-workshop/](docs/workshop-qr.png)

The world is abuzz with talk about AI. Most of us now have experience using chatbots for complex queries, editing text and making pictures. A more recent development is "agentic AI"—letting AI do actual work, such as manipulating files, writing and testing code, and setting up and executing complex analyses.

For tasks that involve multiple steps and would otherwise require substantial manual work, agentic AI can be of tremendous help. Using it effectively, however, involves more than simply giving it a task: it also means setting up the agent for the work at hand—for example by providing instructions, tools, skills and relevant context—and designing a workflow in which its work can be reviewed and verified. But how exactly does this work? That is what this workshop is about.

Through practical examples from research work—exploring sample size and statistical power for a planned trial, reproducing and extending a published analysis, and preparing parts of a grant application with a custom agent—we will explore how to specialize an agent for a particular task, delegate multi-step work, and check whether the result is actually what you intended.

By the end, you will understand the basic principles of working with agentic AI and have a starting point for applying them to your own work.

No preparation is required—just bring your laptop.

## Exercises

The workshop uses Microsoft Copilot. Follow along on the [participant pages](https://luntergroup.github.io/health-in-context-agents-workshop/). Source material is in [`material/`](material/).

1. **Sample size and power.** Plot analytical power curves for a hypothetical two-arm trial and use follow-up prompts to explore how assumptions change the graph and required sample size. See [`material/sample-size/workshop_exercise.md`](material/sample-size/workshop_exercise.md).
2. **Research and reproducibility.** Re-implement a published mortality model from a paper and public data, then extend it step by step and compare the choices with the published analysis. See [`material/reproducibility/`](material/reproducibility/).
3. **Grant preparation.** Build a Copilot agent, give it skills for personnel costs and a project timeline, and use them on an example grant proposal. See [`material/grant/workshop_exercises.md`](material/grant/workshop_exercises.md).
