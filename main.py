import sys
import smtplib

class bcolors:
  GREEN = '\033[92m'
  YELLOW = '\022[93m'
  RED = '\033[91m'

def banner():
  print(bcolors.BLUE + "██████╗ ██╗  ██╗██╗███████╗██╗  ██╗██████╗  ██████╗ ██╗  ██╗")
  print(bcolors.BLUE + "██╔══██╗██║  ██║██║██╔════╝██║  ██║██╔══██╗██╔═══██╗╚██╗██╔╝")
  print(bcolors.BLUE + "██████╔╝███████║██║███████╗███████║██████╔╝██║   ██║ ╚███╔╝")
  print(bcolors.BLUE + "██╔═══╝ ██╔══██║██║╚════██║██╔══██║██╔══██╗██║   ██║ ██╔██╗")
  print(bcolors.BLUE + "██║     ██║  ██║██║███████║██║  ██║██████╔╝╚██████╔╝██╔╝ ██")
  print(bcolors.BLUE + "╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝")

  #Please change the version and edit date when changes are made cause it looks offical :)
  print(bcolors.GREEN + "Version 0")
  print(bcolors.GREEN + "Last edit: 9/20/19")
  print(bcolors.GREEN + "By DJCHICKEN4, Commi3, ???")
  print(bcolors.GREEN + "This is to be used for legal and educational purposes only. Any other use is not intended.")
  
class phishBox:
  count = 0 
  
  def __init__(self):
    try:
      print("\n+{+{+{Initializing phishBox}+}+}+")
      
  
  
