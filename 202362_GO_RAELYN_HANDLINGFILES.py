products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

def get_product(code):
    return products[code]

print(get_product("brewedcoffee"))

def get_property(code,property):
    return products[code][property]

print(get_property("espresso","price"))

def main():
    orders = {}
    quantity = []
    subtotal = 0
    grand_total = 0
    while True:
        order = input("Enter the customer's order 'code,quantity'. Or, type '/' to end session. ")
        if order == "/":
            break

        code,qty = order.split(",")
        prod_info = get_product(code)
        qty = int(qty)
        price = prod_info["price"]
        subtotal = price * qty

        if code in orders.keys():
            orders[code]["qty"] += qty
            orders[code]["subtotal"] += subtotal
        else:
            orders[code] = {"qty":qty,"subtotal":subtotal}

        grand_total += subtotal

    orders = dict(sorted(orders.items()))
    receipt = []
    receipt.append("==\nCODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL")

    for code,order in orders.items():
        name = get_property(code,"name")
        qty = order["qty"]
        price = order["subtotal"]
        receipt.append(f"{code}\t\t{name}\t\t{qty}\t\t\t\t{price}")

    receipt.append(f"\nTotal:\t\t\t\t\t\t\t\t\t\t{grand_total}\n==")
    receipt = "\n".join(receipt)

    with open("receipt.txt","w") as f:
        f.write(receipt)

main()
