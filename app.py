import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="RailGuard X", layout="wide")

# --- HEADER ---
st.title("MITM Railway Attacks Simulator")
st.markdown("Interactive simulation that demonstrates how man-in-the-middle cyberattacks impact real-time railway systems")

# --- SIDEBAR ---
st.sidebar.header("Simulation Settings")

attack_enabled = st.sidebar.toggle("Enable Attacker", True)

attack_type = st.sidebar.selectbox(
    "Attack Type",
    ["None", "Data Manipulation", "Command Injection", "Replay Attack"]
)

security_enabled = st.sidebar.toggle("Enable Security (Encryption & Validation)", False)

# --- STATE INIT ---
if "speed" not in st.session_state:
    st.session_state.speed = 100

if "log" not in st.session_state:
    st.session_state.log = []

if "history" not in st.session_state:
    st.session_state.history = []

if "risk" not in st.session_state:
    st.session_state.risk = 0

if "last_command" not in st.session_state:
    st.session_state.last_command = "MAINTAIN"

if "command_history" not in st.session_state:
    st.session_state.command_history = []

# --- LOG FUNCTION ---
def add_log(message, level="INFO"):
    st.session_state.log.insert(0, f"[{level}] {message}")

# --- TRAIN DATA ---
def generate_train_data():
    return {
        "speed": st.session_state.speed,
        "status": "OK",
        "signal": "GREEN"
    }

# --- COMMAND ---
def generate_command():
    return random.choice(["STOP", "GO", "SLOW", "MAINTAIN"])

# --- ATTACK LOGIC ---
def apply_attack(data, command):
    if not attack_enabled or attack_type == "None":
        return data, command, "No attack"

    if "command_history" not in st.session_state:
        st.session_state.command_history = []

    attack_desc = ""

    if attack_type == "Data Manipulation" and data:
        original_speed = data["speed"]
        data["speed"] = original_speed + random.randint(80, 150)
        data["status"] = "CORRUPTED"
        attack_desc = f"Speed changed {original_speed} → {data['speed']}"
        st.session_state.risk += 3

    elif attack_type == "Command Injection" and command:
        original_cmd = command
        command = "GO" if command != "GO" else "STOP"
        attack_desc = f"Command changed {original_cmd} → {command}"
        st.session_state.risk += 4

    elif attack_type == "Replay Attack" and command:
        if len(st.session_state.command_history) > 0:
            old_cmd = random.choice(st.session_state.command_history)
            attack_desc = f"Replayed old command {old_cmd}"
            command = old_cmd
            st.session_state.risk += 2
        else:
            attack_desc = "No previous command to replay"

    add_log(f"ATTACK: {attack_desc}", "CRITICAL")

    return data, command, attack_desc

# --- SECURITY ---
def security_check(original, modified):
    if not security_enabled:
        return modified, False

    if original != modified:
        add_log("Intrusion detected! Data blocked.", "CRITICAL")
        return original, True

    return modified, False

# --- LAYOUT ---
col1, col2, col3 = st.columns(3)

# --- TRAIN ---
with col1:
    st.subheader("Train")

    if st.button("Send Telemetry"):
        data = generate_train_data()
        attacked_data, _, desc = apply_attack(data.copy(), None)

        attacked_data, blocked = security_check(data, attacked_data)

        st.session_state.original_data = data
        st.session_state.modified_data = attacked_data

        if blocked:
            add_log("Telemetry attack blocked", "SUCCESS")

    if "original_data" in st.session_state:
        st.markdown("### Original vs Tampered")

        c1, c2 = st.columns(2)

        with c1:
            st.success("Original")
            st.json(st.session_state.original_data)

        with c2:
            st.error("Tampered")
            st.json(st.session_state.modified_data)

# --- ATTACKER ---
with col2:
    st.subheader("Attacker")

    if attack_enabled:
        st.error("ATTACK ACTIVE")
    else:
        st.success("No attacker")

    st.write(f"Attack Type: {attack_type}")

# --- CONTROL ---
with col3:
    st.subheader("Control Center")

    if st.button("Send Command"):
        cmd = generate_command()
        original_cmd = cmd

        _, attacked_cmd, desc = apply_attack({}, cmd)
        attacked_cmd, blocked = security_check(original_cmd, attacked_cmd)

        st.session_state.command = attacked_cmd
        st.session_state.last_command = attacked_cmd

        st.session_state.original_cmd = original_cmd

        st.session_state.command_history.append(attacked_cmd)

        if blocked:
            add_log("Command blocked by security", "SUCCESS")

    if "original_cmd" in st.session_state:
        st.markdown("### Original vs Tampered")

        c1, c2 = st.columns(2)

        with c1:
            st.success("Original")
            st.write(st.session_state.original_cmd)

        with c2:
            st.error("Tampered")
            st.write(st.session_state.command)

# --- SYSTEM ---
st.markdown("---")
st.header("System Behavior")

if "command" in st.session_state:
    cmd = st.session_state.command

    if cmd == "STOP":
        st.session_state.speed = max(0, st.session_state.speed - 50)
        add_log("Train slowing down", "INFO")

    elif cmd == "GO":
        st.session_state.speed += 40
        add_log("Train accelerating", "INFO")

    elif cmd == "SLOW":
        st.session_state.speed -= 20
        add_log("Train slowing", "INFO")

# --- CRITICAL CONDITIONS ---
if st.session_state.speed > 180:
    st.error("CRITICAL: Overspeed! Risk of derailment!")
    st.session_state.risk += 5

if st.session_state.speed == 0 and st.session_state.command == "GO":
    st.warning("Conflicting signals detected!")

# --- HISTORY ---
st.session_state.history.append({
    "speed": st.session_state.speed,
    "risk": st.session_state.risk
})

# --- DASHBOARD ---
colA, colB = st.columns([2,1])

with colA:
    st.subheader("System Metrics")
    df = pd.DataFrame(st.session_state.history)
    st.line_chart(df)

with colB:
    st.subheader("Risk Level")

    if st.session_state.risk < 5:
        st.success(f"LOW ({st.session_state.risk})")
    elif st.session_state.risk < 10:
        st.warning(f"MEDIUM ({st.session_state.risk})")
    else:
        st.error(f"HIGH ({st.session_state.risk})")

# --- LOGS ---
st.markdown("---")
st.subheader("System Logs")

for log in st.session_state.log[:12]:
    st.text(log)

