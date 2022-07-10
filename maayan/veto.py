import urllib.request
import json

def open_url(url):  
    fileobj = urllib.request.urlopen(url)
    fileobj = fileobj.readlines()[0].decode()
    fileobj = json.loads(fileobj)
    return fileobj
cocktails = open_url("https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita")
drinks = cocktails["drinks"]
cocktail = []
ingredients = []
for d in drinks:
    ing = [d["strIngredient1"],d["strIngredient2"],d["strIngredient3"],d["strIngredient4"]]
    cocktail.append([d["strDrink"],d["strInstructions"],ing])
    ingredients.append(ing)
print(cocktail)
flat_ing = [x for xs in ingredients for x in xs]
ingredients_set = set(flat_ing)
print(ingredients_set)

your_ing = ""
list_ing = []
while your_ing != "stop":
    your_ing = input(f"Which of these ingredients do you have? {ingredients_set} ,type stop when finish ")
    if your_ing != "stop":
        list_ing.append(your_ing)
print(list_ing)

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3
your_cocktails = []
for c in cocktail:
    if len(intersection(list_ing,c[2]))>=2:
        your_cocktails.append(c[0])
print(f"You can do the following cocktails based of the ingredients you have: {c[0]}")