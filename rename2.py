import os
import shutil
# 指定要修改文件名的文件夹路径
folder_path = '/home/ybc/MedSAM/data/LiTS/labels'
# 获取文件夹中所有文件的文件名
filenames = os.listdir(folder_path)
# 遍历文件名列表，对每个文件名进行修改
for filename in filenames:
# 在文件名中添加或删除指定的文本
    new_filename = filename.replace('segmentation', 'volume')
# 指定旧文件名和新文件名的完整路径
    old_file_path = os.path.join(folder_path, filename)
    new_file_path = os.path.join(folder_path, new_filename)
# 重命名文件
    shutil.move(old_file_path, new_file_path)