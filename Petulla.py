#!/usr/bin/env python3

import subprocess
import os
import sys
import time

def install_figlet():
    # Check if figlet is installed
    result = subprocess.run(["which", "figlet"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print("Installing figlet...")
        subprocess.run(["sudo", "apt", "install", "figlet", "-y"])

def run_zphisher():
    print("Cloning and running ZPhisher...")
    subprocess.run(["git", "clone", "--depth=1", "https://github.com/htr-tech/zphisher.git"])
    os.chdir("zphisher")
    subprocess.run(["bash", "zphisher.sh"])

def run_sqlmap():
    print("Cloning and running sqlmap...")
    subprocess.run(["git", "clone", "--depth", "1", "https://github.com/sqlmapproject/sqlmap.git", "sqlmap-dev"])
    os.chdir("sqlmap-dev")
    subprocess.run(["sudo", "python3", "sqlmap.py", "--wizard"])

def run_wifi_tools():
    print("Running Wi-Fi tools...")
    subprocess.run(["figlet", "Choose one"])
    time.sleep(2)
    print("1) Airmon-ng")
    print("2) Wifite")
    
    choice = input("Select an option: ")
    
    if choice == "1":
        subprocess.run(["airmon-ng"])
    elif choice == "2":
        subprocess.run(["wifite"])
    else:
        print("Invalid choice.")

def main():
    # Check if the script is run with root privileges
    if os.geteuid() != 0:
        print("You must run this as root!")
        sys.exit(1)

    # Install figlet if not already installed
    install_figlet()

    # Display a message using figlet
    subprocess.run(["figlet", "Petulla Terminal"])

    # Display menu options
    print("1) Phishing attack")
    print("2) Sql attack")
    print("3) Wifi attack")
    
    choice = input("Select an option: ")
    
    if choice == "1":
        print("Running ZPhisher in 5 seconds...")
        time.sleep(5)
        run_zphisher()
    elif choice == "2":
        run_sqlmap()
    elif choice == "3":
        run_wifi_tools()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
