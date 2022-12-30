#!/usr/bin/env/python3
# This Python file uses the following encoding: utf-8

# ===== #
# Website:  https://www.hacktadine.blogspot.com
# Author:   adithya uday kumar | hacktadine
# GitHub:   https://github.com/hacktadine
# linkedin: https://www.linkedin.com/in/adithya-uday-kumar-moganti-b90129251/
# instagram:https://instagram.com/hacktadine
# Facebook: https://www.facebook.com/profile.php?id=100069546190609
# Twitter:  https://twitter.com/hacktadine
# Youtube:  https://www.youtube.com/channel/UCs7tw5VNmQVg_kEOpeZLpT
# ===== #

# ===== #
# Created october 2022 | Copyright (c) 2022 hacktadine
# ===== #

########################################################################

# A note to all nerds,n00bs and techfreaks
# If you copy my work you will never because hacker.
# Respect and support all developers
# be secure, respect privacy
# respect existence and expect presistence
########################################################################
import twint
import sys
import time


def banner():
    print(""" \033[1;34m
 
 
 .__                   __      __              .___.__               
|  |__ _____    ____ |  | ___/  |______     __| _/|__| ____   ____  
|  |  \\__  \ _/ ___\|  |/ /\   __\__  \   / __ | |  |/    \_/ __ \ 
|   Y  \/ __ \\  \___|    <  |  |  / __ \_/ /_/ | |  |   |  \  ___/ 
|___|  (____  /\___  >__|_ \ |__| (____  /\____ | |__|___|  /\___  >
     \/     \/     \/     \/           \/      \/         \/     \/                                                                                   
            \033[1;m
             \033[34mtw34k3r Twitter OSINT \033[0m
             \033[34mAuthor: hacktadine  \033[0m
             \033[34mGithub:  https://github.com/hacktadine \033[0m
             \033[34mWebsite: https://hacktadine.blogspot.com \033[0m
              i do hacking for fun: this is my instant dopamine
              be secure, respect privacy
              respect existence or expect presistence""")


def menu():
    print("\n\033[1;34m[+] 1. Search - Fetch Tweets using the search filters\033[1;m")
    print("\033[1;34m[+] 2. Email - Fetch Tweets with Email Adress\033[1;m")
    print("\033[1;34m[x] 0. Exit\033[1;m\n")


def b00m():
    choice = ("1")
    banner()

    while choice != ("12"):
        menu()
        choice = input("\033[1;34m[+]\033[1;m \033[1;91mEnter your choice:\033[1;m ")

        if choice == ("1"):
            search = input("\n[~] \033[34mTwitter Search: \033[0m ")
            output = input("\n[~] \033[34mGive the file a name: \033[0m ")
            try:
                c = twint.Config()
                c.Search = search
                c.User_full = True
                c.Profile_full = True
                c.Replies = True
                c.Show_hashtags = True
                c.Stats = True
                c.Get_replies = True
                c.Store_csv = True
                c.Output = output + ".csv"

                twint.run.Search(c)

            except KeyboardInterrupt:
                print("\n")
                print("\033[1;91m[!] User Interruption Detected..!\033[0")
                time.sleep(0.5)
                print("\n\n\t\033[1;91m[!] you make sense dude, happy hacking \033[0m\n\n")
                time.sleep(0.5)

        elif choice == ("2"):
            search = input("\n[~] \033[34mUserName: \033[0m ")
            output = input("\n[~] \033[34mGive the file a Name: \033[0m ")
            try:
                c = twint.Config()
                c.Username = search
                c.User_full = True
                c.Email = True
                c.Store_csv = True
                c.Output = output + ".csv"

                twint.run.Search(c)

            except KeyboardInterrupt:
                print("\n")
                print("\033[1;91m[!] User Interruption Detected..!\033[0")
                time.sleep(0.5)
                print("\n\n\t\033[1;91m[!] for more follow me \033[0m😃\n\n")
                time.sleep(0.5)

        elif choice == ("0"):
            time.sleep(1)
            print(
                "\n\t\033[34mtw34k3r\033[0m DONE.. \033[34m[!] living in hacking \033[0m😃\n\n\033[0m\n")
            sys.exit()

        else:
            os.system("reset")
            print("\033[1;31m[-] Invalid option..! \033[1;m")


# =====# Main #===== #
if __name__ == "__main__":
    b00m()
