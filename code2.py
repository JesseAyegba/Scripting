"""
Pre-requisites:
    1) Ensure you have python3 installed on your local computer.
    2) Install the requests library ------  run 'pip install requests' - for windows
                                                        and
                                            'pip3 install requests' - for mac
    3) Install the Pandas library ------  run 'pip install Pandas' - for windows
                                                        and
                                            'pip3 install Pandas' - for mac

--------------------------------------------------------------------
This script makes a request  to the reqres api(https://reqres.in) and 
stores the data in an excel sheet called table

It should be noted that for this script to work properly, You need
a good internet connection.
"""
import json
import requests
import pandas as pd


res = requests.get("https://reqres.in/api/users?page=2")
status = res.status_code
response = json.loads(res.text)
data_section = response.get("data")
 
table = pd.DataFrame({
    "Id": [item.get("id") for item in data_section],
    "Email": [item.get("email") for item in data_section],
    "FirstName": [item.get("first_name") for item in data_section],
    "LastName": [item.get("last_name") for item in data_section],
    "Avatar": [item.get("avatar") for item in data_section]
})

table.to_csv("table.csv")

    