import json
def merge_json(json1, json2):
    for key in json2:
        if key in json1:
            if isinstance(json1[key], dict) and isinstance(json2[key], dict):
                merge_json(json1[key], json2[key])
            else:
                json1[key] = json2[key]
        else:
            json1[key] = json2[key]
    return json1
json1 = json.loads(input("Enter 1st Obj-")) # Get input from user
json2 = json.loads(input("Enter 2nd Obj-"))
merged = merge_json(json1, json2) # Merging JSON objects
print(json.dumps(merged, indent=2))
                