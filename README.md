# Vuln-Scanner-Cys
A lightweight Python-based vulnerability scanner that detects open ports, analyzes potential risks, and generates detailed HTML/JSON security reports. Designed for beginners and security enthusiasts who want a simple yet effective scanning tool

\# Vuln Scanner Cys



A lightweight Python-based vulnerability scanner that detects open ports, analyzes potential risks, and generates detailed HTML/JSON security reports.  

Designed for beginners and security enthusiasts who want a simple yet effective scanning tool.



\---



\## Features



\- \*\*Port Scanning:\*\* Scans common ports on a target IP or domain.

\- \*\*Risk Assessment:\*\* Classifies detected ports by risk level (High, Medium, Low).

\- \*\*Service Banner Detection:\*\* Attempts to grab service banners when available.

\- \*\*Report Generation:\*\* Automatically generates:

&#x20; - `report.json` — structured machine-readable report

&#x20; - `report.html` — human-friendly report for browser viewing

\- \*\*User-friendly CLI:\*\* Simple command-line interface that prompts for target input.



\---



\## How It Works



1\. The tool prompts the user to enter a \*\*target IP or domain\*\*.

2\. It scans a predefined set of ports.

3\. For each open port, it:

&#x20;  - Identifies the port

&#x20;  - Attempts to grab the service banner

&#x20;  - Assigns a risk level

4\. Results are saved as:

&#x20;  - `report.json`

&#x20;  - `report.html`



\---



\## Installation



> Requirements:

> - Python 3.x installed on your system



1\. \*\*Clone the repository:\*\*

&#x20;  ```bash

&#x20;  git clone https://github.com/<your-username>/Vuln-Scanner-Cys.git

&#x20;  cd Vuln-Scanner-Cys

python -m venv venv

source venv/bin/activate   # On Linux/Mac

venv\\Scripts\\activate      # On Windows

pip install -r requirements.txt

