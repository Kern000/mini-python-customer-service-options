"""
x = 3
y = -10
z = 50
username = "janesmith"
password = "applepie"

print(x > 0 and y < 0 or z > 0)
print(username=="janesmith" and password=="applepie" or username=="admin")
print(username=="janesmith" or username=="admin" and password =="applepie")
print(min(x,y) > 0 and max(x,y) > z or x + y + z > 0)
print(username=="janesmith" or z == 50 and password=="rotiprata" or x < 10)
print(username=="janesmith" and z == 50 or password=="rotiprata" and x < 10)
print(username=="janesmith" and (z == 50 or password =="rotiprata") and x < 10)
"""
###

data = {
 'books':['Lord of the Rings', 'Chronicles of Narnia', 'Twilight'],
 '42':'Forty-two',
 '41':'Forty-one',
 '40':'Forty',
 'Thirty': 30,
 True:'The truth is out there',
 'is_raining': True,
 'fruits':{
   'a':'apple',
   'b':['bananas', 'blueberries', 'blackcurrant'],
   'c':['cherries', 'crab apples', 'cucumber']
 }
}

x = 4
y = 2
sunny = False

print("data['is_raining'] =>           ", data['is_raining'])
print("data['is_raining'] == sunny =>  ", (data['is_raining'] == sunny))
print("data['fruits']['a'] =>          ", data['fruits']['a'])
print("data['books'][y] =>             ", data['books'][y])
print("data['fruits']['b'][x-y] =>     ", data['fruits']['b'][x-y])
print("data[sunny == False] =>         ", data[sunny == False])
print("data['Thirty'] * y + x =>       ", data['Thirty'] * y + x)	
print("data[str(x*10+y)] =>            ", (data[str(x*10+y)]))


# adhere to style guide
# How to name functions (names are descriptive)
# How to name variables (snake case, descriptive names)
# How many characters per line of code
# Python style guide is PEP8 - only have 80 characters per line of code
# Each organization may have its own rule

# del todo_list[2]       -- Delete by index
# todo_list.remove("wash the car") -- remove by value
# for index, p in enumerate(products):
# print("Index => ", index, "product= ", p)

file_ptr = open("data.txt")
while True:
    each_line = file_ptr.readline()
    if not each_line:
        break
    print(each_line)







