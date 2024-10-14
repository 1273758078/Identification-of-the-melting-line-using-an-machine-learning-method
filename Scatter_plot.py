import matplotlib.pyplot as plt
import numpy as np

# Set font to display Chinese characters and properly handle minus signs in plots
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# Initialize lists for storing cutting points and accuracies
cutting = []
cutting2 = []
cutting3 = []
accuracy1 = []
accuracy2 = []
accuracy3 = []

# Dictionaries representing data for different cutting points (κ) and their corresponding values (Γ)
dict1 = {
    0.30: 135.0583449, 0.34: 136.1118453, 0.39: 127.6067065, 0.47: 139.1056209, 
    0.59: 145.7532899, 0.79: 192.2989888, 1.18: 176.9904061, 1.40: 248.4895032, 
    1.57: 318.2367828, 1.89: 341.5961861
}

dict2 = {
    0.30: 131.5483166, 0.34: 131.5338431, 0.79: 170.6218402, 1.18: 185.9948904, 
    1.40: 278.7662597, 1.57: 341.4678864, 1.89: 373.2765917
}

dict3 = {
    1.40: 221.7008909, 1.57: 274.6922917, 1.89: 319.3357758
}

# Lists of cutting points for the plots
list1 = [0.30, 0.34, 0.39, 0.47, 0.59, 0.79, 1.18, 1.40, 1.57, 1.89]
list2 = [0.30, 0.34, 0.79, 1.18, 1.40, 1.57, 1.89]
list3 = [1.40, 1.57, 1.89]

# Populate the accuracy lists using the dictionaries
for i in list1:
    cutting.append(i)
    accuracy1.append(dict1[i])

for i in list2:
    cutting2.append(i)
    accuracy2.append(dict2[i])

for i in list3:
    cutting3.append(i)
    accuracy3.append(dict3[i])

# Plot settings
plt.xlim(0.2, 2.5)  # X-axis range
plt.ylim(10, 5000)  # Y-axis range
plt.yscale('log')  # Logarithmic scale for the Y-axis
plt.title('Phase Transition Diagram from the Program')  # Plot title
plt.xlabel('κ', fontsize=20)  # X-axis label
plt.ylabel('Γ', fontsize=20)  # Y-axis label
plt.xticks(fontsize=15)  # Font size for X-axis ticks
plt.yticks(fontsize=15)  # Font size for Y-axis ticks

# Plot the data points
plt.scatter(cutting, accuracy1, marker='.', color='red', label="Predicted Points")
plt.scatter(cutting2, accuracy2, marker='.', color='g', label="Errors")
plt.scatter(cutting3, accuracy3, marker='.', color='b', label="Errors")

# Display the plot
plt.legend()  # Show legend
plt.show()
