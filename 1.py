x = int(input())
print("%5.0f" % x)
print("{0:5.0f}".format(x))
print(f"{x:5.0f}")

a_float_1 = float(input())
print("%11f" % a_float_1)
print("{0:11f}".format(a_float_1))
print(f"{a_float_1:11f}")

b_float_2 = float(input())
print("%7.4f" % b_float_2)
print("{0:7.4f}".format(b_float_2))
print(f"{b_float_2:7.4f}")

str = input()
print("{0:.5}".format(str))
print(f"{str:.5}") 

bb = 1 < 0
#bb = False - или так
print(bb)