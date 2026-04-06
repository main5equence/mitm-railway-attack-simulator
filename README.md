# MITM Railway Attack Simulator

An interactive cybersecurity simulation that demonstrates how **Man-in-the-Middle (MITM) attacks** can disrupt real-time railway control systems.

![Cybersecurity](https://img.shields.io/badge/domain-cybersecurity-blue)
![MITM Simulation](https://img.shields.io/badge/type-MITM%20simulation-red)
![AI / Simulation](https://img.shields.io/badge/focus-attack%20simulation-orange)
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
├── .gitignore
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

<img width="1826" height="572" alt="image" src="https://github.com/user-attachments/assets/c7e1b276-e4ba-4771-8690-34f249a8f99e" />


---

### Command Injection
- Modifies commands sent to the train  
- Example: STOP → GO  
- Impact: unsafe system behavior (unexpected acceleration)  


<img width="1828" height="563" alt="image" src="https://github.com/user-attachments/assets/660a8931-792f-4f1d-b9a0-258abfa8346c" />


---

### Replay Attack
- Reuses previously sent commands  
- Example: repeats an old STOP command  
- Impact: delayed or inconsistent system response  


<img width="1831" height="548" alt="image" src="https://github.com/user-attachments/assets/c7ad999d-614b-416d-92e1-c9a640537b76" />



---

## Security Mode

The simulation includes a security layer that represents:

- Data validation  
- Integrity checks  
- Secure communication mechanisms  

When enabled:
- Manipulated data is detected  
- Attacks are blocked  
- System behavior stabilizes  


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
