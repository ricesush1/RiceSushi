"""
menuy.py - function style menu
"""


# Main menu example
def menu(banner, options):
    # header for menu
    print()
    print(banner)

    # build a dictionary from options
    prompts = {0: ["\u001b[31mExit\u001b[0m", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # execute selection
    try:  # try converting to integer
        # convert to number
        choice = int(choice)
        if choice == 0:  # exit choice, stop loop
            return  # return means leave function
        try:  # try to run as playground function
            action = prompts.get(choice)[1]
            exec(open(action).read())
        except:
            try:  # try to run as function
                action()
            except:
                print(f"Bad action: {action}")
            # end function try
        # end playground try
    except ValueError:  # not a number error
        print(f"Not a number: {choice}")
    except:  # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    menu(banner, options)  # recursion, start menu over again
