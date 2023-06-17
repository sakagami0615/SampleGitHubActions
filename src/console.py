
def cursor_hyde():
    print('\033[?25l', end='')

def cursor_show():
    print('\033[?25h', end='')

def cursor_up(n):
    print(f'\033[{n}A', end='')
