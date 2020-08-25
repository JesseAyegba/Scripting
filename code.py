"""
Pre-requisites:
    1) Ensure you have python3 installed on your local computer.
    2) Install the requests library ------  run 'pip install requests' - for windows
                                                        and
                                            'pip3 install requests' - for mac

--------------------------------------------------------------------
This script makes a request  to the reqres api(https://reqres.in), 
stores the data and renders it to the terminal(or any platform it's being run on)

It should be noted that for this script to work properly, You need
a good internet connection.
"""

import requests
import json



res = requests.get("https://reqres.in/api/users?page=2")
status = res.status_code
response = json.loads(res.text)

data_section = response.get("data")

#Error detection decorator
def error_handler(function):
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception:
            print("Please ensure that you are giving this function\nthe right object as argument. Refer to the \nfunction docs below for more details")
            print("---------------------------------------------------------------------------")
            print("                        FUNCTION DOCUMENTATION                             ")
            print("---------------------------------------------------------------------------")
            help(function)
        
    return wrapper


@error_handler
def foo(*args, **kwargs):
    """
        This function works on dictionary objects with
        1) An id key
        2) An email key
        3) A first_name key
        4) A last_name key
        5) An avatar key
        The order in which these keys a declared is not
        very important, however you are advised to follow
        the order used above
     """
    output = args[0]
    print(f"Id==>{output.get('id')}")
    print(f"Email==>{output.get('email')}")
    print(f"FirstName==>{output.get('first_name')}")
    print(f"LastName==>{output.get('last_name')}")
    print(f"Link==>{output.get('avatar')}")

        
        
#Test Case
for item in data_section:
    foo(item)
    print("\n")
    print("-------------------------------------------------------------------------")




 