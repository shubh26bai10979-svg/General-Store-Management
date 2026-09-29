#General stores management software
print("Welcome to the Management Software of our Store")
m=0
products=["Milk","Cheese","Butter","Chocolate","Juice","Chips","Biscuits","Maggie","Coffee"]
counts=[0,0,0,0,0,0,0,0,0]
bills = []
prices=[70,150,60,20,30,10,10,15,50]

def do_billling():
    t=0
    more=0
    while(more<=0):
        print("Code","Products"," ","Prices")
        print()
        for j in range(len(products)):
            print(j+1,"  ",products[j]," "*(len(products)-len(products[j])),prices[j])
        
        b=int(input("Enter Product Code for input"))
        if(b in range(1,10)):
            if(b==1):
                t=t+70
            elif(b==2):
                t=t+150
            elif(b==3):
                t=t+60
            elif(b==4):
                t=t+20
            elif(b==5):
                t=t+30
            elif(b==6):
                t=t+10
            elif(b==7):
                t=t+10
            elif(b==8):
                t=t+15
            elif(b==9):
                t=t+50
            counts[b-1]=counts[b-1]+1
            print(products[b-1],"Added")
            print("Total amount =",t)
            print("Enter 0 to add more product")
            print("Enter 1 to checkout")
            more=5
            while(more!=0 and more!=1):
                more=int(input("Enter"))
                if(more!=0 and more!=1):
                    print("Enter Valid Operation")
            if(more==0):
                continue
            elif(more==1):
                print("Complete Payment")
        else:
            print("Enter Valid Code")
    return(t)

def show_history():
    print("Products"," ","Quantity Sold")
    print()
    for i in range(len(products)):
        print(products[i]," "*(len(products)-len(products[i])),counts[i])
    print()
    for k in range(len(bills)):
        print("Bill",k+1,":",bills[k])
    print()
        
while(m!=2):
    print("Menu")
    print("Enter 0 to start billing")
    print("Enter 1 to check history")
    print("Enter 2 to exit")
    m=int(input("Enter"))
    if(m==0):
        total = do_billling()
        bills.append(total)
        print("Final total is", total)
    elif(m==1):
        show_history()
    elif(m==2):
        print("Thankyou")
    else:
        print("Enter valid operation")