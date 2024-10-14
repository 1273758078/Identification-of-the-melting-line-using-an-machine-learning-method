import os

# Function to delete specific images based on the given name in the specified folder
def delete_specific_images(folder_path, image_name):
    file_list = os.listdir(folder_path)  # List all files in the folder
    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)  # Full path to the file
        if file_name == image_name:  # Check if the file matches the given image name
            os.remove(file_path)  # Remove the file
            # print("Image deleted successfully")

num = str(700)
AB = ['A', 'B']

# Loop through each section (A or B)
for i in AB:
    for j in range(731):
        print(str(i) + str(j))  # Print the current section and iteration
        filePath = 'D:/training_' + num + '/section' + str(i) + str(j)  # Construct the path to the section

        # Loop through 731 possible image prefixes
        for m in range(731):
            # Loop through specific ranges of image suffixes (20 to 23 inclusive)
            for n in range(20, 24):
                name = str(m) + "_" + str(n) + ".png"  # Construct the image name
                delete_specific_images(filePath, name)  # Attempt to delete the image
