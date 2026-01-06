import pyperclip
import time as t
def copy(prosto):
    try:
        virazhenie = input(f"\n{reg}- your exception:     ")
        okey1 = eval(virazhenie)
        print(f"{reg} - your answer is {okey1}")
        pyperclip.copy(okey1)
    except ValueError as v:
        print(f"\n{reg} - Error(s) is/are: {v}")
    except TypeError as t:
        print(f"\n{reg} - Error(s) is/are: {t}")
    except IndexError as i:
        print(f"\n{reg} - Error(s) is/are: {i}")
    except ZeroDivisionError as z:
        print(f"\n{reg} - Error(s) is/are: {z}")
    except SyntaxError as s:
        print(f"\n{reg} - Error(s) is/are: {s}")
    except NameError as n:
        print(f"\n{reg} - Error(s) is/are: {n}")
    except ImportError as im:
        print(f"\n{reg} - Error(s) is/are: {im}")
reg = input("Your name:     ")
while True:
    print(f"{reg}: type 1 for go it! [0 - guide!]")
    tyoe = input("")
    if tyoe == "1":
        t.sleep(1.333)
        print("\n")
        t.sleep(0.33)
        copy(reg)
    elif tyoe == "0":
        t.sleep(3)
        print(f"\n{reg}, welcome!")
        print("Operators: \nReal life:\n -, +, *, :.\nIn Python:\n -, +, *, /.")
        t.sleep(1)
        print("Calculate numerical expressions using this program, and errors will be detected.\n The answer will be copied to the clipboard.")
        print("\n")
    else:
        print(f"{reg} - I don't understand you!")
