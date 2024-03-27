#pandas library example

'''
import pandas as pd
my_dict ={
    'Name' :['Ravi','Raju','Alex','Anusha','Gayathri','Neha','Vennela','Durga'],
    'Marks' :[40,48,40,40,50,42,46,42]
}
df=pd.DataFrame(data=my_dict)
df.plot.line(title='Marks')
pic = df.plot.line()
pic=pic.get_figure()
pic.savefig('a.jpg')

'''

#matplotlib,NumPy
'''
import matplotlib.pyplot as plt
import numpy as np
y=np.array([35,25,25,15])
mylabels=["DBMS","Python","OS","MP"]
plt.pie(y,labels=mylabels,startangle=90)
plt.show()
'''

#Example 4
'''
import numpy as np
# Creating a NumPy array
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

# Basic operations on arrays
sum_arr1 = np.sum(arr1)
mean_arr2 = np.mean(arr2)

print("Sum of 1D Array:", sum_arr1)
print("Mean of 2D Array:", mean_arr2)

# Element-wise operations
squared_arr1 = np.square(arr1)
sqrt_arr2 = np.sqrt(arr2)

print("Squared elements of arr1:", squared_arr1)
print("Square root of arr2:", sqrt_arr2)

'''

#Example 5
'''
import matplotlib.pyplot as plt
import numpy as np
regnum = ['101', '102', '103']
categories = ["DBMS", "Python", "OS", "MP"]
values = np.array([
    [35, 25, 25, 15],  # Values for category "DBMS"
    [20, 30, 15, 35],  # Values for category "Python"
    [10, 40, 20, 30],  # Values for category "OS"
])
colors = ['blue', 'green', 'pink', 'light red']
# Plot area for each registration number and category
for i, reg in enumerate(regnum):
    plt.fill_between(categories, 0, values[i], label=f'Registration {reg}', color=colors[i], alpha=0.7)
# Add labels and title
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Area Plot with Different Colors")
plt.legend()
plt.show()
'''


