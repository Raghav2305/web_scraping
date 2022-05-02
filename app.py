import os
from certifi import contents
from flask import Flask, render_template, request, json, jsonify
import general_scraping as gs
from download_pdf import download_pdfs
# from general_scraping import contents

app = Flask(__name__)

path_for_images = "C:/Users/ASUS/Desktop/Cloudstrats/Web Scraping/web_scraping/static/images"

def remove(path):
    loc=os.listdir(path)
    # print(loc)
    if loc != []:
        for p in loc:
            os.remove(path + "/" + p)




with open('content.json', 'r') as myfile:
    data = myfile.read()

@app.route('/',methods=['GET', 'POST'])
def main():
    return render_template("index.html")

@app.route('/render', methods=['GET','POST'])
def render():
    data = {
        'images': ""
    }

    

    if request.method == "POST": 
        url=request.form['user_url']
        print(url)
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
            # return render_template("render.html", url=url)
        else:
            print("NO tables")
        if request.form.get("images"):

            remove(path_for_images)
            gs.download_images(url)
            my_contents = gs.contents
            img_list = os.listdir("static/images")

            print(f"\n-------------------->\nimages : {img_list}\n")
            # data.clear()
            data['images'] = img_list
            # return render_template("render.html", url=url)
        else:
            print("NO images")
        if request.form.get("PDF's"):
            download_pdfs(url)
            my_contents = gs.contents

            print(my_contents)
            # return render_template("render.html", url=url)
        else:
            print("NO pdfs")
    else:
        print("not found")
    
    return render_template("render.html", data = data, contents = my_contents)

if __name__=="__main__":
    app.run(port=5000, debug=True)



