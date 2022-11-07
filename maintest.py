from cgi import print_environ
from itertools import product
from os import remove
from queue import Empty
from pyfiglet import Figlet
import qrcode

class mainmedia:
    def __init__(self):
        print('start program')
        self.PRODUCTS = []
        print("loading...")
        myfile = open('database.txt','r+')
        data = myfile.read()
        self.prouduct_list = data.split('\n')
        a = len(self.prouduct_list)
        for i in range(len(self.prouduct_list)):
            prouduct_info = self.prouduct_list[i].split(',')

            self.PRODUCTS.append({'id': (prouduct_info[0]),'name':prouduct_info[1], 'director':(prouduct_info[2]), 'time':int(prouduct_info[3]),'producer':(prouduct_info[4])})
        print("welcome")
        print(len(self.prouduct_list))

        f = Figlet(font='standard')
        print (f.renderText('list media'))
        self.show_menu()
        self.main()
        self.tekrar()
        from ast import Delete, Not

    def show_list(self):
        for i in range(len(self.PRODUCTS)):
            print(self.PRODUCTS)
            self.qr() 

    def tekrar(self):
        repeat="y"
        while repeat == "y":
            repeat=input("aya edameh midahid?  (y or n)")
            if repeat=="y":
                self.show_menu()
                self.main() 

    def show_menu(self):
        print('1-Add media')
        print('2-Edit media')
        print('3-Delete media')
        print('4-Search')
        print('5-Show List & qrcode')
        print('6-Exit & save')

    def add_media(self):
        
        n = int(input('How many media do you add?  '))
        a = len(self.PRODUCTS)
        for i in range(n):
        
            code =int(i+1+a)  
            name = input(' media name :  ')
            while name in self.prouduct_list:
                print("media tekrari hast")
                print("be edit bravid")
                name = input(' media name :  ')
            director =input(' director :  ')
            time =int(input(' media number :  '))
            producer = input(' media producer :  ') 
            mydict1 = {}
            mydict1['id'] = code
            mydict1['name'] = name
            mydict1['director'] = director
            mydict1['time'] = time
            mydict1['producer'] = producer
            self.PRODUCTS.append(mydict1)        
        for i in range(len(self.PRODUCTS)):
            print(self.PRODUCTS[i])    


    def edit_media(self):
        a=input('aya az tarigh media id edit mikonid?(y or n)')
        if a=="y" :
            b=input("id ra vared konid? ")
            c=int(b)
        else:
            c=input("name kala ra vard konid?  ")    
        for i in range(len(self.PRODUCTS)):
            #mydictn2 = PRODUCTS[i]
            if  c==self.PRODUCTS[i]['id'] or  c==self.PRODUCTS[i]['name']  :
                print(self.PRODUCTS[i])
                n1= input("aya media name ra taghir midahid? y or no")
                if n1=="y":
                    self.PRODUCTS[i]['name'] = input("new name")
                n2= input("aya director ra taghir midahid? y or no")
                if n2=="y": 
                    self.PRODUCTS[i]['director'] =float(input("new director")) 
                n3= input("aya time ra taghir midahid? y or no")
                if n3=="y":
                    self.PRODUCTS[i]['time'] =int(input("new time"))
                n4= input("aya producer ra taghir midahid? y or no")
                if n4=="y":
                    self.PRODUCTS[i]['producer'] =int(input("new producer"))            
                print(self.PRODUCTS[i])

    def qr(self):
        for i in range (len(self.PRODUCTS)):
            n = str(i)
            ss = list(self.PRODUCTS[i].values())
            w = qrcode.make(ss)  
            w.save(n+".png") 

    def search(self):
        a = input('word enter for search??  ')
        for i in range(len(self.PRODUCTS)):
            if  str(self.PRODUCTS[i]['id'])==a or  self.PRODUCTS[i]['name']==a or  self.PRODUCTS[i]['director']==a or  self.PRODUCTS[i]['producer']==a :
                print(self.PRODUCTS[i])
            else:
                print("word for search not found")

    def save_exit (self):
        f = open("database.txt", "w")
        n = len(self.PRODUCTS)
        #s=n-1
        print(n) 
        for i in range(len(self.PRODUCTS)):
            ss = list(self.PRODUCTS[i].values())
            print(self.PRODUCTS[i])
            if i == 0:
                f.write(str(ss[0])+','+str(ss[1])+','+str(ss[2])+','+str(ss[3])+','+str(ss[4]))
            else:
                f.write('\n'+str(ss[0])+','+str(ss[1])+','+str(ss[2])+','+str(ss[3])+','+str(ss[4]))   
        f.close()

    def main(self):
        choice = int(input('please choose a number :  '))
        if choice ==1:
            self.add_media()
        elif choice == 2:
            self.edit_media()
        elif choice == 3:
            self.delete_media()
        elif choice == 4:
            self.search()    
        elif choice == 5:
            self.show_list()
        elif choice == 6:
            self.save_exit()

    def delete_media(self):    
        a=input('aya az tarigh media id delet mikonid?(y or n)')
        if a=="y" :
            b=input("id ra vared konid? ")
            c=int(b)
        else:
            c=input("media name or director or producer ra vard konid?  ")    
        for i in range(len(self.PRODUCTS)):
            if  c==self.PRODUCTS[i]['id'] or  c==self.PRODUCTS[i]['name']or  c==self.PRODUCTS[i]['director']or  c==self.PRODUCTS[i]['producer']  :
                print(self.PRODUCTS[i])
                del self.PRODUCTS[i]
                break
        x=input('aya kode kalaha morattab shavad?(y or n') 
        if x=="y":   
            for i in range(len(self.PRODUCTS)):
                self.PRODUCTS[i]['id']=i+1

mainmedia()




#dfdgdfg


