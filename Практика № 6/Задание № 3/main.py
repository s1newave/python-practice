from PIL import Image, ImageDraw, ImageFont

im = Image.open("source_image.jpg")

im = im.rotate(45)

draw = ImageDraw.Draw(im)
font = ImageFont.truetype("arial.ttf", 30)

draw.text(
    im.size + (-30, -30),
    "Лотов Арсений",
    fill = "red",
    font = font,
    anchor = "rb"
)

im.save("result_image.png")

im.close()