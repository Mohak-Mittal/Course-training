# Step 1: Validation Function

def validate_record(record):
    # List of required fields
    required_fields = ["message_id", "customer_id", "message", "channel", "language"]

    # Check each field
    for field in required_fields:
        if field not in record or record[field] is None or record[field] == "":
            return False
        else:
            return True

# Step 2: Cleaning

def clean_message(record):
    # Variable for required data cleaning
    cleaning_data = "message"
    a = ""

    # Cleaning data in if codition
    if cleaning_data in record:
        a = record[cleaning_data].strip().lower().strip().replace("!!!","!")
        return a
    else:
        return False

# Step 3: Counting
def count_message_stats(a):
    # Vairables that are required to count data in words and characters
    Character_Count = len(a)
    word = a.split()
    Word_count = 0

    # loop to count words
    for i in word:
        if i.isalpha():
            Word_count += 1
    return Character_Count,Word_count

# Step 4: Messege checking
def detect_urgency(a):
    urgentword = ["late","urgent","help","immediately"]
    for i in urgentword:
        if i in a:
            return True
        else:
            pass

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

def extract_keywords(a):
    d_word = a.split()
    ignoring_word = ["is","the","for","!","my"]
    e_word = []
    for i in d_word:
        if i in ignoring_word:
            pass
        else:
            e_word.append(i)
    return e_word

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
