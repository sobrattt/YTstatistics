import json
from datetime import datetime, timedelta


def get_credentials():
    file = open("./credentials.json", "r")
    credentials = json.load(file)
    credentials = credentials.get("web")
    file.close()
    return credentials

def transform_analytic_response(statistics):
    header_names = []
    for column in statistics["columnHeaders"]:
        header_names.append(column["name"])
    rows = statistics["rows"]
    num_columns = len(header_names)
    column_sums = [0.0] * num_columns
    num_rows = len(rows)
    for row in rows:
        for i in range(1, num_columns):
            value = row[i]
            try:
                column_sums[i] += float(value)
            except (ValueError, TypeError):
                continue

    averages = ["Average"]
    for i in range(1, num_columns):
        if num_rows > 0:
            avg = column_sums[i] / num_rows
        else:
            avg = 0
        averages.append(round(avg, 2))
    table = [header_names] + rows
    return table, averages

def get_time_gaps():
    start_date_current_week = datetime.now() - timedelta(days=7)
    start_date_current_week = start_date_current_week.strftime("%Y-%m-%d")
    end_date_current_week = datetime.now().strftime("%Y-%m-%d")
    start_date_last_week = datetime.now() - timedelta(days=14)
    start_date_last_week = start_date_last_week.strftime("%Y-%m-%d")
    end_date_last_week = datetime.now() - timedelta(days=7)
    end_date_last_week = end_date_last_week.strftime("%Y-%m-%d")
    return [start_date_current_week, end_date_current_week, start_date_last_week, end_date_last_week]







