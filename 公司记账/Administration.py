#     print(' +----------------------------------------------+')
#     print(' |1)  往仓库进货                                 |')
#     print(' |2)  从仓库向门店发货                            |')
#     print(' |3)  在门店销售货物                             |')
#     print(' |4)  查询门店货物                               |')
#     print(' |4)  查询仓库货物                               |')
#     print(' |q)  退出                                      |')
#     print(' +----------------------------------------------+')

from goods import Goods


# 仓库买入
def buy():
    L = []  # 创建一个空列表准备存放
    while True:
        buy_goods = input('请输入货物:')
        if not buy_goods:  # 如果未输入则直接跳出
            break
        money = int(input('请输入价格:'))
        d = Goods(buy_goods, money)
        L.append(d)
    return L


# 显示仓库存货
def show_goods(lst1):
    global m, b
    print('+----------+----------+')
    print('|buy_goods |   money  |')
    print('+----------+----------+')
    for d in lst1:
        buy_goods, money = d.get_goods()
        b = str(buy_goods).center(10)
        m = str(money).center(10)
        print('|%s|%s|' % (b, m))
    print('+----------+----------+')


# 从仓库向门店发货
def transmit(lst1, lst2):
    while True:
        transport_goods = input('请输入货物名称:')
        if not transport_goods:
            break
        lst1.append(transport_goods)
        lst2.remove(transport_goods)
    return lst1, lst2
