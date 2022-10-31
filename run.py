# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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
    while True:
        print('Please enter sales data from last market.')
        print('Data should be six numbers, separated by a comma')
        print('Example: 10,20,30,40,50,60\n')

        data_str = input('Enter your data here: ')
        
        sales_data = data_str.split(',') 

        if validate_data(sales_data):
            print('Data is valid')
            break

    return sales_data


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
        return False
    
    return True

def update_sales_worksheet(data):
    """
    This function updates the sales worksheet with sales data provided
    Function is called in main function
    """
    print('Updating the sales data worksheet....\n') 
    sales_worksheet = SHEET.worksheet('sales')
    sales_worksheet.append_row(data)
    print('Sales Worksheet updated successfully.\n')

def calculate_sales_surplus(sales_row):
    """    Calculate surplus sandwiches made per day
    """
    print('Calculating surplus data....\n')
    stock = SHEET.worksheet('stock').get_all_values()
    #pprint(stock)
    stock_row = stock[-1]    

    surplus_data = []  #empty list to hold the surplus calculations
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)
    
    return surplus_data

def update_surplus_worksheet(surplus):
    """
    This function updates the surplus worksheet with surplus - sales data
    Function is called in main function
    """
    print('Updating the surplus worksheet....\n') 
    surplus_worksheet = SHEET.worksheet('surplus')
    surplus_worksheet.append_row(surplus)
    print('Surplus Worksheet updated successfully.\n')
    



def main():
    """
        Run the program functions
    """    
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_sales_worksheet(sales_data)    
    new_surplus_data = calculate_sales_surplus(sales_data) 
    update_surplus_worksheet(new_surplus_data)

print('Welcome to love sandwiches data automation')
main()
