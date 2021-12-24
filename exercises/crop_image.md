We are going to create an application that takes an image name (which is located in the app directory), 
and create two cropped image with two different sizes with following rules:

1. newly created images should be in two different sizes, one with **300x300** as an `icon` and other one with **600x600** size as an `image`
2. you should create two different directory for each type of images, one should be named **icons**, and other one should be named **images**
3. you should create two sub directories based on the year and month and place icons or images in the month directory (see bellow example)
4. you should name the newly created images like this:  `original_image_name + _ + some random characters + _ + 300x300 + .png`
5. you should use one class for icons and one class for images that both of them extends a base image class
6. you should at least wirte your codes in two different modules

for example:

**original:**

`profile.png`

**icon:**

`icons/2021/12/profile_f34gd2_300x300.png`

**image:**

`images/2021/12/profile_f34gd2_600x600.png`

Note: you can use [pillow module](https://pypi.org/project/Pillow/) to process and crop images
