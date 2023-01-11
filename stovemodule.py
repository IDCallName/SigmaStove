import socket
import os
import subprocess

import warnings as w

import urllib.request

from hashlib import sha256 as makeHash

version: str = "0.0.1"

# ===========================
#
# VISUAL METHODS
#
# ===========================

POPUP_MESSAGES = (
    "",
    "Invalid choice option"
    )

COLOURS = {
    "End":      "\033[0m",
    "Green":    "\033[92m",
    "Yellow":   "\033[93m"
    }

def clScreen():
    """Removes previous text from console window."""
    
    
    os.system('cls' if os.name == 'nt' else 'clear')


def printLogo(small: bool = False):
    """Prints Stove logo (header for console application)
    
    If parameter "small" is True, prints normal text
    instead of ASCII art."""
    
    
    # An option for devices that have narrow screen
    if(small):
        print("σ Stove v{}".format(version))
    else:
        print("""{grn}
           _____ _                 
          / ____| |                
   ____  | (___ | |_ _____   _____ 
  /  ._)  \___ \| __/ _ \ \ / / _ \ 
 ( () )   ____) | || (_) \ V /  __/ 
  \__/   |_____/ \__\___/ \_/ \___|{end} Version {vers}
    """.format(grn = COLOURS["Green"], end = COLOURS["End"], vers = version))



def printChoice(*args: str):
    """Prints a list of multiple options in format
    
    1. args[0]
    2. args[1]
    ...
    n+1. args[n]"""
    
    
    # Warn if list is empty
    if len(args) == 0:
        w.warn("Empty choice list call")
    
    for i in range(1, len(args)+1):
        print("\t{}. {}".format(i, args[i-1]))
    print()


# Prints a popup message
def printPopup(popup: int):
    """Prints one of the couple of pre-determined
    popup texts. Check POPUP_MESSAGES tuple in this
    module for more info.
    
    Mostly used right after printLogo"""
    
    
    print(POPUP_MESSAGES[popup])
    print()
    
# ===========================
#
# FILE METHODS
#
# ===========================



# ===========================
#
# CONNECTION METHODS
#
# ===========================

# Getting global IP from ident.me
def getGlobalIp() -> str:
    """Gets computer's global IP from ident.me
    for operations with sockets"""
    
    
    return urllib.request.urlopen('https://ident.me').read().decode('utf8')

# Waiting for handshakes while online
def listenHandshakes():
    """Starts waiting for other connections to
    handshake with them"""
    
    
    myIP = getGlobalIp
    
    try:
        listenSocket = socket.socket()
    
    except socket.error as err:
        print(err)


def firstHandshake(ip: str, username: str, password: str):
    """Handshakes with a new user in stovespace"""
    
    
    pass
    # Sending first handshake request
    # Getting hash1
    # Adding hash1 to the password, hashing into hash2
    # Sending hash2

# ===========================
#
# OTHER METHODS
#
# ===========================

