def initialize_int_nested_list(num_floor, num_room):

    dict_ = {}
    result = []
    for num in range(num_floor):
        dict_[f'col{num+1}'] = num_room

    for item in dict_:
        list_ = []
        for num in range(dict_[item]):
            list_.append(0)
        result.append(list_)

    return  result
class Room:
	def  __init__(self, floor = 1 , room  = 1, customer = "name" , status = "available"):
		self.__floor = floor
		self.__room = room
		self.__status = status
		self.__customer = customer

	@property
	def floor(self):
		return  self.__floor

	@property
	def room(self):
		return  self.__room

	@property
	def status(self):
		return  self.__status
	@property
	def customer(self):
		return  self.__customer



class Customer:
	def  __init__(self,  name = "name" , promotion = {"discount":0} , penalty = {"late" : 0 }, others = {"do_meth" : ["notes", 0]}):
		self.__name = name
		self.__promotion = promotion
		self.__penalty = penalty
		self.__other = others

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self,new_nm):
		if not isinstance(new_nm,str):
			raise TypeError("name must be alphabets")

		self.__name = new_nm

	@property
	def promotion(self):
		if not isinstance(self.__promotion , dict):
			raise TypeError("promotion must be a dictionary")
		return self.__promotion

	@promotion.setter
	def promotion(self, new_pro):
		if not isinstance(self.__promotion , dict):
			raise TypeError("promotion must be a dictionary")
		self.__promotion = new_pro

	@property
	def penalty(self):
		if not isinstance(self.__penalty,dict):
			raise  TypeError("Penalty must be a dictionary")
		return  self.__penalty

	@penalty.setter
	def penalty(self,new_p):
		if isinstance(new_p,dict):
			raise  TypeError("Penalty must be a dictionary")

		self.__penalty = new_p

class Bill:

	"""initialize """
	def  __init__(self, electric = 0 , water = 0  , room = Room() , customer = Customer()):
		self.__electric = electric
		self.__water = water
		self.__room = room
		self.__customer = customer

	@property
	def room(self):
		return  self.__room

	@property
	def customer(self):
		return  self.__customer

	@property
	def electric(self):
		return  self.__electric

	@electric.setter
	def electric(self,new_e):
		self.__electric = new_e

	@property
	def water(self):
		return  self.__water

	@water.setter
	def water(self, new_w):
		self.__water = new_w
	def calculate_costs(self,num_floor, num_room):
		"""the highest floor is 5 which has the cheapest room
		   cost of 4000 Baht. further more if room number is 3
		   or 4 they will cost 100 Baht less
		"""
		elec_cost = self.electric * 8
		water_cost = self .water * 18
		room_cost = 4000 + (5-num_floor)*100
		if num_room == 3 or num_room == 4:
			room_cost -= 100
		else:
			pass

		return elec_cost,water_cost,room_cost



