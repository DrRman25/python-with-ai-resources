import database

# A messy, unorganized order processor with global scope mistakes
TAX_RATE = 0.10

def process(item_id, qty):
    # Feature 2 targets this file for refactoring
    item = database.inventory.get(item_id)
    if item != None:
        if item["stock"] >= qty:
            # Logic calculation floating around out in the open
            cost = item["price"] * qty
            tax = cost * TAX_RATE
            total = cost + tax
            
            # Direct database manipulation without helper functions
            database.inventory[item_id]["stock"] = item["stock"] - qty
            
            print("ORDER SUCCESSFUL")
            return total
        else:
            print("Out of stock")
            return 0
    else:
        print("Item completely missing!")
        return 0
