def main():
    s = input("st?->")
    chess(s)

def chess(s):
    x = s[0]
    y = s[1]
    if x.isdigit() < 9 and y.isdigit() < 9:
        print("Error! Only 1 number allowed!")
    elif s.isalpha():
        print("Error! Only 1 letter allowed!")
    else:
        if len(s) > 2:
            print("Error! Only 2 characters allowed!")
        else:
                if x == "a" or x == "h" or y == "a" or y == "h":
                    print("Border")
                elif x == "1" or x == "8" or y=="1" or y == "8":
                    print("Border")
                else:
                    print("Inside")           

            
main()