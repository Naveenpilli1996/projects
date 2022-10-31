import urllib.request


def dl_img(url,File_Path,file_name):
    full_path=File_Path+file_name+'.jpg'
    urllib.request.urlretrieve(url,full_path)






url=input('Enter your website : ')
File_Path='/home/ubuntu/Programming/Python/Downloading Images/Images'
file_name=input('Enter your file name :')
dl_img(url,File_Path,file_name)