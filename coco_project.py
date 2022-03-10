from gettext import install

print('select an operation')
o=int(input('1)image converter\n2)image resizer\n3)exit'))
#body for image conversion
if(o==1):
    print("select image conversion")
    a=int(input("1)png to jpg     2)jpg to png"))
    from PIL import Image
    from tkinter import Tk     # from tkinter import Tk for Python 3.x
    from tkinter.filedialog import askopenfilename

    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    print(filename)

    #image from png to jpg
    if( a==1):   
        img=Image.open(filename)
        rgb=img.convert('RGB')
        rgb.save("converted_png.jpg")
        print("done png>>jpg")

    #image from jpg to png
    elif (a==2):
        im=Image.open(filename)
        im.save("converted_jpg.png")
        print("done jpg>>png")
    else:
        print("invalid input")

#body for image resizer
elif(o==2):
    from PIL import  Image
    from tkinter.filedialog import askopenfilename
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    print(filename)


    image=Image.open(filename)
    width,height=image.size
    print(width,height)

    print("enter new parameters")
    w=int(input("enter width"))
    h=int(input("enter height"))

    resized_img=image.resize((w,h))
    print(resized_img.size)
    resized_img.show()

    resized_img.save('resized_new.jpg')
    print("operation successfull")

else:
    print('operation not found')
    exit()