import pandas as pd
import numpy as np

# random integers
x = int(input('place values here'))
x = np.random.randint(1, x, 10)
x


# TASK3: Perform Mathematical Operations
x = np.arange(1, 10)
x

y = np.arange(1,10)
y

# add 2 numpy arrays together
sum = x + y
sum

### squared
squared = x ** 2
squared

#sqrt
sqrt = np.sqrt(squared)
sqrt

#exp
z = np.exp(y)
z

#obtain the distance
array1 = np.array([5, 7, 20])
array2 = np.array([9, 15, 4])

distance = np.sqrt(array1**2 + array2**2)
distance

#TASK 4: PERFORM ARRAYS SLICING AND INDEXING
my_numpy_array = np.array([3, 5, 6, 2, 8, 10, 20, 50])
my_numpy_array

#access specific elements
my_numpy_array[0]
my_numpy_array[-1]

#array slicing/get the first three elements not including 3
my_numpy_array[0:3]

#broadcasting, altering several values in a numpy array
my_numpy_array[0:4] = 7
my_numpy_array

#matrix slicing
matrix = np.random.randint(1, 10, (4,4))
matrix

#access the first row
matrix[0]

#access a single element
matrix[0][2]

#replace the values
matrix_2 = np.array([[2, 30, 20, -2, -4], 
                     [3, 4, 40, -3, -2], 
                     [-3, 4, -6, 90, 10], 
                     [13, 24, 22, 32, 37]])
matrix_2[3] = 0
# or matrix_2[-1] = 0
matrix_2

#TASK 5 PERFORM ELEMENTS SELECTION (CONDITIONAL)
matrix = np.random.randint(1, 10, (5,5))
matrix

#filter on that matrix and only obtain elements greater than 5
new_matrix = matrix[matrix > 7]
new_matrix

#obtain odd elements
new_matrix = matrix[matrix % 2 == 1]
new_matrix

#obtain even
new_matrix = matrix[matrix % 2 == 0]
new_matrix

#challenge replace negative elements by 0 and odd elements with -2
matrix_3 = np.array([[2, 30, 20, -2, -4],[3, 4, 40, -3, -2], [-3, 4, -6, 90, 10], [13, 24, 22, 32, 37]])
matrix_3[matrix_3 < 0 ] = 0
matrix_3[matrix_3 % 2 == 1] = -2
matrix_3


### PANDAS AND FUNDAMENTALS ###
import pandas as pd

#create a pandas df 
bankclient_df = pd.DataFrame({'Bank client': [111, 222, 333, 444], 'Bank Client Name': ['Chanel', 'Steve', 'Mitch', 'Ryan'],'Net Worth $':[3500, 29000, 10000, 20000],'Years with bank': [3,4,9,5]})
bankclient_df

type(bankclient_df)

#show the first rows
bankclient_df.head()

#show the last two rows
bankclient_df.tail(2)


## MINI CHALLENGE
portfolio_df = pd.DataFrame({"Stocks": ['NDAQ', 'CHWY', 'MSFT'], "Number of Shares": [28, 49, 82], "Price Per Share": [50, 16, 326]})
#create a new column
portfolio_df['Total Value'] =portfolio_df['Number of Shares'] * portfolio_df['Price Per Share']

portfolio_df['Total Value'].sum()

#Pandas with CSV and HTML Data
import pandas as pd
house_price_df = pd.read_html('https://www.livingin-canada.com/house-prices-canada.html')
#first table
house_price_df[0]
#second table
house_price_df[1]

#mini challenge
normal_retirement_age = pd.read_html('https://www.ssa.gov/oact/progdata/nra.html')
normal_retirement_age[0]

#PANDAS OPERATIONS
bankclient_df = pd.DataFrame({'Bank client': [111, 222, 333, 444], 'Bank Client Name': ['Chanel', 'Steve', 'Mitch', 'Ryan'],'Net Worth $':[3500, 29000, 10000, 20000],'Years with bank': [3,4,9,5]})
bankclient_df

#select those who are loyal with the bank
df_loyal = bankclient_df[   bankclient_df['Years with bank'] >= 5  ]
df_loyal

#delete a column
del bankclient_df['Bank client']
bankclient_df

high_net_worth = bankclient_df[bankclient_df['Net Worth $'] >= 5000]
high_net_worth['Net Worth $'].sum()

#PANDAS WITH FUNCTIONS
bankclient_df = pd.DataFrame({'Bank client': [111, 222, 333, 444], 'Bank Client Name': ['Chanel', 'Steve', 'Mitch', 'Ryan'],'Net Worth $':[3500, 29000, 10000, 20000],'Years with bank': [3,4,9,5]})
bankclient_df

#define a function
def networth_update(balance): 
    return balance * 1.2

bankclient_df['Net Worth $'].apply(networth_update)

bankclient_df['Bank Client Name'].apply(len)

#mini challenge
def triple(stock):
    return ((stock * 3) + 200)

portfolio_df = pd.DataFrame({"Stocks": ['NDAQ', 'CHWY', 'MSFT'], 
                             "Number of Shares": [28, 49, 82], 
                             "Price Per Share": [50, 16, 326]})

portfolio_df

new_portfolio = portfolio_df['Price Per Share'].apply(triple)
new_portfolio.sum()

# PERFORM SORTING AND ORDERING IN PANDAS
bankclient_df = pd.DataFrame({'Bank client': [111, 222, 333, 444], 
                              'Bank Client Name': ['Chanel', 'Steve', 'Mitch', 'Ryan'],
                              'Net Worth $':[3500, 29000, 10000, 20000],
                              'Years with bank': [3,4,9,5]})
bankclient_df

#sort data frame
bankclient_df.sort_values(by = 'Years with bank')

#change in memory
bankclient_df.sort_values(by = 'Years with bank', inplace = True)

#TASK 11: PERFORM CONCATENATING AND MERGING WITH PANDAS
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3'],
                     'C': ['C0', 'C1', 'C2', 'C3'],
                     'D': ['D0', 'D1', 'D2', 'D3']},
                   index = [0, 1, 2, 3])

df1


df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                     'B': ['B4', 'B5', 'B6', 'B7'],
                     'C': ['C4', 'C5', 'C6', 'C7'],
                     'D': ['D4', 'D5', 'D6', 'D7']},
                   index = [4, 5, 6, 7])

df2

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                     'B': ['B8', 'B9', 'B10', 'B11'],
                     'C': ['C8', 'C9', 'C10', 'C11'],
                     'D': ['D8', 'D9', 'D10', 'D11']},
                   index = [8, 9, 10, 11])

df3

pd.concat([df1, df2, df3])

#PROJECT AND CONCLUDING REMARKS
rawdata = pd.DataFrame({'Bank Client ID': ['1', '2', '3', '4', '5'],
                        'First Name': ['Kate', 'Kaye', 'Raquel', 'Marlon', 'Seth'],
                        'Last Name': ['Martinez', 'Acosta', 'Platon', 'Martinez', 'Alexander']},
                       )

bankdf1 = pd.DataFrame(rawdata, columns = ['Bank Client ID', 'First Name', 'Last Name'])

rawdata = pd.DataFrame({'Bank Client ID': ['6', '7', '8', '9', '10'],
                        'First Name': ['Jules', 'CJ', 'Kit', 'Lucille', 'Dylan'],
                        'Last Name': ['Pantangco', 'Olayvar', 'Mulliken', 'Lacanienta', 'Berdin']},
                       )

bankdf2 = pd.DataFrame(rawdata, columns = ['Bank Client ID', 'First Name', 'Last Name'])
bankdf2

#BANK SALARY
rawdata = {'Bank Client ID': ['1', '2', '3', '4', '5','6', '7', '8', '9', '10'],
           'Annual Salary': [40000, 45000, 55000, 60000, 52000, 72000, 98000, 100000, 20000, 50000]}

bankdfsalary = pd.DataFrame(rawdata, columns = ['Bank Client ID', 'Annual Salary'] )
bankdfsalary

#CONCATENATE
banksalaryall = pd.concat([bankdf1, bankdf2])
banksalaryall


banksalaryall = pd.merge(banksalaryall, bankdfsalary, on = 'Bank Client ID')
banksalaryall

new_client = {'Bank Client ID': ['11'],
              'First Name': 'Kate',
              'Last Name': 'Martinez',
              'Annual Salary': 90000}

new_client = pd.DataFrame(new_client, columns = ['Bank Client ID', 'First Name', 'Last Name', 'Annual Salary'] )
new_client

finalsalaryclient = pd.concat([banksalaryall, new_client], axis = 0)
finalsalaryclient