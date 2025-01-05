import os
import subprocess
import sys
import base64

def print_welcome():
    print("Welcome to Hackers Taskforce Ethical Hacking Basics!")
    print("This script will guide you through some basic steps in ethical hacking.")
    print("Make sure you have Kali Linux or a compatible environment installed.")

def install_nmap():
    print("\nStep 1: Installing Nmap...")
    if sys.platform == "win32":
        print("On Windows, please download and install Nmap from: https://nmap.org/download.html")
    else:
        subprocess.run(["sudo", "apt", "update"])
        subprocess.run(["sudo", "apt", "install", "-y", "nmap"])
        print("Nmap has been installed successfully!")

def run_nmap():
    print("\nStep 2: Running Nmap to scan a target...")
    print("For learning purposes, you can scan your own network or a known IP address.")
    target_ip = input("Enter the IP address to scan: ")
    subprocess.run(["nmap", target_ip])

def nmap_recon():
    print("\nStep 3: Understanding basic network reconnaissance with Nmap.")
    print("Nmap can help us gather information about devices on a network.")
    print("Use the following command to scan all open ports of a target:")
    print("nmap -p- <target_ip>")

def install_metasploit():
    print("\nStep 4: Installing Metasploit Framework (Optional, for learning purposes)")
    if sys.platform == "win32":
        print("On Windows, you can download and install Metasploit from: https://metasploit.help.rapid7.com/docs/installing-the-metasploit-framework")
    else:
        subprocess.run(["sudo", "apt", "install", "-y", "metasploit-framework"])
        print("Metasploit Framework is now installed.")

def secret_message():
    print("\nStep 5: Hidden Secret Message...")
    print("To reveal the hidden message, follow these steps:")
    print("1. Open this script in a text editor like nano or vim.")
    print("2. Locate the function call that hides a secret message.")
    print("3. Use your hacking skills to uncover it.")
    print("\nHint: If you're stuck, check out the HackerCMD repository on GitHub for more help.\n")
    
    # Secret Message Hidden (Base64 Encoded Version)
    hidden_message = base64.b64encode(b"The real hack is in the journey, not just the destination.").decode("utf-8")
    print(f"Tip: Inspect the script or use your tools to decode this string: {hidden_message}")
    
    # Saving hidden message in a text file (decoded)
    decoded_message = base64.b64decode(hidden_message).decode("utf-8")
    with open("hidden_message.txt", "w") as file:
        file.write(decoded_message)

    print(f"Your hidden message has been saved to 'hidden_message.txt'. Check there for your next hint!\n")

def final_reminder():
    print("\nRemember: Always use these skills ethically, with permission, and for educational purposes.")
    print("Never attempt unauthorized access or attacks on any network or system.\n")
    print("Happy Hacking! Stay curious and continue your learning journey!")

    # Suggest HackerCMD GitHub installation or exploration
    print("\nTo decode the encripted message go the the github repo and downlod it (and leave us a star :D)")
    print("Visit: https://github.com/Hackers-Taskforce/HackerCMD")
    print("Clone the repository to access more advanced scripts and tools for ethical hacking!\n")

def main():
    print_welcome()
    install_nmap()
    run_nmap()
    nmap_recon()
    install_metasploit()
    secret_message()
    final_reminder()

if __name__ == "__main__":
    main()
