import os
import random
from QuoteEngine import Ingestor
from QuoteEngine import QuoteModel
from PIL import Image, ImageFont, ImageDraw


class MemeEngine():

    def __init__(self, output_dir):
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def make_meme(self, img_path, text, author, width=500):
        print('./_data/photos/dog/' + img_path, text, author)
        img = Image.open(img_path)
        outfile = os.path.join(self.output_dir, "temp.jpg")
        real_width, real_height = img.size
        height = int(real_height * width / real_width)

        resized_im = img.resize((width, height))

        font1 = ImageFont.truetype("./_data/fonts/FreeMono.ttf", 22)
        font2 = ImageFont.truetype("./_data/fonts/FreeMono.ttf", 18)
        text_position = random.choice(range(30, height - 50))
        fill = (255, 0, 0)

        # Draw the text on image
        draw = ImageDraw.Draw(resized_im)
        draw.text((50, text_position), text, fill, font1)
        draw.text((70, text_position + 25), f"- {author}", fill, font2)

        resized_im.save(outfile, "JPEG")
        return outfile
