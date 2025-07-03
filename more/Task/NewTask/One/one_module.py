import sys
import os
sys.path.append(os.getcwd())

from NewTask.Three.three_module import get_three_module
from NewTask.Two.two_module import get_two_module


def get_one_module():
    print("one module ...")


def print_option():
    print("1. for one module")
    print("2. for two module")
    print("3. for three module")

def run_module():
    print_option()
    opt= input("Please enter an option : ") 

    option = int(opt) 

    while(True):
        if option == 1:
            get_one_module()
            break
        elif option == 2:
            get_two_module()
            break
        elif option == 3:
            get_three_module()
            break
        else:
            print("Please enter  a right number")

run_module()            














