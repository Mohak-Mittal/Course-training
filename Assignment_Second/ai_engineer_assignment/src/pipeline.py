from src.validation import validate_record
from src.preprocessing import clean_message, count_message_stats, detect_urgency, extract_keywords
from src.classification import classify_message

def create_standard_record(record):
    if validate_record(record) is True:
        print("Valid Inputs")
        print("Old messege is :-",record["message"])
        a = clean_message(record)
        print ("New messege is :-",a)
        b,c = count_message_stats(clean_message(record))
        print("Character Count ",b, "\nWord Count ", c)
        if detect_urgency(a) is True:
            print ("is_urgent : True")
        else:
            print ("is_urgent : False")
        d = classify_message(a)
        if d == "l1":
            print("Order Problem\n")
        elif d == "l2":
            print("Payent Problem\n")
        elif d == "l3":
            print("Accounnt Problem\n")
        elif d == "l4":
            print("Technical Problem\n")
        else:
            print("Generar Inqurie")
        e = extract_keywords(a)
        print("Keywords Are :-",e)
    else:
        print("Invalid Input")
    print()
    print()


def process_batch(records):
    for record in records:
        create_standard_record(record)


# Example record (like a row of data)
records = [
    {"message_id": "M001", "customer_id": "C101", "message": "My order is late !!!", "channel": "web", "language": "English"},
    {"message_id": "M002", "customer_id": "C102", "message": "Refund not received", "channel": "mobile", "language": "English"},
    {"message_id": "M003", "customer_id": "C103", "message": "Login error, cannot access account", "channel": "web", "language": "English"},
    {"message_id": "M004", "customer_id": "C104", "message": "App keeps crashing when I open it", "channel": "mobile", "language": "English"},
    {"message_id": "M005", "customer_id": "C105", "message": "Thank you for the support", "channel": "web", "language": "English"}
]
# Check if record is valid
process_batch(records)