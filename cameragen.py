import os
import shutil
from jinja2 import Environment, FileSystemLoader
from PIL import Image
import json

if not os.path.isfile("conf.json"):
    path = input("Enter your Camera folder (ex. /home/admin/Camera/): ")
    address = input("Enter your ip address or domen (ex. http://localhost:3000/): ")
    site_conf = { "path": path, "address": address }
    with open("conf.json", "w") as conf_file:
        json.dump(site_conf, conf_file)
        conf_file.close()
path = 0
address = 0
with open("conf.json", "r") as conf_file:
    site_conf = json.load(conf_file)
    path = site_conf["path"]
    address = site_conf["address"]
    conf_file.close()
articles = os.listdir(path)
photos = []
videos = []
for article in articles:
    if article.endswith(".jpg") or article.endswith(".png"):
        photos.append(article)
for article in articles:
    if article.endswith(".mp4"):
        videos.append(article)
size = 256, 512
if not os.path.isdir(path + "thumbnails"):
    os.mkdir(path + "thumbnails")
for photo in photos:
    with Image.open(path + photo) as img:
        img.thumbnail(size)
        img.save(path + "thumbnails/" + photo + ".thumbnail", "JPEG")
thumbnails = os.listdir(path + "thumbnails")
thumbnails.sort(reverse=True)
videos.sort(reverse=True)
env = Environment(loader = FileSystemLoader("./"))
template = env.get_template("index.html")
index_output = open(path + "index.html", "w")
index_output.write(template.render(address = address, thumbnails = thumbnails, videos = videos))
index_output.close()
shutil.copyfile("styles.css", path + "styles.css")
shutil.copyfile("index.js", path + "index.js")
