from  Classes import  Room , Bill , Customer

floors = 5
room = 4
init_txt = "9_2022.txt"
new_txt = "10_2022.txt"

def initialize_nested_list(num_rows, num_cols):
    list1 = []
    list2 = []

    for i in range(num_rows):
        list2.append(list1)

    return list2

def operate(init_txt):
    floors = 5
    room = 4
    init_txt = "9_2022.txt"
    new_txt = "10_2022.txt"

    init_lines = open(init_txt).read().splitlines()
    new_lines = open(new_txt).read().splitlines()
    init_table = [x.split(",") for x in init_lines if x != ""]
    new_table = [x.split(",") for x in new_lines if x != ""]
    inted_init = []
    inted_new = []

    for row in init_table:
        _list = []
        for num in row:
            _list.append(int(num))
        inted_init.append(_list)

    for row in new_table:
        _list = []
        for num in row:
            _list.append(int(num))
        inted_new.append(_list)

    apartment = initialize_nested_list(floors, room)

    for floor in apartment:
        for room in floor:
            room.append(inted_init[0])

    print(inted_init)
    print(inted_new)
    print(apartment)


# meth = input("1.set size: \n 2.set text: \n 3. exit")
while True:
    print("Please insert text file in Rent_Calculator folder")
    init_txt = input("enter initial month text name(mm_yyyy.txt): ")
    new_txt = input("enter current month text name(mm_yyyy.txt): ")
    meth = int(input("1.set size: \n2.change data: \n3.show \n0.exit \nenter choice: "))
    if meth == 0:
        break

    if meth == 1:
        floors = int(input("how many floors?: "))
        room = int(input("how many rooms per floor?: "))
    elif meth == 2:
        print("Please insert text file in Rent_Calculator folder")
        initmon_yr = input("enter initial month text name(month_year ex. 11_21): ")
        newmon_yr = input("enter current month text name(month_year ex. 12_21): ")
        init_txt = f""


    elif meth == 3:
        operate(init_txt,new_txt)

    else:
        print("incorrect answer try again")

print("closed")
