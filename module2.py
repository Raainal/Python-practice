# # import module1 as mod
# # # when u make an alias( as mod ) then u can only acces the command using the alias
# # print(mod.pi)
# # mod.square(4)
# # mod.welcome("amal","nair")

# #to import a specific function
# from module1 import pi,square
# print(pi)
# print(square(4))

# from random import *
# for i in range(10):
#     #print(random()) # random value between 1 and 0
#     #print(randint(1,10000)) # random value between 1 and 10000
#     print(uniform(1,10))

from random import *
list=["amal","rahul","ashish","asas"]
for i in range(10):
    print(choice(list)) # random value from the list

