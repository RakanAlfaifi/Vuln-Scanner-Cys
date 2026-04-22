from scanner import scan_ports
from analyzer import analyze
from report import save_json, save_html

target = input("Enter target IP or Domain: ")

print(f"\n[+] Scanning {target} ...\n")

raw_results = scan_ports(target)
final_results = []

for item in raw_results:
    analyzed = analyze(item["port"], item["banner"])
    final_results.append(analyzed)
    print(f"Open Port: {analyzed['port']} | Banner: {analyzed['banner']} | Risk: {analyzed['risk']}")

save_json(final_results)
save_html(final_results)

print("\n[+] Reports saved as report.json and report.html")