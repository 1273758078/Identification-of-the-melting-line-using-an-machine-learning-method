import os
def delete_specific_images(folder_path, image_name):
    file_list = os.listdir(folder_path)
    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)
        if file_name == image_name:
            os.remove(file_path)
            # print("图片删除成功")

num = str(700)
AB = ['A', 'B']
for i in AB:
    for j in range(731):
        print(str(i) + str(j))
        filePath = 'D:/training_' + num + '/section' + str(i) + str(j)
        for m in range(731):
            for n in range(20, 24):
                name = str(m) + "_" + str(n) + ".png"
                delete_specific_images(filePath, name)
