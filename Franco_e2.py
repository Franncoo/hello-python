import sys
#print("Input Sustained Winds:", sys.argv[1]

#print("ads")
x = sys.argv[1]
x = int(sys.argv[1])


if  x >= 220:
    print ("Category:Super Typhoon")
elif x >= 118 or x == 220:
    print ("Category:Typhoon")
elif x >= 89 or x >= 117:
    print ("Category:Severve Tropical Strom")
elif x >= 62 or x >= 88:
    print ("Category:Tropical Strom")
elif x <= 61:
    print ("Category:Tropical Despression")

