fruit = {"mango": "yellow colour",
         "grapes": "green colour",
         "papaya": "orange colour",
         "apple": "red colour"}

print(fruit)
# print(fruit["grapes"])
# fruit["pear"] = "light green colour"
# print(fruit)
# while True:
#    dict_key = input("pls enter a fruit")
#   if dict_key == "quit":
#      break
# if dict_key in fruit:
#        description =fruit.get(dict_key)
#        print(description)
#   else:
#      print("niklo yaha se ")

# for i in range(6):
#    for snack in fruit:
#        print(snack + " is " + fruit[snack])
#    print("*" * 40)
print(fruit.items())
f_tuple = tuple(fruit.items())
print(f_tuple)
for snack in f_tuple:
    item,description = snack
    print(item + " is " + description)