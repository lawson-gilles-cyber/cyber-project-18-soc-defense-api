# Threat analysis engine

def analyze_log(log):

    if "LOGIN FAILED" in log:
        return "Brute force attempt"

    if "LOGIN SUCCESS - admin" in log:
        return "Suspicious admin login"

    if "confidential" in log:
        return "Sensitive data access"

    return "Normal activity"
