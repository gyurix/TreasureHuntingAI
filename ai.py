from random import randint, random

from sortedcontainers import SortedList

from data import Program


def mutation_invert_20_random_bits(pr):
    for i in range(20):
        byte_id = randint(0, 63)
        mask = 2 ** randint(0, 7)
        pr.pr[byte_id] ^= mask
    return pr


def mutation_change_5_random_bytes(pr):
    for i in range(5):
        byte_id = randint(0, 63)
        pr.pr[byte_id] = randint(0, 255)
    return pr


def mutation_swap_4_random_bytes(pr):
    for i in range(4):
        byte_id1 = randint(0, 63)
        byte_id2 = randint(0, 63)
        old = pr.pr[byte_id1]
        pr.pr[byte_id1] = pr.pr[byte_id2]
        pr.pr[byte_id1] = old
    return pr


def mutation_invert_6_random_bytes(pr):
    for i in range(6):
        byte_id = randint(0, 63)
        pr.pr[byte_id] ^= 255
    return pr


def crossover_xor_10_random_bytes(pr1, pr2):
    for i in range(10):
        byte_id = randint(0, 63)
        pr1.pr[byte_id] ^= pr2.pr[byte_id]
    return pr1


def crossover_copy_13_random_bytes(pr1, pr2):
    for i in range(13):
        byte_id = randint(0, 63)
        pr1.pr[byte_id] = pr2.pr[byte_id]
    return pr1


def crossover_and_8_random_bytes(pr1, pr2):
    for i in range(8):
        byte_id = randint(0, 63)
        pr1.pr[byte_id] &= pr2.pr[byte_id]
    return pr1


ALL_MUTATION = (mutation_invert_20_random_bits,
                mutation_change_5_random_bytes,
                mutation_swap_4_random_bytes,
                mutation_invert_6_random_bytes)

ALL_CROSSOVER = (crossover_xor_10_random_bytes,
                 crossover_copy_13_random_bytes,
                 crossover_and_8_random_bytes)


def format_crossovers(cs, with_ids=True):
    return str([((str(c + 1) + '. ') if with_ids else '') + cs[c].__name__ for c in range(len(cs))]).replace(
        "'", "").replace('crossover_', '').replace('_', ' ')[1:-1]


def format_mutations(ms, with_ids=True):
    return str([((str(c + 1) + '. ') if with_ids else '') + ms[c].__name__ for c in range(len(ms))]).replace(
        "'", "").replace('mutation_', '').replace('_', ' ')[1:-1]


def run_ai(map, max_iterations=-1, instances=50, keep=5,
           cross_chance=0.2, mutations=ALL_MUTATION, crossovers=ALL_CROSSOVER):
    if map is None:
        print('Map is not set.')
        return
    last_score = -1
    generations = [Program() for pr in range(instances)]
    iterations = 1
    while 1:
        executed = [pr.clone() for pr in generations]
        for pr in executed:
            pr.execute()
        score = SortedList(key=lambda pr: pr.score)
        for pr in executed:
            pr.score = map.collect(pr.result)
            score.add(pr)

        iterations += 1
        if (score[-1].score == len(map.rewards)):
            print('This is the ', iterations, '. generation.\nSuccesfully collected all the ', score[-1].score,
                  ' points.'
                  '.\nIt is reached by program ', score[-1].original, '.',
                  sep='')
            return score[-1].original
        if max_iterations == -1 and score[-1].score > last_score:
            last_score = score[-1].score
            print('This is the ', iterations, '. generation.\nThe best score is ', score[-1].score,
                  '.\nIt is reached by program ', score[-1].original, '.',
                  sep='')
            cont = input('Should we try to find a better one? (y = yes)')
            if cont.lower() != 'y':
                return score[-1].original
        elif iterations == max_iterations:
            print('Reached iteration limit.')
            return score[-1].original

        for i in range(instances - keep):
            if random() <= cross_chance:
                generations[i] = crossovers[randint(0, len(crossovers) - 1)](score[i].original.clone(),
                                                                             score[randint(0, instances - 1)])
            else:
                generations[i] = mutations[randint(0, len(mutations) - 1)](score[i].original.clone())
        for i in range(instances - keep, instances):
            generations[i] = score[i].original.clone()
