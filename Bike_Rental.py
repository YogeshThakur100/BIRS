class bikeShop:
    def __init__(self,stock):
        self.stock=stock
    def displaybike(self):
        print('Total Bikes',self.stock)
    def rentforbike(self,q):
        
        if q<=0:
            print("Enter the positive value or greater than zero")
        elif q>self.stock:
            print("Enter the value (less then stock)")
        else:
            self.stock=self.stock-q
            print('Total Prices',q*100)
            print("Total Bikes",self.stock)
            
while True:
    obj=bikeShop(100)
    uc=int(input(''' 
    1 Display Stock
    2 Rent a Bike
    3 Exit
    
    '''))
    
    if uc==1:
        obj.displaybike()
    elif uc==2:
        n=int(input("Enter the value"))
        obj.rentforbike(n)
    else:
        break;