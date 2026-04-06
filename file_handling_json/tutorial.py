import json

json_string = '''
{
  "name": "TheSilentDefender",
  "age": 25,
  "skills": ["Python", "DFIR", "SIEM"],
  "is_active": true
}
'''

data = json.loads(json_string)

print(data)
print(type(data))


new_json = json.dumps(data, indent = 4)
print(new_json)
print(type(new_json))

with open("file_handling_json\\data.json") as f:
    data = json.load(f)

print(data)
print(type(data))

with open("file_handling_json\\new_data.json", mode='w') as f:
    json.dump(data,f,indent=4)

