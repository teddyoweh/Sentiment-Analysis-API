def green_function(color):
    # Execute some code, for example print the color + number "1"
    print(f"{color} 2")
def blue_function(color):
    # Execute some code, for example print the color + number "1"
    print(f"{color} 1")
def red_function(color):
    # Execute some code, for example print the color + number "1"
    print(f"{color} 1")
def pink_function(color):
    # Execute some code, for example print the color + number "1"
    print(f"{color} 1")
user_input = int(input(""))
colors_dict = {
    user_input>=4: green_function,
    "blue": blue_function,
    "red": red_function,
    "pink": pink_function,
}


colors_dict.get(user_input)(user_input)
    