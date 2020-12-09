def get_text_input(input_str,event):
    import pygame


    if event.type == pygame.KEYDOWN:
        # print(str(event.key) + event.unicode)
        if (event.key==8):
            if (len(input_str)>0):
                input_str = input_str[:-1]
        else:
            input_str = input_str + event.unicode
        # print (input_str)
    return input_str

def text_box(location, size, display):
    text_str=""
    typing = True
    gameExit = False
    while (typing):
        # cover previous input
        pygame.draw.rect(display, (255, 255, 255), location + size)
        pygame.draw.rect(display, (0, 0, 0), location + size, 10)

        text = font2.render(text_str, True, (0, 0, 0))
        display.blit(text, (location[0] + 10, location[1] + 10))

        for Event in pygame.event.get():

            if Event.type == pygame.QUIT:
                gameExit = True
                typing = False

            if (Event.type == pygame.KEYDOWN and Event.key == 13):
                typing = False
            else:
                text_str = get_text_input(text_str, Event)

        pygame.display.update()
    return gameExit,text_str


def print_list(resultList, position, display, page):
    i = 0
    button_color = (150, 150, 150)

    item_per_page = 10
    number_of_page = len(resultList) // item_per_page + (1 * ((len(resultList) % item_per_page) > 0))

    for x in resultList[((page - 1) * item_per_page):(page * item_per_page - 1)]:
        resultList_str = x[0] + ":" + x[1] + ":" + x[2] + ":" + str(int(x[3]))
        resultList_text = font.render(resultList_str, True, (0, 0, 0))
        display.blit(resultList_text, (position[0], position[1] + 20 * i))
        i = i + 1

    if number_of_page > 1:
        page_count = font.render(str(page) + "/" + str(number_of_page), True, (0, 0, 0))
        display.blit(page_count, (position[0]+135, position[1] + 10 + 20 * item_per_page))

    if number_of_page > 1:
        prevPageButtonLoc = [position[0] + 20, position[1] + 20 * item_per_page + 10]
        prevPageButtonSize = [100, 50]
        pygame.draw.rect(display, button_color, prevPageButtonLoc + prevPageButtonSize)
        prevPageButtonText = font2.render("prev", True, (0, 0, 0))
        display.blit(prevPageButtonText, (prevPageButtonLoc[0] + 10, prevPageButtonLoc[1] + 10))

        nextPageButtonLoc = [position[0] + 170, position[1] + 20 * item_per_page + 10]
        nextPageButtonSize = [100, 50]
        pygame.draw.rect(display, button_color, nextPageButtonLoc + nextPageButtonSize)
        nextPageButtonText = font2.render("next", True, (0, 0, 0))
        display.blit(nextPageButtonText, (nextPageButtonLoc[0] + 10, nextPageButtonLoc[1] + 10))



    return position

def change_page(resultList, position, page):


    item_per_page = 10
    number_of_page = len(resultList) // item_per_page + (1 * ((len(resultList) % item_per_page) > 0))

    prevPageButtonLoc = [position[0] + 20, position[1] + 20 * item_per_page + 10]
    prevPageButtonSize = [100, 50]

    nextPageButtonLoc = [position[0] + 150, position[1] + 20 * item_per_page + 10]
    nextPageButtonSize = [100, 50]

    if number_of_page > 1:
        if event.type == pygame.MOUSEBUTTONDOWN:
            loc = pygame.mouse.get_pos()
            if (prevPageButtonLoc[0] + prevPageButtonSize[0] > loc[0] and loc[0] > prevPageButtonLoc[0] and
                    prevPageButtonLoc[1] + prevPageButtonSize[1] > loc[1] and loc[1] > prevPageButtonLoc[1]):
                if page > 1:
                    page = page - 1

        if event.type == pygame.MOUSEBUTTONDOWN:
            loc = pygame.mouse.get_pos()
            if (nextPageButtonLoc[0] + nextPageButtonSize[0] > loc[0] and loc[0] > nextPageButtonLoc[0] and
                    nextPageButtonLoc[1] + nextPageButtonSize[1] > loc[1] and loc[1] > nextPageButtonLoc[1]):
                if page < number_of_page:
                    page = page + 1

    return page

def set_background(path,window_height,display):

    background = pygame.image.load(path)

    size = background.get_rect().size
    size_scale = window_height / size[1]
    background = pygame.transform.scale(background, (int(size[0] * size_scale), int(size[1] * size_scale)))

    backgroundLoc = (0, 0)
    display.blit(background, backgroundLoc)


import pygame
import Subfunc
import CanteenInfo

canteens_location =CanteenInfo.canteens_location

pygame.init()
gameDisplay = pygame.display.set_mode([1000,700])

# pygame.display.flip()
# pygame.display.update()
gameExit = False
white=(255,255,255)
gameDisplay.fill((white))
button_color=(150,150,150)

#resize map
maps = pygame.image.load('map.jpg')
size=maps.get_rect().size
size_scale=700/size[1]
maps = pygame.transform.scale(maps, (int(size[0]*size_scale),int( size[1]*size_scale)))
mapsSize=maps.get_rect().size
mapsloc=(0,0)
map_scale= 2011.86/mapsSize[1]

# print(map_scale)
# print(mapsSize[1])

#font
font= pygame.font.SysFont("dejavusans",20)
font2= pygame.font.SysFont("dejavusans",30)
font3= pygame.font.SysFont("dejavusans",50)
font4= pygame.font.SysFont("dejavusans",80)
#start on menu page
state = 0

#initialize state variable
loc_str=""
distance=[]
map_click = 0
foodName_str=""
foodSearchResult=[]
minPrice_str = ""
maxPrice_str = ""
page = 1

while not gameExit:

    if (state == 0):
        for event in pygame.event.get():
            gameDisplay.fill((white))
            set_background("background.jpeg",700, gameDisplay)


            rankTitleText = font4.render("NTU Canteen", True, (0, 0, 0))
            gameDisplay.blit(rankTitleText, (300 , 100))



            if event.type == pygame.QUIT:
                gameExit = True
          #create Map Button
            mapButtonLoc=[700,500]
            mapButtonSize=[200,50]
            pygame.draw.rect(gameDisplay, button_color, mapButtonLoc + mapButtonSize)
            mapButtonText = font2.render("Distance", True, (0, 0, 0))
            gameDisplay.blit(mapButtonText, (mapButtonLoc[0]+10 , mapButtonLoc[1]+10))

            if event.type == pygame.MOUSEBUTTONDOWN:
                loc=pygame.mouse.get_pos()
                if (mapButtonLoc[0]+mapButtonSize[0]>loc[0] and loc[0]>mapButtonLoc[0] and mapButtonLoc[1]+mapButtonSize[1]>loc[1] and loc[1]>mapButtonLoc[1]):
                    state = 1

                    # initialize state variable
                    loc_str = ""
                    distance = []
                    map_click = 0
                    foodName_str = ""
                    foodSearchResult = []
                    minPrice_str = ""
                    maxPrice_str = ""
                    page = 1

            # create name search Button
            searcNameLoc = [100, 500]
            searcNameSize = [200, 50]
            pygame.draw.rect(gameDisplay, button_color, searcNameLoc + searcNameSize)
            searcNameText = font2.render("Search by Name", True, (0, 0, 0))
            gameDisplay.blit(searcNameText, (searcNameLoc[0] + 10, searcNameLoc[1] + 10))



            if event.type == pygame.MOUSEBUTTONDOWN:
                loc = pygame.mouse.get_pos()
                if (searcNameLoc[0] + searcNameSize[0] > loc[0] and loc[0] > searcNameLoc[0] and searcNameLoc[1] +
                    searcNameSize[1] > loc[1] and loc[1] > searcNameLoc[1]):
                    state = 2
                    # initialize state variable
                    loc_str = ""
                    distance = []
                    map_click = 0
                    foodName_str = ""
                    foodSearchResult = []
                    minPrice_str = ""
                    maxPrice_str = ""
                    page = 1

            # create price search Button
            searchPriceLoc = [100, 600]
            searchPriceSize = [200, 50]

            pygame.draw.rect(gameDisplay, button_color, searchPriceLoc + searchPriceSize)
            searchPriceText = font2.render("Search by price", True, (0, 0, 0))

            gameDisplay.blit(searchPriceText, (searchPriceLoc[0] + 10, searchPriceLoc[1] + 10))

            if event.type == pygame.MOUSEBUTTONDOWN:
                loc = pygame.mouse.get_pos()
                if (searchPriceLoc[0] + searchPriceSize[0] > loc[0] and loc[0] > searchPriceLoc[0] and searchPriceLoc[1] +
                        searchPriceSize[1] > loc[1] and loc[1] > searchPriceLoc[1]):
                    state = 3
                    # initialize state variable
                    loc_str = ""
                    distance = []
                    map_click = 0
                    foodName_str = ""
                    foodSearchResult = []
                    minPrice_str = ""
                    maxPrice_str = ""
                    page = 1

            # create rank Button
            rankLoc = [700, 600]
            rankSize = [200, 50]
            pygame.draw.rect(gameDisplay, button_color, rankLoc + rankSize)
            rankText = font2.render("Rank", True, (0, 0, 0))
            gameDisplay.blit(rankText, (rankLoc[0] + 10, rankLoc[1] + 10))

            if event.type == pygame.MOUSEBUTTONDOWN:
                loc = pygame.mouse.get_pos()
                if (rankLoc[0] + rankSize[0] > loc[0] and loc[0] > rankLoc[0] and rankLoc[1] +
                        rankSize[1] > loc[1] and loc[1] > rankLoc[1]):
                    state = 4
                    # initialize state variable
                    loc_str = ""
                    distance = []
                    map_click = 0
                    foodName_str = ""
                    foodSearchResult = []
                    minPrice_str = ""
                    maxPrice_str = ""
                    page = 1

    if (state == 1):
        for event in pygame.event.get():


            gameDisplay.fill((white))
            set_background("background.jpeg",700, gameDisplay)

            gameDisplay.blit(maps, mapsloc)

            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                loc = pygame.mouse.get_pos()
                map_click = 0
                if (mapsloc[0]+mapsSize[0]>loc[0] and loc[0]>mapsloc[0] and mapsloc[1]+mapsSize[1]>loc[1] and loc[1]>mapsloc[1]):
                    distance = Subfunc.sort_distance(loc, map_scale)
                    shortest = canteens_location[distance[0][0]]['Position']
                    map_click=1

            text = font.render(loc_str, True, (0, 0, 0))
            gameDisplay.blit(text, (700, 20))
            i=0

            for x in distance:
                distance_str=x[0]+":  "+str(int(x[1]))+"m"
                distance_text = font.render(distance_str, True, (0, 0, 0))
                gameDisplay.blit(distance_text, (700, 50+20*i))
                i=i+1

            for canteen in canteens_location:
                pygame.draw.circle(gameDisplay, (0,255,0),canteens_location[canteen]['Position'], 5)


            if (map_click == 1):
                pygame.draw.circle(gameDisplay,(255,0,0),shortest,5)

            if (map_click == 1):
                pygame.draw.circle(gameDisplay,(0,0,255),loc,5)

            homeButtonLoc = [750, 500]
            homeButtonSize = [100, 50]
            pygame.draw.rect(gameDisplay, button_color, homeButtonLoc + homeButtonSize)
            homeButtonText = font2.render("Home", True, (0, 0, 0))
            gameDisplay.blit(homeButtonText, (homeButtonLoc[0] + 10, homeButtonLoc[1] + 10))

            if event.type == pygame.MOUSEBUTTONDOWN:
                loc = pygame.mouse.get_pos()
                if (homeButtonLoc[0] + homeButtonSize[0] > loc[0] and loc[0] > homeButtonLoc[0] and homeButtonLoc[1] +
                        homeButtonSize[
                            1] > loc[1] and loc[1] > homeButtonLoc[1]):
                    state = 0
                    # initialize state variable
                    loc_str = ""
                    distance = []
                    map_click = 0
                    foodName_str = ""
                    foodSearchResult = []
                    minPrice_str = ""
                    maxPrice_str = ""
                    page = 1

    if (state == 2):
        # print(foodName_str )
        for event in pygame.event.get():


            gameDisplay.fill((white))
            set_background("background.jpeg",700, gameDisplay)



            if event.type == pygame.QUIT:
                gameExit = True

            #create input Button
            foodNameLoc=[100,100]
            foodNameSize=[300,50]

            pygame.draw.rect(gameDisplay, (255, 255, 255), foodNameLoc + foodNameSize)
            pygame.draw.rect(gameDisplay, (0, 0, 0), foodNameLoc + foodNameSize, 10)

            foodNameText = font2.render("Food Name", True, (0, 0, 0))
            gameDisplay.blit(foodNameText, (foodNameLoc[0]+10 , foodNameLoc[1]-30))

            foodName = font2.render(foodName_str, True, (0, 0, 0))
            gameDisplay.blit(foodName, (foodNameLoc[0] + 10, foodNameLoc[1] + 10))

            #textbox function
            if (event.type == pygame.MOUSEBUTTONDOWN):
                loc=pygame.mouse.get_pos()
                if (foodNameLoc[0] + foodNameSize[0] > loc[0] and loc[0] >foodNameLoc[0] and foodNameLoc[1] + foodNameSize[1] > loc[1] and loc[1] > foodNameLoc[1]):
                    gameExit,foodName_str = text_box(foodNameLoc, foodNameSize,gameDisplay)
                    foodSearchResult = Subfunc.search_by_food(foodName_str)
                    page=1


            # if event.type == pygame.KEYDOWN:
            #     print(event.key)



            # #print List
            list_position = print_list(foodSearchResult, [100, 200], gameDisplay, page)
            if event.type == pygame.MOUSEBUTTONDOWN:
                page= change_page(foodSearchResult, list_position , page)

            #homebutton
            homeButtonLoc = [750, 500]
            homeButtonSize = [100, 50]
            pygame.draw.rect(gameDisplay, button_color, homeButtonLoc + homeButtonSize)
            homeButtonText = font2.render("Home", True, (0, 0, 0))
            gameDisplay.blit(homeButtonText, (homeButtonLoc[0] + 10, homeButtonLoc[1] + 10))

            if event.type == pygame.MOUSEBUTTONDOWN:
                loc = pygame.mouse.get_pos()
                if (homeButtonLoc[0] + homeButtonSize[0] > loc[0] and loc[0] > homeButtonLoc[0] and homeButtonLoc[1] +
                        homeButtonSize[
                            1] > loc[1] and loc[1] > homeButtonLoc[1]):
                    state = 0

                    # initialize state variable
                    loc_str = ""
                    distance = []
                    map_click = 0
                    foodName_str = ""
                    foodSearchResult = []
                    minPrice_str = ""
                    maxPrice_str = ""
                    page = 1

    if (state == 3):

        for event in pygame.event.get():

            gameDisplay.fill((white))
            set_background("background.jpeg", 700, gameDisplay)

            if event.type == pygame.QUIT:
                gameExit = True

            # create input Button
            minPriceLoc = [100, 100]
            minPriceSize = [300, 50]
            pygame.draw.rect(gameDisplay, (255, 255, 255),  minPriceLoc + minPriceSize)
            pygame.draw.rect(gameDisplay, (0, 0, 0), minPriceLoc + minPriceSize, 10)
            minPriceText = font2.render("min price", True, (0, 0, 0))
            gameDisplay.blit(minPriceText, (minPriceLoc[0] + 10, minPriceLoc[1] - 30))

            # create input Button
            maxPriceLoc = [500, 100]
            maxPriceSize = [300, 50]
            pygame.draw.rect(gameDisplay, (255, 255, 255), maxPriceLoc + maxPriceSize)
            pygame.draw.rect(gameDisplay, (0, 0, 0), maxPriceLoc + maxPriceSize, 10)
            maxPriceText = font2.render("max price", True, (0, 0, 0))
            gameDisplay.blit(maxPriceText, (maxPriceLoc[0] + 10, maxPriceLoc[1] - 30))

            minPrice = font2.render(minPrice_str, True, (0, 0, 0))
            gameDisplay.blit(minPrice, (minPriceLoc[0] + 10, minPriceLoc[1] + 10))

            maxPrice = font2.render(maxPrice_str, True, (0, 0, 0))
            gameDisplay.blit(maxPrice, (maxPriceLoc[0] + 10, maxPriceLoc[1] + 10))

            # textbox function
            if (event.type == pygame.MOUSEBUTTONDOWN):
                loc = pygame.mouse.get_pos()
                if (minPriceLoc[0] + minPriceSize[0] > loc[0] and loc[0] > minPriceLoc[0] and minPriceLoc[1] + minPriceSize[ 1] > loc[1] and loc[1] > minPriceLoc[1]):
                    gameExit,  minPrice_str = text_box(minPriceLoc, minPriceSize, gameDisplay)
                    foodSearchResult = Subfunc.Search_by_price(minPrice_str,maxPrice_str)
                    page = 1



            # textbox function
            if (event.type == pygame.MOUSEBUTTONDOWN):
                loc = pygame.mouse.get_pos()
                if (maxPriceLoc[0] + maxPriceSize[0] > loc[0] and loc[0] > maxPriceLoc[0] and maxPriceLoc[1] + maxPriceSize[1] > loc[1] and loc[1] > maxPriceLoc[1]):
                    gameExit, maxPrice_str = text_box(maxPriceLoc, maxPriceSize, gameDisplay)
                    foodSearchResult = Subfunc.Search_by_price(minPrice_str, maxPrice_str)
                    page = 1


            # print List
            list_position = print_list(foodSearchResult, [100, 200], gameDisplay, page)
            if event.type == pygame.MOUSEBUTTONDOWN:
                page= change_page(foodSearchResult, list_position , page)


            # homebutton
            homeButtonLoc = [750, 500]
            homeButtonSize = [100, 50]
            pygame.draw.rect(gameDisplay, button_color, homeButtonLoc + homeButtonSize)
            homeButtonText = font2.render("Home", True, (0, 0, 0))
            gameDisplay.blit(homeButtonText, (homeButtonLoc[0] + 10, homeButtonLoc[1] + 10))

            if event.type == pygame.MOUSEBUTTONDOWN:
                loc = pygame.mouse.get_pos()
                if (homeButtonLoc[0] + homeButtonSize[0] > loc[0] and loc[0] > homeButtonLoc[0] and homeButtonLoc[1] +
                        homeButtonSize[
                            1] > loc[1] and loc[1] > homeButtonLoc[1]):
                    state = 0

                    loc_str = ""
                    distance = []
                    map_click = 0
                    foodName_str = ""
                    foodSearchResult = []
                    minPrice_str = ""
                    maxPrice_str = ""
                    page = 1

            # if event.type == pygame.KEYDOWN:
            #     print(type(event.unicode))
    if (state == 4):
        for event in pygame.event.get():
            gameDisplay.fill((white))
            set_background("background.jpeg", 700, gameDisplay)

            rankTitleText = font3.render("Canteen Rank", True, (0, 0, 0))
            gameDisplay.blit(rankTitleText, (400 , 100))

            rank_list = Subfunc.sort_by_rank()

            i=0
            for x in  rank_list:
                rank_str=x[0]+"  "+str(int(x[1]))
                rank_text = font.render(rank_str, True, (0, 0, 0))
                gameDisplay.blit(rank_text, (400, 150+20*i))
                i=i+1



            # homebutton
            homeButtonLoc = [750, 500]
            homeButtonSize = [100, 50]
            pygame.draw.rect(gameDisplay, button_color, homeButtonLoc + homeButtonSize)
            homeButtonText = font2.render("Home", True, (0, 0, 0))
            gameDisplay.blit(homeButtonText, (homeButtonLoc[0] + 10, homeButtonLoc[1] + 10))

            if event.type == pygame.MOUSEBUTTONDOWN:
                loc = pygame.mouse.get_pos()
                if (homeButtonLoc[0] + homeButtonSize[0] > loc[0] and loc[0] > homeButtonLoc[0] and homeButtonLoc[1] +
                        homeButtonSize[
                            1] > loc[1] and loc[1] > homeButtonLoc[1]):
                    state = 0

                    # initialize state variable
                    loc_str = ""
                    distance = []
                    map_click = 0
                    foodName_str = ""
                    foodSearchResult = []
                    minPrice_str = ""
                    maxPrice_str = ""
                    page = 1
            if event.type == pygame.QUIT:
                gameExit = True

    pygame.display.update()



pygame.quit()
quit()