print("Hey hai, Welcome to our e-kart shopping!!!")
l={"bread":40,"cookies":80,"cheese":180,"butter":120,"yogurt":60}#40,80,180,120,60
cl={}
while(True):
    print("What do you want to do")
    print("press 1 for Viewing the items")
    print("press 2 for adding the items")
    print("press 3 for updating the items")
    print("press 4 for deleting the items")
    print("press 5 for Billing")
    n=int(input("Enter your choice"))
    if n==1:
        print("here's a look for our hotel menu")
        print("Name: bread Price: 40")
        print("Name: cookies Price: 80")
        print("Name: butter Price: 120")
        print("Name: cheese Price: 180")
        print("Name: yoghurt Price: 60")
    elif n==2:
        name=input("Enter the item name")
        num=int(input("Enter the quantity"))
        cl[name]=num
    elif n==3:
        name=input("What u want to update")
        uq=int(input("enter the updated quantity"))
        cl[name]=uq
    elif n==4:
        name=input("what item u want to delete")
        if name not in cl:
            print("There is no item found in ur cart")
        else:
            cl.pop(name)
    elif n==5:
        s=0
        for i in cl.keys():
            if i in l.keys():
                s+=cl[i]*l[i]
                print("you ordered ",i,"in ",cl[i],"quantity,So the money is:",cl[i]*l[i])
        print("The Total Bill is:",s)
        print("Thank You, Visit Again")
        break
    
        
