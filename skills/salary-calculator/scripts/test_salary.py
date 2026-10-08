from untitest import TestCase

from salary import calculate_salary


class TestSalaryCalculation(TestCase):
    def test_salary_calculation(self):
        """Test salary calculator against a ground truth result."""
        total = calculate_salary(
            scale="A10",
            start_step=11,
            periodicity_month=8,
            start_date_str="01/10/2026",
            end_date_str="01/10/2027",
            fte=0.6,
            surcharge_pct=18.05,
        )
        self.assertEqual(round(total, 2), 74924.80)
