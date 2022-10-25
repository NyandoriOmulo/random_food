
import pandas as pd
import random
df_macro = pd.read_csv("food.csv")
df=df_macro.rename(columns={'Unnamed: 0':'Index'})

df1= df[df['Category']=='Breads, cereals, fastfood,grains']
list1 = []
for x in df1['Food']:
    list1.append(x)
list2 = []
for i in df_macro.Category.unique():
    list2.append(i)
def random_food(categ):
    df1 = df[df['Category']==categ]
    list_of_food= []
    for x in df1['Food']:
        list_of_food.append(x)
    return random.choice(list_of_food)

from tkinter import *

OPTIONS = list2

master = Tk()

master.geometry("700x350")
variable = StringVar(master)
variable.set(list2[0]) # default value

w = OptionMenu(master, variable, *OPTIONS)
w.config(width="250")
w.pack()

def ok():
    newWindow = Toplevel(master)
    
    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")
 
    # sets the geometry of toplevel
    newWindow.geometry("700x350")
 
    # A Label widget to show in toplevel
    Label(newWindow,
          text = "The selected food is "+  random_food(variable.get()).upper(), bg="red" ).pack()
    
   
    
    button = Button(master, text="Back", command=ok)
    

button = Button(master, text="OK", command=ok, bg='#000', fg='#ff0')

button.pack()


mainloop()