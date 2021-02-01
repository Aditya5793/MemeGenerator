Meme Generator

Overview
A web application and a command line tool that generates random or custom memes by laying quotes and 
authors on existing images. 

Instructions to setup and start running the project

Install all dependencies given in the requirements.txt file using pip:
pip install -r requirements.txt

Download and install the pdftotext command line tool from: https://www.xpdfreader.com/download.html

The application can be started by running the following command:

python meme.py -> will randomly pick one image, quote and author from _data folder and create meme
python meme.py --image_path --QuoteBody --Author  -> will use arguments passed to create a meme
Example : python meme.py --path ./_data/photos/dog/xander_1.jpg --body "He who smelt it..." --author Stinky


A web application build with Flask server framework is also avaiable which can be run like this
1. set FLASK_APP=app.py
2. flask run
3. You can access the application at: http://127.0.0.1:5000/

Server can also be started by running python3 app.py

Modules

MemeGenerator
This module contains logic to accept an image, a quote and an author. It lays the quote
and author on the image using pillow library and returns the new image.

QuoteEngine
This modules contains Ingestors to ingest csv, txt, docx and pdf files with quotes and authors
If a quote is not provided through command line , a random image and quote is selected and 
passed to Memegenerator.

Authors

Aditya Madhusudan Thati - Developer -
Acknowledgments Udacity
