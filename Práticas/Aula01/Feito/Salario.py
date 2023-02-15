import math

nome = input("Qual é o teu nome?")
apelido = input("Qual é o teu apelido?")
salário = float(input("Quanto recebes de salário?"))
subsidio = float(input("Quanto recebes de subsidio?"))

salariototal = 12*salário
subsidiototal = 12*subsidio
total = salariototal + subsidiototal

message = """

A/O {} {} recebe:
	{} euros de salário ao fim de 1 ano
	{} euros de subsidio de alimentaçao ao fim de 1 ano
	{} no total ao fim de 1 ano

"""

print(message.format(nome,apelido,math.ceil(salariototal *100)/100,100* math.ceil(subsidiototal *100)/100,math.ceil(total *100)/100))


