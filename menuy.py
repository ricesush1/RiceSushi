def menu(banner, options):
    print()
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
            exec(open(action).read())
        except:
            try: 
                action()
            except:
                print(f"Bad action: {action}")
    except ValueError:  
        print(f"Not a number: {choice}")
    except: 
        print(f"Invalid choice: {choice}")
  
    menu(banner, options)  