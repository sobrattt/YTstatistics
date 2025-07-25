import json

def get_credentials():
    file = open("./credentials.json", "r")
    credentials = json.load(file)
    credentials = credentials.get("web")
    file.close()
    return credentials

def transform_analytic_response(statistics):

    header_names = []
    for name in statistics["columnHeaders"]:
        name = name.get("name")
        header_names.append(name)
    rows = statistics["rows"]
    rows.insert(0, header_names)
    return rows





