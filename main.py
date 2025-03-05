import requests
import time as t
import os 
import random as r
from PIL import Image as I

folder = os.path.join(os.path.expanduser("~"), "Documents", "AI Images")
if os.path.exists(folder):
    pass
else:
    print("Error: Nonexistent File Path. Please go to your documents folder and create a folder named 'AI Images' (It must be capitalized like AI Images.) When done, start the program again.")
    exit()
userprompt = input("What do you want an AI image of? --> ")
userlink = userprompt.replace(' ', "%20")
seed = r.randint(1, 100)
image_url = f"https://image.pollinations.ai/prompt/{userlink}?seed={seed}&model=flux"
img_data = requests.get(image_url).content
file_path = os.path.join(os.path.expanduser("~"), "Documents", "AI Images", f"{userprompt}.jpg")
path = userprompt
error = False
if os.path.exists(file_path):
    error = True
number = 0
while error:
    path = f"{userprompt}{number}"
    file_path = os.path.join(os.path.expanduser("~"), "Documents", "AI Images", f"{path}.jpg")
    number += 1
    if os.path.exists(file_path):
        error = True
    else:
        error = False
with open(file_path, 'wb') as handler:
    handler.write(img_data)
image = I.open(f"{file_path}", "r")
image.show()


print(f"Done! Filename is {f'{path}.jpg'}")
t.sleep(10)
