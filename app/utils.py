import json

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







