#!/usr/bin/env python
# -*- coding: utf-8-unix -*-

"""Read CSV file from libreconnect."""

import csv
from datetime import datetime
from zoneinfo import ZoneInfo


def main() -> None:
    """Convert libreconnect CSV to home assistant.

    Reads CSV file from libreconnect and converts it to home assistant
    recorder format.
    """
    # since = datetime.now(tz=ZoneInfo("Europe/London"))
    with open("CharlieRusbridger_glucose_11-5-2025.csv", newline="") as csvfile:
        dialect = csv.Sniffer().has_header(
            "Device,Serial Number,Device Timestamp,Record Type,Historic Glucose mmol/L,"
            "Scan Glucose mmol/L,Non-numeric Rapid-Acting Insulin,"
            "Rapid-Acting Insulin (units),Non-numeric Food,"
            "Carbohydrates (grams),Carbohydrates (servings),"
            "Non-numeric Long-Acting Insulin,Long-Acting Insulin Value (units),Notes,"
            "Strip Glucose mmol/L,Ketone mmol/L,Meal Insulin (units),"
            "Correction Insulin (units),User Change Insulin (units)"
        )

        csvfile.readline()  # Skip first line
        reader = csv.DictReader(csvfile, dialect=dialect)

        records: list[dict[str, str]] = []
        for row in reader:
            if row["Record Type"] in ["5", "6"]:
                continue
            start = datetime.strptime(
                row["Device Timestamp"], "%d-%m-%Y %H:%M"
            ).replace(tzinfo=ZoneInfo("Europe/London"))
            if row["Record Type"] == "0":
                state = float(row["Historic Glucose mmol/L"])
            elif row["Record Type"] == "1":
                state = float(row["Scan Glucose mmol/L"])
            else:
                continue

            records.append(
                {
                    "start": start.isoformat(),
                    "state": state,
                }
            )

        # Sort records by start timestamp
        records.sort(key=lambda record: record["start"])

        # Print records in home assistant recorder format
        for record in records:
            print(f"{record('start')}")
            print(f"{record('state')}")


if __name__ == "__main__":
    main()
