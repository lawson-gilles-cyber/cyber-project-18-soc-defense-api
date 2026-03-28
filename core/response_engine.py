# Defensive response engine

def generate_response(threat):

    if threat == "Brute force attempt":
        return "Block IP and monitor"

    if threat == "Suspicious admin login":
        return "Trigger investigation"

    if threat == "Sensitive data access":
        return "Alert SOC and restrict access"

    return "No action required"
