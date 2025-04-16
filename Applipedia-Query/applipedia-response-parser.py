import json
from bs4 import BeautifulSoup
from datetime import datetime
import os

# Load the HTML content from the file
with open("applipedia_response.txt", "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Initialize a list to store the application data
applications = []

# Find all table rows in the HTML
rows = soup.find_all("tr")

# Iterate through each row to extract application details
for row in rows:
    cells = row.find_all("td")
    if len(cells) == 5:
        # Extract application name
        app_link = cells[0].find("a")
        app_name = app_link.get_text(strip=True) if app_link else ""

        # Extract category
        category = cells[1].get_text(strip=True)

        # Extract sub-category
        sub_category = cells[2].get_text(strip=True)

        # Extract risk level from the image filename
        risk_img = cells[3].find("img")
        risk_level = ""
        if risk_img and "src" in risk_img.attrs:
            src = risk_img["src"]
            if "risk_" in src:
                risk_level = "Level " + src.split("risk_")[1].split(".")[0]

        # Extract technology
        technology = cells[4].get_text(strip=True)

        # Append the extracted data to the applications list
        applications.append({
            "Application Name": app_name,
            "Category": category,
            "Sub-category": sub_category,
            "Risk": risk_level,
            "Technology": technology
        })

# Generate a timestamped filename
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"applipedia_data_{timestamp}.json"

# Save the extracted data to the timestamped JSON file
with open(filename, "w", encoding="utf-8") as json_file:
    json.dump(applications, json_file, indent=4)

print(f"✅ Application data has been successfully parsed and saved to '{filename}'.")
# Print the number of applications extracted
print(f"Total applications extracted: {len(applications)}")
# Print the first few applications for verification
print("First few applications:")
for app in applications[:5]:
    print(app)
# Print the file size
file_size = os.path.getsize(filename)
print(f"File size: {file_size} bytes")
# Print the file path
file_path = os.path.abspath(filename)
print(f"File path: {file_path}")
# Print the file creation time
creation_time = os.path.getctime(filename)
creation_time_str = datetime.fromtimestamp(creation_time).strftime("%Y-%m-%d %H:%M:%S")
print(f"File creation time: {creation_time_str}")
