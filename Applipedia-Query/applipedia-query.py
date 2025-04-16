import subprocess

# Existing code for pulling Applipedia data...


import requests

# Define the URL for the POST request
url = "https://applipedia.paloaltonetworks.com/Home/GetApplicationListView"

# Define the payload for the POST request
payload = {
    "category": "",
    "subcategory": "",
    "technology": "",
    "risk": "",
    "characteristic": "",
    "searchstring": ""
}

# Define the headers for the POST request
headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent": "Mozilla/5.0"
}

# Send the POST request
response = requests.post(url, data=payload, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Save the raw response content to a text file
    with open("applipedia_response.txt", "wb") as file:
        file.write(response.content)
    print("✅ Data successfully saved to 'applipedia_response.txt'")
else:
    print(f"❌ Failed to retrieve data. Status code: {response.status_code}")



# Assuming the data is saved and ready for parsing
print("Data pulled successfully. Now calling the parser script...")

# Call the parser script
try:
    subprocess.run(["python3", "applipedia-response-parser.py"], check=True)
    print("Parser script executed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error occurred while running the parser script: {e}")

