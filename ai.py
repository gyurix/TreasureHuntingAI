from random import randint, random

from sortedcontainers import SortedList

from data import Program


def to_bin(num):
    return bin(num)[2:].zfill(8)


def mutation_invert_20_random_bits(pr, debug=False):
    for i in range(20):
        byte_id = randint(0, 63)
        mask = 2 ** randint(0, 7)
        if debug:
            print('mutation invert 20 random bits - #', i + 1, ': apply XOR mask ', to_bin(mask), ' to ', byte_id,
                  '. byte of the program: ', to_bin(pr.pr[byte_id]), ' => ', to_bin(pr.pr[byte_id] ^ mask), sep='')
        pr.pr[byte_id] ^= mask
    return pr


def mutation_change_5_random_bytes(pr, debug=False):
    for i in range(5):
        byte_id = randint(0, 63)
        rand_num = randint(0, 255)
        if debug:
            print('mutation change 5 random bytes - #', i + 1, ': change ', byte_id, '. byte of the program: ',
                  to_bin(pr.pr[byte_id]), ' => ', to_bin(rand_num), sep='')
        pr.pr[byte_id] = rand_num
    return pr


def mutation_swap_4_random_bytes(pr, debug=False):
    for i in range(4):
        byte_id1 = randint(0, 63)
        byte_id2 = randint(0, 63)
        if debug:
            print('mutation swap 4 random bytes - #', i + 1, ': swap byte #', byte_id1, ' (', to_bin(pr.pr[byte_id1]),
                  ') with #', byte_id2,
                  '(', to_bin(pr.pr[byte_id2]), ') of the program', sep='')
        old = pr.pr[byte_id1]
        pr.pr[byte_id1] = pr.pr[byte_id2]
        pr.pr[byte_id1] = old
    return pr


def mutation_invert_6_random_bytes(pr, debug=False):
    for i in range(6):
        byte_id = randint(0, 63)
        if debug:
            print('mutation invert 6 random bytes - #', i + 1, ': change ', byte_id, '. byte of the program: ',
                  to_bin(pr.pr[byte_id]), ' => ', to_bin(pr.pr[byte_id] ^ 255), sep='')
        pr.pr[byte_id] ^= 255
    return pr


def crossover_xor_10_random_bytes(pr1, pr2, debug=False):
    for i in range(10):
        byte_id = randint(0, 63)
        if debug:
            print('crossover xor 10 random bytes - #', i + 1, ': XOR ', byte_id, '. bytes of the two programs: ',
                  to_bin(pr1.pr[byte_id]), ' XOR ', to_bin(pr2.pr[byte_id]), ' = ',
                  to_bin(pr1.pr[byte_id] ^ pr2.pr[byte_id]), sep='')
        pr1.pr[byte_id] ^= pr2.pr[byte_id]
    return pr1


def crossover_copy_13_random_bytes(pr1, pr2, debug=False):
    for i in range(13):
        byte_id = randint(0, 63)
        if debug:
            print('crossover copy 13 random bytes - #', i + 1, ': Copy ', byte_id,
                  '. byte of the second program to the first one: ',
                  to_bin(pr1.pr[byte_id]), ' => ', to_bin(pr2.pr[byte_id]), sep='')
        pr1.pr[byte_id] = pr2.pr[byte_id]
    return pr1


def crossover_and_8_random_bytes(pr1, pr2, debug=False):
    for i in range(8):
        byte_id = randint(0, 63)
        if debug:
            print('crossover and 8 random bytes - #', i + 1, ': AND ', byte_id, '. bytes of the two programs: ',
                  to_bin(pr1.pr[byte_id]), ' AND ', to_bin(pr2.pr[byte_id]), ' = ',
                  to_bin(pr1.pr[byte_id] & pr2.pr[byte_id]), sep='')
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


def run_ai(map, max_iterations=-1, instances=25, keep=1,
           cross_chance=0.2, mutations=ALL_MUTATION, crossovers=ALL_CROSSOVER,
           debug_generations=False, debug_operations=False, debug_from_to=False, debug_exact_steps=False):
    if map is None:
        print('Map is not set.')
        return
    last_score = -1
    generations = [Program() for pr in range(instances)]
    iterations = 0
    while 1:
        if debug_generations:
            print('Generation #' + str(iterations + 1) + ':', generations)
        executed = [pr.clone() for pr in generations]
        for pr in executed:
            pr.execute()
        score = SortedList(key=lambda pr: pr.score)
        for pr in executed:
            pr.score = map.collect(pr.result)
            score.add(pr)

        iterations += 1
        if score[-1].score == len(map.rewards):
            if max_iterations == -1:
                print('This is the  ', iterations, '. generation.\nSuccesfully collected all the ', score[-1].score,
                      ' points. \nIt is reached by program ', score[-1].original, '.', sep='')
            return score[-1]
        if max_iterations == -1 and score[-1].score > last_score:
            last_score = score[-1].score
            print('This is the ', iterations, '. generation.\nThe best score is ', score[-1].score,
                  '.\nIt is reached by program ', score[-1].original, '.', sep='')
            cont = input('Should we try to find a better one? (y = yes): ')
            print('')
            if cont.lower() != 'y':
                return score[-1]
        elif iterations == max_iterations:
            # print('Reached iteration limit.')
            return score[-1]

        for i in range(instances - keep):
            if random() <= cross_chance:
                cid = randint(0, len(crossovers) - 1)
                target = randint(0, instances - 1)
                if debug_operations:
                    print('Instance #', i, ' = ' + crossovers[cid].__name__.replace('_', ' ') + '(#', i, ', #', target,
                          ')', sep='')
                generations[i] = crossovers[cid](score[i].original.clone(), score[target], debug_exact_steps)
                if debug_from_to:
                    print('FROM: ', score[i].original)
                    print('TO: ', generations[i])
            else:
                mid = randint(0, len(mutations) - 1)
                if debug_operations:
                    print('Instance #', i, ' = ' + mutations[mid].__name__.replace('_', ' ') + '(#', i, ')', sep='')
                generations[i] = mutations[mid](score[i].original.clone(), debug_exact_steps)
                if debug_from_to:
                    print('FROM: ', score[i].original)
                    print('TO: ', generations[i])
        for i in range(instances - keep, instances):
            generations[i] = score[i].original.clone()
