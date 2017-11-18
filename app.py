def fizz_buzz(number1, number2):
    for number in range(number1, number2+1):
        FizzBuzzDict = {
            "fizz" : multiple(number, 3),
            "buzz" : multiple(number, 5),
            "boom" : multiple(number, 7),
            "bam" : multiple(number, 12)
        }
        myString = make_string(FizzBuzzDict)
        if(myString != ""):
            print(myString)
        else:
            print(number)

def multiple(number, multiple):
    if(number % multiple == 0):
        return True
    else:
        return False

def make_string(dictionary):
    myString = ""
    for key, value in dictionary.items():
        if(value):
            myString += str(key)
    return myString

fizz_buzz(1,100)