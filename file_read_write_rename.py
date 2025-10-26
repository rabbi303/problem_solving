#Rename .png files to .jpg 

import os

folder = "/media/rabbi/83afe739-1cf3-417b-8249-ba6841296dca/rabbi/office/anpr/remove"

for file in os.listdir(folder):
	if file.endswith(".png"):

		old_path= os.path.join(folder, file)
		new_name =  file.replace(".png", ".jpg")
		new_path= os.path.join(folder, new_name)

		os.rename(old_path, new_path)
print("rename done")

