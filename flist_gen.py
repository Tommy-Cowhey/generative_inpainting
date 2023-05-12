import os

dir_path = '../train/images'
flist_path = './train_flist.txt'

#dir_path = '../valid/images'
#flist_path = './valid_flist.txt'

with open(flist_path, 'w') as f:
    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)
        if os.path.isfile(file_path):
            f.write(file_path + '\n')