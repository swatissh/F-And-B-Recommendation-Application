


import CanteenInfo

def distance_a_b(location_of_a, location_of_b):
    dis = ((((location_of_a[0]-location_of_b[0])**2) +((location_of_a[1]-location_of_b[1])**2))**0.5)
    return dis

def sort_distance(user_location, scale, canteens_location=CanteenInfo.canteens_location ):
    distances_list = []
    for canteen in canteens_location:
        tupplePos = canteens_location[canteen]['Position']
        distances_list.append([canteen , distance_a_b(user_location, tupplePos)*scale])
    # print(distances_list)
    distances_list.sort(key=lambda x: x[1])
    return distances_list


def search_by_food(foodname, foodlist_canteens=CanteenInfo.foodlist_canteens):
    list_canteens = []
    for canteen in foodlist_canteens:
        for stall in foodlist_canteens[canteen]:
            # python2.7 has_key(); python3 key in dict
            for food in foodlist_canteens[canteen][stall]:
                if foodname.lower().replace(" ", "") in food.lower().replace(" ", ""):
                    list_canteens.append([canteen, stall, food, foodlist_canteens[canteen][stall][food]])

    list_canteens.sort(key=lambda x: x[3])
    return list_canteens

def Search_by_price(minprice,maxprice, foodlist_canteens = CanteenInfo.foodlist_canteens):
    list_canteens = []
    if (minprice == ""):
        minprice = "0"

    try:
        if (maxprice==""):
            minprice = float(minprice)
            for canteen in foodlist_canteens:
                for stall in foodlist_canteens[canteen]:
                    for foodname in foodlist_canteens[canteen][stall]:
                        if (foodlist_canteens[canteen][stall][foodname] >= minprice):
                            list_canteens.append([canteen, stall, foodname, foodlist_canteens[canteen][stall][foodname]])
        else:
            minprice = float(minprice)
            maxprice = float(maxprice)
            for canteen in foodlist_canteens:
                for stall in foodlist_canteens[canteen]:
                    for foodname in foodlist_canteens[canteen][stall]:
                        if foodlist_canteens[canteen][stall][foodname] >= minprice and foodlist_canteens[canteen][stall][foodname] <= maxprice:
                            list_canteens.append([canteen, stall, foodname,foodlist_canteens[canteen][stall][foodname]])
    except:

        list_canteens.append(["value error","", "", "0"])

    list_canteens.sort(key=lambda x: x[3])
    return list_canteens

def sort_by_rank(ranklist_canteens = CanteenInfo.canteens_location):
    ranks_list = []
    for canteen in ranklist_canteens:
        rank = ranklist_canteens[canteen]['Rank']
        ranks_list.append([canteen, rank])

    ranks_list.sort(key=lambda x: x[1])

    return ranks_list
