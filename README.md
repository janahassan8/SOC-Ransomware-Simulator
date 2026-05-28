# SOC Ransomware Simulator

## Overview

This project is an educational ransomware simulation designed for SOC Analyst training and malware analysis practice within isolated virtual lab environments.

The simulation demonstrates the core stages of a ransomware attack, including file discovery, encryption, ransom note deployment, and data recovery through decryption. It is intended to help cybersecurity students and analysts better understand ransomware behavior, detection opportunities, and defensive strategies.

---

# Features

## File Scanning

The simulator scans a specified target directory for commonly targeted file types, including:

* `.txt`
* `.jpg`
* `.png`
* `.pdf`
* `.docx`

---

## File Encryption

* Uses the Python Cryptography library with Fernet (AES-128)
* Generates a unique encryption key for each execution
* Encrypts targeted files and appends the `.locked` extension
* Removes original files after successful encryption

---

## Ransom Note Simulation

The program creates a simulated ransom note within the target directory containing:

* Fake cryptocurrency payment instructions
* Simulated wallet address
* Mock payment deadline

This behavior replicates common techniques used by real-world ransomware families.

---

## File Decryption

A separate decryptor utility is included to restore encrypted files.

The decryptor:

* Uses the locally stored `encryption.key`
* Decrypts `.locked` files back to their original format
* Removes encrypted copies after restoration

---

# Real-World Ransomware Comparison

Examples of real ransomware families:

* WannaCry
* LockBit
* REvil

| Feature           | Simulation    | Real Ransomware     |
| ----------------- | ------------- | ------------------- |
| AES Encryption    | Yes           | Yes                 |
| File Targeting    | Yes           | Yes                 |
| Ransom Notes      | Yes           | Yes                 |
| Key Management    | Local Storage | Remote C2 Servers   |
| Network Spreading | No            | Often Uses Exploits |

---

# Detection Opportunities for SOC Analysts

## Indicators of Compromise (IoCs)

* Mass file renaming within a short timeframe
* Sudden appearance of `.locked` file extensions
* High disk write activity from a single process
* Creation of ransom note files
* Encryption key artifacts stored locally

---

## Suggested SIEM Detection Rules

* Detect rapid file extension changes
* Monitor excessive file deletion and recreation activity
* Alert on known ransom note filenames
* Identify abnormal encryption-related process behavior

---

# Defensive Measures

Recommended security controls against ransomware attacks:

1. Maintain offline and immutable backups (3-2-1 strategy)
2. Deploy EDR/XDR solutions for behavioral monitoring
3. Enforce least privilege access controls
4. Implement network segmentation
5. Disable unnecessary remote access services such as RDP
6. Regularly patch and update operating systems and software

---

# Technologies Used

* Python 3
* Cryptography Library (Fernet / AES-128)
* Kali Linux Virtual Machine
* VMware Workstation

---

# Lab Environment

This project should only be executed in:

* Isolated virtual machines
* Controlled cybersecurity labs
* Offline testing environments

Do not execute on production systems or personal devices.

---

# Disclaimer

This project was created strictly for educational and defensive cybersecurity purposes.

The author does not support or condone malicious activity, unauthorized access, or deployment outside controlled lab environments. Users are solely responsible for ensuring ethical and legal usage.
