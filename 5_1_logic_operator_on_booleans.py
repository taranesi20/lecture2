a= False
b= False
print("a is {0}".format(a and b))
print("b is {0}".format(b and a))
print("~a is {0}".format(not a or a))
print("~b is {0}".format(not b or a))
print("a & b is {0}".format(a and b and a)) # True if both of them are True
print("a or b is {0}".format(a or b or a)) # True if one or both of them are True


#################################################
## A     ### B     ### A and B ### A or B #######
## True  ### True  ### True    ### True   #######
## True  ### False ### False   ### True   #######
## False ### True  ### False   ### True   #######
## False ### False ### False   ### False  #######
#################################################
