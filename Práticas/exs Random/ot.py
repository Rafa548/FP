comboio_1 = {'primeira-classe': (5, [(12345, 'Anabela', 70), (9999, 'Luís', 70)]),
 'segunda-classe': (8, [(52346, 'Rita', 18)]),
 'terceira-classe': (10,[(324524534, 'Luís Santos', 70),
   (24456356, 'Luís Bastos', 70),
   (2224524, 'Luís Rodrigues', 70),
   (3256456, 'inês', 20),
   (996775645, 'andré', 22)])}

def ordenar(comboio):
    for passageiros in comboio.values():
        idade = passageiros[2]
        return idade
a = sorted(comboio_1, key = lambda x: (lista[2](x),lista[1](x)))
print(a)