# 🛡️ cyber-project-18-soc-defense-api
Cyber defense API for real-time threat analysis and response


## Context

Modern cyber defense systems rely on APIs to centralize detection and response.

This project simulates a defensive API handling security events.

---

## Objective

* Receive logs via API
* Analyze threats
* Return defensive actions

---

## ⚙️ Features

* Threat analysis
* Response engine
* API endpoints

---

## Run

```id="cd4"
pip install flask
python app.py
```

---

## Key Takeaways

* API security design
* Cyber defense architecture
* Detection + response integration

---

## 👨‍💻 Author

Part of my cybersecurity learning journey.





## API Testing

You can test the API using curl:

```bash
curl -X POST http://127.0.0.1:5000/analyze \
-H "Content-Type: application/json" \
-d '{"log": "LOGIN SUCCESS - admin - 45.33.32.1"}'
