hora_de_inicio = int(input("A que horas saiu de casa?"))
min_de_inicio = int(input("A que minutos saiu de casa?"))
kilometros_feitos = float(input("Quantos kilometros foram feitos?"))
kilometros_feitos_2 = float(input("Quantos kilometros foram feitos?"))

temp_1 = kilometros_feitos * 10
temp_2 = kilometros_feitos_2 * 6
temp_3 = (kilometros_feitos + kilometros_feitos_2) * 10

temp = temp_1 + temp_2 + temp_3
h = temp//60
min = temp%60
z = 60

hora_final = hora_de_inicio + h
min_final = min_de_inicio + min

if min_final > 59:
    hora_final = hora_final + min_final//60
    min_final = min_final%60

message = """
        Chegou ás {} horas e aos {} mins
"""

print(message.format(hora_final,min_final))
