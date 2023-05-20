
import random

def main():
    secret = random.randrange(1, 101)
    n = int(input("Can you guess my secret?"))  
    while n != secret:
        if n > secret:
            print("Too High")
            n = int(input("Can you guess my secret?")) 
        else:
            print("Too Low")
            n = int(input("Can you guess my secret?")) 
    if n == secret:
        print("U Won")    

main()
