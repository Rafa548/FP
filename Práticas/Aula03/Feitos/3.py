def bodyMassIndex(height, weight):
    bmi = weight/height**2
    return bmi

def bmiCategory(bmi):
    assert bmi>0
    
    if bmi<18.5:
        return("underweight")
    elif 18.5<bmi<25:
        return("Normal weight")
    elif 25<bmi<30:
        return("overweight")
    else:
        return("Obesity")

def main():
    print("Índice de Massa Corporal")
    
    altura = float(input("Altura (m)? "))
    if altura < 0:
        print("ERRO: altura inválida!")
        exit(1)

    peso = float(input("Peso (kg)? "))
    if peso < 0:
        print("ERRO: peso inválido!")
        exit(1)

    imc = bodyMassIndex(peso,altura)
    cat = bmiCategory(imc)

    print("BMI:", imc, "kg/m2")
    print("BMI category:", cat)

main()