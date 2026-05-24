import database

TAX_RATE = 0.10

def process(item_id, qty):
    item = database.inventory.get(item_id)
    if item != None:
        if item["stock"] >= qty:
            cost = item["price"] * qty
            tax = cost * TAX_RATE
            total = cost + tax
            
            database.inventory[item_id]["stock"] = item["stock"] - qty
            
            print("ORDER SUCCESSFUL")
            return total
        else:
            print("Out of stock")
            return 0
    else:
        print("Item completely missing!")
        return 0
