from sys import argv
from traceback import print_exc

from ui import ui_main, Map, run_ai


def file_mode():
    for arg in argv[1:]:
        print('===== Processing File', arg, '=====')
        # noinspection PyBroadException
        try:
            with open(arg, 'r') as f:
                lines = f.readlines()
                m = Map(lines)
                run_ai(m)

        except:
            print_exc()
    pass


if __name__ == '__main__':
    print('Args:', argv)
    if len(argv) > 1:
        file_mode()
    else:
        ui_main()
