Mtr_bike = 2000
print("The original cost of the motor bike is: "+ str( Mtr_bike ) + "")
while Mtr_bike >= 1000:
    perc_lst = Mtr_bike * 10/100
    Mtr_bike-= perc_lst
    print("The new price of the motor bike is: "+ str(int(Mtr_bike)) +"")