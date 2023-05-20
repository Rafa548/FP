
comboio_1 = {'primeira-classe': (5, [(12345, 'Anabela', 70), (9999, 'Luís', 70)]),
 'segunda-classe': (8, [(52346, 'Rita', 18)]),
 'terceira-classe': (10,
  [(324524534, 'Luís Santos', 70),
   (24456356, 'Luís Bastos', 70),
   (2224524, 'Luís Rodrigues', 70),
   (3256456, 'inês', 20),
   (996775645, 'andré', 22)])}

def sair_do_comboio(comboio, bilhete):
    for carruagem in comboio.values():
        passageiros = carruagem[1]
        for passageiro in passageiros:
            if passageiro[0] == bilhete:
                passageiros.remove(passageiro)

#sair_do_comboio(comboio_1, 12345)
#print(comboio_1)

def procura_passageiro_nome(comboio, nome):
    for carruagem in comboio.values():
        passageiros = carruagem[1]
        for passageiro in passageiros:
            if passageiro[1] == nome:
                print(passageiro)

#só tá a dar 1
#procura_passageiro_nome(comboio_1, "Luís")

def lotação_carruagem(comboio, classe):
    for classee,carruagem in comboio.items():
        if classe == classee:
            lot = carruagem[0]
            n_passageiros = len(carruagem[1])
            lot_c = (n_passageiros*100)/lot
            print(lot_c)

#lotação_carruagem(comboio_1, "primeira-classe")

def lotação_comboio(comboio):
    lot_1 = 0
    n_p = 0
    for carruagem in comboio.values():
        lot = carruagem[0]
        lot_1 += lot
        n_passageiros = len(carruagem[1])
        n_p += n_passageiros
    lot_c = (n_p*100)/lot_1
    print(lot_c)


#lotação_comboio(comboio_1)

def quantidade_seniores(comboio):
    x = 0
    for carruagem in comboio.values():
        passageiros = carruagem[1]
        for passageiro in passageiros:
            if passageiro[2] > 65:
                x += 1
    print(x)

#quantidade_seniores(comboio_1)

h = comboio_1.values()

comboio_1 = sorted(comboio_1, key = lambda x : (h[1[2]]))

def teste(comboio):
  for x  in comboio.values():
      print(x)

#teste(comboio_1)
