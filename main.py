""" menu.py has been using abstraction.
One of the key skills of programming is data and logic abstraction.  Object-Oriented-Programming (OOP) is a standard technique used to abstract both data and logic.

Comments will focus on abstraction.
"""
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders
import menuy  # abstracted files in local directory
from mody import advy  # abstracted files in a folder (aka module)
from mody import questy
from wipy import termy
from wipy import biny
from wipy import funcy

# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function refereces will be executed directly file.function()

main_menu = [

]

math_practice = [

    ["Factorial", "math/classfactorial.py"],
    ["Fibonacci p.1", "math/classfibonacci.py"],
    ["Factors", "math/factors.py"],
    ["Fibonacci p.2", "math/math/fibonacci.py"],
    ["Number Swap", "math/numswap.py"],
]

printing_practice = [
]

search_practice = [
    ["List and Loop", "math/listloop.py"],
]



# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def menu():
    title = "\u001b[31mFunction Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["\u001b[33mMath", math])
    menu_list.append(["\u001b[35mPrint", print])
    menu_list.append(["\u001b[36mSearch", search])
    menuy.menu(title, menu_list)


# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()

def math():
    title = "Math" + banner
    menuy.menu(title, math_practice)

def print():
    title = "Print" + banner
    menuy.menu(title, printing_practice)

def search():
    title = "Search" + banner
    menuy.menu(title, search_practice)

# def menuc
# using main_menu list:
# 1. custom title is created for menu
# 2  main menu and submenu references are created [Prompts, Actions]
# 3. menu_list is sent as parameter to questy.Menus class that creates an object that will be used to support menu control
# 4  object (m.) has method (menu()) that support menu control
def menuc():
    title = "Class Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Submenu", submenuc])
    m = questy.Menu(title, menu_list)
    m.menu()  # method and data reside in object


# def submenuc
# using main_menu list:
# submenuc works similarly to menuc
def submenuc():
    title = "Class Submenu" + banner
    m = questy.Menu(title, sub_menu)
    m.menu()


# def shell
# using main_menu list and sub_menu list
# using class questy.Prompts, a parent to questy.Menus creates an object that will be used to support shell style Prompts
# object (p.) illustrates usage of setter, shell, and getter methods
def shell():
    menu_list = main_menu + sub_menu
    p = questy.Prompts(menu_list)
    p.set_recurse(True)  # change data after object is created
    p.shell()
    print("Last Choice: ", p.get_choice())  # obtaining data after shell has exited


# this code is activated when file is executed directly
if __name__ == "__main__":
    menu()
    # menuc()
    # shell()
