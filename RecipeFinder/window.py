import tkinter as tk
from tkinter import ttk
from db_functions import connect, disconnect, test_connect, get_connection
import re

parsed_words = []
matched_recipes = []

def submit(): #parsing given sentence
    print("Recieved: ", input.get())
    input_text = input.get()

    print("parsing...")

    singular_words = parse(input_text)
    compare_keywords(singular_words)

def parse(input_text): #parses text
    global parsed_words
    parsed_words = input_text.split()
    print (parsed_words)

    singular_words = [plural_to_singular_func(word) for word in parsed_words]
    print("Singular words:", singular_words)

    return singular_words

def compare_keywords(singular_words):
    connect()
    connection = get_connection()
    if connection is None:
            print("No active database connection. Attempting to connect...")
            connect()
            if connection is None:
                print("Failed to establish connection to database")
                return
            
    crsr = connection.cursor()

    for word in singular_words:
        crsr.execute("SELECT name FROM recipe_data WHERE ingredients LIKE %s", ('%' + word + '%',))
        results = crsr.fetchall()

        for result in results:
            recipe_name = result[0]
            if recipe_name not in matched_recipes:
                matched_recipes.append(recipe_name)
                print(f"Matched recipe: {recipe_name} with ingredient: {word}")
    if matched_recipes:
        print("Recipes found:", matched_recipes)
    else:
        print("No matching recipes found.")

    crsr.close()
    disconnect()
    window.quit()

def plural_to_singular_func(word):
    return plural_to_singular.get(word.lower(), word.lower())

plural_to_singular = {
    'eggs': 'egg',
    'beefs': 'beef',
    'onions': 'onion',
    'garlics': 'garlic',  # garlic does not have a plural form
    'tomatoes': 'tomato',
    'ricottas': 'ricotta',
    'mozzarellas': 'mozzarella',
    'basil': 'basil',  # basil does not have a plural form
    'milks': 'milk',
    'butters': 'butter',
    'sugars': 'sugar',  # sugar does not have a plural form
    'baking powders': 'baking powder',
    'vanillas': 'vanilla',
    'ladyfingers': 'ladyfinger',
    'espressos': 'espresso',
    'cocoas': 'cocoa',  # cocoa does not have a plural form
    'rums': 'rum',
    'chickens': 'chicken',
    'shrimp': 'shrimp',  # shrimp does not have a plural form
    'bell peppers': 'bell pepper',
    'tofus': 'tofu',  # tofu does not have a plural form
    'peanuts': 'peanut',
    'limes': 'lime',
    'fishes': 'fish',  # fish does not have a plural form
    'seas': 'sea',
    'wasabis': 'wasabi',
    'tortillas': 'tortilla',
    'fries': 'fry',  # fries is a plural form, singular is 'fry'
    'cheese curds': 'cheese curd',
    'pork': 'pork',  # pork does not have a plural form
    'cabbages': 'cabbage',
    'gingers': 'ginger',
    'scallions': 'scallion',
    'sesames': 'sesame',
    'avocados': 'avocado',
    'bacon': 'bacon',  # bacon does not have a plural form
    'blue cheeses': 'blue cheese',
    'raisins': 'raisin',
    'hummuses': 'hummus',
    'falafels': 'falafel',
    'zucchinis': 'zucchini',
    'eggplants': 'eggplant',
    'thyme': 'thyme',  # thyme does not have a plural form
    'corianders': 'coriander',
    'cardamoms': 'cardamom',
    'oregano': 'oregano',  # oregano does not have a plural form
    'cilantros': 'cilantro',
    'chilies': 'chili',
    'galangals': 'galangal',
    'shepherd’s pies': 'shepherd’s pie',
    'walnuts': 'walnut',
    'phyllo doughs': 'phyllo dough',
    'cheeses': 'cheese',
    'spring rolls': 'spring roll',
    'pulled pork': 'pulled pork'  # pulled pork does not have a plural form
}

window = tk.Tk() #creates main window
window.title('Recipe Finder')
window.geometry('300x150')

title_lable = ttk.Label(master = window, text = "What sounds good?", font = "Calibri 24 bold")
title_lable.pack() #packs lable into window

input_frame = ttk.Frame(master = window)#creates input frame
input = tk.StringVar() #where sentence will be stored
entry = ttk.Entry(master = input_frame, textvariable = input) #entry box
button = ttk.Button(master = input_frame, text = 'Submit', command = submit) #button to submit
entry.pack(side = 'left', padx = 10) #packs entry box
button.pack(side = 'left') #packs button
input_frame.pack(pady = 10) #packs input_frame containing entry and button

window.mainloop() #runs window
