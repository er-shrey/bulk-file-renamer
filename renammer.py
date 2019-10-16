import os
path = 'D:\\books\\\\Wallpapers'
files = os.listdir(path)


for index, file in enumerate(files):
    try:
        os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index+128), '.jpg'])))
    except:
        print index, file
        
