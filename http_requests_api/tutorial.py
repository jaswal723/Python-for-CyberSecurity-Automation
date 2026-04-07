import requests
import os
import csv
import time
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("VT-API-KEY")

hashes = []
with open("http_requests_api\\hashes.csv", mode='r') as f:
    data = csv.DictReader(f)
    for row in data:
        hashes.append(row['hash'])

headers = {
    "x-apikey": api_key,
    "accept": "application/json"
}

final_data=[]

for x in hashes:
    temp = {}
    temp['Hash'] = x
    url = "https://www.virustotal.com/api/v3/files/" + x
    our_request = requests.get(url, headers=headers)

    if our_request.status_code != 200:
        print(f'There is an error. Status code - {our_request.status_code}')
    else:
        temp['Score'] = our_request.json()['data']['attributes']['last_analysis_stats']['malicious']
        if temp['Score'] == 0:
            temp['Verdict'] = "Safe"
        elif temp['Score'] <= 2:
            temp['Verdict'] = "Suspicious"
        elif temp['Score'] <= 5:
            temp['Verdict'] = "Malicious"
        else:
            temp['Verdict'] = "Highly Malicious"
    final_data.append(temp)
    time.sleep(20)

with open("http_requests_api\\output.csv",mode='w',newline="") as file:
    writer = csv.DictWriter(file, fieldnames = ["Hash","Score","Verdict"])
    writer.writeheader()
    writer.writerows(final_data)

