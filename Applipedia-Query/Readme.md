# Applipedia Query and Parser

This project consists of two Python scripts that work together to scrape application data from Palo Alto's Applipedia and parse it into a structured JSON file.

## Overview

1. **`Applipedia-Query.py`**: This script pulls raw data from Applipedia using a POST request and saves the response to a file (`applipedia_response.txt`).
2. **`applipedia-response-parser.py`**: This script processes the raw response file and converts it into a structured JSON file (`applipedia_data.json`).

The two scripts are designed to work together, with the query script automatically calling the parser script after retrieving the data.

---

## Scripts

### 1. `Applipedia-Query.py`

#### Purpose
This script sends a POST request to the Applipedia API to retrieve application data. The data is saved as a raw text file for further processing.

#### Key Features
- Sends a POST request to the Applipedia API endpoint:  
  `https://applipedia.paloaltonetworks.com/Home/GetApplicationListView`
- Saves the raw response to a file named `applipedia_response.txt`.
- Automatically calls the parser script (`applipedia-response-parser.py`) to process the data.

#### Workflow
1. Define the API endpoint, payload, and headers.
2. Send a POST request using the `requests` library.
3. Save the response content to `applipedia_response.txt`.
4. Call the parser script to process the saved data.

#### Output
- `applipedia_response.txt`: The raw response data from the Applipedia API.

---

### 2. `applipedia-response-parser.py`

#### Purpose
This script parses the raw response file (`applipedia_response.txt`) and converts it into a structured JSON file.

#### Key Features
- Reads the raw response data from `applipedia_response.txt`.
- Extracts relevant fields such as:
  - Application Name
  - Category
  - Sub-category
  - Risk Level
  - Technology
- Saves the parsed data into a JSON file named `applipedia_data.json`.

#### Workflow
1. Open and read the `applipedia_response.txt` file.
2. Parse the data using Python's `json` module or custom logic.
3. Save the structured data to `applipedia_data.json`.

#### Output
- `applipedia_data.json`: A JSON file containing structured application data.

---

## How to Use

### Prerequisites
- Python 3.x
- Required Python libraries:
  - `requests`
  - `subprocess`

Install dependencies using:
```bash
pip install requests
