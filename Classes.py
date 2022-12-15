import copy
def initialize_nested_list(num_rows, num_cols):
    empty_tab = []
    for r in range(num_rows):
        empty_tab.append([])

    for f in range(len(empty_tab)):
        for r in range(num_cols):
            empty_tab[f].append(0)

    return empty_tab


class Room:

    def __init__(self, floor=1, room=1, water=0, electric=0, status="available", cost=4000):
        self.__floor = floor
        self.__room = room
        self.__status = status
        self.__electric = electric
        self.__water = water
        self.cost = cost

    @property
    def floor(self):
        return self.__floor

    @property
    def room(self):
        return self.__room

    @property
    def electric(self):
        return self.__electric

    @electric.setter
    def electric(self, new_e):
        self.__electric = new_e

    @property
    def water(self):
        return self.__water

    @water.setter
    def water(self, new_w):
        self.__water = new_w

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self,new_stat):
        self.__status = new_stat


class Customer:
    def __init__(self, name="", floor=1, room=1, others={"discount": -0, "penalty": +0, "others(example)": 0}):
        self.__name = name
        self.__floor = floor
        self.__room = room
        self.__other = others

    def __repr__(self):
        return f"customer's name : {self.name} room : {self.floor}0{self.room}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_nm):
        if not isinstance(new_nm, str):
            raise TypeError("name must be alphabets")

        self.__name = new_nm

    @property
    def floor(self):
        return self.__floor

    @property
    def room(self):
        return self.__room

    @property
    def other(self):
        if not isinstance(self.__other, dict):
            raise TypeError("promotion must be a dictionary")
        return self.__other

    @other.setter
    def other(self, new):
        if not isinstance(self.__other, dict):
            raise TypeError("promotion must be a dictionary")
        self.__other = new


class Bill:
    """initialize """

    def __init__(self, floor_size, room_size, rooms=[], customers=[], ):
        self.fs = floor_size
        self.rs = room_size
        self.__rooms = rooms
        self.__customers = customers
        for room in range(len(self.rooms)):
            self.rooms[room].status = "unavailable"

    @property
    def rooms(self):
        if not isinstance(self.__rooms, list):
            raise TypeError("rooms must be a list")
        for room in self.__rooms:
            if not isinstance(room, Room):
                raise TypeError("Must be room")

        return self.__rooms

    @rooms.setter
    def rooms(self, n_rooms):
        if not isinstance(n_rooms, list):
            raise TypeError("rooms must be a list")
        for room in n_rooms:
            if not isinstance(room, Room):
                raise TypeError("Must be room")
        self.__rooms = n_rooms

    @property
    def customers(self):
        if not isinstance(self.__customers, list):
            raise TypeError("customers must be a list")
        for c in self.__customers:
            if not isinstance(c, Customer):
                raise TypeError("Must be customer")

        return self.__customers

    @customers.setter
    def customers(self, n_cus):
        if not isinstance(n_cus, list):
            raise TypeError("customers must be a list")
        for c in n_cus:
            if not isinstance(c, Customer):
                raise TypeError("Must be customer")

    def get_calculated_costs(self, previous_bill):
        blank_nested = initialize_nested_list(self.fs, self.rs)
        water_tab = copy.deepcopy(blank_nested)
        elec_tab = copy.deepcopy(blank_nested)
        total_tab = copy.deepcopy(blank_nested)
        roomc_tab = copy.deepcopy(blank_nested)
        """ Apparently , according to the law you have to charge people water and electric cost
        for 18 and 8 Baht per unit accordingly"""
        for room in range(len(self.rooms)):
            water_cost = (self.rooms[room].water - previous_bill.rooms[room].water) * 18
            elec_cost = (self.rooms[room].electric - previous_bill.rooms[room].electric) * 8
            roomcost = self.rooms[room].cost
            room_total = water_cost + elec_cost + roomcost
            water_tab[self.rooms[room].floor - 1][self.rooms[room].room - 1] = water_cost
            elec_tab[self.rooms[room].floor - 1][self.rooms[room].room - 1] = elec_cost
            roomc_tab[self.rooms[room].floor - 1][self.rooms[room].room - 1] = roomcost
            total_tab[self.rooms[room].floor - 1][self.rooms[room].room - 1] = room_total

        return water_tab, elec_tab, roomc_tab, total_tab

    def get_name_table(self):
        name_tab = initialize_nested_list(self.fs, self.rs)
        for r in range(len(self.rooms)):
            if self.rooms[r].status == "available":
                name_tab[self.rooms[r].floor - 1][self.rooms[r].room - 1] = "available"
            else:
                name_tab[self.rooms[r].floor - 1][self.rooms[r].room - 1] = self.customers[r].name

        return name_tab

    def add_customer(self, floor, room, name, cost, waterc, elecc):
        self.customers.append(Customer(name, floor, room))
        self.rooms.append(Room(floor, room, waterc, elecc, "unavailable", cost))

    def remove_customer(self, name):
        fl = 1
        rm = 1
        for c in self.customers:
            if c.name == name:
                fl = c.floor
                rm = c.room
                self.customers.remove(c)

        for r in self.rooms:
            if r.floor == fl and r.room == rm:
                self.rooms.remove(r)

    def remove_all(self):
        for c in self.customers:
            self.customers.remove(c)

        for r in self.rooms:
            self.rooms.remove(r)


class Vector:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        if not isinstance(self.__x, (int, float)):
            raise TypeError("Must be a number")
        return self.__x

    @x.setter
    def x(self, newx):
        if not isinstance(newx, (int, float)):
            raise TypeError("Must be a number")

        self.__x = newx

    @property
    def y(self):
        if not isinstance(self.__y, (int, float)):
            raise TypeError("Must be a number")
        return self.__y

    @y.setter
    def y(self, newy):
        if not isinstance(newy, (int, float)):
            raise TypeError("Must be a number")
        self.__y = newy
