## Gantt chart rendering receipe
Here are step-by-step instructions how to build the Gantt chart.
- Plan the dimensions of the grid so that the width of the table corresponds to the
  chronological order of the project. Divide the grid into columns. Work packages and
  tasks span one or more columns, depending on their duration. For example, columns of 3
  months (quarter) or 6 months (half a year). All rows have the same height.
- Introduce a two-level table header with bold faced text labels placed inside the centre of
  the cells:
   * A major time granularity block on the first header row (e.g., years; example text:
     "Year 1 (2026)") spanning multiple columns. Put a thin black solid line border
     around each block.
   * Divide each major time block into minor time units (the columns) on the second
     header row (e.g., three month duration; example text: "Q2"). Put a thin black solid
     line border around these columns.
- For each work package:
   * Render a header:
      - The header is a rectangle. The width corresponds to the duration, and it's
        placement follows the chronological order of project.
      - Use the second lightest tone as background color for the header, and a thin
        black solid line border.
      - Label each header by placing text inside, indicating the work package title (or
        an abbreviation thereof, if needed).
   * Below the header, make one separate row per work package task. For each task:
      - Render the row as a rectangle the size of the duration, following the
        chronological order of the work package.
      - Use the lightest color tone (corresponding to the work package color family) to
        fill the rectangle, with a black solid line border.
      - Place a left aligned label inside, indicating the task (e.g., "Task 2.1").
   * Demarcate the entire work package using an an enveloping solid black line (the same
     thickness as the individual tasks).
   * Respect the grid space minimization constraint: determine if this work package
      logically follows, and therefore can be placed back-to-back with, a preceding WP.
- Add an enveloping solid line around the entire grid.
- Place diamonds at the dates of the milestones in the corresponding tasks (with the
  diamond horizontally centred around the date).
   * Height of the diamond: 80% of the row. Fill with the corresponding
     workpackage base tone colour, and a black solid line border.
- Ensure that labels are always ordered on top, should the diamonds overlap text.
- Add extra margin around the illustration (i.e., a larger viewport).