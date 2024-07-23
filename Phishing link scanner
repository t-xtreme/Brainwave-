# Import Python Modules for HTTP (requests) and JSON
import requests
import json

# Ask user to provide the URL for scanning
suspicious_url = input("[x] Please provide the URL for scanning (): ")
api_key = input("[x] Please provide the URLSCAN.IO Api Key : ")


# Check the URL on UrlScan.io 
print(f"[x] Searching for URL : {suspicious_url}")


# Generate API Key and paste it here
headers = {'API-Key':api_key,'Content-Type':'application/json'}

# As per URLScan.io website
data = {"url": suspicious_url, "visibility": "public"}

# Escape \ with /\ as URLScan.io cannot read this.
fixed_url = suspicious_url.replace("/","\/")

# Search for the existing report
search_response = requests.get(f'https://urlscan.io/api/v1/search/?q=page.url:{fixed_url}',headers=headers)

# Count the number of result found
result_found = search_response.json()['total']

data = {"url": suspicious_url, "visibility": "public"}

if result_found == 0:
    print("-- No Report Found. Submitting new request...")
    new_response = requests.post('https://urlscan.io/api/v1/scan/',headers=headers, data=json.dumps(data))

    if "Error" not in new_response.json()['message']:
        targeted_url = new_response.json()['result']
        report_id = new_response.json()['uuid']

    else:
        print(f"[-] Sorry, {new_response.json()['message']}. {new_response.json()['description']}")
        
else:
    print(f"[{result_found}] Found previous results. Fething details...")
    for url in search_response.json()['results']:
        targeted_url = url['result']
        report_id = url['_id']
        print(f"-> Report Found : {targeted_url} on {report_id}")
        if suspicious_url in url:
            print("True")

if report_id:

    # Fetch the scan results:
    fetch_response = requests.get(f'https://urlscan.io/api/v1/result/{report_id}/',headers=headers)
    response_data = fetch_response.json()

    print(f"""
URL Scanned  : {targeted_url}
Report ID    : {report_id}
Threat Score : {response_data['verdicts']['overall']['score']}
Is Malicious : {response_data['verdicts']['overall']['malicious']}
    """)
