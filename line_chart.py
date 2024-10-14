import matplotlib.pyplot as plt

# These two lines resolve the issue of displaying Chinese characters in the plot
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# Initialize lists for cutting positions and accuracy values
cutting = []
accuracy = []

# Dictionary containing cutting positions and corresponding accuracy values
dict1 = {
    150: 12171.71239,
    160: 13163.29306,
    170: 14316.96492,
    180: 15219.85566,
    190: 16194.48655,
    200: 17344.19508,
    210: 18167.67463,
    220: 19299.58296,
    230: 20362.91521,
    240: 21346.78235,
    250: 22737.66136
}

dict2 = {
    150: 0.936159610748291,
    160: 0.9401496052742004,
    170: 0.9421446323394775,
    180: 0.9431421160697937,
    190: 0.9441396594047546,
    200: 0.949127197265625,
    210: 0.9571072459220886,
    220: 0.968578577041626,
    230: 0.9596009850502014,
    240: 0.9511221647262573,
    250: 0.9271820187568665
}

# List of cutting positions
list1 = [210, 220, 230, 240, 250, 260, 270, 280, 290]

# List of accuracy values corresponding to the cutting positions
list2 = [0.952394009, 0.951573193, 0.955129981, 0.961422682, 0.96497947, 
         0.976744175, 0.986867309, 0.984404922, 0.970451415]

# Populate the cutting and accuracy lists
for i in range(9):
    cutting.append(list1[i])
    accuracy.append(list2[i])

# Plot the data
plt.plot(cutting, accuracy, '.-', label='Accuracy')

# Set the title, labels, and ticks for the plot
plt.title('Debye=200 (Partial)', fontsize=20)
plt.xticks(cutting)  # Set x-axis ticks to cutting positions
plt.tick_params(labelsize=15)  # Set font size for the ticks
plt.xlabel('Cutting Position', fontsize=20)  # Set x-axis label
plt.legend(fontsize=20)  # Display the legend

# Show the plot
plt.show()
