import sys
import smtplib
import requests
import os

no = ['no','No','NO','N','n']
yes = ['yes','Yes','YES','YEs','YeS','yES','y','Y']

class bcolors:
    PROMPT = '\033[33m'
    ERROR = '\033[91m'
    OK = '\033[92m'

def start():
    print("start")

def checkVersion():
    versionFile = open("version.txt")
    global version
    version = versionFile.read()
    float(version)
    versionFile.close()

def checkUpdate():
    githubVersion = requests.get('https://raw.githubusercontent.com/TheMasterOfE/PhishBox/master/version.txt')
    statusCode = githubVersion.status_code
    int(statusCode)
    if statusCode == 200:
        latestVersion = githubVersion.text
        float(latestVersion)
        if latestVersion == version:
            print(bcolors.OK + 'Looks like PhishBox is up to date!')
        else:
            print(bcolors.ERROR + 'It looks like you are using an outdated version of PhishBox!')
            promptUpdate()
    else:
        print(bcolors.ERROR + "ERROR " + statusCode)

def update():
    print(bcolors.OK + "E")
    os.system("cd ..")
    os.system("rm -rf PhishBox")
    os.system("git clone https://github.com/TheMasterOfE/PhishBox")

def promptUpdate():
    willUpdate = input(bcolors.PROMPT + "Would you like to update Y/N\n")
    if willUpdate in yes:
        update()
    elif willUpdate in no:
        start()
    else:
        print("Please enter either Yes or No")
        promptUpdate()

def banner():
    print(bcolors.OK + "██████╗ ██╗  ██╗██╗███████╗██╗  ██╗██████╗  ██████╗ ██╗  ██╗")
    print(bcolors.OK + "██╔══██╗██║  ██║██║██╔════╝██║  ██║██╔══██╗██╔═══██╗╚██╗██╔╝")
    print(bcolors.OK + "██████╔╝███████║██║███████╗███████║██████╔╝██║   ██║ ╚███╔╝")
    print(bcolors.OK + "██╔═══╝ ██╔══██║██║╚════██║██╔══██║██╔══██╗██║   ██║ ██╔██╗")
    print(bcolors.OK + "██║     ██║  ██║██║███████║██║  ██║██████╔╝╚██████╔╝██╔╝ ██")
    print(bcolors.OK + "╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝")

    # Please change the version and edit date when changes are made cause it looks offical :)
    # A note to future us we could impliment an api to check the latest commit and version to see if an update is available
    print(bcolors.OK + "Version " + version)
    print(bcolors.OK + "Last edit: 9/20/19")
    print(bcolors.OK + "By DJCHICKEN4, Commi3, ???")
    print(bcolors.OK + "This is to be used for legal and educational purposes only. Any other use is not intended.")

class phishBox:
    count = 0

    def __init__(self):
            print("\n+{+{+{Initializing PhishBox}+}+}+")

checkVersion()
banner()
checkUpdate()
