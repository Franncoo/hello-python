#message = input("Please type a message; ")
#print("Youe said '{}'".format(message))

message = input("Please type a " + 
"comma separeted list of values: ")

values = message.split(",")


print("the first two element " + 
"of your list are: {} and {}."
.format(values[0], values[1]))


