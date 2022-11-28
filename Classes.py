class Bill:

	"""initialize """
	# def  __init__(self, electric = 0 , water = 0  , room = Room() , customer = Customer()):




# class Room:
# 	def  __init__(self, floor = 1 , room  = 1, name =  "name" , status = "unbooked"):

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

	# @property
	# def penalty(self):


