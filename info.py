class Currency:
    """
    Klasa Waluta
    """
    def __init__(self, code, name, flag):
        self.code = code
        self.name = name
        self.flag = flag

    def __repr__(self):
        return f'<Currency {self.code}>'


ob = Currency('USD', 'Dollar', 'usd.png')
print(ob)  # <__main__.Currency object at 0x0000029BFB5FD400>
# po dodaniu metody __repr__
# <Currency USD>
print(Currency.__doc__)