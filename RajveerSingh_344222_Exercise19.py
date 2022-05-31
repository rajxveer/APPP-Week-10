# Importing the pandas library as pd
import pandas as pd

# Importing the dataset into the Spyder enviroment
house = pd.read_csv("C:\\Users\\User\\Downloads\\USA_Housing.csv")
print(house)
print("As seen from output above, the dataset has been imported")

print("\nOutput below shows some basic info and stats of the dataset:")
print(house.info())
print(house.describe())

print("\nThe output below swaps the rows and columns of the dataset")
house_transpose = house.transpose()
print(house_transpose)

print("\nThe output below shows the missing values from the dataset")
print(house.isnull())
print(house.isnull().sum())
print("\nThe output above shows there are no missing values")

print("\nSince there are no missing values, there is no need to remove any.")
print("Encoding is not required too since the dataset is fine the way it is.\n")

print("The actual target variable (y) should be if the customer subscribe or not")
print("However, that data is not available in the provided dataset")
print("As such, I will choose the 'Price' variable as the target variable (y)")

x = house.drop('Price', axis = 1) # Dropping only the 'Price' variable
y = house.iloc[:,5] # 'Price' variable chosen as target variable

train_size = int(0.8 * len(house)) # Setting 80% train, 20% test
x_train = x[:train_size]
x_test = x[train_size:]
y_train = y[:train_size]
y_test = y[train_size:]

print("\nx_train shape: ", x_train.shape)
print("x_test shape: ", x_test.shape)
print("y_train shape: ", y_train.shape)
print("y_test shape: ", y_test.shape)

# Importing the matplotlib library as plt
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 12, 'figure.figsize': (10, 8)}) # Updating the plot sizes

# Scatter plot of Price against Avg. Area Income
house.plot(kind = 'scatter', x = 'Avg. Area Income', y = 'Price', title = 'Price against Avg. Area Income')

# Scatter plot of Price against Avg. Area House Age
house.plot(kind = 'scatter', x = 'Avg. Area House Age', y = 'Price', title = 'Price against Avg. Area House Age')

# Scatter plot of Price against Avg. Area Number of Rooms
house.plot(kind = 'scatter', x = 'Avg. Area Number of Rooms', y = 'Price', title = 'Price against Avg. Area Number of Rooms')

# Scatter plot of Price against Avg. Area Number of Bedrooms
house.plot(kind = 'scatter', x = 'Avg. Area Number of Bedrooms', y = 'Price', title = 'Price against Avg. Area Number of Bedrooms')

# Scatter plot of Price against Area Population
house.plot(kind = 'scatter', x = 'Area Population', y = 'Price', title = 'Price against Area Population')
