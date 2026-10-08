---
name: salary-calculator
description: Calculate researcher salary costs based on the 2026 UMCG salary grid. Use when asked to determine wage costs, estimate project budgets, or calculate researcher salaries over a specific time period.
---

# Salary Calculator

## Overview

This skill enables calculation of UMCG researcher salary costs by referencing the official
2026 salary grid. It accounts for time-based thresholds (inflation/CAO bumps) and annual step
increments.

## Periodicity

**Periodicity** (Periodiek) is the calendar month (1-12) when an employee receives their
automatic annual salary step increment (e.g., advancing from step 11 to 12).

For example, a periodicity of `8` (August) means the employee's "step" increments on August
1st every year.

## Usage

To perform a calculation, use the `calculate_salary` function from the bundled `salary.py`
script.

### Python Example

```python
import sys
from pathlib import Path

# Add the skill scripts directory to sys.path to import the module
# Adjust the path based on where the skill is installed (workspace or user scope)
# You can find the script path by searching for 'salary.py' in the skill folder
skill_scripts_path = Path("<path_to_skill>/scripts")
sys.path.append(str(skill_scripts_path))

from salary import calculate_salary

total = calculate_salary(
    scale="A10",
    start_step=11,
    periodicity_month=8,
    start_date_str="01/10/2026",
    end_date_str="01/10/2027",
    fte=0.6,
    surcharge_pct=18.05
)

print(f"Total Salary Cost: {total:.2f}")
```

### Parameters

- **scale**: Salary scale string (e.g., `"A10"`). Must match the grid.
- **start_step**: Initial salary step (e.g., `11`).
- **periodicity_month**: Calendar month (1-12) of the annual increment.
- **start_date_str**: Calculation start date (`DD/MM/YYYY`).
- **end_date_str**: Calculation end date (`DD/MM/YYYY`).
- **fte**: Full-Time Equivalent (e.g., `0.6`).
- **surcharge_pct**: Overhead surcharge percentage (e.g., `18.05`). Depends on the funder (commercial, charity, etc.).

These  parameters are employee specific and have to be elicited:
- Scale
- Start step
- Periodicity month
- FTE

## Resources

- **assets/salary_grid.csv**: The hardcoded salary grid containing monthly base salaries across various date thresholds.
- **scripts/salary.py**: The functional implementation of the calculation logic.
