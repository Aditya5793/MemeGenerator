import random
import os
import requests
from flask import Flask, render_template, abort, request

# @TODO Import your Ingestor and MemeEngine classes
from QuoteEngine import Ingestor
from MemeGenerator import MemeEngine
app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for f in quote_files:
        try:
            quotes.extend(Ingestor.parse(f))
        except ValueError as error:
            print(f"ValueError: {error}")

    images_path = "./_data/photos/dog/"

    imgs = os.listdir(images_path)
    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """
    print("here")
    img = './_data/photos/dog/' + random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    print(path)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """
    img = "./temp_image.jpg"
    image_url = request.form.get("image_url")
    img_data = requests.get(image_url, stream=True).content
    with open(img, "wb") as f:
        f.write(img_data)

    path = meme.make_meme(img, request.form.get("body", ""),
                          request.form.get("author", ""))
    os.remove(img)
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
