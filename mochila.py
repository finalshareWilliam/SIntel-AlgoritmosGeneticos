from random import randint, random
from operator import add
from functools import reduce

def individual(tam, min, max): #faz o random entre minimo e maximo;

    return [randint(min, max) for x in range(tam)]


def population(count, tam, min, max): #array de indivíduos (possíveis soluções) para o range do tamanho da população;

    return [individual(tam, min, max) for x in range(count)]


def fitness(individual, peso_mochila, itens): #aptidão da mochila. Recebe individuo(array tamanho 10), recebe o tamanho, e recebe os itens;

    soma_valor = 0
    soma_peso = 0

    for i in range(len(itens)): #percorre todos os itens e verifica se tem o item;
        if individual[i] == 1:
            soma_valor += itens[i]["valor"]  #soma o valor;
            soma_peso += itens[i]["peso"] #soma o peso;

    if soma_peso <= peso_mochila:
        return soma_valor
    else:
        return 0



def media_fitness(pop, peso_mochila, itens): #média fitness de todos os indivíduos da população;
    somatorio = reduce(add, (fitness(x, peso_mochila, itens) for x in pop))
    return somatorio / (len(pop) * 1.0)


def evolve(pop, peso_mochila, itens, mutate=0.01):
    avalia_fitness = [(fitness(x, peso_mochila, itens), x) for x in pop] #avalia fitness é lista de tuplas, que é atrelado ao fitness do indivíduo e o valor do indivíduo;
    all_fitness = []  #array para receber a aptidão relativa do indivíduo;
    for individual in avalia_fitness:  #no array, estão todas as aptidões relativas, que é o fitness;
        if individual[0] not in all_fitness:
            all_fitness.append(individual[0])

    soma_total_fitness = 0.0
    soma_total_fitness += sum(all_fitness)  #soma de todas as fitness no array;
    pais = []

    'utiliza a roleta para selecionar os pais'
    while len(pais) < 2:  #estabelece pai e mãe;
        for individual in avalia_fitness:  #passa por todos indivíduos;

            if (individual[0]/soma_total_fitness) > random(): #verifica se o fitness do primeiro indivíduo dividido pela fitness total;
                pais.append(individual[1])
    for individual in pais:  #mutacao soma individual;
        if mutate > random():
            pos_to_mutate = randint(0, len(individual)-1)

            if individual[pos_to_mutate] == 0:
                individual[pos_to_mutate] = 1
            else:
                individual[pos_to_mutate] = 0

    parents_length = len(pais) #crossover para criar filhos;

    desired_length = len(pop) - parents_length #tamanho deseja da população de filhos;
    filho = []

    while len(filho) < desired_length:

        male = randint(0, parents_length-1)
        female = randint(0, parents_length-1)
        if male != female:
            male = pais[male]
            female = pais[female]
            half = len(male) // 2

            child = male[:half] + female[half:]
  
            filho.append(child)

    pais.extend(filho)
    return pais