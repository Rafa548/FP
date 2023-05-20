def intersects(a1, b1, a2, b2):
      assert a1<=b1
      assert a2<=b2
      if (a1>=b2):
          return "False"
      elif (a2>=b1):
          return "False"
      else:
          return "True"

def main():
    a1 = int(input("Valor de a1->"))
    a2 = int(input("Valor de a2->"))
    b1 = int(input("Valor de b1->"))
    b2 = int(input("Valor de b2->"))
    intersects(a1,b1,a2,b2)   

if __name__ == "__main__":
    main()