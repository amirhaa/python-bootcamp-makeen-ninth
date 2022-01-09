import os
from image import Image, Icon

accepted_extensions = ['.jpg', '.jpeg', '.png']

def get_img_name():
    img_name = input("Enter your image name: \n")
    img_ext = None

    for ext in accepted_extensions:
        if os.path.exists(f"{img_name}{ext}"):
            img_ext = ext
            break

    if img_ext:
        print(img_name + img_ext)

    return img_name, img_ext

def start_app():
    img_name, img_ext = None, None

    i = 0
    while not img_ext and i < 3:
        img_name, img_ext = get_img_name()
        if i < 2 and not img_ext:
            print("Invalid image name, please enter correct one")
        i += 1

    if img_ext:
        img_path = f"{img_name}{img_ext}"
        
        image = Image(img_name=img_name, img_ext=img_ext)
        image.resize()

        icon = Icon(img_name=img_name, img_ext=img_ext)
        icon.resize()

if __name__ == "__main__":
    start_app()