from traceback import print_exc

from ai import *
from data import Map


def ui_main():
    cross_chance = 0.2
    cs = ALL_CROSSOVER
    instances = 50
    iterations = -1
    keep = 5
    m = None
    ms = ALL_MUTATION
    while True:
        print('\n\nTreasureHuntingAI - Main Menu')
        print('••► cc <0-1> = Set the chance of using crossing instead of mutation (currently '
              + str(cross_chance) + ')')
        print('••► cs <strategy-ids> = Set crossover strategies (currently ' + format_crossovers(cs, False) + ')')
        print('    ' + format_crossovers(ALL_CROSSOVER))
        print('')
        print('••► g <generations> = Set testing instance count in a generation (currently ' + str(instances) + ')')
        print('••► i <iterations> = Set iteration count (currently ' + str(iterations) + '), -1 = manual mode')
        print('••► k <generations> = Set the amount of best instances to keep (currently ' + str(keep) + ')')
        print('')
        print('••► m = Set map')
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
                pass
            elif cmd == 'cs':
                cs = [ALL_CROSSOVER[int(x) - 1] for x in d[1:]]
                print('Set crossovers to',
                      str([str(c + 1) + '. ' + cs[c].__name__ for c in range(len(cs))])
                      .replace("'", "")[1:-1])
                pass
            elif cmd == 'g':
                instances = max(5, int(d[1]))
                print('Set testing instance count to', instances)
                if keep >= instances:
                    keep = instances / 5
                    print('Set the amount of best instances to keep to', keep)
                pass
            elif cmd == 'i':
                iterations = max(-1, int(d[1]))
                print('Set iteration count to', iterations)
                pass
            elif cmd == 'k':
                keep = max(min(instances - 1, int(d[1])), 1)
                print('Set the amount of best instances to keep to', keep)
                pass
            elif cmd == 'm':
                lines = (input('Enter maxx and maxy separated by space: '),
                         input('Enter starting x and starting y separated by space: '),
                         input('Enter the rewarding point coordinates in a x;y format, separated by space: '))
                m = Map(lines)
            elif cmd == 'ms':
                ms = [ALL_MUTATION[int(x) - 1] for x in d[1:]]
                print('Set mutations to',
                      str([str(m + 1) + '. ' + cs[m].__name__ for m in range(len(ms))])
                      .replace("'", "")[1:-1])
                pass
            elif cmd == 's':
                run_ai(m, iterations, instances, keep, cross_chance, ms, cs)
            elif cmd == 'x':
                break
        except:
            print_exc()
    pass
