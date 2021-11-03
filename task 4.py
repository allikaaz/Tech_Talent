Mtr_bike = 2000
print("The original cost of the motor bike is: "+ str( Mtr_bike ) + "")
perc_lst = Mtr_bike * 10/100
Mtr_bike-= perc_lst
while Mtr_bike >= 1000:
    print("The new price of the motor bike is: "+ str(int(Mtr_bike)) +"")
    Mtr_bike-= perc_lst
