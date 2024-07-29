from datetime import datetime

name=input("enter your name: ")

lists='''
rice     rs 20/kg
sugar    rs 30/kg
salt     rs 20/kg
oil      rs 90/li
paneer   rs 60/kg
maggi    rs 10/pack
boost    rs 100/pack
colgate  rs 85/pack
'''
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]

#rates for items
items={'rice':20,'sugar':30,'salt':20,'oil':90,'paneer':60,'maggi':10,'boost':100,'colgate':85}
option=int(input("for list of items press 1"))
if option==1:
    print(lists)
for i in range (len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit: "))
    if inp1==2:
        break
    if inp1==1:
        item=input("enter your items:")
        quantity=int(input("enter quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry, the item you have entered is not available.")
    else:
        print("you have entered wrong number")
    inp=input("can i bill the items yes or no: ")
    if inp=='yes':
        pass  
        if finalamount!=0:
            print(25*"=","srinivas supermarket",25*"=")
            print(28*" ","dharanalakota")
            print("name:",name,30*" ","date:",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',8*" ",'quantity',3*" ",'price')
            for i in range(len(pricelist)):

                print(i,8*' ',8*' ',ilist[i],3*' ',qlist[i],plist[i])
                print(50*" ",'totalamount:','rs',totalprice)
                print("gst amount",50*" ",'rs',gst)
                print(75*"-")
                print(50*" ",'finalamount:','rs',finalamount)
                print(75*"_")
                print(50*" ","thanks for visiting")
                print(75*"-")
