from sys import argv
from traceback import print_exc

from ai import *
from data import Map


def ui_main():
    cross_chance = 0.2
    cs = ALL_CROSSOVER
    instances = 50
    iterations = -1
    debug_generations = True
    debug_operations = False
    debug_from_to = False
    debug_exact_steps = False
    keep = 5
    m = None if len(argv) < 2 else Map(argv[1])
    ms = ALL_MUTATION
    while True:
        print('\n\nTreasureHuntingAI - Main Menu')
        print('••► cc <0-1> = Set the chance of using crossing instead of mutation (currently '
              + str(cross_chance) + ')')
        print('••► cs <strategy-ids> = Set crossover strategies (currently ' + format_crossovers(cs, False) + ')')
        print('    ' + format_crossovers(ALL_CROSSOVER))
        print('')
        print('••► dg = Toggle debugging every generation (currently ' + (
            'enabled' if debug_generations else 'disabled') + ')')
        print('••► do = Toggle debugging every operation applied to instances (currently ' + (
            'enabled' if debug_operations else 'disabled') + ')')
        print('••► doft = Toggle debugging every operations from-to states'
              ' (currently ' + ('enabled' if debug_from_to else 'disabled') + ')')
        print('••► dos = Toggle debugging the exact steps of each operation'
              ' (currently ' + ('enabled' if debug_exact_steps else 'disabled') + ')')
        print('')
        print('••► g <generations> = Set testing instance count in a generation (currently ' + str(instances) + ')')
        print('••► i <iterations> = Set iteration count (currently ' + str(iterations) + '), -1 = manual mode')
        print('••► k <generations> = Set the amount of best instances to keep (currently ' + str(keep) + ')')
        print('')
        print('••► m = Set map')
        print('••► mf <file>= Load map from file')
        print('••► ms <strategy-ids> = Set mutation strategies (currently ' + format_mutations(ms, False) + ')')
        print('    ' + format_mutations(ALL_MUTATION))
        print('')
        print('••► s = Start the AI')
        print('••► x = Exit the program', end='\n\n')
        try:
            d = input('>>> ').split(' ')
            cmd = d[0].lower()
            if cmd == 'cc':
                cross_chance = max(min(1.0, float(d[1])), 0.0)
                print('Set cross chance to', cross_chance)
            elif cmd == 'cs':
                cs = [ALL_CROSSOVER[int(x) - 1] for x in d[1:]]
                print('Set crossovers to',
                      str([str(c + 1) + '. ' + cs[c].__name__ for c in range(len(cs))])
                      .replace("'", "")[1:-1])
            elif cmd == 'dg':
                debug_generations = not debug_generations
                print(('Enabled' if debug_generations else 'Disabled') + ' debugging every generation')
            elif cmd == 'do':
                debug_operations = not debug_operations
                print(('Enabled' if debug_operations else 'Disabled') + ' debugging every operation')
            elif cmd == 'doft':
                debug_from_to = not debug_from_to
                print(('Enabled' if debug_from_to else 'Disabled') + ' debugging every operation from to states')
            elif cmd == 'dos':
                debug_exact_steps = not debug_exact_steps
                print(('Enabled' if debug_exact_steps else 'Disabled') + ' debugging exact steps of each operation')
            elif cmd == 'g':
                instances = max(5, int(d[1]))
                print('Set testing instance count to', instances)
                if keep >= instances:
                    keep = instances / 5
                    print('Set the amount of best instances to keep to', keep)
            elif cmd == 'i':
                iterations = max(-1, int(d[1]))
                print('Set iteration count to', iterations)
            elif cmd == 'k':
                keep = max(min(instances - 1, int(d[1])), 1)
                print('Set the amount of best instances to keep to', keep)
            elif cmd == 'm':
                lines = (input('Enter maxx and maxy separated by space: '),
                         input('Enter starting x and starting y separated by space: '),
                         input('Enter the rewarding point coordinates in a x;y format, separated by space: '))
                m = Map(lines)
                print('Created map.')
            elif cmd == 'mf':
                m = Map(d[1])
                print('Loaded map from file.')
            elif cmd == 'ms':
                ms = [ALL_MUTATION[int(x) - 1] for x in d[1:]]
                print('Set mutations to',
                      str([str(m + 1) + '. ' + cs[m].__name__ for m in range(len(ms))])
                      .replace("'", "")[1:-1])
            elif cmd == 's':
                run_ai(m, iterations, instances, keep, cross_chance, ms, cs,
                       debug_generations, debug_operations, debug_from_to, debug_exact_steps)
            elif cmd == 'x':
                break
        except:
            print_exc()
    pass
