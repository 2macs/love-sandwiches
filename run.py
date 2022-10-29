# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')


def get_sales_data():

    """    This function will get the sales data from the user    
    """
    print('Please enter sales data from last market.')
    print('Data should be six numbers, separated by a comma')
    print('Example: 10,20,30,40,50,60\n')

    data_str = input('Enter your data here: ')
    
    sales_data = data_str.split(',') 
    validate_data(sales_data)


def validate_data(values):
    """
    Validates the data received from the user, must be 6 values and converted to integers
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(f'Exactly 6 values expected, you provided {len(values)}')
    except ValueError as e:
            print(f'Invalid data {e}, please try again \n')

    print(values)

    
get_sales_data()

