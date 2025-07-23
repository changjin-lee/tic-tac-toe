from PIL import Image

def make_icon():
    # Open an image.
    image = Image.open("ttt-icon.png")

    # Distplay the image.
    # image.show()

    # Resize the image (ex.: 64x64).
    resized_image = image.resize((64, 64))

    # Save it as an icon file (ex.: ico file).
    resized_image.save("ttt-icon.ico", format="ICO")