from usda import search
import pandas as pd

usda_list = search.GetNutrienlist("Plain yogurt")
for key,dict_item in usda_list.items():
    for i in dict_item:
        print(i['id'])

