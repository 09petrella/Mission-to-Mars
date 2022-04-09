#Use Flask to render a template, redirecting to another URL, and creating a URL
from flask import Flask, render_template, redirect, url_for
#Use PyMongo to interact with Mongo Database
from flask_pymongo import PyMongo
#To use scraping code, we'll convert from Jupyter notebook to Python
import scraping

#Setting up Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"

mongo = PyMongo(app)

#defining route for HTML homepage
@app.route("/")

def index():
    mars = mongo.db.mars.find_one()

    return render_template("index.html", mars=mars)

@app.route("/scrape")

def scrape():

    mars = mongo.db.mars

    mars_data = scraping.scrape_all()

    mars.update_one({}, {"$set":mars_data}, upsert=True)

    return redirect('/', code=302)

if __name__ == "__main__":
    app.run()
