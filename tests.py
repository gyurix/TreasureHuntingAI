import inspect

from ai import *
from data import Program, Map


def gen_random_map(maxx=5, maxy=5, points=6):
    return Map((str(maxx) + ' ' + str(maxy),
                str(randint(0, maxx - 1)) + ' ' + str(randint(0, maxy - 1)),
                str([str(randint(0, points - 1)) + ';' + str(randint(0, points - 1))
                     for i in range(points)])[1:-1].replace(',', '').replace("'", '')))


maps = [gen_random_map() for m in range(10)]


def test_program_execution():
    pr = Program('00000000 01000001 11000000 11000001 10111111 00000000 00000000 00000000 '
                 '00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 '
                 '00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 '
                 '00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 '
                 ''
                 '00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 '
                 '00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 '
                 '00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 '
                 '00000000 00000000 00000000 00000000 00000000 00000000 00000000 11000000')
    pr.execute()
    assert pr.result == [1, 64, 1]


def test_mutation_crossover_all():
    total = 0
    for m in maps:
        total += run_ai(m, 15).score
    print('\n' + inspect.stack()[0][3], total)


def test_mutation_all():
    total = 0
    for m in maps:
        total += run_ai(m, 15, cross_chance=0).score
    print('\n' + inspect.stack()[0][3], total)


def test_crossover_all():
    total = 0
    for m in maps:
        total += run_ai(m, 15, cross_chance=1).score
    print('\n' + inspect.stack()[0][3], total)


def test_crossover_xor_10_random_bytes():
    total = 0
    for m in maps:
        total += run_ai(m, 15, crossovers=[crossover_xor_10_random_bytes], cross_chance=1).score
    print('\n' + inspect.stack()[0][3], total)


def test_crossover_copy_13_random_bytes():
    total = 0
    for m in maps:
        total += run_ai(m, 15, crossovers=[crossover_copy_13_random_bytes], cross_chance=1).score
    print('\n' + inspect.stack()[0][3], total)


def test_crossover_and_8_random_bytes():
    total = 0
    for m in maps:
        total += run_ai(m, 15, crossovers=[crossover_and_8_random_bytes], cross_chance=1).score
    print('\n' + inspect.stack()[0][3], total)


def test_mutation_invert_20_random_bits():
    total = 0
    for m in maps:
        total += run_ai(m, 15, mutations=[mutation_invert_20_random_bits], cross_chance=0).score
    print('\n' + inspect.stack()[0][3], total)


def test_mutation_change_5_random_bytes():
    total = 0
    for m in maps:
        total += run_ai(m, 15, mutations=[mutation_change_5_random_bytes], cross_chance=0).score
    print('\n' + inspect.stack()[0][3], total)


def test_mutation_swap_4_random_bytes():
    total = 0
    for m in maps:
        total += run_ai(m, 15, mutations=[mutation_swap_4_random_bytes], cross_chance=0).score
    print('\n' + inspect.stack()[0][3], total)


def test_mutation_invert_6_random_bytes():
    total = 0
    for m in maps:
        total += run_ai(m, 15, mutations=[mutation_invert_6_random_bytes], cross_chance=0).score
    print('\n' + inspect.stack()[0][3], total)
