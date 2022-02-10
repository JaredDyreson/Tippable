"""Module containing the implementation of the employee manifest"""

from Tippable.dataclasses.employee import Employee

import dataclasses
import typing
import tabulate

from decimal import localcontext, Decimal, ROUND_HALF_UP


@dataclasses.dataclass
class EmployeeManifest:
    """Manifest that contains all the employees on the tip roll"""

    container: typing.List[Employee] = dataclasses.field(default_factory=lambda: [])
    tips_accrued: int = 0

    @property
    def tippable_hours(self) -> float:
        """Compute all the tippable hours"""
        return sum(employee.tippable_hours for employee in self.container)

    @property
    def tip_rate(self) -> float:
        """Compute the tip rate that each hour worked is worth"""

        return self.tips_accrued / self.tippable_hours

    def distribute_assets(self):
        """
        Compute the amount of money to distribute to each employee
        This is called `bankers rounding`.

        Legend:
        - Floating point with a mantissa of 0.49 or lower, round down
        - Floating point with a mantissa of 0.5 or higher, round up

        Source: https://stackoverflow.com/a/33019948

        @return int : rounding error obtained during calculations

        Legend:
        - Positive integer: leftover
        - Negative integer: not enough cash, please consult calculations
        """

        total: int = 0

        with localcontext() as ctx:
            ctx.rounding = ROUND_HALF_UP
            for employee in self.container:
                calculation = Decimal(employee.tippable_hours * self.tip_rate)
                value = int(calculation.to_integral_value())
                employee.amount_received = value
                total += value

        return self.tips_accrued - total

    def __repr__(self) -> str:
        return tabulate.tabulate(
            [dataclasses.astuple(element) for element in self.container],
            headers=["Name", "ID", "Tippable Hours", "Amount Received"]
        )
