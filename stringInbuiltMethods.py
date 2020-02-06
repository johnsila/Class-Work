x="hello mercy"
y="HELLO"
#(len(),lower(),upper(), capitalize())
#count x characters
print ("1.",len(x))

#rewrite y in lower case
print ("2.",y.lower())

#rewrite x in upper case
print ("3.",x.upper())

#capitolize 1st character of x sytring
print ("4.",x.capitalize())

#find()-finds the first occurrence of the specified value.
z="hi, how are you?"
q=z.find("are")
print("5.",q)

#center()  center align the string, using a specified character (space is default) as the fill character.
m=z.center(50)
print("6.",m)

#endswith()method returns True if the string ends with the specified value, otherwise False.
c=z.endswith("?")
print("7.",c)

#replace()
d=z.replace("hi","hey")
print('8.',d)
