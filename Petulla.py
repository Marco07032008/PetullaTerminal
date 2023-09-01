#!/usr/bin/env python3

import subprocess
import os
import sys
import time
import threading

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
    print("If you are running this in a VM, you should use an external wireless card because the VM may not recognize your internal wireless card.")
    print("1) Start monitor mode")
    print("2) Wifite")
    
    choice = input("Select an option: ")
    
    if choice == "1":
        print("Setting up monitor mode...")
        subprocess.run(["sudo", "apt", "install", "aircrack-ng", "-y"])
        subprocess.run(["figlet", "Setting up monitor mode..."])
        time.sleep(3)
        subprocess.run(["airmon-ng"])
        subprocess.run(["airmon-ng", "check"])
        subprocess.run(["airmon-ng", "start", "wlan0"])
        subprocess.run(["airodump-ng", "wlan0mon"])
        subprocess.run(["airodump-ng", "wlan0"])
    elif choice == "2":
        print("Installing and running Wifite...")
        subprocess.run(["sudo", "apt", "install", "wifite", "-y"])
        subprocess.run(["wifite"])
    else:
        print("Invalid choice.")

def run_ip_geolocation():
    print("Cloning and setting up IP Geolocation...")
    subprocess.run(["git", "clone", "https://github.com/maldevel/IPGeoLocation"])
    os.chdir("IPGeoLocation")
    subprocess.run(["sudo", "apt", "install", "python3-pip", "-y"])
    subprocess.run(["clear"])
    subprocess.run(["figlet", "IP Geolocation"])
    time.sleep(2)
    print("To use this tool, run:")
    print("cd IPGeoLocation")
    print("pip3 install -r requirements.txt --user")
    print("python3 ipgeolocation.py -t X.X.X.X (replace X.X.X.X with the victim's IP)")
    print("[104] Exit")
    while True:
        user_choice = input("Enter your choice: ")
        if user_choice == "104":
            subprocess.run(["Ctrl+C"])
            subprocess.run(["Ctrl+C"])
            break

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
    print("1) Phis attack")
    print("2) Sql attack")
    print("3) Wifi attack")
    print("4) IP Geolocation")
    
    choice = input("Select an option: ")
    
    if choice == "1":
        print("Running ZPhisher in 5 seconds...")
        time.sleep(5)
        run_zphisher()
    elif choice == "2":
        run_sqlmap()
    elif choice == "3":
        run_wifi_tools()
    elif choice == "4":
        run_ip_geolocation()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
