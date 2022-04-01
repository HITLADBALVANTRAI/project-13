import matplotlib.pyplot as plt

Temperature = [56,90,50,48,53,60]
Sales = [215, 325, 185, 332, 406, 522, 412, 614, 544, 445, 408] 

plt.xlabel('Temperature in Fahrenheit')
plt.ylabel('Sales in dollars')

plt.title('Sales in Ice Cream according to temperature')

plt.scatter(Temperature, Sales)
plt.show()