import os
import shutil
from flask import Flask, render_template, request, json, jsonify
import general_scraping as gs
from download_pdf import download_pdfs
from keyword_scraping import scrape_keywords
from username_scraping import scrape_username
from zipfile import ZipFile
# from general_scraping import contents

app = Flask(__name__)

path_for_images = r"C:\Users\ASUS\PycharmProjects\Scraping Engine\web_scraping\static\my_images"
dir_name = r"C:\Users\ASUS\PycharmProjects\Scraping Engine\web_scraping\PDFs"
output_filename = "pdf"
img_dir = r"C:\Users\ASUS\PycharmProjects\Scraping Engine\web_scraping\static\my_images"
output_filename_img = 'imgs'
PDF_Folderpath = r"C:\Users\ASUS\PycharmProjects\Scraping Engine\web_scraping\PDFs"


def check_size(path):
    size = 0
    for path, dirs, files in os.walk(path):
        for f in files:
            fp = os.path.join(path, f)
            size += os.path.getsize(fp)
    return size // 1000


gs.contents.clear()


def remove(path):
    loc = os.listdir(path)
    # print(loc)
    if loc != []:
        for p in loc:
            os.remove(path + "/" + p)


def create_zip(dir_name, output_filename):
    shutil.make_archive(output_filename, 'zip', dir_name)


with open('content.json', 'r') as myfile:
    data = myfile.read()


@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template("index.html")


@app.route('/twitter', methods=['GET', 'POST'])
def twitter():
    return render_template("twitter.html")


@app.route('/facebook', methods=['GET', 'POST'])
def facebook():
    return render_template("facebook.html")


@app.route('/instagram', methods=['GET', 'POST'])
def instagram():
    return render_template("instagram.html")


@app.route('/scrape_keyword', methods=['GET', 'POST'])
def scrape_keyword():
    if request.method == 'POST':
        keywords = request.form['my_keywords']
        print(keywords)
        scrape_keywords(keywords)
        return render_template("twitter.html")


@app.route('/my_usernames', methods=['GET', 'POST'])
def my_usernames():
    if request.method == 'POST':
        username = request.form['my_username']
        print(username)
        scrape_username(username)
        return render_template("twitter.html")


@app.route('/all_twitter', methods=['GET', 'POST'])
def all_twitter():
    if request.method == 'POST':
        keywords = request.form['query']
        username = request.form['query']
        scrape_keywords(keywords)
        scrape_username(username)
        return render_template("twitter.html")


@app.route('/render', methods=['GET', 'POST'])
def render():
    data = {
        'images': ""
    }

    if request.method == "POST":
        url = request.form['user_url']
        print(url)
        gs.contents.clear()
        if request.form.get("contents"):
            gs.contents.clear()
            gs.scrape(url)
            my_contents = gs.contents
            # print(my_contents)
            # return render_template("render.html",url=url)
        else:
            print("Noooooo content")
        if request.form.get("tables"):
            gs.scrape_tables(url)
            my_contents = gs.contents
            # return render_template("render.html", url=url)
        else:
            print("NO tables")
        if request.form.get("images"):

            remove(path_for_images)
            gs.download_images(url)
            my_contents = gs.contents
            img_list = os.listdir("static/my_images")

            print(f"\n-------------------->\nimages : {img_list}\n")
            # data.clear()
            data['images'] = img_list
            if check_size(path=path_for_images) > 1:
                create_zip(img_dir, output_filename_img)
            # return render_template("render.html", url=url)
        else:
            print("NO images")
        if request.form.get("PDF's"):
            download_pdfs(url)
            my_contents = gs.contents

            if check_size(path=PDF_Folderpath) > 1:
                create_zip(dir_name, output_filename)
            print(my_contents)
            # return render_template("render.html", url=url)
        else:
            print("NO pdfs")
    else:
        print("not found")

    zip_obj = ZipFile('contents.zip', 'w')
    zip_obj.write('content.json')

    # try:

    # except:
    #     print("No images found")

    # try:

    # except:
    #     print("No pdfs found")

    # return render_template("render.html", data=data, contents=my_contents)
    return render_template("download.html")


if __name__ == "__main__":
    app.run(port=5000, debug=True)
