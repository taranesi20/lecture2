####################################
# following variables are the same #
####################################
 str1=" salam! "
 str2='salam!'

######################
## concat two string #
######################
 name='tarane'
 family='andalib'
 greeting= str1+name+family
 print(greeting)

 greeting2=str1+" "+name+" "+famliy
 print(greeting2)

 print(("\'"+greeting2+" \'") * 5)
######################################
## some useful operations on strings #
######################################
 print(greeting2.capitalize())
 print(greeting2.upper())
 print(greeting2.rsplit(' ')) # splitting the string by blank
 print(greeting2.strip(' ')) # remove the blanks before and after the string

###########################################
### another sample of printing a varibale #
###########################################
a = 256.652
print(a)
str_a = str(a)
print("a number is : ", a)  # print each part of input separately
print("a number is : " + str(a))  # concat two string
