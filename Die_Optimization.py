#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Created on Monday July 9th 2018
@author: taiwoalabi
"""

import pandas as pd
import time
import math



class Optimization_Of_Area:

	""" This class is defined for optimization of the Die-Area based on several inputs from the user included as dimensions """

	def __init__(self,Reticle_FieldX, Reticle_FieldY, Die_SizeX, Die_SizeY, Scribe_Width):
		self.Reticle_FieldX = Reticle_FieldX
		self.Reticle_FieldY = Reticle_FieldY
		self.Die_SizeX = Die_SizeX
		self.Die_SizeY = Die_SizeY
		self.Scribe_Width = Scribe_Width


	def Generate_Global_Die_Map(self):

		self.Coordinate = {"DieMap": None,"Center_Coord": None,"RIGHT_TOP_Coord": None,"LEFT_TOP_Coord": None,"BOTTOM_RIGHT_Coord": None}
		self.Area_Die = (self.Die_SizeX + (2 * self.Scribe_Width)) * (self.Die_SizeY + (2* self.Scribe_Width))


		###__Calculating the Total Number of Possible Dies Possible within the Frame defined__###
		self.Reticle_Field_Area = self.Reticle_FieldX * self.Reticle_FieldY
		self.Total_Number_Dies = round(self.Reticle_Field_Area/self.Area_Die)
		#print("The total Number of possible Dies are: {}".format(Total_Number_Dies))

		###__Placement of the Dies along or across the Reticle field frames__###

	###__Checking to see if a 3x? or a 2x?__###

		if ((self.Total_Number_Dies % 2) == 0):
			self.Die_Return = (self.Total_Number_Dies/2)
			###print("The Total Number of Possible Dies is Divisible by 2")

			###__Continuation of the code to evaluate divisibility by 4__###
			#if((self.Total_Number_Dies % 4) == 0):
				### print("The total Number of Possible Dies is also Divisible by 4")


		elif ((self.Total_Number_Dies % 3) == 0):
			self.Die_Return = self.Total_Number_Dies/3
			### print("The Total Number of Possible Dies is Divisible by 3")



		elif ((self.Total_Number_Dies % 5) == 0):
			self.Die_Return = self.Total_Number_Dies/5
			###print("The Total Number of Possible Dies is Divisible by 5")

		else:
			###print("Non-Divisible by either 2, 3, or 5")
			None


		###__Returning the Center Coordinate Depending on the number of Dies per reticle Field__###

		###__Recall X,Y 0,0 location is defined as the Bottom, left-most part of the Die__###

		if ((self.Total_Number_Dies % 2) == 0):

			if (self.Die_Return == 2):
				self.Reticle_Field_X_Center = self.Die_SizeX + self.Scribe_Width + (self.Scribe_Width/2)
				self.Reticle_Field_Y_Center = self.Die_SizeY + self.Scribe_Width +  (self.Scribe_Width/2)

				###__Extreme Top-Right Coordinate__###
				self.RIGHT_CORNER_X = 2 * self.Reticle_Field_X_Center
				self.RIGHT_CORNER_Y = 2 * self.Reticle_Field_Y_Center

				###__Extreme Top-Left Coordinate__###
				self.LEFT_CORNER_X = 0
				self.LEFT_CORNER_Y = self.RIGHT_CORNER_Y


				###__Extreme Bottom-Right Coordinate__###
				self.RIGHT_BOTTOM_X = self.RIGHT_CORNER_X
				self.RIGHT_BOTTOM_Y = 0
				###__Dies are labelled horizontally(to the right) 1,2 and then step up then horizontally (to the left) 3,4__###

				###__Other Dependencies__###
				self.Coordinate["Center_Coord"] = [str(self.Reticle_Field_X_Center) + "x" + str(self.Reticle_Field_Y_Center)]
				self.Coordinate["RIGHT_TOP_Coord"] = [str(self.RIGHT_CORNER_X) + "x" + str(self.RIGHT_CORNER_Y)]
				self.Coordinate["LEFT_TOP_Coord"] = [str(self.LEFT_CORNER_X) + "x" + str(self.LEFT_CORNER_Y)]
				self.Coordinate["BOTTOM_RIGHT_Coord"] = [str(self.RIGHT_BOTTOM_X) + "x" + str(self.RIGHT_BOTTOM_Y)]



			elif (self.Die_Return == 3):
				self.Reticle_Field_X_Center = self.Die_SizeX + self.Scribe_Width + (self.Scribe_Width/2)
				self.Reticle_Field_Y_Center = self.Die_SizeY + (2*self.Scribe_Width) + (self.Die_SizeY/2)

				###__Extreme Corner Coordinate__###
				self.RIGHT_CORNER_X = 2 * self.Reticle_Field_X_Center
				self.RIGHT_CORNER_Y = 2 * self.Reticle_Field_Y_Center

				###__Extreme Top-Left Coordinate__###
				self.LEFT_CORNER_X = 0
				self.LEFT_CORNER_Y = self.RIGHT_CORNER_Y


				###__Extreme Bottom-Right Coordinate__###
				self.RIGHT_BOTTOM_X = self.RIGHT_CORNER_X
				self.RIGHT_BOTTOM_Y = 0

				###__Other Dependencies__###
				self.Coordinate["Center_Coord"] = [str(self.Reticle_Field_X_Center) + "x" + str(self.Reticle_Field_Y_Center)] 
				self.Coordinate["RIGHT_TOP_Coord"] = [str(self.RIGHT_CORNER_X) + "x" + str(self.RIGHT_CORNER_Y)]
				self.Coordinate["LEFT_TOP_Coord"] = [str(self.LEFT_CORNER_X) + "x" + str(self.LEFT_CORNER_Y)]
				self.Coordinate["BOTTOM_RIGHT_Coord"] = [str(self.RIGHT_BOTTOM_X) + "x" + str(self.RIGHT_BOTTOM_Y)]



			elif (self.Die_Return == 4):
				self.Reticle_Field_X_Center = self.Die_SizeX + self.Scribe_Width + (self.Scribe_Width/2)
				self.Reticle_Field_Y_Center = (2* self.Die_SizeY) + (2*self.Scribe_Width) +  (self.Scribe_Width/2)       

				###__Extreme Corner Coordinate__###
				self.RIGHT_CORNER_X = 2 * self.Reticle_Field_X_Center
				self.RIGHT_CORNER_Y = 2 * self.Reticle_Field_Y_Center


				###__Extreme Top-Left Coordinate__###
				self.LEFT_CORNER_X = 0
				self.LEFT_CORNER_Y = self.RIGHT_CORNER_Y

				###__Extreme Bottom-Right Coordinate__###
				self.RIGHT_BOTTOM_X = self.RIGHT_CORNER_X
				self.RIGHT_BOTTOM_Y = 0  

				###__Other Dependencies__###
				self.Coordinate["Center_Coord"] = [str(self.Reticle_Field_X_Center) + "x" + str(self.Reticle_Field_Y_Center)]
				self.Coordinate["RIGHT_TOP_Coord"] = [str(self.RIGHT_CORNER_X) + "x" + str(self.RIGHT_CORNER_Y)]
				self.Coordinate["LEFT_TOP_Coord"] = [str(self.LEFT_CORNER_X) + "x" + str(self.LEFT_CORNER_Y)]
				self.Coordinate["BOTTOM_RIGHT_Coord"] = [str(self.RIGHT_BOTTOM_X) + "x" + str(self.RIGHT_BOTTOM_Y)]




			elif (self.Die_Return == 5):
				self.Reticle_Field_X_Center = self.Die_SizeX + self.Scribe_Width + (self.Scribe_Width/2)
				self.Reticle_Field_Y_Center = (2.5* self.Die_SizeY) + (3*self.Scribe_Width)       

				###__Extreme Corner Coordinate__###
				self.RIGHT_CORNER_X = 2 * self.Reticle_Field_X_Center
				self.RIGHT_CORNER_Y = 2 * self.Reticle_Field_Y_Center


				###__Extreme Top-Left Coordinate__###
				self.LEFT_CORNER_X = 0
				self.LEFT_CORNER_Y = self.RIGHT_CORNER_Y

				###__Extreme Bottom-Right Coordinate__###
				self.RIGHT_BOTTOM_X = self.RIGHT_CORNER_X
				self.RIGHT_BOTTOM_Y = 0  

				###__Other Dependencies__###
				self.Coordinate["Center_Coord"] = [str(self.Reticle_Field_X_Center) + "x" + str(self.Reticle_Field_Y_Center)]
				self.Coordinate["RIGHT_TOP_Coord"] = [str(self.RIGHT_CORNER_X) + "x" + str(self.RIGHT_CORNER_Y)]
				self.Coordinate["LEFT_TOP_Coord"] = [str(self.LEFT_CORNER_X) + "x" + str(self.LEFT_CORNER_Y)]
				self.Coordinate["BOTTOM_RIGHT_Coord"] = [str(self.RIGHT_BOTTOM_X) + "x" + str(self.RIGHT_BOTTOM_Y)]
				###__This ends the die-return that have a [2 x ??] valuation on the Die-quantity__### 



		elif ((self.Total_Number_Dies % 3)== 0):


			if (self.Die_Return == 2):
				self.Reticle_Field_X_Center = self.Die_SizeX + self.Scribe_Width + (self.Scribe_Width/2)
				self.Reticle_Field_Y_Center = (1.5 * self.Die_SizeY) + (2* self.Scribe_Width)

				###__Extreme Corner Coordinate__###
				self.RIGHT_CORNER_X = 2 * self.Reticle_Field_X_Center
				self.RIGHT_CORNER_Y = 2 * self.Reticle_Field_Y_Center

				###__Extreme Top-Left Coordinate__###
				self.LEFT_CORNER_X = 0
				self.LEFT_CORNER_Y = self.RIGHT_CORNER_Y

				###__Extreme Bottom-Right Coordinate__###
				self.RIGHT_BOTTOM_X = self.RIGHT_CORNER_X
				self.RIGHT_BOTTOM_Y = 0 

				###__Die Center Coordinate for each die__###
				###__Dies are labelled horizontally(to the right) 1,2 and then step up then horizontally (to the left) 3,4__###
				#Coordinate["DieMap"]= ['2 x '+ str(Die_Return)]
				self.Coordinate["Center_Coord"] = [str(self.Reticle_Field_X_Center) + "x" + str(self.Reticle_Field_Y_Center)] 
				self.Coordinate["RIGHT_TOP_Coord"] = [str(self.RIGHT_CORNER_X) + "x" + str(self.RIGHT_CORNER_Y)]
				self.Coordinate["LEFT_TOP_Coord"] = [str(self.LEFT_CORNER_X) + "x" + str(self.LEFT_CORNER_Y)]
				self.Coordinate["BOTTOM_RIGHT_Coord"] = [str(self.RIGHT_BOTTOM_X) + "x" + str(self.RIGHT_BOTTOM_Y)]


			elif (self.Die_Return == 3):
				self.Reticle_Field_X_Center = (1.5*self.Die_SizeX) + (2*self.Scribe_Width)
				self.Reticle_Field_Y_Center = (1.5*self.Die_SizeY) + (2*self.Scribe_Width)

				###__Extreme Corner Coordinate__###
				self.RIGHT_CORNER_X = 2 * self.Reticle_Field_X_Center
				self.RIGHT_CORNER_Y = 2 * self.Reticle_Field_Y_Center

				###__Extreme Top-Left Coordinate__###
				self.LEFT_CORNER_X = 0
				self.LEFT_CORNER_Y = self.RIGHT_CORNER_Y

				###__Extreme Bottom-Right Coordinate__###
				self.RIGHT_BOTTOM_X = self.RIGHT_CORNER_X
				self.RIGHT_BOTTOM_Y = 0

				###__Other Dependencies__###
				self.Coordinate["Center_Coord"] = [str(self.Reticle_Field_X_Center) + "x" + str(self.Reticle_Field_Y_Center)] 
				self.Coordinate["RIGHT_TOP_Coord"] = [str(self.RIGHT_CORNER_X) + "x" + str(self.RIGHT_CORNER_Y)]
				self.Coordinate["LEFT_TOP_Coord"] = [str(self.LEFT_CORNER_X) + "x" + str(self.LEFT_CORNER_Y)]
				self.Coordinate["BOTTOM_RIGHT_Coord"] = [str(self.RIGHT_BOTTOM_X) + "x" + str(self.RIGHT_BOTTOM_Y)]


			elif (self.Die_Return == 4):
				self.Reticle_Field_X_Center = (2*self.Die_SizeX) + (2.5*self.Scribe_Width) 
				self.Reticle_Field_Y_Center = (1.5* self.Die_SizeY) + (2*self.Scribe_Width)       

				###__Extreme Corner Coordinate__###
				self.RIGHT_CORNER_X = 2 * self.Reticle_Field_X_Center
				self.RIGHT_CORNER_Y = 2 * self.Reticle_Field_Y_Center

				###__Extreme Top-Left Coordinate__###
				self.LEFT_CORNER_X = 0
				self.LEFT_CORNER_Y = self.RIGHT_CORNER_Y

				###__Extreme Bottom-Right Coordinate__###
				self.RIGHT_BOTTOM_X = self.RIGHT_CORNER_X
				self.RIGHT_BOTTOM_Y = 0

				self.Coordinate["Center_Coord"] = [str(self.Reticle_Field_X_Center) + "x" + str(self.Reticle_Field_Y_Center)] 
				self.Coordinate["RIGHT_TOP_Coord"] = [str(self.RIGHT_CORNER_X) + "x" + str(self.RIGHT_CORNER_Y)]
				self.Coordinate["LEFT_TOP_Coord"] = [str(self.LEFT_CORNER_X) + "x" + str(self.LEFT_CORNER_Y)]
				self.Coordinate["BOTTOM_RIGHT_Coord"] = [str(self.RIGHT_BOTTOM_X) + "x" + str(self.RIGHT_BOTTOM_Y)]



		if ((self.Total_Number_Dies % 2) == 0):
			self.Coordinate["DieMap"]= ['2 x '+ str(self.Die_Return)]
			#return (print(Coordinate))
			return(self.Coordinate)
		elif ((self.Total_Number_Dies % 3) == 0):
			self.Coordinate["DieMap"]= ['3 x '+ str(self.Die_Return)]
			#return(print(Coordinate))
			return(self.Coordinate)







	def GenerateVertical_HorizontalLSTM(self, Coordinate):

		## This will generate both the Horizontal and Vertical numbers of LSTM(s) for each Row and Column ##
		self.Coordinate = Coordinate
		self.Vert = int(self.Coordinate['DieMap'][0].split('x')[0]) + 1

		###__Getting the Length Coordinate for navigation purposes__###

		self.Lengths = float(self.Coordinate['RIGHT_TOP_Coord'][0].split('x')[1])


		###__Getting the number of horizontal coordinate axes to generate__###

		self.Hori = int(float(self.Coordinate['DieMap'][0].split('x')[1])) + 1


		###__Getting the Length Coordinate on the Vertical Axis for Navigation Purposes__###

		self.LengthsZ = (float(self.Coordinate['RIGHT_TOP_Coord'][0].split('x')[0]) - (self.Vert * 0.08))/(self.Vert)

		return {"Vert#": self.Vert, "Vert_Length": self.Lengths, "Hori#": self.Hori, "Hori_Length": self.LengthsZ}




	def CreateVerticalLSTM(self, LengthValues):

		###This creates the vertical LSTM module using the Vertical and Horizontal Variables available and pre-computed from above###

		self.LengthValues = LengthValues 

		self.LengthX = float(self.LengthValues["Vert_Length"])

		###__Compare-X are numerical intCompare_X = []

		self.Compare_X = []
		self.ZZ = 0
		for self.ii in range(int(round(self.LengthX))):
			self.Compare_X.append(self.ii)
		self.Compare_X.append(self.LengthX)

		###__Find out the number of LengthX to generate__###
		self.NumberX = int(self.LengthValues["Vert#"])

		###__Instantiate that combination of X lengths__###

		self.Stored_Lengths= []
		for self.ii in range(self.NumberX):
			self.YY = "LengthX" + str(self.ii)
			self.Stored_Lengths.append(self.ii)

		self.LengthsX = {self.iii: self.Compare_X for self.iii in self.Stored_Lengths}

		###__This is to define all the X-Coordinates that needs to be optimized for Die-Placement__###



		self.Scribe_Width_Range = [self.ii/100 for self.ii in range(0,((int(self.Scribe_Width * 100)+1)),1)]

		#print(Scribe_Width_Range)

		####__Looping through a dictionary and generating a dictionary of dictionary of Lists__####
		#LengthsX = {"LengthX0": [0,1,2,3,4,5,6,7,8], "LengthX1": [0,1,2,3,4,5,6,7,8], "LengthX2": [0,1,2,3,4,5,6,7,8]}

		self.Dictionary1= {}

		self.WidthScribe = [self.ii/100 for self.ii in range(0,9,1)]
		for self.i,(self.key,self.value) in enumerate(self.LengthsX.items()):
			self.Dictionary1[self.key] = []
			for self.iii in self.value:
				self.Dictionary2 = {}
				self.Dictionary2[self.iii] =self.Scribe_Width_Range
				self.Dictionary1[self.key].append(self.Dictionary2)


		return(self.Dictionary1)    

		###__A dictionary of a list of a dictionary of a list for storing for each location the X and Y coordinate into memory
		###__This enables storing information about every inch of the scribe and removing those information and updating the
		###__information as necessary!



	def CreateHorizontalLSTM(self, LengthValues):

		##__This module creates the Horizontal LSTM Tables__##

		self.LengthValues = LengthValues
		self.LengthX = float(self.LengthValues["Hori_Length"])

		###_Compare-X are numerical intCompare_X = [] _###

		self.Compare_X = []
		self.ZZ = 0
		for self.ii in range(int(round(self.LengthX))):
			self.Compare_X.append(self.ii)
		self.Compare_X.append(self.LengthX)

		###__Find out the number of LengthX to generate__###
		self.NumberX = int(self.LengthValues["Hori#"])

		###__Instantiate that combination of X lengths__###

		self.Stored_Lengths= []
		for self.ii in range(self.NumberX):
			self.YY = "LengthX" + str(self.ii)
			self.Stored_Lengths.append(self.ii)

		self.LengthsX = {self.iii: self.Compare_X for self.iii in self.Stored_Lengths}

		###__This is to define all the X-Coordinates that needs to be optimized for Die-Placement__###



		###__This generates a Scribe Width-Range__###
		self.Scribe_Width_Range = [self.ii/100 for self.ii in range(0,((int(self.Scribe_Width * 100)+1)),1)]

		#print(Scribe_Width_Range)

		####__Looping through a dictionary and generating a dictionary of dictionary of Lists__####
		#LengthsX = {"LengthX0": [0,1,2,3,4,5,6,7,8], "LengthX1": [0,1,2,3,4,5,6,7,8], "LengthX2": [0,1,2,3,4,5,6,7,8]}

		self.Dictionary1= {}

		self.WidthScribe = [self.ii/100 for self.ii in range(0,9,1)]
		for self.i,(self.key,self.value) in enumerate(self.LengthsX.items()):
			self.Dictionary1[self.key] = []
			for self.iii in self.value:
				self.Dictionary2 = {}
				self.Dictionary2[self.iii] =self.Scribe_Width_Range
				self.Dictionary1[self.key].append(self.Dictionary2)


		return(self.Dictionary1)    

			####__A dictionary of a list of a dictionary of a list for storing for each location the X and Y coordinate into memory__####
			####__This enables storing information about every inch of the scribe and removing those information and updating the__####
			####__information as necessary!__####

	def Place_P_Cell(self, X_dim, Y_dim, Dictionary1, Collateral_Name, Scribe_Width, Scribe_Location, Stack, Start):

		self.X_dim = X_dim
		self.Y_dim = Y_dim
		self.Dictionary1 = Dictionary1
		self.Scribe_Width = Scribe_Width
		self.Stack = Stack
		self.Start = Start
		self.Scribe_Location1 = Scribe_Location
		self.End = End
		##__ This is the main brain for placing the P-Cells__##

		self.Scribe_Width_Range = [self.ii/100 for self.ii in range(0,((int(self.Scribe_Width * 100)+1)),1)]

		self.Global_Key = 0
		self.Global_Keys = 0
		self.Num_Added = []
		self.CopyList3 = []
		self.CopyList2 = []
		self.Count = 0
		self.Count1 = 0
		self.ZZ = 0
		self.ZZZ = 0
		self.Y_Dim_Real = 0
		self.Real_Golden3 = 0
		self.yy =[]
		self.X_dim_Real = X_dim
		self.Gold_X = 0
		self.Z = []
		self.DictKeys = []

		
		### -- Generating the Dictionary key values for understanding all the input keys in the Dictionary to prevent double insertion -- ###
		for self.ikk in self.Dictionary1[self.Scribe_Location1]:
			self.DictKeys.append(list(self.ikk.keys())[0])
		### -- This is the end of the identity crisis for this segment of the coding example -- ###


		###__Making Definitions for the X-Coordinate__###

		for self.key,self.value in self.Dictionary1.items():
			if(self.key == self.Scribe_Location1):
				#print(key)
				for self.ii in self.value:    #List Recall
					self.Copyii = dict(self.ii)
					#print(Copyii)
					for self.keys,self.values in self.Copyii.items():
						self.yy.append(self.keys)

		self.Z = sorted(self.yy, reverse = True)

		if (self.Stack == "False") & (self.Start == "None"):

			###__Determining starting location for X-Placement__###
			#print("yy", self.yy)
			self.Z= sorted(self.yy, reverse=True)
			#print(Z)
			for self.ij in self.Z:
				if ((int(self.ij) - self.ij) != 0):
					self.Num_Added.append(self.ij)
			#print(Num_Added)
			if (len(self.Num_Added) > 1):
				self.Gold_X = self.Num_Added[1]
			elif (len(self.Num_Added) == 1):
				self.Gold_X = self.Z[-1]


		elif(self.Stack == "True") & (self.Start == "None"):

			###__Determining starting location for the X-Placement__###
			#self.Z = sorted(self.yy, reverse=True)
			for self.uy, self.ii in enumerate(self.Z):
				self.List5 = (self.Dictionary1[self.Scribe_Location1][self.uy])[self.ii]
				if((self.List5[-1] - self.List5[0]) <= self.Y_dim):
					if((self.Z[self.uy] - self.Z[-1]) >= self.X_dim):
						self.Gold_X = self.Z[self.uy]

		elif(self.Stack == "True") & (self.Start != "None"):
			print("hahahahahaha")
			self.Gold_X = float(self.Start)


		elif(self.Stack == "True"):
			print("Edge placement hahahaha")
			self.Gold_X = max(self.DictKeys) - self.X_dim_Real


		print("This is the value of Gold_X: ", float(self.Gold_X))
		###__Gold_X is a preminum for determining the starting point for the X-placement__###



		###__Making the Definitions for the Y-Coordinate__###

		for self.key,self.value in self.Dictionary1.items():
			if(self.key == self.Scribe_Location1):
				for self.ii in self.value:
					self.Copyiii=dict(self.ii)
					for self.keys,self.values in self.Copyiii.items():
						if(self.Count == 0):
							self.Count +=1
						if((int(self.keys) - self.Gold_X) < self.X_dim):
							self.CopyList2 = self.Copyiii[self.keys]

							self.ZZ+=1
							self.Y_Dim_Real = self.Y_dim + self.CopyList2[0]
							self.Global_Key = self.key

							self.Global_Keys = self.keys




		####__The major Code that transitions between Vertical and Horizontal Stackings__####

		###__Comparing the Y-Coordinate to determine Vertical | Horizontal Stacking sequence__###
		self.Counter=0
		self.Delete = []
		if (self.Y_Dim_Real) < 0.08:
			for self.Val in self.CopyList2:
				if((self.Val-self.CopyList2[0]) <= self.Y_dim):
					self.Delete.append(self.Val)

			self.CopyList3= sorted(list(set(self.CopyList2).difference(set(self.Delete))))
			self.CopyList3 = [self.Y_Dim_Real] + self.CopyList3
			#print(CopyList3)
			#print(Dictionary1)
			for self.it,self.ik in enumerate(self.Dictionary1[self.Global_Key]):
				if (((list(self.ik.keys()))[0] >= self.Gold_X) & ((list(self.ik.keys()))[0] < (self.Gold_X + self.X_dim))):
					self.Dictionary1[self.Global_Key][self.it] = {((list(self.ik.keys()))[0]): self.CopyList3}


			self.X_dim_Real = self.Gold_X + self.X_dim
			if(self.X_dim_Real not in self.DictKeys):
				self.Dictionary1[self.Scribe_Location1].insert(self.ZZ, {self.X_dim_Real:self.CopyList3})
			elif(self.X_dim_Real in self.DictKeys) & (self.Stack == "True") & (self.Start == "None"):
				self.Dictionary1[self.Scribe_Location1].pop(self.ZZ - 1)
				self.Dictionary1[self.Scribe_Location1].insert(self.ZZ-1, {self.X_dim_Real:self.CopyList3})

			if ((self.Stack == "True") & (self.Start != "None") & (self.Counter == 0) & ((int(self.Gold_X) - self.Gold_X) !=0)):
				###__Checking that The Stack is True and The Start is Not None and The Counter is Zero__###
				for self.iit,self.iik in enumerate(self.Dictionary1[self.Global_Key]):
					if ((((list(self.iik.keys()))[0] >= self.Gold_X)) & (self.Gold_X not in self.DictKeys)):
						if (self.Counter == 0):
							self.Dictionary1[self.Scribe_Location1].insert(self.iit, {self.Gold_X:self.CopyList3})    
							self.Counter += 1
		elif (self.Y_Dim_Real >= 0.08):
			return ("The Width direction for the Scribe at this location is used-up already - Please rerun and switch to another X-location")





		return {"LSTM":self.Dictionary1, "Y_Real": self.Y_Dim_Real, "X_Real": self.X_dim_Real}




###__Running the program in the Length Direction__###
##XX= Collateral(4.368,0.0268,Dictionary1,"Taiwo", 0.08, 0, Stack = True, Start = 8.8765) 

##print(XX)








#Area_Optimization(100, 100,25,25,3)
#Area_Optimization(70, 70,25,25,3)
#Area_Optimization(60,60,25,25,3)

#Area_Optimization(73,73,25,25,3)
#Area_Optimization(74,74,25,25,3)
#Area_Optimization(85,85,25,25,3)
#Area_Optimization(87,87,25,25,3)
#Area_Optimization(92,92,25,25,3)

#Area_Optimization(27,32,7.25646,10.7881,0.08)
#ZZZ = Area_Optimization(25,28,7.25646,10.7881,0.08)
#print(ZZZ)


try:

	print("This program will calculate the optimized Die-placement and return an LSTM for both the Vertical and Hporizontal Subsections of Die-Placement")
	time.sleep(2)
	print("This is how the LSTM breaks apart the Vertical and Horizontal placements of a Die-group")

	print("----------------------------------------------")
	print("----------------------------------------------")
	print("----------------------------------------------")
	print("---                 ---                    ---")
	print("---                 ---                    ---")
	print("---                 ---                    ---")
	print("---                 ---                    ---")
	print("----------------------------------------------")
	print("----------------------------------------------")
	print("----------------------------------------------")
	print("---                 ---                    ---")
	print("---                 ---                    ---")
	print("---                 ---                    ---")
	print("---                 ---                    ---")
	print("----------------------------------------------")
	print("----------------------------------------------")
	print("----------------------------------------------")


	print("LSTM-Vertical")
	print("---                 ---                    ---")
	print("---                 ---                    ---")
	print("---                 ---                    ---")
	print("---                 ---                    ---")
	print("---                 ---                    ---")
	print("---                 ---                    ---")
	print("---                 ---                    ---")
	print("---                 ---                    ---")
	print("---                 ---                    ---")
	print("---                 ---                    ---")
	print("---                 ---                    ---")
	print("---                 ---                    ---")
	print("---                 ---                    ---")
	print("---                 ---                    ---")
	print("---                 ---                    ---")
	print("---                 ---                    ---")
	print("---                 ---                    ---")




	print("LSTM-Horizontal")
	print("   ----------------   -------------------      ")
	print("   ----------------   -------------------      ")
	print("   ----------------   -------------------      ")
	print("\n")
	print("\n")
	print("\n")
	print("\n")
	print("   ----------------   -------------------      ")
	print("   ----------------   -------------------      ")
	print("   ----------------   -------------------      ")
	print("\n")
	print("\n")
	print("\n")
	print("\n")
	print("   ----------------   -------------------      ")
	print("   ----------------   -------------------      ")
	print("   ----------------   -------------------      ")


	time.sleep(10)

	Reticle_FieldX = float(input("Please input the reticle field X-dimension:  "))
	Reticle_FieldY = float(input("Please enter the reticle field Y-dimension:  "))
	Die_SizeX = float(input("Please enter the Die-Size X-dimension:  "))
	Die_SizeY = float(input("Please enter the Die_Size Y-dimension:  "))
	Scribe_Width= float(input("Please enter the Scribe-Width:  "))

	Y = Optimization_Of_Area(Reticle_FieldX, Reticle_FieldY, Die_SizeX, Die_SizeY, Scribe_Width)
	Z = Y.Generate_Global_Die_Map()
	time.sleep(5)
	print("These is the Dictionary returned for the best possible Die(s) placement per available reticle-field area")
	print(Z)

	time.sleep(3)
	print("The optimal die arrangement is:")
	print(Z["DieMap"])

	time.sleep(3)
	print("The frame center coordinate is:")
	print(Z["Center_Coord"])


	time.sleep(3)
	print("The right-top coordinate is:")
	print(Z["RIGHT_TOP_Coord"])


	time.sleep(3)
	print("The left-top coordinate is:")
	print(Z["LEFT_TOP_Coord"])


	time.sleep(3)
	print("The bottom-right coordinate is:")
	print(Z["BOTTOM_RIGHT_Coord"])



	print("Proceeding to get the number of parameters to hold in the Vertical and Horizontal LSTMs")
	time.sleep(5)

	#This instantiates both the Vertical & Horizontal LSTM(s)
	XX = Y.GenerateVertical_HorizontalLSTM(Z)

	##--Generating and printing the LSTM for the Vertical Plane
	XXX = Y.CreateVerticalLSTM(XX)

	print("This is the resultant shape of the Vertical LSTM")
	time.sleep(3)
	print(XXX)

	##-- Generating and printing the LSTM for the Horizontal Plane
	YYY = Y.CreateHorizontalLSTM(XX)

	print("This is the resultant shape of the Horizontal LSTM")
	time.sleep(3)
	print(YYY)


	print("For placing features within the LSTMs please follow the instructions below carefully and pay attention to PLACEMENT SPECIFICATIONS")
	time.sleep(3)
	print("The input parameters to the program for accurate placement and return of next coordinate for placement are:")
	time.sleep(3)

	print(" 1) X_dim - The x-dimension of the p-cell")
	time.sleep(1)
	print(" 2) Y_dim - The y-dimension of the p-cell")
	time.sleep(1)
	print(" 3) Dictionary - An LSTM node available for effecting placement and making updates")
	time.sleep(1)
	print(" 4) Collateral Name - This is not essential npow but can be integrated later on to better accurately from Python understand specific P-Cell placements")
	time.sleep(1)
	print(" 5) Scribe Width - This per discussion should be constant at 0.08 um but if need arises for chnage this can also be an updatable parameter")
	time.sleep(1)
	print(" 6) Scribe Location - This must be provided as it indicates which Vertical(0,1,2,3....) dimension the placement must be made")
	time.sleep(1)
	print(" 7) Stack - The default value is False (Meaning that placement will follow a linear process {along a given row} If there is need to switch rows within the Scribe Width for placement please set to True")
	time.sleep(1)
	print(" 8) Start - The default value is None (Meaning that we do not care where the P-cell is placed) If we do want placement at a specific location please indicate the location's numeric value and enter in it here")



	time.sleep(1)
	#X_dim = float(input("Please input the P-cell X-dimension:"))
	#Y_dim = float(input("Please input the P-cell Y-dimension:"))
	#Dictionary = float(input("Please input the LSTM Dictionary:"))
	#Collateral = str(input("Please input the Collateral name:"))
	#Scribe_Width= float(input("Please enter the Scribe-Width:"))
	#Scribe_Location= float(input("Please enter the Scribe Location:"))
	#Stack= str(input("Please enter the Boolean True or False for the necessity of Stacking:"))
	#Start = float(input("Please insert a preferred numeric start location or leave blank"))


	Vert_Hori = str(input("Please indicate using only the symbols \"V\" or \"H\" for Vertical placement or Horizontal placement "))

	if Vert_Hori == "V":

		#Instantiate the Dictionary with XXX
		i=0
		print("This is the {}'th placement".format(i))
		time.sleep(2)
		X_dim = float(input("Please input the P-cell X-dimension: "))
		Y_dim = float(input("Please input the P-cell Y-dimension: "))
		Collateral = str(input("Please input the Collateral name: "))
		Scribe_Width= float(input("Please enter the Scribe-Width: "))
		Scribe_Location= float(input("Please enter the Scribe Location: "))
		Stack= str(input("Please enter the Boolean True or False for the necessity of Stacking: "))
		Start2 = str(input("Please insert a preferred numeric start location or enter None:  "))
		End = str(input("Please enter the End as either True or False for placement from the right of the Scribe  "))
		if str(Start2) == "None":
			Start = "None"
			print("The result of the placement using the parameters above are:")
			Finale = Y.Place_P_Cell(X_dim, Y_dim, XXX, Collateral, Scribe_Width, Scribe_Location, Stack, Start)
			print(Finale)
		else:
			Start = Start2
			print("The result of the placement using the parameters above are:")
			Finale = Y.Place_P_Cell(X_dim, Y_dim, XXX, Collateral, Scribe_Width, Scribe_Location, Stack, Start)
			print(Finale)



		

		Continue = str(input("Do you want to continue placement ? {Answer Y or N}"))
		while (Continue == "Y"):
			i+=1
			print("This is the {}'th placement".format(i))
			time.sleep(2)
			X_dim = float(input("Please input the P-cell X-dimension:  "))
			Y_dim = float(input("Please input the P-cell Y-dimension:  "))
			Collateral = str(input("Please input the Collateral name:  "))
			Scribe_Width= float(input("Please enter the Scribe-Width:  "))
			Scribe_Location= float(input("Please enter the Scribe Location:  "))
			Stack= str(input("Please enter the Boolean True or False for the necessity of Stacking:  "))
			Start2 = str(input("Please insert a preferred numeric start location or enter None:  "))
			End = str(input("Please enter the End as either True or False for placement from the right of the Scribe"))
			if str(Start2) == "None":
				Start = "None"
				print("The result of the placement using the parameters above are:  ")
				Finale2 = Y.Place_P_Cell(X_dim, Y_dim, Finale["LSTM"], Collateral, Scribe_Width, Scribe_Location, Stack, Start)
				print(Finale2)
			else:
				Start = Start2
				print("The result of the placement using the parameters above are:  ")
				Finale2 = Y.Place_P_Cell(X_dim, Y_dim, Finale["LSTM"], Collateral, Scribe_Width, Scribe_Location, Stack, Start)
				print(Finale2)

			
			#Reinitialize finale
			Finale = Finale2



	elif Vert_Hori == "H":

		#Instantiate the Dictioanry with YYY
		ii=0
		print("This is the {}'th placement".format(ii))
		time.sleep(2)
		X_dim = float(input("Please input the P-cell X-dimension:  "))
		Y_dim = float(input("Please input the P-cell Y-dimension:  "))
		Collateral = str(input("Please input the Collateral name:  "))
		Scribe_Width= float(input("Please enter the Scribe-Width:  "))
		Scribe_Location= float(input("Please enter the Scribe Location:  "))
		Stack= str(input("Please enter the Boolean True or False for the necessity of Stacking:  "))
		Start2 = str(input("Please insert a preferred numeric start location or enter None:  "))
		End = str(input("Please enter the End as either True or False for placement from the right of the Scribe:  "))
		if str(Start2) == "None":
			Start = "None"
			### Run the Code ###
			print("The result of the placement using the parameters above are:  ")
			Finale = Y.Place_P_Cell(X_dim, Y_dim, YYY, Collateral, Scribe_Width, Scribe_Location, Stack, Start)
			print(Finale)
		else:
			Start = Start2
			### Run the Code ###
			print("The result of the placement using the parameters above are:  ")
			Finale = Y.Place_P_Cell(X_dim, Y_dim, YYY, Collateral, Scribe_Width, Scribe_Location, Stack, Start)
			print(Finale)



		

		Continue = str(input("Do you want to continue placement ? {Answer Y or N}  "))

		while (Continue == "Y"):
			ii+=1
			print("This is the {}'th placement".format(ii))
			time.sleep(2)
			X_dim = float(input("Please input the P-cell X-dimension:  "))
			Y_dim = float(input("Please input the P-cell Y-dimension:  "))
			Collateral = str(input("Please input the Collateral name:  "))
			Scribe_Width= float(input("Please enter the Scribe-Width:  "))
			Scribe_Location= float(input("Please enter the Scribe Location:  "))
			Stack= str(input("Please enter the Boolean True or False for the necessity of Stacking:  "))
			Start2 = str(input("Please insert a preferred numeric start location or enter None :  "))
			End = str(input("Please enter the End as either True or False for placement from the right of the Scribe:  "))
			if str(Start2) == "None":
				Start = "None"
				### Run the code ###
				print("The result of the placement using the parameters above are:  ")
				Finale2 = Y.Place_P_Cell(X_dim, Y_dim, Finale["LSTM"], Collateral, Scribe_Width, Scribe_Location, Stack, Start)
				print(Finale2)
			else:
				Start = Start2
				### Run the code ###
				print("The result of the placement using the parameters above are:  ")
				Finale2 = Y.Place_P_Cell(X_dim, Y_dim, Finale["LSTM"], Collateral, Scribe_Width, Scribe_Location, Stack, Start)
				print(Finale2)
			
			#Reinitialize finale
			Finale = Finale2




except Exception as e:
	print("A fatal error occurred because:  " + str(e))


















