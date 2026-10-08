import csv
from datetime import datetime
from pathlib import Path

def _get_applicable_salary(grid_data: dict, scale_step: str, current_date: datetime) -> float:
    """Looks up the applicable salary for a given scale-step and date.
    
    Uses the hardcoded date thresholds from the spreadsheet columns to determine
    the correct salary rate for a specific point in time.

    Args:
        grid_data: The dictionary containing the salary grid rows keyed by scale-step.
        scale_step: The concatenated scale and step identifier (e.g., "A10-11").
        current_date: The date for which the salary should be evaluated.

    Raises:
        KeyError: If the scale_step is not present in the provided grid_data.
        ValueError: If the current_date is earlier than the earliest supported data,
            or if the target cell is empty.

    Returns:
        The applicable monthly base salary.
    """
    if scale_step not in grid_data:
        raise KeyError(f"Scale and step '{scale_step}' not found in the salary data. Valid combinations must strictly match the spreadsheet.")

    row = grid_data[scale_step]
    
    # Define thresholds in chronological order corresponding to spreadsheet columns
    thresholds = [
        ("2023-11-01", datetime(2023, 11, 1)),
        ("2024-01-01", datetime(2024, 1, 1)),
        ("2024-05-01", datetime(2024, 5, 1)),
        ("2025-01-01", datetime(2025, 1, 1)),
        ("2025-07-01", datetime(2025, 7, 1)),
        ("2026-01-01", datetime(2026, 1, 1)),
        ("2026-07-01", datetime(2026, 7, 1)),
        ("2027-01-01", datetime(2027, 1, 1)),
        ("2028-01-01", datetime(2028, 1, 1)),
        ("2029-01-01", datetime(2029, 1, 1)),
        ("2030-01-01", datetime(2030, 1, 1)),
        ("2031-01-01", datetime(2031, 1, 1)),
        ("2032-01-01", datetime(2032, 1, 1)),
    ]

    if current_date < thresholds[0][1]:
        raise ValueError(f"Calculations before {thresholds[0][0]} are not supported by the current salary framework.")

    # Find the most recent threshold passed
    applicable_col = thresholds[0][0] 
    for col_name, t_date in thresholds:
        if current_date >= t_date:
            applicable_col = col_name
        else:
            break
            
    val = row.get(applicable_col)
    if not val or str(val).strip() == '' or str(val).lower() == 'nan':
        raise ValueError(f"No salary value defined for '{scale_step}' at period '{applicable_col}'.")
        
    return float(val)


def calculate_salary(
    scale: str,
    start_step: int,
    periodicity_month: int,
    start_date_str: str,
    end_date_str: str,
    fte: float,
    surcharge_pct: float,
    grid_file_path: Path = None
) -> float:
    """Calculates the total salary cost over a designated period.
    
    This calculation utilizes the exact hardcoded lookup values from the 
    underlying spreadsheet grid, segmenting the date range whenever a 
    spreadsheet threshold is crossed or an annual step increment occurs.

    Args:
        scale: Salary scale (e.g., "A10").
        start_step: Starting step (e.g., 11).
        periodicity_month: The calendar month (1-12) when the employee receives their automatic annual step increment (e.g., advancing from step 11 to 12).
        start_date_str: Start date in DD/MM/YYYY format.
        end_date_str: End date in DD/MM/YYYY format.
        fte: Full-Time Equivalent fraction (e.g., 0.6).
        surcharge_pct: Overhead surcharge percentage (e.g., 18.05).
        grid_file_path: Path to the extracted salary grid. Resolves automatically if None.

    Returns:
        Total accumulated salary cost over the specified period.
    """
    if grid_file_path is None:
        # Automatically resolve the grid relative to this script inside the skill folder
        grid_file_path = Path(__file__).parent.parent / "assets" / "salary_grid.csv"

    # Load grid purely functionally
    grid_data = {}
    max_steps = {}
    with open(grid_file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            scale_step_key = row['scale_step']
            grid_data[scale_step_key] = row
            if '-' in scale_step_key:
                s, st = scale_step_key.split('-', 1)
                st_int = int(st)
                max_steps[s] = max(max_steps.get(s, 0), st_int)

    if scale not in max_steps:
        raise ValueError(f"Invalid scale '{scale}'. Not found in the salary grid.")

    start_date = datetime.strptime(start_date_str, "%d/%m/%Y")
    end_date = datetime.strptime(end_date_str, "%d/%m/%Y")

    if end_date <= start_date:
        return 0.0

    total_cost = 0.0
    current_date = start_date
    current_step = start_step

    # Track all column bump thresholds to dynamically split calculation segments
    threshold_dates = [
        datetime(2023, 11, 1),
        datetime(2024, 1, 1),
        datetime(2024, 5, 1),
        datetime(2025, 1, 1),
        datetime(2025, 7, 1),
        datetime(2026, 1, 1),
        datetime(2026, 7, 1),
        datetime(2027, 1, 1),
        datetime(2028, 1, 1),
        datetime(2029, 1, 1),
        datetime(2030, 1, 1),
        datetime(2031, 1, 1),
        datetime(2032, 1, 1),
    ]

    while current_date < end_date:
        # 1. When does the next step bump occur?
        next_period_year = current_date.year if current_date.month < periodicity_month else current_date.year + 1
        next_periodicity = datetime(next_period_year, periodicity_month, 1)

        # 2. When does the next column/inflation bump occur?
        next_threshold = datetime(9999, 1, 1)
        for t_date in threshold_dates:
            if t_date > current_date:
                next_threshold = t_date
                break
                
        # 3. The current computational segment ends whichever comes first
        segment_end = min(next_periodicity, next_threshold, end_date)

        # 4. Math logic for calculating cost of this segment
        months_diff = (segment_end.year - current_date.year) * 12 + (segment_end.month - current_date.month)
        days_diff = segment_end.day - current_date.day
        segment_months = months_diff + (days_diff / 30.0)

        if segment_months > 0:
            effective_step = min(current_step, max_steps[scale])
            scale_step = f"{scale}-{effective_step}"
            base_salary = _get_applicable_salary(grid_data, scale_step, current_date)
            
            monthly_cost = base_salary * (1 + (surcharge_pct / 100.0))
            segment_cost = monthly_cost * segment_months * fte
            total_cost += segment_cost

        # 5. Move the clock forward
        current_date = segment_end

        # Check if we landed directly on a step increment
        if current_date.month == periodicity_month and current_date.day == 1:
            current_step += 1

    return total_cost
