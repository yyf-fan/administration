class Goods:
    def __init__(self, b, m):
        self.buy_goods, self.money = b, m

    def get_goods(self):
        """此方法为调用者提供货物和金额组成的的元组"""
        return self.buy_goods, self.money

    def get_money(self):
        return self.money

    def get_buy_goods(self):
        return self.buy_goods

    def write_to(self, f):
        f.write(str(self.buy_goods))
        f.write(',')
        f.write(self.money)
        f.write('\n')
