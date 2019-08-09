from menu import show_menu
from Administration import *


def main():
    lst1 = []  # 用于存放仓库货物的列表
    lst2 = []  # 用于存放门店货物的列表
    while True:
        show_menu()
        s = input('请选择:')
        if s == '1':
            lst1 += buy()
        if s == '2':
            lst1 += transmit()
            lst2 -= transmit()
        if s == '4':
            show_goods(lst1)
        elif s == 'q':
            break


if __name__ == '__main__':
    main()