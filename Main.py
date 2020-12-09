#This is the start of our python program.
import pygame
from Distance import Distance
import CanteenInfo
from Position import Position
from operator import itemgetter
from tkinter import *
import tkinter.messagebox
import tkinter as tk
from tkinter.ttk import *
from sys import exit
class Main:
    def __init__(self):
        self.clickX = 0
        self.clickY = 0
        self.maprect = None
    #display of map
    def display_map(self, filepath = "map.jpg", width = 1600, height = 900):
        map = pygame.image.load(filepath)
        #print(map.get_rect())
        maprect = map.get_rect()
        #print(maprect)
        self.maprect = maprect
        width = maprect.width
        height = maprect.height
        SCREEN_SIZE = (width, height)
        #print(width)
        #print(height)
        #map = pygame.transform.scale(map, (width, height))          
        screen = pygame.display.set_mode(SCREEN_SIZE)
        screen.blit(map,(0,0))
        pygame.display.flip()


    def get_user_location(self):
        #print("x="+str(self.clickX)+"y="+str(self.clickY))
        return self.clickX, self.clickY

    def distance_a_b(self, location_of_a, location_of_b):
        dis = Distance()
        return dis.getDistance(location_of_a, location_of_b)
    

    def sort_distance(self, user_location, canteens_location = CanteenInfo.canteens_location):
        distances_list = {}
        for canteen in canteens_location:
            tuplePos = canteens_location[canteen]['Position']
            pos = Position(tuplePos[0],tuplePos[1])
            distances_list[canteen] = self.distance_a_b(user_location,pos)
        #print(distances_list)
        sorted_distances = sorted(distances_list.items(), key=lambda distance: distance[1])
        return sorted_distances

    def search_by_food(self, foodname, foodlist_canteens = CanteenInfo.foodlist_canteens):
        list_canteens = []
        for canteen in foodlist_canteens:
            for stall in foodlist_canteens[canteen]:
            # pthon2.7 has_key(); python3 key in dict
                for food in foodlist_canteens[canteen][stall]:
                    if foodname.lower().replace(" ", "") in food.lower().replace(" ", ""):
                        list_canteens.append([canteen,stall,food,foodlist_canteens[canteen][stall][food]])
        return list_canteens

    def sort_by_rank(self, ranklist_canteens = CanteenInfo.canteens_location):
        ranks_list = {}
        for canteen in ranklist_canteens:
            rank = ranklist_canteens[canteen]['Rank']
            ranks_list[canteen] = rank
        #print(ranks_list)
        #descending order
        sorted_ranks = sorted(ranks_list.items(), key = lambda rank: rank[1],  reverse = True)
        return sorted_ranks

    # two dim dict
    def addtwodimdict(self, thedict, key_a, key_b, val):
        if key_a in thedict:
            thedict[key_a].update({key_b: val})
        else:
            thedict.update({key_a:{key_b: val}})

    def Search_by_price(self, price, foodlist_canteens = CanteenInfo.foodlist_canteens):
        list_canteens = []
        for canteen in foodlist_canteens:
            for stall in foodlist_canteens[canteen]:
                for foodname in foodlist_canteens[canteen][stall]:
                    if foodlist_canteens[canteen][stall][foodname] >= float(price[0]) and foodlist_canteens[canteen][stall][foodname] <= float(price[1]):
                        list_canteens.append([canteen, stall, foodname,foodlist_canteens[canteen][stall][foodname]])
        return list_canteens

    # change Canteen name 
    def Update_information(self, oldname, newname,  foodlist_canteens = CanteenInfo.foodlist_canteens, canteens_location = CanteenInfo.canteens_location):
        foodlist_canteens[newname] = foodlist_canteens.pop(oldname)
        canteens_location[newname] = canteens_location.pop(oldname)

    def transport (self, user_location, dest_location):
        x = dest_location.x - user_location.xfoodlist_canteens
        y = dest_location.y - user_location.y
        if x >= 0 :
            print("go east for "+ str(x))
        else :
            print("go west for "+ str(-x))
        if y >= 0 :
            print("go north for "+ str(y))
        else :
            print("go south for "+ str(-y))


    def mouseclick(self):
        flag = True
        while flag:
            pygame.init()
            self.display_map()
            for event in pygame.event.get():
                #esc quit
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT:
                    flag = False
                # students choose position
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    print('Your Position is (' + str(pos[0])+','+str(pos[1])+')')
                    if pos[0] >= self.maprect.right or pos[1] >= self.maprect.bottom:
                        pass
                    else:
                        self.clickX = pos[0]
                        self.clickY = pos[1]
                    pygame.quit()
                    return

    

    # window command
    def win_get_user_location(self):
        outstr = 'Your Position is (' + str(main.clickX)+','+str(main.clickY)+')'
        tkinter.messagebox.showinfo(message=outstr)


    def win_sort_distance(self):
        tkinter.messagebox.showinfo(message = self.sort_distance(Position(self.clickX,self.clickY)))

    def win_search_by_foodname(self, foodname):
        print(self.search_by_food(foodname))
        tkinter.messagebox.showinfo(message = self.search_by_food(foodname))
    def win_search_by_food(self):
            root = Tk()
            l_foodname =Label(root,text='food name:')
            l_foodname.grid(row=0,sticky=W)
            e_foodname =Entry(root,textvariable=input_data)
            e_foodname.grid(row=0,column=1,sticky=E)
            b_login = Button(root,text='search',command = lambda: main.win_search_by_foodname(e_foodname.get()))
            b_login.grid(columnspan=2)
            root.mainloop()

    def win_sort_by_rank(self):
        tkinter.messagebox.showinfo(message=self.sort_by_rank())


    def  win_Search_by_pricepara(self, price):
        tkinter.messagebox.showinfo(message=self.Search_by_price(price))
    def win_Search_by_price(self):
        root = Tk()
        l_low =Label(root,text='lowest price:')
        l_low.grid(row=0,sticky=W)
        e_low =Entry(root,textvariable=input_data)
        e_low.grid(row=0,column=1,sticky=E)

        l_high = Label(root,text='highest price:')
        l_high.grid(row=1,sticky=W)
        e_high = Entry(root,textvariable=input_data_other)
        e_high.grid(row=1,column=1,sticky=E)
        b_login = Button(root,text='search',command = lambda: main.win_Search_by_pricepara((e_low.get(),e_high.get())))
        b_login.grid(columnspan=2)
        root.mainloop()

    # change Canteen name
    def win_Update_informationpara(self,oldname, newname):
        self.Update_information(oldname,newname)
        tkinter.messagebox.showinfo(message='update successfully')

    def win_Update_information(self):
        root = Tk()
        l_low =Label(root,text='old name:')
        l_low.grid(row=0,sticky=W)
        e_low =Entry(root,textvariable=input_data)
        e_low.grid(row=0,column=1,sticky=E)

        l_high = Label(root,text='new name:')
        l_high.grid(row=1,sticky=W)
        e_high = Entry(root,textvariable=input_data_other)
        e_high.grid(row=1,column=1,sticky=E)
        b_login = Button(root,text='update',command = lambda: self.win_Update_informationpara(e_low.get(),e_high.get()))
        b_login.grid(columnspan=2)
        root.mainloop()
        

    def win_transportpara(self, user_location, dest_location):
        x = dest_location.x - user_location.x
        y = dest_location.y - user_location.y
        if x >= 0 :
            outstring ="go east for "+ str(x)
        else :
            outstring="go west for "+ str(-x)
        outstring += '\n'
        if y >= 0 :
            outstring += "go north for "+ str(y)
        else :
            outstring += "go south for "+ str(-y)
        tkinter.messagebox.showinfo(message=outstring)
        
    def win_transport(self):
        user_location = Position(self.clickX,self.clickY)
        root = Tk()
        l_low =Label(root,text='destination x:')
        l_low.grid(row=0,sticky=W)
        e_low =Entry(root,textvariable=input_data)
        e_low.grid(row=0,column=1,sticky=E)

        l_high = Label(root,text='destination y:')
        l_high.grid(row=1,sticky=W)
        e_high = Entry(root,textvariable=input_data_other)
        e_high.grid(row=1,column=1,sticky=E)
        b_login = Button(root,text='search',command = lambda: main.win_transportpara(user_location,Position(int(e_low.get()),int(e_high.get()))))
        b_login.grid(columnspan=2)
        root.mainloop()
        pass

    def win_quitsystem (self):
        sys.exit(0)

if __name__ == "__main__":

    main = Main()
    #test mouseclick
    '''
    main.mouseclick()
    '''

    #test search_by_food
    '''
    print(main.search_by_food('fish vermicelli soup'))
    print(main.search_by_food('Soya sauce'))
    '''

    #test sort_distance
    '''
    Pos = Position()
    Pos.setposition(100,100)
    print(main.sort_distance(Pos))
    '''

    #test sort_by_rank
    '''
    print(main.sort_by_rank())
    '''


    #test Search_by_price
    '''
    print(main.Search_by_price((0,3)))
    '''

    #test Update_information
    '''
    main.Update_information('Canteen 2','Canteen 8')
    print(CanteenInfo.foodlist_canteens)
    print(CanteenInfo.canteens_location)
    '''

    #test transport
    '''
    Pos1= Position()
    Pos1.setposition(100,100)
    Pos2= Position()
    Pos2.setposition(200,200)
    main.transport(Pos1,Pos2)
    '''

    '''
    main.mouseclick()
    while(True):
        try:
            #input 0-7
            choose = int(input('------\n0.quit\n1.get_user_location\n2.search_by_food\n3.sort_distance\n4.sort_by_rank\n5.Search_by_price\n6.Update_information\n7.transport\n8.choose position\nchoose number:'))
            if choose == 0 :
                break
            elif choose ==1 :
                print('Your Position is (' + str(main.clickX)+','+str(main.clickY)+')')
            elif choose ==2 :
                name = str(input("input food name:"))
                print(main.search_by_food(name))
            elif choose ==3:
                Pos = Position()
                Pos.setposition(main.clickX,main.clickY)
                print(main.sort_distance(Pos))
            elif choose ==4:
                print(main.sort_by_rank())
            elif choose ==5:
                begin=int(input("input lowest price:"))
                end =int(input("input highest price:"))
                print(main.Search_by_price((begin,end)))
            elif choose ==6:
                oldname=str(input("input old name:"))
                newname =str(input("input new name:"))
                main.Update_information(oldname,newname)
                print(CanteenInfo.foodlist_canteens)
                print(CanteenInfo.canteens_location)
            elif choose ==7:
                YourPos= Position(main.clickX, main.clickY)
                x=int(input("input destination position x:"))
                y =int(input("input destination position y:"))
                Pos= Position(x,y)
                main.transport(YourPos,Pos)
            elif choose ==8:
                yourchoose = str(input('Whether to reselect your position:'))
                if yourchoose == 'yes':
                    main.mouseclick()
                else:
                    pass
        finally:
            pass
    '''
    # define variables

    mainwindow = Tk()
    mainwindow.title("MainWindow")
    input_data = StringVar()
    input_data_other = StringVar()



    quitSystem = Button(mainwindow, text="quit",command= lambda: main.win_quitsystem())
    get_user_location = Button(mainwindow, text="get_user_location",command = lambda: main.win_get_user_location())
    sort_distance = Button(mainwindow, text="sort_distance",command = lambda: main.win_sort_distance())
    search_by_food = Button(mainwindow, text="search_by_food",command = lambda: main.win_search_by_food())
    sort_by_rank = Button(mainwindow, text="sort_by_rank",command = lambda: main.win_sort_by_rank())
    Search_by_price = Button(mainwindow, text="Search_by_price" ,command = lambda: main.win_Search_by_price())
    Update_information = Button(mainwindow, text="Update_information" ,command = lambda: main.win_Update_information())
    transport = Button(mainwindow, text="transport",command = lambda: main.win_transport())
    choose_position = Button(mainwindow, text="choose position", command=lambda: main.mouseclick())

    choose_position.grid(row=1, column=1)
    sort_distance.grid(row=1, column=2)
    get_user_location.grid(row=1, column=3)
    search_by_food.grid(row=1, column=4)
    sort_by_rank.grid(row=1, column=5)
    Search_by_price.grid(row=1, column=6)
    Update_information.grid(row=1, column=7)
    transport.grid(row=1, column=8)
    quitSystem.grid(row=1, column=9)

    mainwindow.mainloop()