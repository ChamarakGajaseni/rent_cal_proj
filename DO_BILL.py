from  Classes import  Room , Bill , Customer


def get_bills(init_txt,new_txt,floors,rooms):

    init_lines = open(init_txt).read().splitlines()
    new_lines = open(new_txt).read().splitlines()
    init_table = [x.split(",") for x in init_lines if x != ""]
    new_table = [x.split(",") for x in new_lines if x != ""]
    inted_init = []
    inted_new = []

    for row in init_table:
        _list = []
        for num in range(len(row)-1):
            _list.append(int(row[num]))
        _list.append(row[5])
        inted_init.append(_list)

    for row in new_table:
        _list = []
        for num in range(len(row)-1):
            _list.append(int(row[num]))
        _list.append(row[5])
        inted_new.append(_list)

    currooms = []
    prerooms = []
    curcustoms = []
    precustoms = []

    for room in range(len(inted_init)):
        curroom = Room(inted_new[room][0],inted_new[room][1],inted_new[room][2],inted_new[room][3],"unavailable",inted_new[room][4])
        preroom = Room(inted_init[room][0],inted_init[room][1],inted_init[room][2],inted_init[room][3],"unavailable",inted_init[room][4])
        curcustomer = Customer(inted_new[room][5],inted_new[room][0],inted_new[room][1])
        precustomer = Customer(inted_new[room][5],inted_new[room][0],inted_new[room][1])
        currooms.append(curroom)
        prerooms.append(preroom)
        curcustoms.append(curcustomer)
        precustoms.append(precustomer)

    curbill = Bill(floors,rooms,currooms,curcustoms)
    prebill = Bill(floors,rooms,prerooms,precustoms)

    return curbill,prebill

def draw_table(table,cell_height,cell_width):
    print('|', end = '')
    for j in range(cell_width+1):
        print('-'*9 + '|', end = '')
    print()
    print('|'+' '*9, end='|')
    for j in range(cell_width):
        print(f'{j+1:^9}|', end='')
    print()
    print('|', end = '')
    for j in range(cell_width+1):
        print('-'*9 + '|', end = '')
    print()

    for j in range(cell_height):
        print('|', end='')
        print(f'{j + 1:^9}',end = '')
        print('|',end='')
        for k in range(cell_width):
            if table[j][k] == 0:
                x = " "*9
            else:
                x = table[j][k]
            print(f'{x:^9}|' , end = '')
        print()
        print('|',end='')
        for k in range(cell_width+1):
            print('-' * 9 + '|', end='')
        print()


print("Please insert text file in Rent_Calculator folder")
print("")
nmon, nyr = int(input("Enter billing month(answer in number ex. 12): ")), int(input("year (answer in number ex. 2021): "))
init_txt = f"{nmon - 1}_{nyr}.txt"
new_txt = f"{nmon}_{nyr}.txt"
floors = int(input("How many floors? : "))
rooms = int(input("How many rooms? : "))
curbill,prebill = get_bills(init_txt,new_txt,floors,rooms)
water_tab,elec_tab,roomc_tab,total_tab = curbill.get_calculated_costs(prebill)
custable = curbill.get_name_table()
print("")

"""an attempt to do turtle graphic was made (it only works for 3th and 4th function)"""
# import turtle
# t = turtle.Turtle()
# screen = turtle.Screen()
# t.penup()
# t.hideturtle()
# def operate(x,y):
#     meth = 0
#     t.goto(x, y)
#     if -84 < x <= 84 and -267 < y <= -110:
#         screen.bye()
#
#     # elif -322 < x <= -155 and 118 < y <= 272:
#     #     meth = 1
#     #     floors = screen.numinput("set floor","How many floors? ")
#     #     rooms = screen.numinput("set floor","How many rooms? ")
#     #     curbill, prebill = get_bills(init_txt, new_txt, floors, rooms)
#     #     water_tab, elec_tab, roomc_tab, total_tab = curbill.get_calculated_costs(prebill)
#     #     custable = curbill.get_name_table()
#     #
#     # elif -84 < x <= 84 and 118 < y <= 272:
#     #     meth = 2
#     #     print("Please insert text file in Rent_Calculator folder")
#     #     nmon, nyr = int(input("Enter billing month(number only ex. 12): ")), int(input("year (number ex. 2021): "))
#     #     init_txt = f"{nmon - 1}_{nyr}.txt"
#     #     new_txt = f"{nmon}_{nyr}.txt"
#     #     curbill, prebill = get_bills(init_txt, new_txt, floors, rooms)
#     #     water_tab, elec_tab, roomc_tab, total_tab = curbill.get_calculated_costs(prebill)
#     #     custable = curbill.get_name_table()
#
#     elif -322 < x <= -155 and -76 < y <= 80:
#         meth = 3
#         draw_table(total_tab, floors, rooms)
#
#     elif -84 < x <= 84 and -76 < y <= 80:
#         meth = 4
#         draw_table(custable, floors, rooms)
#
#     # elif 155 < x <= 323 and 118 < y <= 272:
#     #     meth = 5
#     #     rfloor = int(input("What floor? : ")) - 1
#     #     rroom = int(input("What room? : ")) - 1
#     #     print(f"Customer name : {custable[rfloor][rroom]}")
#     #     print(f"Electric cost = {water_tab[rfloor][rroom]}")
#     #     print(f"Electric cost = {elec_tab[rfloor][rroom]}")
#     #     print(f"Room cost =  {roomc_tab[rfloor][rroom]}")
#     #     print(f"Total cost = {total_tab[rfloor][rroom]}")
#     #
#     # elif 155 < x <= 323 and -76 < y <= 79:
#     #     meth = 6
#     #     name = input("What's customer's name? : ")
#     #     rfloor = int(input("What floor? : "))
#     #     rroom = int(input("What room? : "))
#     #     cost = int(input("Room cost? : "))
#     #     initwater = int(input("init water? : "))
#     #     initelec = int(input("init electric? : "))
#     #     water = int(input("current water? : "))
#     #     elec = int(input("current electric? : "))
#     #     curbill.add_customer(rfloor, rroom, name, cost, water, elec)
#     #     prebill.add_customer(rfloor, rroom, name, cost, initwater, initelec)
#     #     print(f"Added {name}")
#     #     water_tab, elec_tab, roomc_tab, total_tab = curbill.get_calculated_costs(prebill)
#     #     custable = curbill.get_name_table()
#     #
#     # elif 155 < x <= 323 and -267 < y <= -110:
#     #     meth = 7
#     #     name = input("What's customer's name? : ")
#     #     curbill.remove_customer(name)
#     #     prebill.remove_customer(name)
#     #     print(f"Removed {name}")
#     #     water_tab, elec_tab, roomc_tab, total_tab = curbill.get_calculated_costs(prebill)
#     #     custable = curbill.get_name_table()
#     #
#     # elif -322 < x <= -155 and -267 < y <= -110:
#     #     meth = 8
#     #     for i in range(floors):
#     #         curbill.remove_all()
#     #         prebill.remove_all()
#     #
#     #     water_tab, elec_tab, roomc_tab, total_tab = curbill.get_calculated_costs(prebill)
#     #     custable = curbill.get_name_table()
#     #
#     # return init_txt,new_txt,floors,rooms,curbill,prebill,water_tab,elec_tab,roomc_tab,total_tab,custable
#
# screen.setup(width=841,height=593)
# screen.bgpic("main_menu.png")
# turtle.onscreenclick(operate)
# screen.mainloop()

while True:
    meth = int(input("1.change size \n2.change datas \n3.show all room rent \n4.show all customer \n5.show specific room detail \n6.add customer manually\n7.remove customer manually\n8.remove all customer \n0.exit \nenter choice: "))
    if meth == 0:
        break
    elif meth == 1:
        floors = int(input("How many floors?: "))
        rooms = int(input("How many rooms?: "))
        curbill, prebill = get_bills(init_txt, new_txt, floors, rooms)
        water_tab, elec_tab, roomc_tab, total_tab = curbill.get_calculated_costs(prebill)
        custable = curbill.get_name_table()

    elif meth == 2:
        print("Please insert text file in Rent_Calculator folder")
        nmon, nyr = int(input("Enter billing month(number only ex. 12): ")), int(input("year (number ex. 2021): "))
        init_txt = f"{nmon - 1}_{nyr}.txt"
        new_txt = f"{nmon}_{nyr}.txt"
        curbill, prebill = get_bills(init_txt, new_txt, floors, rooms)
        water_tab, elec_tab, roomc_tab, total_tab = curbill.get_calculated_costs(prebill)
        custable = curbill.get_name_table()

    elif meth == 3:
        draw_table(total_tab,floors,rooms)
    elif meth == 4:
        draw_table(custable,floors,rooms)
    elif meth == 5:
        rfloor = int(input("What floor? : "))-1
        rroom = int(input("What room? : "))-1
        print(f"Customer name : {custable[rfloor][rroom]}")
        print(f"Electric cost = {water_tab[rfloor][rroom]}")
        print(f"Electric cost = {elec_tab[rfloor][rroom]}")
        print(f"Room cost =  {roomc_tab[rfloor][rroom]}")
        print(f"Total cost = {total_tab[rfloor][rroom]}")

    elif meth == 6:
        name = input("What's customer's name? : ")
        rfloor = int(input("What floor? : "))
        rroom = int(input("What room? : "))
        cost = int(input("Room cost? : "))
        initwater = int(input("init water? : "))
        initelec = int(input("init electric? : "))
        water = int(input("current water? : "))
        elec = int(input("current electric? : "))
        curbill.add_customer(rfloor,rroom,name,cost,water,elec)
        prebill.add_customer(rfloor,rroom,name,cost,initwater,initelec)
        print(f"Added {name}")
        water_tab, elec_tab, roomc_tab, total_tab = curbill.get_calculated_costs(prebill)
        custable = curbill.get_name_table()

    elif meth == 7:
        name = input("What's customer's name? : ")
        curbill.remove_customer(name)
        prebill.remove_customer(name)
        print(f"Removed {name}")
        water_tab, elec_tab, roomc_tab, total_tab = curbill.get_calculated_costs(prebill)
        custable = curbill.get_name_table()

    elif meth == 8:
        for i in range(floors):
            curbill.remove_all()
            prebill.remove_all()

        water_tab, elec_tab, roomc_tab, total_tab = curbill.get_calculated_costs(prebill)
        custable = curbill.get_name_table()

    else:
        print("incorrect answer try again")
    print("")



print("\nclosed")
