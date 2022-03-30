import menuy


main_menu = [
  ["Swap", "Week 0/numswap.py"],
  ["Factors", "Week 2/factors.py"],
  ["Factorial with classes", "Week 2/classfactorial.py"],
  ["Fibonacci", "Week 1/fibonacci.py"],
  ["Fibonacci with classes", "Week 2/classfibonacci.py"],
  ["Lists & Loops", "Week 1?listloop.py"]
]
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"
def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menuy.menu(title, menu_list)

print(menu)
if __name__ == "__main__":
    menu()