from MyPakage.Api.api_module import get_api_module
from MyPakage.database.database_module import get_database_module
from MyPakage.images.images_moduls import get_images_module
from MyPakage.report.report_module import get_report_module

def print_option():
    print("1. For Api")
    print("2. For Database")
    print("3. For images")
    print("4. For reports")

  
def dash_board():
    print_option() 
    while(True):
       option = int(input("Enter a number : "))
     
       if option == 1:
          get_api_module()
       elif option == 2:
          get_database_module()
       elif option == 3:
          get_images_module()
       elif option == 4:
          get_report_module()
    