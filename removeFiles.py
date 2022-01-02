import os

# os.chdir("/Volumes/everything/iPhone media/upto2021")
directory = '/Volumes/everything/iPhone media/upto2021'

for filename in os.listdir(directory):
    # print(filename)
    if filename.endswith(".AAE"):
        print("removing bad stuff")
        os.remove(directory+"/"+filename)
