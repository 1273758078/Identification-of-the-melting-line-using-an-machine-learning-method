import os
num = str(800)
AB = ['A', 'B']
for i in AB:
    for j in range(731):
        filePath = 'D:/training_' + num + '/section' + str(i) + str(j)
        if not os.path.exists(filePath):
            os.makedirs(filePath)
        print(filePath)

for k in range(731):
    filePath = 'D:/training_' + num + '/sectionA' + str(k) + '/j_128'
    if not os.path.exists(filePath):
        os.makedirs(filePath)
    print(filePath)
for k in range(731):
    filePath = 'D:/training_' + num + '/sectionB' + str(k) + '/f_128'
    if not os.path.exists(filePath):
        os.makedirs(filePath)
    print(filePath)


# 判断文件夹是否存在，不存在则创建文件夹
# for i in range(701):
#     for k in range(-1, i-701, -1):
#         print(k)