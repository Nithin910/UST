print("Hey hai, Welcome to our e-kart shopping!!!")
l=["bread","cookies","cheese","butter","yogurt"]#40,80,180,120,60
lc=[40,80,180,120,60]
cl=[]
clq=[]
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
        cl.append(name)
        clq.append(num)
    elif n==3:
        name=input("What u want to update")
        uq=int(input("enter the updated quantity"))
        for i in range(len(cl)):
            if name==cl[i]:
                t=i
                break
        clq[i]=uq
    elif n==4:
        name=input("what item u want to delete")
        if name not in cl:
            print("There is no item found in ur cart")
        else:
            for i in range(len(cl)):
                if name==cl[i]:
                    t=clq[i]
                    break
            cl.remove(name)
            clq.remove(t)
                    
    elif n==5:
        s=0
        for i in range(len(cl)):
            for j in range(len(l)):
                if cl[i]==l[j]:
                    s+=clq[i]*lc[j]
                    print("you ordered ",cl[i],"in ",clq[i],"quantity,So the money is:",clq[i]*lc[j])
                    break
        print("The Total Bill is:",s)
        print("Thank You, Visit Again")
        break
    
        
