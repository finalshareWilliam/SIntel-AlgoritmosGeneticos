from mochilaAG import *

itens = [{
    "item": "Tablet",
    "peso": 10,
    "valor": 30,
},
    {
    "item": "MacBook",
    "peso": 15,
    "valor": 10,
},
    {
    "item": "Cabo HDMI",
    "peso": 2,
    "valor": 4,
},
    {
    "item": "Estojo",
    "peso": 4,
    "valor": 4,
},
    {
    "item": "Carregador",
    "peso": 3,
    "valor": 3,
},
    {
    "item": "Caderno",
    "peso": 9,
    "valor": 5,
},
    {
    "item": "Pendrive",
    "peso": 1,
    "valor": 10,
}, {
    "item": "Lanche",
    "peso": 5,
    "valor": 50,
}, {
    "item": "Blusa",
    "peso": 1,
    "valor": 40,
}, {
    "item": "Oculos",
    "peso": 50,
    "valor": 30,
}, ]

peso_mochila = 20  #Peso desejado;
tam_itens = len(itens)  #tamanho da lista de itens;
i_min = 0  #pra entrar ou sair  da mochila na função random;
i_max = 1  #aqui etá na lista e entra na mochila pela função random;
tam_pop = 100  #tamanho da população;
epochs = 30  #números Gerações evolutivas;
p = population(tam_pop, tam_itens, i_min, i_max)

fitness_history = [media_fitness(p, peso_mochila, itens) ] #aqui foi adicionado os itens nas funções, pois precisa dos itens;
for i in range(epochs):
    p = evolve(p, peso_mochila, itens)  #itens adicionados aqui;
    fitness_history.append(media_fitness(p, peso_mochila, itens)) #itens adicionados nessa função;

for print_fitness in fitness_history:  #imprime a media dos fitness gerados de cada geração (baseados na população, peso da mochila e itens);
    print(print_fitness)
