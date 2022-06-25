import json

def get_token(name):
    with open('D:/tokens.json') as f:
        token_json = json.load(f)
    return token_json[name]