import os
import shutil
os.mkdir("./train")
os.mkdir("./valid")
os.mkdir("./test")

ls = os.listdir('./data')
txt_count = 0
jpg_count = 0
for i in ls:
    if i[-4:]==".txt":
        txt_count+=1
    elif i[-4:]==".jpg":
        jpg_count+=1


total = jpg_count
train = round(jpg_count*0.85)
valid = round(jpg_count*0.1)
test = round(jpg_count*0.05)


# print('放入train文档中的数量为:',train)
# print('放入valid文档中的数量为:',valid)
# print('放入test文档中的数量为:',test)



new_path2 = fr"C:\Users\86132\Desktop\python高级\文件与目录操作\text1\test"
new_path3 = fr"C:\Users\86132\Desktop\python高级\文件与目录操作\text1\valid"
# print(new_path1)
# print(new_path2)
# print(new_path3)
new_path1 = fr"C:\Users\86132\Desktop\python高级\文件与目录操作\text1\train"
for i in range(train):
    old_path = fr"C:\Users\86132\Desktop\python高级\文件与目录操作\text1\data\img{i+1}.jpg"
    shutil.copy(old_path,new_path1)

new_path2 = fr"C:\Users\86132\Desktop\python高级\文件与目录操作\text1\test"
for i in range(valid):
    old_path = fr"C:\Users\86132\Desktop\python高级\文件与目录操作\text1\data\img{i+1+valid}.jpg"
    shutil.copy(old_path,new_path2)


new_path3 = fr"C:\Users\86132\Desktop\python高级\文件与目录操作\text1\valid"
for i in range(test):
    old_path = fr"C:\Users\86132\Desktop\python高级\文件与目录操作\text1\data\img{i+1+valid+train}.jpg"
    shutil.copy(old_path,new_path3)


