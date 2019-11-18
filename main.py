import tkinter
import random

# Change the image when this function is called when the button is pressed
def changeImage():
    # We are grabbing a random imageListArray to the imageSet variable
    imageListArray = ["cat1.png", "spaceGuy.png", "squirrel-coffee.png", "vigo.png"]
    randomNumber = random.randint(0, 3)

    # Get the random number equal to the array here
    imageLabel.config(image=imageListArray[randomNumber])


# Make a new root window here
root = tkinter.Tk()
root.geometry("800x500")
root.columnconfigure(0, minsize=100)
root.columnconfigure(1, minsize=200)


# Make a static label for the images to change here
imageLabel = tkinter.Label(root, text="images", img)
imageLabel.grid(row=10, rowspan=3, column=3)


# Now make a button to change the image
myButton = tkinter.Button(root, command=changeImage, text="Click here to change the image on 'images'")
myButton.grid(row=1, column=0)

# Run on a loop, the program
root.mainloop()
