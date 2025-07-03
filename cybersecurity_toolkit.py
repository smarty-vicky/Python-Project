import socket
import hashlib
import requests
import re
import os

def port_scanner(target):
    print(f"🔎 Scanning ports on {target}...\n")
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"✅ Port {port} is open")
        sock.close()

def password_strength(password):
    print("\n🔐 Checking password strength...")
    length = len(password) >= 8
    upper = bool(re.search(r"[A-Z]", password))
    lower = bool(re.search(r"[a-z]", password))
    digit = bool(re.search(r"[0-9]", password))
    symbol = bool(re.search(r"[^A-Za-z0-9]", password))

    score = sum([length, upper, lower, digit, symbol])

    if score == 5:
        print("✅ Strong password 💪")
    elif score >= 3:
        print("⚠️ Moderate password")
    else:
        print("❌ Weak password!")

def ip_lookup(ip):
    print(f"\n🌐 IP Lookup for {ip}...")
    try:
        res = requests.get(f"https://ipinfo.io/{ip}/json")
        data = res.json()
        for key in ['ip', 'city', 'region', 'country', 'org']:
            print(f"{key.capitalize()}: {data.get(key)}")
    except:
        print("❌ Failed to fetch IP data.")

def hash_generator(text):
    print("\n📜 Hashes:")
    print(f"MD5: {hashlib.md5(text.encode()).hexdigest()}")
    print(f"SHA1: {hashlib.sha1(text.encode()).hexdigest()}")
    print(f"SHA256: {hashlib.sha256(text.encode()).hexdigest()}")

def clear_dns_cache():
    print("\n🧼 Clearing DNS cache...")
    os.system("ipconfig /flushdns")

def menu():
    while True:
        print("\n🔧 CYBERSECURITY TOOLKIT")
        print("1. Port Scanner")
        print("2. Password Strength Checker")
        print("3. IP Info Finder")
        print("4. Hash Generator")
        print("5. Clear DNS Cache (Windows)")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            target = input("Enter target IP or domain: ")
            port_scanner(target)
        elif choice == '2':
            pwd = input("Enter password to test: ")
            password_strength(pwd)
        elif choice == '3':
            ip = input("Enter IP address: ")
            ip_lookup(ip)
        elif choice == '4':
            text = input("Enter text to hash: ")
            hash_generator(text)
        elif choice == '5':
            clear_dns_cache()
        elif choice == '6':
            print("👋 Exiting... Stay safe online!")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    menu()
