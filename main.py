main_menu = [
]

math = [
    ["Factorial", "math/classfactorial.py"],
    ["Factors", "math/factors.py"],
    ["Fibonacci OOP", "math/classfibonacci.py"],
    ["Swap", "math/numswap.py"],
    ["Fibonacci Imperative", "Week 1/fibonacci.py"],
]

print = [

]

search = [
    ["InfoDb", "search/listloop.py"],
]

border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"

def menu():
  print()
  title = "Function Menu" + banner
  menu_list = main_menu.copy()
  menu_list.append(["Math", math])
  menu_list.append(["Print", print])
  menu_list.append(["Search", search])
  buildMenu(title, menu_list)

def math():
  title = "Math" + banner
  buildMenu(title, math)
  
def print():
  title = "Print" + banner
  buildMenu(title, print)

def search():
  title = "Search" + banner
  buildMenu(title, search)


def buildMenu(banner, options):
    print(banner)
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    for key, value in prompts.items():
        print(key, '->', value[0])

    choice = input("Type your choice> ")

    try:
        choice = int(choice)
        if choice == 0:
            return
        try:
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
          
    except ValueError:
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        print(f"Invalid choice: {choice}")
    except TypeError:
        print(f"Not callable {action}")

    buildMenu(banner, options)  


if __name__ == "__main__":
    menu()