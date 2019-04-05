from random import randint, random

from sortedcontainers import SortedList

from data import Program


def mutation_invert_20_random_bits(pr):
    for i in range(20):
        byte_id = randint(0, 63)
        mask = 2 ** randint(0, 7)
        pr.pr[byte_id] ^= mask


def mutation_change_5_random_bytes(pr):
    for i in range(5):
        byte_id = randint(0, 63)
        pr.pr[byte_id] = randint(0, 255)


def mutation_swap_4_random_bytes(pr):
    for i in range(4):
        byte_id1 = randint(0, 63)
        byte_id2 = randint(0, 63)
        old = pr.pr[byte_id1]
        pr.pr[byte_id1] = pr.pr[byte_id2]
        pr.pr[byte_id1] = old


def mutation_invert_6_random_bytes(pr):
    for i in range(6):
        byte_id = randint(0, 63)
        pr.pr[byte_id] ^= 255


def crossover_xor_10_random_bytes(pr1, pr2):
    for i in range(10):
        byte_id = randint(0, 63)
        pr1.pr[byte_id] ^= pr2.pr[byte_id]


def crossover_copy_13_random_bytes(pr1, pr2):
    for i in range(13):
        byte_id = randint(0, 63)
        pr1.pr[byte_id] = pr2.pr[byte_id]


def crossover_and_8_random_bytes(pr1, pr2):
    for i in range(8):
        byte_id = randint(0, 63)
        pr1.pr[byte_id] &= pr2.pr[byte_id]


ALL_MUTATION = (mutation_invert_20_random_bits,
                mutation_change_5_random_bytes,
                mutation_swap_4_random_bytes,
                mutation_invert_6_random_bytes)

ALL_CROSSOVER = (crossover_xor_10_random_bytes,
                 crossover_copy_13_random_bytes,
                 crossover_and_8_random_bytes)


def run_ai(map, max_iterations=-1, gen_count=50, keep_gen=5,
           cross_chance=0.2, mutations=ALL_MUTATION, crossovers=ALL_CROSSOVER):
    generations = [Program() for pr in range(gen_count)]
    iterations = 1
    while 1:
        executed = [pr.clone() for pr in generations]
        for pr in executed:
            pr.execute()
        score = SortedList(lambda pr: -pr.score)
        for pr in executed:
            pr.score = map.collect(pr.result)
            score.add(pr)

        iterations += 1
        if max_iterations == -1:
            print('This is the ', iterations, '. generation.\nThe best score is ', score[-1].score,
                  '.\nIt is reached by program ', score[-1].original, '.',
                  sep='')
            cont = input('Should we try to find a better one? (y = yes)')
            if cont.lower() != 'y':
                return score[-1].original
        elif iterations == max_iterations:
            return score[-1].original

        for i in range(gen_count - keep_gen):
            if random() <= cross_chance:
                generations[i] = crossovers[randint(0, len(crossovers) - 1)](score[i].original.clone(),
                                                                             score[randint(0, gen_count - 1)])
            else:
                generations[i] = mutations[randint(0, len(mutations) - 1)](score[i].original.clone())
        for i in range(gen_count - keep_gen, gen_count):
            generations[i] = score[i].original.clone()
