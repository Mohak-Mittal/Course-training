# Step 5: Classification
def classify_message(a):
    l1 = ["order","late","delivery"]
    l2 = ["payment", "refund","money"]
    l3 = ["login","password","account"]
    l4 = ["error","bug","crash"]
    for i in l1:
        if i in a:
            return "l1"
            break
        else:
            pass
    for i in l2:
        if i in a:
            return "l2"
            break
        else:
            pass
    for i in l3:
        if i in a:
            return "l3"
            break
        else:
            pass
    for i in l4:
        if i in a:
            return "l4"
            break
        else:
            pass