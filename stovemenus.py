import socket
import subprocess
import getpass as gp

import stovemodule as smod

#
# A menu that is launched when my/userdata is empty
#
def menuStart(popup: int = 0):
    smod.clScreen()
    
    smod.printLogo()
    smod.printPopup(popup)
    smod.printChoice("Login", "Start a network", "Exit")
    
    choice: str = input("\t")
    
    if choice == "1":
        menuLogin()
    elif choice == "2":
        pass # start waiting for connections
    elif choice == "3":
        exit()
    else:
        menuStart(popup = 1)


#
# A menu with username/password/ip fields
#
def menuLogin(popup: int = 0):
    smod.clScreen()
    
    smod.printLogo()
    smod.printPopup(popup)
    
    print("\t{yel}Username{end}".format(yel = smod.COLOURS["Yellow"], end = smod.COLOURS["End"]))
    uname: str = input("\t")
    
    print("\n\t{yel}Password{end}".format(yel = smod.COLOURS["Yellow"], end = smod.COLOURS["End"]))
    passw: str = gp.getpass("\t")
    
    print("\n\t{yel}IP to connect through{end}".format(yel = smod.COLOURS["Yellow"], end = smod.COLOURS["End"]))
    stvip: str = input("\t")
    
    