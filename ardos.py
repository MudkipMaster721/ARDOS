import random
import time
import math
import getpass
def calculator():
    import math
    print('Welcome to Calculator')
    print('What kind of calculations would you like to do? (enter corresponding number)')
    print('1. Area and Perimeter')
    print('2. Addition and Subtraction')
    print('3. Multiplication and Division')
    print('4. Conversion of Measurements')
    print('5. Pythagoras')
    print('6. Volume and Surface Area')
    mathtype = input('>>> ')
    if mathtype == '1':
        print('Please choose one. (enter the corresponding number)')
        print('1. Area')
        print('2. Perimeter')
        areaperim = input('>>> ')
        if areaperim == '1':
            print('What shape is it? (enter corresponding number)')
            print('1. Square or Rectangle')
            print('2. Triangle')
            print('3. Kite')
            print('4. Trapezium')
            print('5. Parallelogram')
            print('6. Circle')
            shape = input('>>> ')
            if shape == '1':
                print('What is the base of the object?')
                base = int(input('>>> '))
                print('What is the height of the object?')
                height = int(input('>>> '))
                area = base * height
                print(f'{area}')
                calculator()
            elif shape == '2':
                print('What is the base of the object?')
                base = int(input('>>> '))
                print('What is the height of the object?')
                height = int(input('>>> '))
                area = 0.5 * base * height
                print(f'{area}')
                calculator()
            elif shape == '3':
                print('How long is the object from top to bottom?')
                length = int(input('>>> '))
                print('How wide is the object from side to side?')
                width = int(input('>>> '))
                area = length * width / 2
                print(f'{area}')
                calculator()
            elif shape == '4':
                print('How long is the bottom edge?')
                bottomedge = int(input('>>> '))
                print('How long is the top edge?')
                topedge = int(input('>>> '))
                print('How high is the object from top to bottom?')
                height = int(input('>>> '))
                area = ((bottomedge + topedge) / 2 ) * height
                calculator()
            elif shape == '5':
                print('What is the base of the object?')
                base = int(input('>>> '))
                print('What is the height of the object?')
                height = int(input('>>> '))
                area = base * height
                print(f'{area}')
                calculator()
            elif shape == '6':
                print('Do you have the radius or diameter?')
                print('1. Radius')
                print('2. Diameter')
                radordim = input('>>> ')
                if radordim == '1':
                    print('What is the objects radius?')
                    radius = int(input('>>> '))
                    area = (22 / 7) * radius * radius
                    print(f'{radius}')
                elif radordim == '2':
                    print('What is the objects diameter?')
                    diameter = int(input('>>> '))
                    area = (22 / 7) * ((diameter / 2) * (diameter / 2))
            else:
                print('Please enter a valid number')
                calculator()
        if areaperim == '2':
            print('What shape is it? (enter corresponding number)')
            print('1. Square or Rectangle')
            print('2. Triangle')
            print('3. Kite')
            print('4. Trapezium')
            print('5. Parallelogram')
            print('6. Circle')
            print('7. Other')
            shape = input('>>> ')
            if shape == '1':
                print('How long is the first side? ')
                side1 = int(input('>>> '))
                print('How long is the second side? ')
                side2 = int(input('>>> '))
                print('How long is the third side? ')
                side3 = int(input('>>> '))
                print('How long is the fourth side? ')
                side4 = int(input('>>> '))
                perimeter = side1 + side2 + side3 + side4
                print(f'{perimeter}')
                calculator()
            elif shape == '2':
                print('How long is the first side? ')
                side1 = int(input('>>> '))
                print('How long is the second side? ')
                side2 = int(input('>>> '))
                print('How long is the third side? ')
                side3 = int(input('>>> '))
                perimeter = side1 + side2 + side3
                print(f'{perimeter}')
                calculator()
            elif shape == '3':
                print('How long is the first side? ')
                side1 = int(input('>>> '))
                print('How long is the second side? ')
                side2 = int(input('>>> '))
                print('How long is the third side? ')
                side3 = int(input('>>> '))
                print('How long is the fourth side? ')
                side4 = int(input('>>> '))
                perimeter = side1 + side2 + side3 + side4
                print(f'{perimeter}')
                calculator()
            elif shape == '4':
                print('How long is the first side? ')
                side1 = int(input('>>> '))
                print('How long is the second side? ')
                side2 = int(input('>>> '))
                print('How long is the third side? ')
                side3 = int(input('>>> '))
                print('How long is the fourth side? ')
                side4 = int(input('>>> '))
                perimeter = side1 + side2 + side3 + side4
                print(f'{perimeter}')
                calculator()
            elif shape == '5':
                print('How long is the first side? ')
                side1 = int(input('>>> '))
                print('How long is the second side? ')
                side2 = int(input('>>> '))
                print('How long is the third side? ')
                side3 = int(input('>>> '))
                print('How long is the fourth side? ')
                side4 = int(input('>>> '))
                perimeter = side1 + side2 + side3 + side4
                print(f'{perimeter}')
                calculator()
            elif shape == '6':
                print('Do you have the radius or diameter? (enter corresponding number)')
                print('1. Radius')
                print('2. Diameter')
                radordim = input('>>> ')
                if radordim == '1':
                    print('What is the radius?')
                    radius = int(input('>>> '))
                    circumference = 2 * (22 / 7) * radius
                    print(f'{circumference}')
                elif radordim == '2':
                    print('What is the diameter?')
                    diameter = int(input('>>> '))
                    circumference = (22 / 7) * diameter
                    print(f'{circumference}')
                else:
                    print('Please enter a valid number')
                    calculator()
            elif shape == '7':
                print('How many edges does it have? 2, 3, 5, or 6?')
                edges = int(input('>>> '))
                if edges == '2':
                    print('How long is the first edge?')
                    edge1 = int(input('>>> '))
                    print('How long is the second edge?')
                    edge2 = int(input('>>> '))
                    perimeter = edge1 + edge2
                    print(f'{perimeter}')
                    calculator()
                elif edges == '3':
                    print('How long is the first edge?')
                    edge1 = int(input('>>> '))
                    print('How long is the second edge?')
                    edge2 = int(input('>>> '))
                    print('How long is the third edge?')
                    edge3 = int(input('>>> '))
                    perimeter = edge1 + edge2 + edge3
                    print(f'{perimeter}')
                    calculator()
                elif edges == '5':
                    print('How long is the first edge?')
                    edge1 = int(input('>>> '))
                    print('How long is the second edge?')
                    edge2 = int(input('>>> '))
                    print('How long is the third edge?')
                    edge3 = int(input('>>> '))
                    print('How long is the fourth edge?')
                    edge4 = int(input('>>> '))
                    print('How long is the fifth edge?')
                    edge5 = int(input('>>> '))
                    perimeter = edge1 + edge2 + edge3 + edge4 + edge5
                    print(f'{perimeter}')
                    calculator()
                elif edges == '6':
                    print('How long is the first edge?')
                    edge1 = int(input('>>> '))
                    print('How long is the second edge?')
                    edge2 = int(input('>>> '))
                    print('How long is the third edge?')
                    edge3 = int(input('>>> '))
                    print('How long is the fourth edge?')
                    edge4 = int(input('>>> '))
                    print('How long is the fifth edge?')
                    edge5 = int(input('>>> '))
                    print('How long is the sixth edge?')
                    edge6 = int(input('>>> '))
                    perimeter = edge1 + edge2 + edge3 + edge4 + edge5 + edge6
                    print(f'{perimeter}')
                    calculator()
                else:
                    print('Please enter a valid option')
                    calculator()
                calculator()
            calculator
        else:
            print('Please enter a valid option')
            calculator()
    elif mathtype == '2':
        print('Addition or Subtraction? (enter corresponding number)')
        print('1. Addition')
        print('2. Subtraction')
        addsub = input('>>> ')
        if addsub == '1':
            print('How many numbers are you adding? 2, 3, or 4?')
            numnumbers = input('>>> ')
            if numnumbers == '2':
                print('What is the first number? ')
                num1 = int(input('>>> '))
                print('What is the second number?')
                num2 = int(input('>>> '))
                finalnum = num1 + num2
                print(f'{finalnum}')
            elif numnumbers == '3':
                print('What is the first number? ')
                num1 = int(input('>>> '))
                print('What is the second number?')
                num2 = int(input('>>> '))
                print('What is the third number?')
                num3 = int(input('>>> '))
                finalnum = num1 + num2 + num3
                print(f'{finalnum}')
            elif numnumbers == '4':
                print('What is the first number? ')
                num1 = int(input('>>> '))
                print('What is the second number?')
                num2 = int(input('>>> '))
                print('What is the third number?')
                num3 = int(input('>>> '))
                print('What is the fourth number?')
                num4 = int(input('>>> '))
                finalnum = num1 + num2 + num3 + num4
                print(f'{finalnum}')
            else:
                print('Please enter a valid number')
                calculator()
            calculator()
        if addsub == '2':
            print('How many numbers are you subtracting? 2, 3, or 4?')
            numnumbers = input('>>> ')
            if numnumbers == '2':
                print('What is the first number? ')
                num1 = int(input('>>> '))
                print('What is the second number?')
                num2 = int(input('>>> '))
                finalnum = num1 - num2
                print(f'{finalnum}')
            elif numnumbers == '3':
                print('What is the first number? ')
                num1 = int(input('>>> '))
                print('What is the second number?')
                num2 = int(input('>>> '))
                print('What is the third number?')
                num3 = int(input('>>> '))
                finalnum = num1 - num2 - num3
                print(f'{finalnum}')
            elif numnumbers == '4':
                print('What is the first number? ')
                num1 = int(input('>>> '))
                print('What is the second number?')
                num2 = int(input('>>> '))
                print('What is the third number?')
                num3 = int(input('>>> '))
                print('What is the fourth number?')
                num4 = int(input('>>> '))
                finalnum = num1 - num2 - num3 - num4
                print(f'{finalnum}')
            else:
                print('Please enter a valid number')
                calculator()
            calculator()
    elif mathtype == '3':
        print('Multiplication or Division? (enter corresponding number)')
        print('1. Multiplication')
        print('2. Division')
        multdiv = input('>>> ')
        if multdiv == '1':
            print('How many numbers are you Multiplying? 2, 3, or 4?')
            numnumbers = input('>>> ')
            if numnumbers == '2':
                print('What is the first number? ')
                num1 = int(input('>>> '))
                print('What is the second number?')
                num2 = int(input('>>> '))
                finalnum = num1 * num2
                print(f'{finalnum}')
            elif numnumbers == '3':
                print('What is the first number? ')
                num1 = int(input('>>> '))
                print('What is the second number?')
                num2 = int(input('>>> '))
                print('What is the third number?')
                num3 = int(input('>>> '))
                finalnum = num1 * num2 * num3
                print(f'{finalnum}')
            elif numnumbers == '4':
                print('What is the first number? ')
                num1 = int(input('>>> '))
                print('What is the second number?')
                num2 = int(input('>>> '))
                print('What is the third number?')
                num3 = int(input('>>> '))
                print('What is the fourth number?')
                num4 = int(input('>>> '))
                finalnum = num1 * num2 * num3 * num4
                print(f'{finalnum}')
            else:
                print('Please enter a valid number')
                calculator()
            calculator()
        if multdiv == '2':
            print('How many numbers are you dividing? 2, 3, or 4?')
            numnumbers = input('>>> ')
            if numnumbers == '2':
                print('What is the first number? ')
                num1 = int(input('>>> '))
                print('What is the second number?')
                num2 = int(input('>>> '))
                finalnum = num1 / num2
                print(f'{finalnum}')
            elif numnumbers == '3':
                print('What is the first number? ')
                num1 = int(input('>>> '))
                print('What is the second number?')
                num2 = int(input('>>> '))
                print('What is the third number?')
                num3 = int(input('>>> '))
                finalnum = num1 / num2 / num3
                print(f'{finalnum}')
            elif numnumbers == '4':
                print('What is the first number? ')
                num1 = int(input('>>> '))
                print('What is the second number?')
                num2 = int(input('>>> '))
                print('What is the third number?')
                num3 = int(input('>>> '))
                print('What is the fourth number?')
                num4 = int(input('>>> '))
                finalnum = num1 / num2 / num3 / num4
                print(f'{finalnum}')
            else:
                print('Please enter a valid number')
                calculator()
            calculator()
    elif mathtype == '4':
        print('What measurements are you converting from? (enter corresponding number)')
        print('1. Meters')
        print('2. Centimeters')
        print('3. Kilometers')
        print('4. Millimeters')
        print('5. Liters')
        print('6. Milliliters')
        convert1 = input('>>> ')
        if convert1 == '1':
            print('What measurements are you converting to? (enter corresponding number)')
            print('1. Centimeters')
            print('2. Kilometers')
            print('3. Millimeters')
            convert2 = input('>>> ')
            print('How many units are we converting?')
            convertnum = int(input('>>> '))
            if convert2 == '1':
                finalnum = convertnum * 100
                print(f'{finalnum}')
                calculator()
            elif convert2 == '2':
                finalnum = convertnum / 1000
                print(f'{finalnum}')
                calculator()
            elif convert2 == '3':
                finalnum = convertnum * 1000
                print(f'{finalnum}')
                calculator()
            else:
                print('Please enter a valid number')
                calculator()
        elif convert1 == '2':
            print('What measurements are you converting to? (enter corresponding number)')
            print('1. Meters')
            print('2. Kilometers')
            print('3. Millimeters')
            convert2 = input('>>> ')
            print('How many units are we converting?')
            convertnum = int(input('>>> '))
            if convert2 == '1':
                finalnum = convertnum * 100
                print(f'{finalnum}')
                calculator()
            elif convert2 == '2':
                finalnum = convertnum / 100000
                print(f'{finalnum}')
                calculator()
            elif convert2 == '3':
                finalnum = convertnum * 10
                print(f'{finalnum}')
                calculator()
            else:
                print('Please enter a valid number')
                calculator()
        elif convert1 == '3':
            print('What measurements are you converting to? (enter corresponding number)')
            print('1. Meters')
            print('2. Centimeters')
            print('3. Millimeters')
            convert2 = input('>>> ')
            print('How many units are we converting?')
            convertnum = int(input('>>> '))
            if convert2 == '1':
                finalnum = convertnum * 1000
                print(f'{finalnum}')
                calculator()
            elif convert2 == '2':
                finalnum = convertnum * 100000
                print(f'{finalnum}')
                calculator()
            elif convert2 == '3':
                finalnum = convertnum * 1000000
                print(f'{finalnum}')
                calculator()
            else:
                print('Please enter a valid number')
                calculator()
        elif convert1 == '4':
            print('What measurements are you converting to? (enter corresponding number)')
            print('1. Meters')
            print('2. Kilometers')
            print('3. Centimeters')
            convert2 = input('>>> ')
            print('How many units are we converting?')
            convertnum = int(input('>>> '))
            if convert2 == '1':
                finalnum = convertnum / 1000
                print(f'{finalnum}')
                calculator()
            elif convert2 == '2':
                finalnum = convertnum / 1000000
                print(f'{finalnum}')
                calculator()
            elif convert2 == '3':
                finalnum = convertnum / 10
                print(f'{finalnum}')
                calculator()
            else:
                print('Please enter a valid number')
                calculator()
        elif convert1 == '5':
            print('What measurements are you converting to? (enter corresponding number)')
            print('1. Milliliters')
            convert2 = input('>>> ')
            print('How many units are we converting?')
            convertnum = int(input('>>> '))
            if convert2 == '1':
                finalnum = convertnum * 1000
                print(f'{finalnum}')
                calculator()
            else:
                print('Please enter a valid number')
                calculator()
        elif convert1 == '6':
            print('What measurements are you converting to? (enter corresponding number)')
            print('1. Liters')
            convert2 = input('>>> ')
            print('How many units are we converting?')
            convertnum = int(input('>>> '))
            if convert2 == '1':
                finalnum = convertnum / 1000
                print(f'{finalnum}')
                calculator()
            else:
                print('Please enter a valid number')
                calculator()
    elif mathtype == '5':
        print('What is the first side of the triangle?')
        side1 = int(input('>>> '))
        print('What is the second side of the trianlge?')
        side2 = int(input('>>> '))
        side3 = math.sqrt(pow(side1, 2) + pow(side2, 2))
        print(f'{side3}')
        calculator()
    elif mathtype == '6':
        print('Are you calculating volume or surface area?')
        print('1. Volume')
        print('2. Surface Area')
        volsurf = input('>>> ')
        if volsurf == '1':
            print('What is the shape you are calculating?')
            print('1. Cube or Rectangular Prism')
            print('2. Trianglar Prism')
            print('3. Sphere')
            shape = input('>>> ')
            if shape == '1':
                print('What is the objects length?')
                length = int(input('>>> '))
                print('What is the objects width?')
                width = int(input('>>> '))
                print('What is the objects height?')
                height = int(input('>>> '))
                volume = length * width * height
                print(f'{volume}')
                calculator()
            elif shape == '2':
                print('What is the objects first base side?')
                baseside1 = int(input('>>> '))
                print('What is the objects second base side?')
                baseside2 = int(input('>>> '))
                print('What is the objects third base side?')
                baseside3 = int(input('>>> '))
                print('What is the objects height?')
                height = int(input('>>> '))
                volume = 0.25 * height * math.sqrt(- pow(baseside1, 4) + 2 * pow((baseside1 * baseside2), 2) + 2 * pow((baseside1 * baseside3), 2) - pow(baseside2, 4) + 2 * pow((baseside2 * baseside3), 2) - pow(baseside3, 4))
                print(f'{volume}')
                calculator()
            elif shape == '3':
                print('What is the radius?')
                radius = int(input('>>> '))
                volume = (4 / 3) * (22 / 7) * pow(radius, 3)
                print(f'{volume}')
                calculator()
        elif volsurf == '2':
            print('What is the shape you are calculating?')
            print('1. Cube or Rectangular Prism')
            print('2. Trianglar Prism')
            print('3. Sphere')
            shape = input('>>> ')
            if shape == '1':
                print('What is the objects length?')
                length = int(input('>>> '))
                print('What is the objects width?')
                width = int(input('>>> '))
                print('What is the objects height?')
                height = int(input('>>> '))
                surfacearea = 2 * (width * length + height * length + height * width)
                print(f'{surfacearea}')
                calculator()
            if shape == '2':
                print('What is the objects first base side?')
                baseside1 = int(input('>>> '))
                print('What is the objects second base side?')
                baseside2 = int(input('>>> '))
                print('What is the objects third base side?')
                baseside3 = int(input('>>> '))
                print('What is the objects height?')
                height = int(input('>>> '))
                surfacearea = baseside1 * height + baseside2 * height + baseside3 * height + 0.5 * math.sqrt(- pow(baseside1, 4) + 2 * pow((baseside1 * baseside2), 2) + 2 * pow((baseside1 * baseside3), 2) - pow(baseside2, 4) + 2 * pow((baseside2 * baseside3), 2) - pow(baseside3, 4))
                print(f'{surfacearea}')
                calculator()
            if shape == '3':
                print('What is the radius?')
                radius = int(input('>>> '))
                volume = 4 * (22 / 7) * pow(radius, 2)
                print(f'{volume}')
                calculator()
    elif mathtype == 'home':
        start()
    else:
        print('Please enter a valid number?')
        calculator()
def timer():
    print('Welcome to Timer')
    print('How long would you like to set an alarm for? ')
    timerlength = input('>>> ')
    if timerlength == 'home':
        start()
    else:
        time.sleep(timerlength)
        print('Your timer is done')
        timer()
def random():
    import random
    print('Welcome to Random')
    print('Choose two numbers to generate a number between them')
    print('Are you generation a number from zero, or choosing a different number? (Y/N)')
    yesno = input('>>> ')
    if yesno == 'home':
        start()
    elif yesno == 'Y':
        print('What is the highest number to randomize to?')
        rand3 = int(input('>>> '))
        randnum= random.randint(1, rand3)
    elif yesno == 'N':
        print('What is the first number?')
        rand1 = input('>>> ')
        print('What is the second number?')
        rand2 = int(input('>>> '))
        randnum = random.randint(rand1, rand2)
        print(f'Your number is {randnum}')
        input()
        random()
    else:
        print('Please enter a valid option')
        random()
def dice():
    import random
    print('Welcome to Dice')
    print('Choose a dice to roll. (enter the corresponding number)')
    print('1. D4')
    print('2. D6')
    print('3. D8')
    print('4. D10')
    print('5. D12')
    print('6. D20')
    print('7. D100')
    dchoice = input('>>> ')
    if dchoice == '1':
        roll = random.randint(1, 4)
        print(f'{roll}')
        input()
        dice()
    elif dchoice == '2':
        roll = random.randint(1, 6)
        print(f'{roll}')
        input()
        dice()
    elif dchoice == '3':
        roll = random.randint(1, 8)
        print(f'{roll}')
        input()
        dice()
    elif dchoice == '4':
        roll = random.randint(1, 10)
        print(f'{roll}')
        input()
        dice()
    elif dchoice == '5':
        roll = random.randint(1, 12)
        print(f'{roll}')
        input()
        dice()
    elif dchoice == '6':
        roll = random.randint(1, 20)
        print(f'{roll}')
        input()
        dice()
    elif dchoice == '7':
        roll = random.randint(1, 100)
        print(f'{roll}')
        input()
        dice()
    elif dchoice == 'home':
        start()
    else:
        print('Please enter a valid number')
        dice()
def question():
    print('calcdos - formula calculator')
    print('timedos - alarm')
    print('randos - random number picker')
    print('dicedos - dice roller')
    print('help - this menu')
    input()
    start()
def startup():
    print('')
    print('░█████╗░██████╗░██████╗░░█████╗░░██████╗')
    print('██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝')
    print('███████║██████╔╝██║░░██║██║░░██║╚█████╗░')
    print('██╔══██║██╔══██╗██║░░██║██║░░██║░╚═══██╗')
    print('██║░░██║██║░░██║██████╔╝╚█████╔╝██████╔╝')
    print('╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═════╝░')
    print('')
    start()
def start():
    print('Enter commands to open apps. type help for help.')
    action = input('>>> ')
    if action == 'calcdos':
        calculator()
    elif action == 'timedos':
        timer()
    elif action == 'randos':
        random()
    elif action == 'dicedos':
        dice()
    elif action == 'help':
        question()
    else:
        start()
startup()