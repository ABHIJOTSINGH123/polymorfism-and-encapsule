class computer:
    def __init__(self):
        self.maxprice=900
    def sell(self):
        print("Selling price:{0}".format(self.maxprice))
    def setMaxprice(self,price):
        self.maxprice=price
c=computer()
c.sell()

c.Maxprice=1000

c.sell()


c.setMaxprice(1000)

c.sell()
