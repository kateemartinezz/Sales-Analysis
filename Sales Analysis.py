### Import libraries
import pandas as pd
import os
import numpy as np

#create a blank data frame to store the final concatenated data
Final_data = pd.DataFrame()


## Merging 12 months of sales data into a single file

path = './Sales_Data'
files = os.listdir(path)
sales_files = [f for f in files if f.endswith('.csv')]

for file in sales_files:
    file_path = os.path.join(path, file)
    data = pd.read_csv(file_path)
    Final_data = pd.concat([Final_data, data])
    print(file)
    
# pd = pd.read_csv('./Sales_Data/Sales_April_2019.csv')
# pd

Final_data = Final_data.dropna()
Final_data = Final_data.reset_index(drop=True)
Final_data.head()

#convert to csv for the final df and download in the computer
Final_data.to_csv('Final_data.csv', index = False)
 
#read into the new file
New_data = pd.read_csv('Final_data.csv') 
New_data.head(5)
print(New_data.dtypes)


#convert the dates to datetime objects
New_data['Order Date'] = pd.to_datetime(New_data['Order Date'], format = '%m/%d/%y')
New_data   

#make a new column for month
# New_data['Month'] = New_data['Order Date'].dt.strftime('%Y-%m')
# New_data

New_data = New_data.drop('Month', axis = 1)
New_data
# New_data.groupby('Month').sum()

#January 2019
# Jan2019 = New_data.loc[New_data['Order Date'] == '01/01/19']['Total Sales'].sum()
# Jan2019

Jan2019 = New_data[(New_data['Order Date'].dt.year == 2019) & 
                   (New_data['Order Date'].dt.month == 1)
                   ]['Total Sales'].sum()
Jan2019

Feb2019 = New_data[(New_data['Order Date'].dt.year == 2019) & 
                   (New_data['Order Date'].dt.month == 2)
                   ]['Total Sales'].sum()
Feb2019

Mar2019 = New_data[(New_data['Order Date'].dt.year == 2019) & 
                   (New_data['Order Date'].dt.month == 3)
                   ]['Total Sales'].sum()
Mar2019

April2019 = New_data[(New_data['Order Date'].dt.year == 2019) & 
                   (New_data['Order Date'].dt.month == 4)
                   ]['Total Sales'].sum()
April2019

May2019 = New_data[(New_data['Order Date'].dt.year == 2019) & 
                   (New_data['Order Date'].dt.month == 5)
                   ]['Total Sales'].sum()
May2019

June2019 = New_data[(New_data['Order Date'].dt.year == 2019) & 
                   (New_data['Order Date'].dt.month == 6)
                   ]['Total Sales'].sum()
June2019

July2019 = New_data[(New_data['Order Date'].dt.year == 2019) & 
                   (New_data['Order Date'].dt.month == 7)
                   ]['Total Sales'].sum()
July2019

Aug2019 = New_data[(New_data['Order Date'].dt.year == 2019) & 
                   (New_data['Order Date'].dt.month == 8)
                   ]['Total Sales'].sum()
Aug2019

Sept2019 = New_data[(New_data['Order Date'].dt.year == 2019) & 
                   (New_data['Order Date'].dt.month == 9)
                   ]['Total Sales'].sum()
Sept2019

Oct2019 = New_data[(New_data['Order Date'].dt.year == 2019) & 
                   (New_data['Order Date'].dt.month == 10)
                   ]['Total Sales'].sum()
Oct2019

Nov2019 = New_data[(New_data['Order Date'].dt.year == 2019) & 
                   (New_data['Order Date'].dt.month == 11)
                   ]['Total Sales'].sum()
Nov2019

Dec2019 = New_data[(New_data['Order Date'].dt.year == 2019) & 
                   (New_data['Order Date'].dt.month == 12)
                   ]['Total Sales'].sum()
Dec2019

Jan2020 = New_data[(New_data['Order Date'].dt.year == 2020) & 
                   (New_data['Order Date'].dt.month == 1)
                   ]['Total Sales'].sum()
Jan2020

### MAKE A FINAL DF FOR THE SALES PER MONTH ### 
TotalSalesPerMonth = pd.DataFrame({'Month & Year': ['Jan 2019', 'Feb 2019', 'Mar 2019',
                                                   'April 2019', 'May 2019', 'June 2019',
                                                   'July 2019', 'Aug 2019', 'Sept 2019',
                                                   'Oct 2019', 'Nov 2019', 'Dec 2019'], 
                                   'Total Sales': [Jan2019, Feb2019, Mar2019,
                                                   April2019, May2019, June2019,
                                                   July2019, Aug2019, Sept2019,
                                                   Oct2019, Nov2019, Dec2019]}
                                #   index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
                                  )
TotalSalesPerMonth

## Get the Max Volume ##
# TotalSalesPerMonth['Total Sales'].max() #December has the most sales

##insert matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# MonthYear = range(1,14)
# bar_plot = plt.bar(MonthYear,TotalSalesPerMonth['Total Sales'])

TotalSalesPerMonth.set_index('Month & Year')['Total Sales'].plot(kind = 'bar')
plt.xlabel('Month & Year')
plt.ylabel('Total Sales')
plt.title('Total Sales Per Month')
plt.show()



### What US City had the highest number of sales ###
#add a city column with the .apply method
def get_city(address):
    return address.split(',')[1]

def get_state(address):
    return address.split(',')[2].split(' ')[1]


New_data['City'] = New_data['Purchase Address'].apply(lambda x: f'{get_city(x)}  ({get_state(x)})')
New_data.head(5)

New_data.drop(columns = 'CityData', inplace = True)

### What US City had the highest number of sales ###
CityData = New_data.drop(columns = 'Order Date', inplace = True)
CityData = New_data.groupby('City').sum()
CityData

##insert matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# MonthYear = range(1,14)
# bar_plot = plt.bar(MonthYear,TotalSalesPerMonth['Total Sales'])
cities = [city for city, df in CityData.groupby('City')]

# cities.set_index('City')['Total Sales'].plot(kind = 'bar')

plt.bar(cities, CityData['Total Sales'])
plt.xticks(cities, rotation = 'vertical', size = 11)
plt.xlabel('City State')
plt.ylabel('Total Sales')
plt.title('City with the Highest Sales')
plt.show()

