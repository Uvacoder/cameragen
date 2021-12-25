import os
import shutil
from jinja2 import Environment, FileSystemLoader

path = input("Enter your Camera folder (ex. /home/admin/Camera/): ")
articles = os.listdir(path)
photos = []
for article in articles:
    if article.endswith(".jpg") or article.endswith(".png"):
        photos.append(article)
env = Environment(loader = FileSystemLoader("./"))
template = env.get_template("index.html")
index_output = open(path + "index.html", "w")
index_output.write(template.render(photos = photos))
index_output.close()
shutil.copyfile("styles.css", path + "styles.css")
