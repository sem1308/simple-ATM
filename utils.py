# TODO: change code for integrating ATM hardware

def input_by_ui():
    return input()

def error(message):
    print(message)

def is_return_home():
    choice = input('if you want to return home, please enter "y"')
    return choice == "y" or choice == "Y"