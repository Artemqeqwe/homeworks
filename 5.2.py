while True:
    numb1 = int(input("Введите первое число:"))
    sign = input("Введите операцию")
    numb2 = int(input("Введите второе число"))
    if sign == "+":
        print(numb1 + numb2)
    elif sign == "-":
        print(numb1 - numb2)
    elif sign == "*":
        print(numb1 * numb2)
    elif sign == "/":
        if numb2 == 0:
            print("Деление на 0 невозможно")
        else:
            print(numb1 / numb2)
    question = input("Continue:")
    if question == 'y':
        question == True
    elif question == 'yes':
        question == True
    else:
        break
