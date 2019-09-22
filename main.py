import sys
import smtplib
import requests

class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\022[93m'
    RED = '\033[91m'

def checkVersion():
    versionFile = open("version.txt")
    global version
    version = versionFile.read()
    int(version)
    versionFile.close()

def checkUpdate():
    githubVersion = requests.get('https://raw.githubusercontent.com/TheMasterOfE/PhishBox/master/version.txt')
    latestVersion = githubVersion.text
    int(latestVersion)
    if latestVersion == version:
        print(bcolors.GREEN + 'Looks like PhishBox is up to date!')
    else:
        print(bcolors.RED + 'It looks like you are using an outdated version of PhishBox!')


def banner():
    print(bcolors.GREEN + "██████╗ ██╗  ██╗██╗███████╗██╗  ██╗██████╗  ██████╗ ██╗  ██╗")
    print(bcolors.GREEN + "██╔══██╗██║  ██║██║██╔════╝██║  ██║██╔══██╗██╔═══██╗╚██╗██╔╝")
    print(bcolors.GREEN + "██████╔╝███████║██║███████╗███████║██████╔╝██║   ██║ ╚███╔╝")
    print(bcolors.GREEN + "██╔═══╝ ██╔══██║██║╚════██║██╔══██║██╔══██╗██║   ██║ ██╔██╗")
    print(bcolors.GREEN + "██║     ██║  ██║██║███████║██║  ██║██████╔╝╚██████╔╝██╔╝ ██")
    print(bcolors.GREEN + "╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝")

    # Please change the version and edit date when changes are made cause it looks offical :)
    # A note to future us we could impliment an api to check the latest commit and version to see if an update is available
    print(bcolors.GREEN + "Version " + version)
    print(bcolors.GREEN + "Last edit: 9/20/19")
    print(bcolors.GREEN + "By DJCHICKEN4, Commi3, ???")
    print(bcolors.GREEN + "This is to be used for legal and educational purposes only. Any other use is not intended.")

class phishBox:
    count = 0

    def __init__(self):
            print("\n+{+{+{Initializing PhishBox}+}+}+")


checkVersion()
banner()
checkUpdate()
