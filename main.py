
import os.path
from tkinter import *
from tkinter import messagebox
import random,os,tempfile,smtplib

def clear():
    bathsoapEntry.insert(0,0)
    facecreamEntry.insert(0, 0)
    facewashEntry.insert(0, 0)
    aloegelEntry.insert(0, 0)
    staymoistEntry.insert(0, 0)
    sunscreamEntry.insert(0, 0)
    srubEntry.insert(0, 0)

    riceEntry.insert(0, 0)
    oilEntry.insert(0, 0)
    wheatEntry.insert(0, 0)
    sugarEntry.insert(0, 0)
    tealeavesEntry.insert(0, 0)
    milkEntry.insert(0, 0)
    daalEntry.insert(0, 0)

    blueberryEntry.insert(0, 0)
    cokeEntry.insert(0, 0)
    redbullEntry.insert(0, 0)
    spriteEntry.insert(0, 0)
    primeEntry.insert(0, 0)
    monsterEntry.insert(0, 0)
    gatoradeEntry.insert(0, 0)

    skincaretaxEntry.delete(0,END)
    grocerytaxEntry.delete(0,END)
    drinkstaxpriceEntry.delete(0,END)

    skincarepriceEntry.delete(0,END)
    grocerypriceEntry.delete(0,END)
    drinkspricepriceEntry.delete(0,END)

    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    billnumberEntry.delete(0,END)

    textarea.delete(1.0,END)


# code for sending gmail starts from here
def send_email():
    def send_gmail():
        try:
            ob=smtplib.SMTP('smtp.gmail.com',587)
            ob.starttls()
            ob.login(senderEntry.get(),passwordEntry.get())
            message=email_textarea.get(1.0,END)
            ob.sendmail(senderEntry.get(),recieverEntry.get(),message)
            ob.quit()
            messagebox.showinfo('Success','Bill is successfully sent',parent=root1)
            root1.destroy()
        except:
                messagebox.showerror('Error','Something went wrong, Please try again',parent=root1)
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is Empty')
        # ends here
    else:
        root1=Toplevel()
        root1.grab_set()
        root1.title('send gmail')
        root1.config(bg='seashell3')


        senderFrame=LabelFrame(root1,text='SENDER',font=('Times new roman',16,'bold'),bd=6,bg='gray20',fg='white')
        senderFrame.grid(row=0,column=0,padx=40,pady=20)

        senderLabel=Label(senderFrame,text="Sender's Email",font=('arial',14,'bold'),bg='gray20',fg='white')
        senderLabel.grid(row=0,column=0,padx=10,pady=8)

        senderEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=GROOVE)
        senderEntry.grid(row=0,column=1,padx=10,pady=8)

        passwordLabel = Label(senderFrame, text="Password", font=('arial', 14, 'bold'), bg='gray20', fg='white')
        passwordLabel.grid(row=1, column=0, padx=10, pady=8)

        passwordEntry = Entry(senderFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=GROOVE,show='*') # show ='*' is used to hide password
        passwordEntry.grid(row=1, column=1, padx=10, pady=8)

        #for Recipeient
        recipientFrame = LabelFrame(root1, text='RECIPIENT', font=('Times new roman', 16, 'bold'), bd=6, bg='gray20',fg='white')
        recipientFrame.grid(row=1, column=0, padx=40, pady=20)

        recieverLabel = Label(recipientFrame, text="Email Address", font=('arial', 14, 'bold'), bg='gray20', fg='white')
        recieverLabel.grid(row=0, column=0, padx=10, pady=8)

        recieverEntry = Entry(recipientFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=GROOVE)
        recieverEntry.grid(row=0, column=1, padx=10, pady=8)

        messageLabel = Label(recipientFrame, text="Message", font=('arial', 14, 'bold'), bg='gray20', fg='white')
        messageLabel.grid(row=2, column=0, padx=10, pady=8)

        email_textarea=Text(recipientFrame,font=('arial', 14, 'bold'),bd=2,relief=SUNKEN,width=42,height=11)
        email_textarea.grid(row=3,column=0,columnspan=2)

        email_textarea.delete(1.0,END)
        email_textarea.insert(END,textarea.get(1.0,END).replace('=','').replace('-','').replace('\t\t\t\t','\t\t'))

        sendButton=Button(root1,text='SEND',font=('arial', 17, 'bold'),width=15,command=send_gmail)
        sendButton.grid(row=4,column=0,pady=20)


    root1.mainloop()






def print_bill():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is Empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')



 # logic for search button
def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0].strip() == billnumberEntry.get().strip():
            f = open(f'bills/{i}','r')
            textarea.delete(1.0,END)
            for data in f:
                textarea.insert(END,data)
            f.close()
            break
    else:
        messagebox.showerror('Error','Invalid Bill Number')



# for creating folder

if not os.path.exists('bills'):
    os.mkdir('bills')
def save_bill():
    global billnumber
    result=messagebox.askyesno('Confirm','Do you want to save the Bill ?')
    if result:
        bill_content=textarea.get(1.0,END)
        file=open(f'bills/ {billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f'Bill Number{billnumber} is saved Successfully')
        billnumber = random.randint(500, 1000)


billnumber = random.randint(500, 1000)
def bill_area():
    if nameEntry.get()=='' or phoneEntry.get()=='':
       messagebox.showerror('Error','Customer Details Required')

    elif skincarepriceEntry.get()=='' and grocerypriceEntry.get()=='' and drinkspricepriceEntry.get()=='':
        messagebox.showerror('Error', 'No products are selected ')

    elif skincarepriceEntry.get()=='0 Rs' and grocerypriceEntry.get()=='0 Rs' and drinkspricepriceEntry.get()=='0 Rs':
        messagebox.showerror('Error', 'No products are selected ')

    else:
            textarea.delete(1.0,END)

            textarea.insert(END,'\t\t\t\t***Welcome Customer***\n\n')
            textarea.insert(END,f'Bill Number: {billnumber}\n')
            textarea.insert(END, f'\nCustomer Name: {nameEntry.get()}\n')
            textarea.insert(END, f'\nCustomer Phone Number: {phoneEntry.get()}\n')
            textarea.insert(END,'\n==============================================================================')
            textarea.insert(END,'Product\t\t\t\tQuantity\t\t\t\tPrice')
            textarea.insert(END, '\n==============================================================================')

            if bathsoapEntry.get()!='0':
             textarea.insert(END,f'\nBath Soap\t\t\t\t{bathsoapEntry.get()}\t\t\t\t{soapprice} Rs')

             if facecreamEntry.get() != '0':
              textarea.insert(END, f'\nFace cream\t\t\t\t{facecreamEntry.get()}\t\t\t\t{facecreamprice}Rs')

             if facewashEntry.get() != '0':
                 textarea.insert(END, f'\nFace wash\t\t\t\t{facewashEntry.get()}\t\t\t\t{facewashprice}Rs')

            if aloegelEntry.get() != '0':
                textarea.insert(END, f'\nAloe gel\t\t\t\t{aloegelEntry.get()}\t\t\t\t{aloegelprice}Rs')

            if staymoistEntry.get() != '0':
                textarea.insert(END, f'\nStay Moist\t\t\t\t{staymoistEntry.get()}\t\t\t\t{staymoistprice}Rs')

            if sunscreamEntry.get() != '0':
                textarea.insert(END, f'\nSuncream\t\t\t\t{sunscreamEntry.get()}\t\t\t\t{sunscreamprice}Rs')

            if srubEntry.get() != '0':
                textarea.insert(END, f'\nScrub\t\t\t\t{srubEntry.get()}\t\t\t\t{srubprice}Rs')

            # Grocery logic

            if riceEntry.get() != '0':
                textarea.insert(END, f'\nRice\t\t\t\t{riceEntry.get()}\t\t\t\t{riceprice}Rs')

            if oilEntry.get() != '0':
                textarea.insert(END, f'\nOil\t\t\t\t{oilEntry.get()}\t\t\t\t{oilprice}Rs')

            if wheatEntry.get() != '0':
                textarea.insert(END, f'\nWheat\t\t\t\t{wheatEntry.get()}\t\t\t\t{wheatprice}Rs')

            if sugarEntry.get() != '0':
                textarea.insert(END, f'\nSugar\t\t\t\t{sugarEntry.get()}\t\t\t\t{sugarprice}Rs')

            if tealeavesEntry.get() != '0':
                textarea.insert(END, f'\nTea Leaves\t\t\t\t{tealeavesEntry.get()}\t\t\t\t{tealeavesprice}Rs')

            if milkEntry.get() != '0':
                textarea.insert(END, f'\nMilk\t\t\t\t{milkEntry.get()}\t\t\t\t{milkprice}Rs')

            if daalEntry.get() != '0':
                textarea.insert(END, f'\nDaal\t\t\t\t{daalEntry.get()}\t\t\t\t{daalprice}Rs')


            # Drinks logic

            if blueberryEntry.get() != '0':
                textarea.insert(END, f'\nBlue-Berry\t\t\t\t{blueberryEntry.get()}\t\t\t\t{blueberryprice}Rs')

            if cokeEntry.get() != '0':
                textarea.insert(END, f'\nCoke\t\t\t\t{cokeEntry.get()}\t\t\t\t{cokeprice}Rs')

            if redbullEntry.get() != '0':
                textarea.insert(END, f'\nRed-Bull\t\t\t\t{redbullEntry.get()}\t\t\t\t{redbullprice}Rs')

            if spriteEntry.get() != '0':
                textarea.insert(END, f'\nSprite\t\t\t\t{spriteEntry.get()}\t\t\t\t{spriteprice}Rs')

            if primeEntry.get() != '0':
                textarea.insert(END, f'\nPrime\t\t\t\t{primeEntry.get()}\t\t\t\t{primeprice}Rs')

            if monsterEntry.get() != '0':
                textarea.insert(END, f'\nMonster\t\t\t\t{monsterEntry.get()}\t\t\t\t{monsterprice}Rs')

            if gatoradeEntry.get() != '0':
                textarea.insert(END, f'\nGatorade\t\t\t\t{gatoradeEntry.get()}\t\t\t\t{gatoradeprice}Rs')

            textarea.insert(END, '\n------------------------------------------------------------------------------')

            if skincaretaxEntry.get()!='0.0 Rs':
                textarea.insert(END,f'\nSkincare Tax\t\t\t\t{skincaretaxEntry.get()}')

            if grocerytaxEntry.get()!='0.0 Rs':
                textarea.insert(END,f'\nGrocery Tax\t\t\t\t{grocerytaxEntry.get()}')

            if drinkstaxpriceEntry.get()!='0.0 Rs':
                textarea.insert(END,f'\nDrinks Tax\t\t\t\t{drinkstaxpriceEntry.get()}')

            textarea.insert(END,f'\n\nTotal Bill \t\t\t\t {totalbill}')

            textarea.insert(END, '\n------------------------------------------------------------------------------')

            save_bill()


def total():
    global soapprice,facecreamprice ,facewashprice , aloegelprice , staymoistprice , sunscreamprice ,srubprice # for Skincare

    global riceprice , oilprice, wheatprice, sugarprice,tealeavesprice,milkprice,daalprice  # for Grocery

    global blueberryprice , cokeprice, redbullprice,spriteprice,primeprice,monsterprice,gatoradeprice # for drinks

    global totalbill

    # skin-care price calculation
    soapprice=int(bathsoapEntry.get())*20
    facecreamprice=int(facecreamEntry.get())*100
    facewashprice = int(facewashEntry.get()) * 100
    aloegelprice = int(aloegelEntry.get()) * 120
    staymoistprice = int(staymoistEntry.get()) * 80
    sunscreamprice = int(sunscreamEntry.get()) * 50
    srubprice = int(srubEntry.get()) * 50

    totalskincareprice = soapprice+facecreamprice+facewashprice+aloegelprice+staymoistprice+sunscreamprice+srubprice
    skincarepriceEntry.delete(0,END)
    skincarepriceEntry.insert(0,str(totalskincareprice)+ 'Rs.')

    skincaretax=totalskincareprice*0.12
    skincaretaxEntry.delete(0,END)
    skincaretaxEntry.insert(0,str(skincaretax)+ ' Rs.')



    # grocery price calculation

    riceprice = int(riceEntry.get())*34
    oilprice = int(oilEntry.get()) * 115
    wheatprice = int(wheatEntry.get()) * 100
    sugarprice = int(sugarEntry.get()) * 60
    tealeavesprice = int(tealeavesEntry.get()) * 135
    milkprice = int(milkEntry.get()) * 55
    daalprice = int(riceEntry.get()) * 30

    totalgroceryprice=riceprice+oilprice+wheatprice+sugarprice+tealeavesprice+milkprice+daalprice
    grocerypriceEntry.delete(0,END)
    grocerypriceEntry.insert(0,str(totalgroceryprice)+ 'Rs.')

    grocerytax = totalgroceryprice * 0.05
    grocerytaxEntry.delete(0, END)
    grocerytaxEntry.insert(0, str(grocerytax) + ' Rs.')

    # Drinks price calculation

    blueberryprice = int(blueberryEntry.get()) * 40
    cokeprice = int(cokeEntry.get()) * 50
    redbullprice = int(redbullEntry.get()) * 100
    spriteprice = int(spriteEntry.get()) * 60
    primeprice = int(primeEntry.get()) * 400
    monsterprice = int(monsterEntry.get()) * 115
    gatoradeprice = int(gatoradeEntry.get()) * 250

    totaldrinksprice = blueberryprice+cokeprice+redbullprice+spriteprice+primeprice+monsterprice+gatoradeprice
    drinkspricepriceEntry.delete(0,END)
    drinkspricepriceEntry.insert(0,str(totaldrinksprice)+ 'Rs.')

    drinkspricetax = totaldrinksprice * 0.08
    drinkstaxpriceEntry.delete(0, END)
    drinkstaxpriceEntry.insert(0, str(drinkspricetax) + ' Rs.')

    totalbill = totalskincareprice+totalgroceryprice+totaldrinksprice+skincaretax+grocerytax+drinkspricetax




root = Tk()

root.title('Retail Billing System')  # the title.

root.geometry('1270x688')  # for changing the window size.

root.iconbitmap('icon.ico') # for putting icon on screen

headingLabel=Label(root,text='Retail Billing System',font=('Times new roman',30,'bold',),bg='gray50',fg='Gold',bd=15,relief=RIDGE)

headingLabel.pack(fill=X,pady=12)

customer_details_frame=LabelFrame(root,text='Customer Details',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=RIDGE , bg='gray25')
customer_details_frame.pack(fill=X)

nameLabel=Label(customer_details_frame,text='Name:-',font=('times new roman',15,'bold' ),bg='gray25', fg='white'  )

nameLabel.grid(row=0,column=0,padx=20,pady=2)

nameEntry=Entry(customer_details_frame , font=('arial',15),bd=9,width=18)
nameEntry.grid(row=0,column=1,padx=8)

phoneLabel=Label(customer_details_frame,text='Phone No:-',font=('times new roman',15,'bold' ),bg='gray25', fg='white')

phoneLabel.grid(row=0,column=2,padx=20,pady=2)

phoneEntry=Entry(customer_details_frame , font=('arial',15),bd=9,width=18)
phoneEntry.grid(row=0,column=3,padx=8)

billnumberLabel=Label(customer_details_frame,text='Bill Number:-',font=('times new roman',15,'bold' ),bg='gray25', fg='white')

billnumberLabel.grid(row=0,column=4,padx=20,pady=2)

billnumberEntry=Entry(customer_details_frame , font=('arial',15),bd=9,width=18)
billnumberEntry.grid(row=0,column=5,padx=8)

searchButton=Button(customer_details_frame,text='SEARCH' , font=('arial',12,'bold') , bd=7,width=10,command=search_bill)
searchButton.grid(row=0,column=6,padx=20,pady=8)

productsFrame=Frame(root)
productsFrame.pack(pady=12)

skincareFrame=LabelFrame(productsFrame,text='SkinCare', font=('times new roman',15,'bold'),fg='gold',bd=8,relief=RIDGE ,bg='gray25')
skincareFrame.grid(row=0, column=0)

bathsoapLabel=Label(skincareFrame,text='Bath Soap' ,font=( 'times now roman',15,'bold'),bg='gray25',fg= 'white')
bathsoapLabel.grid(row=0,column=0 , pady=9,padx=10,sticky='w')

bathsoapEntry=Entry(skincareFrame,font=( 'times now roman',15,'bold'),width=10,bd=5)
bathsoapEntry.grid(row=0,column=1, pady=9,padx=10,sticky='w')
bathsoapEntry.insert(0,0)

facecreamLabel=Label(skincareFrame,text='Face Cream' ,font=( 'times now roman',15,'bold'),bg='gray25',fg= 'white')
facecreamLabel.grid(row=1,column=0 , pady=9,padx=10,sticky='w')

facecreamEntry=Entry(skincareFrame,font=( 'times now roman',15,'bold'),width=10,bd=5)
facecreamEntry.grid(row=1,column=1,pady=9,padx=10,sticky='w')
facecreamEntry.insert(0,0)

facewashLabel=Label(skincareFrame,text='Face Wash' ,font=( 'times now roman',15,'bold'),bg='gray25',fg= 'white')
facewashLabel.grid(row=2,column=0 , pady=9,padx=10,sticky='w')

facewashEntry=Entry(skincareFrame,font=( 'times now roman',15,'bold'),width=10,bd=5)
facewashEntry.grid(row=2,column=1,pady=9,padx=10,sticky='w')
facewashEntry.insert(0,0)

aloegelLabel=Label(skincareFrame,text='AloeGel' ,font=( 'times now roman',15,'bold'),bg='gray25',fg= 'white')
aloegelLabel.grid(row=3,column=0 , pady=9,padx=10,sticky='w')

aloegelEntry=Entry(skincareFrame,font=( 'times now roman',15,'bold'),width=10,bd=5)
aloegelEntry.grid(row=3,column=1,pady=9,padx=10,sticky='w')
aloegelEntry.insert(0,0)

staymoistLabel=Label(skincareFrame,text='StayMoist' ,font=( 'times now roman',15,'bold'),bg='gray25',fg= 'white')
staymoistLabel.grid(row=4,column=0 , pady=9,padx=10,sticky='w')

staymoistEntry=Entry(skincareFrame,font=( 'times now roman',15,'bold'),width=10,bd=5)
staymoistEntry.grid(row=4,column=1,pady=9,padx=10,sticky='w')
staymoistEntry.insert(0,0)

sunscreamLabel=Label(skincareFrame,text='Sunspf50',font=( 'times now roman',15,'bold'),bg='gray25',fg= 'white')
sunscreamLabel.grid(row=5,column=0 , pady=9,padx=10,sticky='w')

sunscreamEntry=Entry(skincareFrame,font=( 'times now roman',15,'bold'),width=10,bd=5)
sunscreamEntry.grid(row=5,column=1,pady=9,padx=10,sticky='w')
sunscreamEntry.insert(0,0)

srubLabel=Label(skincareFrame,text='Scrub',font=( 'times now roman',15,'bold'),bg='gray25',fg= 'white')
srubLabel.grid(row=6,column=0 , pady=9,padx=10,sticky='w')

srubEntry=Entry(skincareFrame,font=( 'times now roman',15,'bold'),width=10,bd=5)
srubEntry.grid(row=6,column=1,pady=9,padx=10,sticky='w')
srubEntry.insert(0,0)

groceryFrame=LabelFrame(productsFrame,text='Grocery', font=('times new roman',15,'bold'),fg='gold',bd=8,relief=RIDGE ,bg='gray25')
groceryFrame.grid(row=0, column=1)

riceLabel=Label(groceryFrame,text='Rice',font=( 'times now roman',15,'bold'),bg='gray25',fg= 'white')
riceLabel.grid(row=0,column=0, pady=9,padx=10,sticky='w')

riceEntry=Entry(groceryFrame,font=('times now roman',15,'bold'),width=10,bd=5)
riceEntry.grid(row=0,column=1,pady=9,padx=10,sticky='w')
riceEntry.insert(0,0)

oilLabel=Label(groceryFrame,text='Oil',font=( 'times now roman',15,'bold'),bg='gray25',fg= 'white')
oilLabel.grid(row=1,column=0, pady=9,padx=10,sticky='w')

oilEntry=Entry(groceryFrame,font=('times now roman',15,'bold'),width=10,bd=5)
oilEntry.grid(row=1,column=1,pady=9,padx=10,sticky='w')
oilEntry.insert(0,0)

wheatLabel=Label(groceryFrame,text='Wheat',font=( 'times now roman',15,'bold'),bg='gray25',fg= 'white')
wheatLabel.grid(row=2,column=0, pady=9,padx=10,sticky='w')

wheatEntry=Entry(groceryFrame,font=('times now roman',15,'bold'),width=10,bd=5)
wheatEntry.grid(row=2,column=1,pady=9,padx=10,sticky='w')
wheatEntry.insert(0,0)

SugarLabel=Label(groceryFrame,text='Sugar',font=( 'times now roman',15,'bold'),bg='gray25',fg= 'white')
SugarLabel.grid(row=3,column=0, pady=9,padx=10,sticky='w')

sugarEntry=Entry(groceryFrame,font=('times now roman',15,'bold'),width=10,bd=5)
sugarEntry.grid(row=3,column=1,pady=9,padx=10,sticky='w')
sugarEntry.insert(0,0)

tealeavesLabel=Label(groceryFrame,text='Tealeaves',font=( 'times now roman',15,'bold'),bg='gray25',fg= 'white')
tealeavesLabel.grid(row=4,column=0, pady=9,padx=10,sticky='w')

tealeavesEntry=Entry(groceryFrame,font=('times now roman',15,'bold'),width=10,bd=5)
tealeavesEntry.grid(row=4,column=1,pady=9,padx=10,sticky='w')
tealeavesEntry.insert(0,0)

milkLabel=Label(groceryFrame,text='Milk',font=( 'times now roman',15,'bold'),bg='gray25',fg= 'white')
milkLabel.grid(row=5,column=0, pady=9,padx=10,sticky='w')

milkEntry=Entry(groceryFrame,font=('times now roman',15,'bold'),width=10,bd=5)
milkEntry.grid(row=5,column=1,pady=9,padx=10,sticky='w')
milkEntry.insert(0,0)

daalLabel=Label(groceryFrame,text='Daal',font=( 'times now roman',15,'bold'),bg='gray25',fg= 'white')
daalLabel.grid(row=6,column=0, pady=9,padx=10,sticky='w')

daalEntry=Entry(groceryFrame,font=('times now roman',15,'bold'),width=10,bd=5)
daalEntry.grid(row=6,column=1,pady=9,padx=10,sticky='w')
daalEntry.insert(0,0)


drinksFrame=LabelFrame(productsFrame,text='Drinks', font=('times new roman',15,'bold'),fg='gold',bd=8,relief=RIDGE ,bg='gray25')
drinksFrame.grid(row=0, column=2)


blueberryLabel=Label(drinksFrame,text='BlueBerry',font=( 'times now roman',15,'bold'),bg='gray25',fg= 'white')
blueberryLabel.grid(row=0,column=0, pady=9,padx=10,sticky='w')

blueberryEntry=Entry(drinksFrame,font=('times now roman',15,'bold'),width=10,bd=5)
blueberryEntry.grid(row=0,column=1,pady=9,padx=10,sticky='w')
blueberryEntry.insert(0, 0)

cokeLabel=Label(drinksFrame,text='Coke',font=( 'times now roman',15,'bold'),bg='gray25',fg= 'white')
cokeLabel.grid(row=1,column=0, pady=9,padx=10,sticky='w')

cokeEntry=Entry(drinksFrame,font=('times now roman',15,'bold'),width=10,bd=5)
cokeEntry.grid(row=1,column=1,pady=9,padx=10,sticky='w')
cokeEntry.insert(0,0)

redbullLabel=Label(drinksFrame,text='Red-Bull',font=( 'times now roman',15,'bold'),bg='gray25',fg= 'white')
redbullLabel.grid(row=2,column=0, pady=9,padx=10,sticky='w')

redbullEntry=Entry(drinksFrame,font=('times now roman',15,'bold'),width=10,bd=5)
redbullEntry.grid(row=2,column=1,pady=9,padx=10,sticky='w')
redbullEntry.insert(0,0)

spriteLabel=Label(drinksFrame,text='Sprite',font=( 'times now roman',15,'bold'),bg='gray25',fg= 'white')
spriteLabel.grid(row=3,column=0, pady=9,padx=10,sticky='w')

spriteEntry=Entry(drinksFrame,font=('times now roman',15,'bold'),width=10,bd=5)
spriteEntry.grid(row=3,column=1,pady=9,padx=10,sticky='w')
spriteEntry.insert(0,0)

primeLabel=Label(drinksFrame,text='Prime',font=( 'times now roman',15,'bold'),bg='gray25',fg= 'white')
primeLabel.grid(row=4,column=0, pady=9,padx=10,sticky='w')

primeEntry=Entry(drinksFrame,font=('times now roman',15,'bold'),width=10,bd=5)
primeEntry.grid(row=4,column=1,pady=9,padx=10,sticky='w')
primeEntry.insert(0,0)

monsterLabel=Label(drinksFrame,text='Monster',font=( 'times now roman',15,'bold'),bg='gray25',fg= 'white')
monsterLabel.grid(row=5,column=0, pady=9,padx=10,sticky='w')

monsterEntry=Entry(drinksFrame,font=('times now roman',15,'bold'),width=10,bd=5)
monsterEntry.grid(row=5,column=1,pady=9,padx=10,sticky='w')
monsterEntry.insert(0,0)

gatoradeLabel=Label(drinksFrame,text='Gatorade',font=( 'times now roman',15,'bold'),bg='gray25',fg= 'white')
gatoradeLabel.grid(row=6,column=0, pady=9,padx=10,sticky='w')

gatoradeEntry=Entry(drinksFrame,font=('times now roman',15,'bold'),width=10,bd=5)
gatoradeEntry.grid(row=6,column=1,pady=9,padx=10,sticky='w')
gatoradeEntry.insert(0,0)

billframe=Frame(productsFrame, bd=8, relief=GROOVE)
billframe.grid(row=0,column=3,padx=10)

billareaLabel= Label(billframe,text='Bill' , font=('times now roman',15,'bold'),bd=7,relief=RIDGE)
billareaLabel.pack(fill=X)

scrollbar=Scrollbar(billframe,orient=VERTICAL) # Created a scroll bar
scrollbar.pack(side=RIGHT,fill=Y)

textarea=Text(billframe,height=22,width=78,yscrollcommand=scrollbar.set)
textarea.pack()

scrollbar.config(command=textarea.yview)# this will move the scroll up and down




billmenuFrame=LabelFrame(root,text='BillMenu :)', font=('times new roman',15,'bold'),fg='gold',bd=8,relief=RIDGE ,bg='gray25')
billmenuFrame.pack()


skincarepriceLabel=Label(billmenuFrame,text='Skin-care Price',font=( 'times now roman',15,'bold'),bg='gray25',fg= 'white')
skincarepriceLabel.grid(row=0,column=0, pady=9,padx=10,sticky='w')

skincarepriceEntry=Entry(billmenuFrame,font=('times now roman',15,'bold'),width=10,bd=5)
skincarepriceEntry.grid(row=0,column=2,pady=9,padx=10,sticky='w')


grocerypriceLabel=Label(billmenuFrame,text='Grocery Price',font=( 'times now roman',15,'bold'),bg='gray25',fg= 'white')
grocerypriceLabel.grid(row=1,column=0, pady=9,padx=10,sticky='w')

grocerypriceEntry=Entry(billmenuFrame,font=('times now roman',15,'bold'),width=10,bd=5)
grocerypriceEntry.grid(row=1,column=2,pady=9,padx=10,sticky='w')


drinkspricepriceLabel=Label(billmenuFrame,text='DrinksPrice',font=( 'times now roman',15,'bold'),bg='gray25',fg= 'white')
drinkspricepriceLabel.grid(row=2,column=0, pady=9,padx=10,sticky='w')

drinkspricepriceEntry=Entry(billmenuFrame,font=('times now roman',15,'bold'),width=10,bd=5)
drinkspricepriceEntry.grid(row=2,column=2,pady=9,padx=10,sticky='w')





skincaretaxLabel=Label(billmenuFrame,text='Skin-care Tax',font=( 'times now roman',15,'bold'),bg='gray25',fg= 'white')
skincaretaxLabel.grid(row=0,column=3, pady=9,padx=10,sticky='w')

skincaretaxEntry=Entry(billmenuFrame,font=('times now roman',15,'bold'),width=10,bd=5)
skincaretaxEntry.grid(row=0,column=4,pady=9,padx=10,sticky='w')


grocerytaxLabel=Label(billmenuFrame,text='Grocery Tax',font=( 'times now roman',15,'bold'),bg='gray25',fg= 'white')
grocerytaxLabel.grid(row=1,column=3, pady=9,padx=10,sticky='w')

grocerytaxEntry=Entry(billmenuFrame,font=('times now roman',15,'bold'),width=10,bd=5)
grocerytaxEntry.grid(row=1,column=4,pady=9,padx=10,sticky='w')


drinkstaxpriceLabel=Label(billmenuFrame,text='Drinks Tax',font=( 'times now roman',15,'bold'),bg='gray25',fg= 'white')
drinkstaxpriceLabel.grid(row=2,column=3, pady=9,padx=10,sticky='w')

drinkstaxpriceEntry=Entry(billmenuFrame,font=('times now roman',15,'bold'),width=10,bd=5)
drinkstaxpriceEntry.grid(row=2,column=4,pady=9,padx=10,sticky='w')






buttonFrame=Frame(billmenuFrame,bd=0,relief=GROOVE)
buttonFrame.grid(row=0,column=5,rowspan=3)

totalButton=Button(buttonFrame,text='Total',font=('arial',15,'bold'),bg='gray25',fg='White',bd=5,width=8 , pady=10,command=total)
totalButton.grid(row=0,column=0,pady=20,padx=5,)


billButton=Button(buttonFrame,text='Bill',font=('arial',15,'bold'),bg='gray25',fg='White',bd=5,width=8 , pady=10,command=bill_area)
billButton.grid(row=0,column=2,pady=20,padx=5,)

emailButton=Button(buttonFrame,text='Email',font=('arial',15,'bold'),bg='gray25',fg='White',bd=5,width=8 , pady=10,command=send_email)
emailButton.grid(row=0,column=3,pady=20,padx=5)

printButton=Button(buttonFrame,text='Print',font=('arial',15,'bold'),bg='gray25',fg='White',bd=5,width=8 , pady=10,command=print_bill)
printButton.grid(row=0,column=4,pady=20,padx=5)

clearButton = Button(buttonFrame,text='Clear',font=('arial',15,'bold'),bg='gray25',fg='White',bd=5,width=8 ,pady=10,command=clear)
clearButton.grid(row=0,column=5,pady=20,padx=5, )

billmenuFrame.pack(fill=X)












root.mainloop() # this is for showing the window.


