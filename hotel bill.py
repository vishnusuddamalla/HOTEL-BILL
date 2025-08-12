print("*********Menu**********\n","chicken\n","mutton\n","veg\n")
item=input("enter item name:")
if item=="chicken":
    print("chicken biriyani\n","chicken lolypop\n","chicken tikka\n")
    dish=input("enter item in chicken:")
    if dish=="chicken biriyani":
        bill=220
        tax=2
        gst=1
        total_bill=bill+tax+gst
        print("total bill:",total_bill)
    elif dish=="chicken lolypop":
        bill=280
        tax=3
        gst=2
        total_bill=bill+tax+gst
        print("total bill:",total_bill)
    elif dish=="chicken tikka":
        bill=300
        tax=3
        gst=2
        total_bill=bill+tax+gst
        print("total bill:",total_bill)
elif item=="mutton" :
    print("mutton biriyani\n","mutton kebab\n","mutton nalli gosh\n")  
    dish=input("enter the dish :")
    if dish=="mutton biriyani":
        bill=350
        tax=2
        gst=4
        total_bill=bill+tax+gst
        print("total bill:",total_bill)
    elif dish=="mutton kebab":
        bill=300
        tax=2
        gst=4
        total_bill=bill+tax+gst
        print("total bill:",total_bill)
    elif dish=="mutton nalli gosh":
        bill=340
        tax=2
        gst=4
        total_bill=bill+tax+gst
        print("total bill:",total_bill)
elif item=="veg":
    print("panner biriyani\n","mushroom biriyani\n")
    dish=input("enter the dish:")   
    if dish=="panner biriyani":
        bill=180
        gst=3
        tax=2
        total_bill=bill+gst+tax
        print("total bill",total_bill)
    elif dish=="mushroom biriyani":
        bill=150
        tax=2
        gst=3
        total_bill=bill+tax+gst
        print("total bill",total_bill)
else:
    print("item is not in list:")