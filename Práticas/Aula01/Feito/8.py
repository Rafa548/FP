n = int(input("Quantos livros?"))
PF = float(20)
PC = float(24.95)
IMP = float((PC*23)/100)
SPA = float(0.20)
Lucro = float(4.95)

Lucrototal = Lucro * n
Taxatotal = SPA * n
ImpostoTotal = IMP * n

message = """
        A livraria recebe {} de lucro
                    é recebido {} em impostos
                    é recebido {} em taxas
"""

print(message.format(Lucrototal,ImpostoTotal,Taxatotal))