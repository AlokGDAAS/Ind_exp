import os
import string
import ctypes

def list_drives():
    bitmask = ctypes.cdll.kernel32.GetLogicalDrives()
    drives = [f"{letter}:\\" for i, letter in enumerate(string.ascii_uppercase) if bitmask & (1 << i)]
    return drives