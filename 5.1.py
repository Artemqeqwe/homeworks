import string
import keyword
symbols = string.punctuation
symbols = symbols.replace("_", ' ')
name = input('Enter variable name:')
if len(name)>0:
    if name[0] == '_' and len(name) == 1 or name[0].isalpha() and name[0].islower() and len(name)==1:
        print('True')
    elif name in keyword.kwlist:
        print(False)
    elif name[0].isalpha() and name.islower():
        is_correct = True
        for letter in name:
            if letter in symbols:
                is_correct = False
                break
        if is_correct:
                print(is_correct)
        else:
            print(False)

    else:
        print(False)

else:
    print(False)
