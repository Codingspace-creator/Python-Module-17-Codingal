while True:
    try:
        num1, num2 = eval(input("Enter two numbers seperated by comma: "))
        result = num1 / num2
    except ValueError as ex:
        print("Value Error: ", ex)
    except ZeroDivisionError as ex:
        print("Zero Division Error: ", ex)
    except SyntaxError as ex:
        print("Syntax Error: ", ex)
    except Exception as ex :
        print("Unexpected Error:",ex)
else:
    print(f"REsult is :{result}")
break
    finally :
    print("Attempt Completed")