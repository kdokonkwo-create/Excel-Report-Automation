import os
import openpyxl


def read_data(filename):
    """
    Reads student records from an Excel file located in the project's data directory
    and returns a list of dictionaries representing each student.
    """

  
    # Validate file existence
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Input file not found at: {filename}")

    # Load workbook
    workbook = openpyxl.load_workbook(filename)
    sheet = workbook.active

    records = []
    headers = ["student_id", "full_name", "course", "score1", "score2", "score3"]

    for row in sheet.iter_rows(min_row=2, values_only=True):
        record = {}

        for index, value in enumerate(row):
            if index >= len(headers):
                break  # Ignore extra columns

            if value is None:
                value = 0  # Normalize missing values

            record[headers[index]] = value

        records.append(record)

    return records
