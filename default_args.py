
import time
#DEFAULT ARG, AFTER POSSIOTIONAL ARG
def count(end, start = 0):
    for x in range(start, end +1):
        print(x)
        time.sleep(1)
    print("done")
count(30)





def net_price(list_price, discount =0, tax = 0.05):
     #default arg
     #default arg
    return list_price * (1 - discount) * (1 + tax)


print(net_price(500))