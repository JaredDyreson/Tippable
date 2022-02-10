"""Parsing the input and output files for Tippable"""

import pathlib
import typing
import json

from Tippable.constants import EMPLOYEE_MANIFEST
from Tippable.exceptions import ParsingException
from Tippable.dataclasses.employee import Employee
from Tippable.dataclasses.employee_manifest import EmployeeManifest


class InputParser:
    """Class to take in JSON data and return an employee manifest"""
    def __init__(self):

        self.employees: typing.List[Employee] = []
        with open(EMPLOYEE_MANIFEST, "r", encoding="utf-8") as fil_ptr:
            # Read in contents

            content = json.loads(fil_ptr.read())
            # Assign each value inside the json file to a specific element

            for id_ in content:
                match content[id_]:
                    case {"name": name}:
                        self.employees.append(Employee(name, id_))
                    case _:
                        # Does not match this, please throw an Exception
                        raise ParsingException(
                            f"Parsing error for content: {content[id_]}"
                        )
        self.employee_manifest_ = EmployeeManifest(self.employees)
