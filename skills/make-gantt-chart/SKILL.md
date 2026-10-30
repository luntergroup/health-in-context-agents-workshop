---
name: make-gantt-chart
description: Extracts project schedules (work packages, tasks, milestones) from text and generates a SVG Gantt chart. Use when a user asks to create a Gantt chart from an application, text, or schedule.
---

# Gantt Chart Maker

Extracts project schedule data (from unstructured text like grant applications or project proposals or spreadsheets) and generates a SVG Gantt chart.

## Workflow
1. **Extract Information**: Read the user's provided document/text. Identify work
   packages, individual tasks, milestones, the dates and durations. Put them in a table
   listing for each work package task, the start date and end date and for each
   milestone the due date.
2. **Plan a grid layout**: Based on the identified work packages and tasks, plan the
  layout of the grid so that the width of the table corresponds to the chronological
  order of the project. Divide the grid into columns so that work packages and tasks
  span one or more columns matching their timelines. For example, columns of 3 months
  (quarter) or 6 months (half a year). All rows have the same height. You are allowed to
  plan with code to write a script that calculates the table coordinates.
3. **Generate SVG**: Use the the instructions and style guide in the assets to construct
   a plain text scalable vector graphics (SVG) file.
5. **Refine**: If the user requests adjustments or color changes, implement and
   regenerate the SVG.
   - Ask for clarification if the user was too ambiguous to complete the task.

## Grid layout
Minimize the grid space, without compromising on fidelity. For example, work packages
are often executed serially if the output of one work package feeds into the next.
Reflect this in the order in the chart. Namely, horizontally align serial work packages
back-to-back, so that subsequent work packages are (partially) on the same rows (to save
vertical space).
When executed (partially) in parallel, place them below each other.

**Example**
Durations of the work packages:
| Work package    | What                               | Date              |
|-----------------|------------------------------------|-------------------|
| WP1: forework   | Task 1.1: Collect data             | Jan 2026–Dec 2026 |
|                 | Task 1.2: Analyze data             | Jul 2026–Dec 2026 |
| WP2: study      | Task 2.1: Do experiment            | Jul 2026–Jun 2027 |
|                 | Task 2.2: Write paper              | Jan 2027–Jun 2027 |
| WP3: validation | Task 3.1: Prospective study        | Jan 2027-Jun 2027 |
|                 | Task 3.2: Analyze data             | Jul 2027–Dec 2027 |
|                 | Task 3.3: Write another paper      | Jul 2027–Dec 2027 |
|                 | Milestone 3.1: Finished inclusion  | 31 Jun 2027       |

WP1 and WP3 can be placed back-to-back:
|        2026         |        2027         |
|----------|----------|----------|----------|
|    H1    |    H2    |    H1    |    H2    |
|---------------------|---------------------|
| WP1                 | WP3                 |
|---------------------|---------------------|
| Task 1.1            | Task 3.1◆|          |
|----------|----------|---------------------|
|          | Task 1.2 |          | Task 3.2 |
|----------|----------|          |----------|
|                     |          | Task 3.3 |
|----------|----------|----------|----------|
|          | WP2                 |          |
|----------|---------------------|----------|
|          | Task 2.1            |          |
|----------|----------|----------|----------|
|          |          | Task 2.2 |          |
|----------|----------|----------|----------|

## Quality assurance checklist
Before presenting your work to the user, do a quality control check.
- [ ] Validate the grid layout:
   * [ ]Test that the coordinates of the task's rectangles are indeed multiples of the
        minor unit (i.e., the chart is indeed a table/grid).
   * [ ] Check the serial work packages are aligned horizontally (minimizing vertical space).
- [ ] Focus on the chart. The rest of the non-visual details go in the grant application.
- [ ] Ensure that the chart is entirely visible (and not clipped because it does not fit the
   viewport).
- [ ] Verify that the SVG XML correctly implemented the rendering recipe.
- [ ] Test the integrity of the SVG XML (i.e., there are no errors).

## Assets
The following files are here to guide the construction of the table:
- `gantt_schema.md`: Style Gantt chart according these colours and fonts.
- `render_recipe.md`: Step-by-step instructions how to construct the table.