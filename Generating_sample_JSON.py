import json
def get_value_by_path(json_obj, path):
    keys = path.split('.')
    try:
        for key in keys:
            json_obj = json_obj[key]
        return json_obj
    except (KeyError, TypeError):
        return "Path does not exist."
json_obj = json.loads(input("Enter JSON obj: "))
path = input("Enter JSON path: ")
result = get_value_by_path(json_obj, path)
print(result)