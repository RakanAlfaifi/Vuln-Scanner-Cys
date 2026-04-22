def analyze(port, banner):
    if port in [21, 23, 80, 110, 143]:
        risk = "High"
    elif port in [22, 443, 3389]:
        risk = "Medium"
    else:
        risk = "Low"

    return {
        "port": port,
        "banner": banner,
        "risk": risk
    }