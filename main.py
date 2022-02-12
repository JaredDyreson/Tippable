"""Driver code implementation"""

from Tippable.parsing import InputParser

import datetime
import pathlib
import glob
import os

INPUT = InputParser()
PROGRAM_LOOP = True


def input_data():
    for employee in INPUT.employee_manifest_.container:
        print(f"[PERSON]: {employee.name}")
        _break = False
        while not _break:
            _value = input("Hours worked: ")
            try:
                employee.tippable_hours = float(_value)
                _break = True
            except ValueError:
                continue

def dump_reciepe():
    input_data()
    print(INPUT.employee_manifest_)

    INPUT.employee_manifest_.dump(pathlib.Path("completed_transactions/dump.json"))

def load_reciepe():
    latest_file = max(glob.glob("completed_transactions/*"), key=os.path.getctime)
    print(f"[INFO] Loading: {latest_file}")

while(PROGRAM_LOOP):
    input_data()

    command = input("[INPUT] Command: ")

    match command:
        case "quit":
            print("[INFO] Exiting...")
            PROGRAM_LOOP = False
