================================================
RANSOMWARE SIMULATION
================================================

OVERVIEW:
This project simulates ransomware behavior in an
isolated VM lab environment for educational purposes.

HOW IT WORKS:
1. SCANNING
   - The malware scans a target folder for files
   - Targets extensions: .txt .jpg .png .pdf .docx

2. ENCRYPTION
   - Each file is encrypted using Fernet (AES-128)
   - A unique encryption key is generated per session
   - Original files are deleted after encryption
   - Encrypted files get a .locked extension

3. RANSOM NOTE
   - A ransom note is dropped in the target folder
   - Demands fake BTC payment (simulation only)
   - Contains fake wallet address and deadline

4. DECRYPTION
   - The decryptor uses the saved encryption.key
   - Restores all .locked files to original state
   - Removes .locked files after restoring

================================================
REAL WORLD COMPARISON:
================================================
Real ransomware examples: WannaCry, LockBit, REvil

Our simulation vs real ransomware:
- Encryption method : Same (AES)
- File targeting    : Same (scan and encrypt)
- Ransom note       : Same concept
- Key management    : We save locally (real sends to C2)
- Spreading         : We dont spread (real uses exploits)

================================================
SOC ANALYST - HOW TO DETECT THIS:
================================================
Indicators of Compromise (IoCs):

1. Mass file renaming in short time period
2. New .locked extensions appearing on files
3. High disk write activity from one process
4. New file created: READ_ME_RANSOM.txt
5. Encryption key file created on disk

SIEM Alert Rules to Create:
- Alert on mass file extension changes
- Alert on rapid file deletion + creation
- Alert on known ransom note filenames

================================================
DEFENSIVE MEASURES:
================================================
1. Regular offline backups (3-2-1 rule)
2. EDR solution to detect mass file changes
3. Least privilege - limit user file access
4. Network segmentation to stop spreading
5. Disable RDP if not needed
6. Keep systems patched and updated

================================================
TOOLS USED:
================================================
- Python 3
- Cryptography library (Fernet/AES-128)
- Kali Linux VM (isolated lab)
- VMware Workstation

================================================
DISCLAIMER:
This is a strictly educational simulation.
Built for SOC Analyst training purposes only.
Never run outside an isolated lab environment.
================================================
