import sys
from wc.word_counter import wc


def run():
    file_name: str = sys.argv[1]
    c_option: bool = False
    l_option: bool = False
    w_option: bool = False

    if "-c" in sys.argv:
        c_option = True
    if "-l" in sys.argv:
        l_option = True
    if "-w" in sys.argv:
        w_option = True

    wc(file_name, l_option, w_option, c_option)


if __name__ == '__main__':
    run()