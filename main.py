import csv

import pandas
# initial reading of csv file
def read_file():
    data = []
    with open('sales.csv', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)
    return data
# ---------------------------------------------

# run data to get general sales for year
def get_yearly_sales():
    data = read_file()

    sales = []
    expenditure = []

    for row in data:
        sale = int(row['sales'])
        sales.append(sale)
        month_expenditure = int(row['expenditure'])
        expenditure.append(month_expenditure)

    total_sales = sum(sales)
    total_expenditure = sum(expenditure)
    total_profit = total_sales - total_expenditure
    print('\n')
    print('_____________________________________________________________')
    print('Total sales for all months in year {}: £{}'.format(row['year'], total_sales))
    print('Total cost for all months in year {}: £{}'.format(row['year'], total_expenditure))
    print('Total profit for all months in year {}: £{}'.format(row['year'], total_profit))
    print('_____________________________________________________________')
    print('\n')
# ---------------------------------------------

# view all months and their relevant sales and profit
def get_monthly_sales():
    data = read_file()
    print('\n')
    print('_____________________________________________________________')
    print('Sales by month report')
    print('_____________________________________________________________')

    # headers
    print('month sales profit')

    for row in data:
        sales = int(row['sales'])
        expenditure = int(row['expenditure'])
        profit = sales - expenditure
        print('{} £{} £{}'.format(row['month'], row['sales'], profit))
    print('\n')
# ---------------------------------------------

# get monthly sales average for the year
def get_average_sales():
    data = read_file()

    total_sales = 0
    # to calculate how many months are in csv file
    counter = 0

    for row in data:
        sales = int(row['sales'])
        total_sales = total_sales + sales
        counter = counter + 1

    average_sales = total_sales / counter

    print('\n')
    print('_____________________________________________________________')
    print('Average monthly sales for year {}: £{:.2f}'.format(row['year'], average_sales))
    print('_____________________________________________________________')
    print('\n')
# ---------------------------------------------

# get name of month with lowest sales and sales amount
def get_lowest_month():
    data = read_file()

    df = pandas.read_csv('sales.csv')
    min = int(df['sales'].min())

    for row in data:
        if (int(row['sales']) == min):
            lowest_month = (row['month'])

    print('\n')
    print('_____________________________________________________________')
    print('Month with lowest sales: {} £{}'.format(lowest_month, min))
    print('_____________________________________________________________')
    print('\n')
# ---------------------------------------------

# get name of month with highest sales and sales amount
def get_highest_month():
    data = read_file()

    df = pandas.read_csv('sales.csv')
    max = int(df['sales'].max())

    for row in data:
        if (int(row['sales']) == max):
            highest_month = (row['month'])

    print('\n')
    print('_____________________________________________________________')
    print('Month with highest sales: {} £{}'.format(highest_month, max))
    print('_____________________________________________________________')
    print('\n')
# ---------------------------------------------

# this function will prompt the user to enter the names of two months and will output the percentage increase or decrease in sales
def get_percentage_change():
    data = read_file()

    # for validation
    months=("january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december")

    print('\n')
    print('_____________________________________________________________')
    print('GET PERCENTAGE CHANGE')

    month_one = input('Input the name of the first month').lower()

    # if input not valid, prompt again
    while month_one not in months:
        month_one = input('Oops...try that again. Input the name of the first month').lower()

    # substring first 3 chars
    month_one = month_one[0:3]

    month_two = input('Input the name of the second month').lower()

    while month_two not in months:
        month_two = input('Oops...try that again. Input the name of the second month').lower()

    month_two = month_two[0:3]

    # for loop to get sales value for the user's chosen months
    for row in data:
        if row['month'] == month_one:
            month_one_value = int(row['sales'])
        if row['month'] == month_two:
            month_two_value = int(row['sales'])

    # compare values to output percentage increase or decrease
    if month_two_value > month_one_value:
        percentage_diff = ((month_two_value-month_one_value)/month_one_value) * 100
        print('Between {} and {} there was a percentage increase of {:.2f}%'.format(month_one, month_two, percentage_diff))
    elif month_one_value > month_two_value:
        percentage_diff = ((month_one_value - month_two_value)/month_one_value) * 100
        print('Between {} and {} there was a percentage decrease of {:.2f}%'.format(month_one, month_two, percentage_diff))
    else:
        print('Between {} and {} there was no percentage difference.'.format(month_one, month_two))

    print('_____________________________________________________________')
    print('\n')


# continuously print menu to user until they choose to exit
print('*** SALES ANALYSIS TERMINAL ***')
while True:
    print('1. View overall yearly sales report')
    print('2. View yearly sales average')
    print('3. View monthly sales report')
    print('4. View lowest monthly sales')
    print('5. View highest monthly sales')
    print('6. View percentage change between given months')
    print('7. Exit system.')
    user_input=input('Choose an option 1-7')
    if user_input == '7': # exit menu
        print('_____________________________________________________________')
        print('TERMINAL CLOSING....')
        print('_____________________________________________________________')
        break
    elif user_input == '1':
        get_yearly_sales()
    elif user_input == '2':
        get_average_sales()
    elif user_input == '3':
        get_monthly_sales()
    elif user_input =='4':
        get_lowest_month()
    elif user_input == '5':
        get_highest_month()
    elif user_input == '6':
        get_percentage_change()
