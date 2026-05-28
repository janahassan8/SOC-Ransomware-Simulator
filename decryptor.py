cat > decryptor.py << 'EOF'
import os
from cryptography.fernet import Fernet

TARGET_FOLDER = "./victims_files"
KEY_FILE = "./encryption.key"

def load_key():
    with open(KEY_FILE, "rb") as f:
        return f.read()

def decrypt_file(filepath, fernet):
    with open(filepath, "rb") as f:
        data = f.read()
    decrypted = fernet.decrypt(data)
    original = filepath.replace(".locked", "")
    with open(original, "wb") as f:
        f.write(decrypted)
    os.remove(filepath)
    print(f"  [DECRYPTED] {original}")

def main():
    print("\n[*] Decryptor Running...")
    key = load_key()
    fernet = Fernet(key)
    for root, dirs, files in os.walk(TARGET_FOLDER):
        for file in files:
            if file.endswith(".locked"):
                decrypt_file(os.path.join(root, file), fernet)
    print("\n[+] All files restored!\n")

if __name__ == "__main__":
    main()
EOF
