# MITM Railway Attack Simulator

An interactive cybersecurity simulation that demonstrates how **Man-in-the-Middle (MITM) attacks** can disrupt real-time railway control systems.

![Cybersecurity](https://img.shields.io/badge/domain-cybersecurity-blue)
![MITM Simulation](https://img.shields.io/badge/type-MITM%20simulation-red)
![AI / Simulation](https://img.shields.io/badge/focus-attack%20simulation-orange)
![Python](https://img.shields.io/badge/python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/streamlit-app-red)
![Security](https://img.shields.io/badge/security-policy-blue)
![Dependabot](https://img.shields.io/badge/dependabot-enabled-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

---

## Overview

MITM Railway Attack Simulator is a Streamlit-based simulation of a railway communication system, where a train exchanges data with a control center. The project demonstrates how an attacker positioned between these components can intercept, manipulate, and replay messages - leading to unsafe system behavior. This simulation highlights the importance of **secure communication in critical infrastructure systems**.

---

Live Demo: 
https://mitm-railway-attack-simulator.streamlit.app/ 

---
## Project Structure

```
mitm-railway-attack-simulator/
│
├── .github/
│   └── workflows/
│       └── codeql.yml
├── app.py
├── requirements.txt
├── README.md
├── SECURITY.md
├── LICENSE
└── .gitignore
```

---

## System Architecture

The system consists of three main components:

- **Train System**  
  Sends telemetry data (speed, status, signal)

- **Control Center**  
  Sends operational commands (STOP, GO, SLOW)

- **Attacker (MITM)**  
  Intercepts and manipulates communication between the two

```mermaid
flowchart LR

    subgraph Railway System
        T[Train]
        C[Control Center]
    end

    A[MITM Attacker]

    T -->|Telemetry| A
    A -->|Tampered Data| C

    C -->|Commands| A
    A -->|Injected Commands| T
```

## MITM Attack Variants

The simulator implements three types of Man-in-the-Middle attacks:

### Data Manipulation
- Alters telemetry data sent from the train  
- Example: speed changes from 60 → 200  
- Impact: control center makes incorrect decisions  

<img width="1392" height="592" alt="Zrzut ekranu 2026-08-14 o 20 26 57" src="https://github.com/user-attachments/assets/06786649-c8bb-4aff-87e9-58d449af1c89" />


---

### Command Injection
- Modifies commands sent to the train  
- Example: STOP → GO  
- Impact: unsafe system behavior (unexpected acceleration)  

<img width="1383" height="561" alt="Zrzut ekranu 2026-08-14 o 20 27 52" src="https://github.com/user-attachments/assets/23d3dbc2-0abf-4142-bd7b-3d2340e9ce7d" />



---

### Replay Attack
- Reuses previously sent commands  
- Example: repeats an old STOP command  
- Impact: delayed or inconsistent system response  

<img width="1374" height="557" alt="Zrzut ekranu 2026-08-14 o 20 28 25" src="https://github.com/user-attachments/assets/010dc55f-9a79-444e-9f7c-db278e8a7ecc" />



---

## Security Mode

The simulation includes a security layer that represents:

- Data validation  
- Integrity checks  
- Secure communication mechanisms

<img width="1350" height="594" alt="Zrzut ekranu 2026-08-14 o 20 29 22" src="https://github.com/user-attachments/assets/c41459c9-5f66-4aec-9417-2b8921dc078b" />

When enabled:
- Manipulated data is detected  
- Attacks are blocked  
- System behavior stabilizes  

<img width="1356" height="582" alt="Zrzut ekranu 2026-08-14 o 20 30 08" src="https://github.com/user-attachments/assets/72926e62-9106-4a62-8fdb-cf9a40ff3826" />


---

## Features

- Real-time system simulation  
- Interactive attack selection  
- Original vs Tampered data comparison  
- Dynamic risk level calculation  
- System logs (SOC-style monitoring)  
- Live charts (speed & risk over time)  
- Critical condition detection (e.g. overspeed)  

---

## System Behavior

The system reacts dynamically to commands and attacks:

- Speed increases/decreases based on commands  
- Overspeed (>180 km/h) triggers critical alerts  
- Conflicting signals generate warnings  
- Risk level increases with malicious activity

---

## Visualization

The dashboard provides:

- Speed & risk charts over time  
- Real-time risk level indicator  
- Event logs showing system activity and attacks  

<img width="1502" height="557" alt="image" src="https://github.com/user-attachments/assets/6130aaa4-91e8-44b9-94b0-a7dba569b6b9" />

<img width="416" height="604" alt="image" src="https://github.com/user-attachments/assets/ae7d7d13-6af6-49ee-88ef-52dfa7c49334" />

---

## Purpose

This project is designed for:

- Educational use (cybersecurity concepts)  
- Demonstrating risks in cyber-physical systems  
- Understanding MITM attack mechanisms  
- Visualizing cause-and-effect in system security  

---

## How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the application:

```bash
streamlit run app.py
```
---

## Key Takeaways
- MITM attacks can manipulate both data and control signals
- Even simple attacks can lead to critical system failures
- Security mechanisms are essential in real-time systems
- Cybersecurity is crucial for critical infrastructure like railways

---

## Future Improvements
- AI-based anomaly detection
- Advanced attack scenarios

---

## License

This project is licensed under the MIT License.
