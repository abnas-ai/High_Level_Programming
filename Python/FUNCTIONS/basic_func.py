
def sum_num(a, b):
    return a + b

 
results = sum_num(3, 5)
results2 = sum_num(17, 12)
# print(results)
# print(results2)

#price of an item
def cart(item, price,quantity=""):
    print(f"{quantity} {item} cost: Ksh. {price:.2f}")
# cart(5, "sugar", 540)
# cart(2, 20, "banana")


#********keyword arguments********
# cart(price=200, quantity=2,  item="banana")

# 

def cost(qty, price, item):
    print(f"{qty}kg {item} is Ksh.{qty*price:.2f}")
    
cost(4, 100, "sugar")
