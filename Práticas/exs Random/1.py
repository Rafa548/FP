def main():
    s= input("")
    n= int(input(""))
    lalal(s, n)

def lalal(s, n):
    s2 = ""
    for x in s:
        x *= n
        s2 += x
        
    print (s2)

        
main()
