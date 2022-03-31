main_menu = [
]

math = [
    ["Swap", "Week 0/numswap.py"],
]

print = [

  ["InfoDb", "Week 1/listloop.py"],
  ["Fibonacci Imperative", "Week 1/fibonacci.py"]
]

search = [
    ["Factorial", "Week 2/classfactorial.py"],
    ["Factors", "Week 2/factors.py"], 
    ["Fibonacci OOP", "Week 2/classfibonacci.py"],
]

border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"

def menu():
  print()
  title = "Function Menu" + banner
  menu_list = main_menu.copy()
  menu_list.append(["Design", week0_func])
  menu_list.append(["Lists", week1_func])
  menu_list.append(["Math", week2_func])
  buildMenu(title, menu_list)

def week0_func():
  title = "Week 0" + banner
  buildMenu(title, week0_list)
  
def week1_func():
  title = "Week 1" + banner
  buildMenu(title, week1_list)

def week2_func():
  title = "Week 2" + banner
  buildMenu(title, week2_list)


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