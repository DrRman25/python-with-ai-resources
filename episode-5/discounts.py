def check(code, current_total):
    if code == "SAVE10":
        t = current_total * 0.90
        print("10% off applied!")
        return t
    elif code == "SUPER20" and current_total > 100:
        t = current_total - 20
        print("$20 off applied!")
        return t
    else:
        print("No discount.")
        return current_total
