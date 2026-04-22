import json

def save_json(data):
    with open("report.json", "w") as f:
        json.dump(data, f, indent=4)

def save_html(data):
    html = """
    <html>
    <head>
        <title>Scan Report</title>
        <style>
            body { font-family: Arial; padding: 20px; }
            table { width: 100%; border-collapse: collapse; }
            th, td { padding: 10px; border: 1px solid #ccc; }
            th { background: #333; color: white; }
        </style>
    </head>
    <body>
        <h2>Vulnerability Scan Report</h2>
        <table>
            <tr><th>Port</th><th>Banner</th><th>Risk</th></tr>
    """

    for item in data:
        html += f"<tr><td>{item['port']}</td><td>{item['banner']}</td><td>{item['risk']}</td></tr>"

    html += "</table></body></html>"

    with open("report.html", "w") as f:
        f.write(html)