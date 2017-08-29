from usda import app
from flask import render_template
from flask import request
from usda import search
import pandas as pd

@app.route('/')
def index():
    usda_list = search.GetNutrienlist("yogurt")
    return render_template("index.html", usda_list=usda_list)

@app.route('/search', methods=['POST', ])
def search_item():
    dbname = request.form.get("content")
    usda_list = search.GetNutrienlist(dbname)
    return render_template("index.html", usda_list=usda_list)

#@app.confirm('/confirm/<string:todo_id>')
#def confirm():
#    pass

