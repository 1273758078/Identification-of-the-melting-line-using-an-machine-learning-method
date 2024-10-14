import os

# Set the folder number as a string
num = str(800)

# Define the sections to iterate over
AB = ['A', 'B']

# Loop through each section (A or B) and create directories if they don't exist
for i in AB:
    for j in range(731):
        filePath = 'D:/training_' + num + '/section' + str(i) + str(j)
        if not os.path.exists(filePath):
            os.makedirs(filePath)  # Create the directory if it doesn't exist
        print(filePath)  # Print the created directory path

# Create directories for section A with subfolder 'j_128'
for k in range(731):
    filePath = 'D:/training_' + num + '/sectionA' + str(k) + '/j_128'
    if not os.path.exists(filePath):
        os.makedirs(filePath)  # Create the directory if it doesn't exist
    print(filePath)  # Print the created directory path

# Create directories for section B with subfolder 'f_128'
for k in range(731):
    filePath = 'D:/training_' + num + '/sectionB' + str(k) + '/f_128'
    if not os.path.exists(filePath):
        os.makedirs(filePath)  # Create the directory if it doesn't exist
    print(filePath)  # Print the created directory path

# The commented section checks if folders exist and creates them accordingly
# # Check if the directory exists, if not, create it
# for i in range(701):
#     for k in range(-1, i - 701, -1):
#         print(k)
