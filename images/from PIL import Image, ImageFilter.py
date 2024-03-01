from PIL import Image

image_path = "images/Neuralnet.gif"
image_file = Image.open(image_path)

image_file.save("image_2Neuralnet.gif", quality=95) 