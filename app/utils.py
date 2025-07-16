import json

def get_credentials():
    file = open("./credentials.json", "r")
    credentials = json.load(file)
    credentials = credentials.get("web")
    file.close()
    return credentials




