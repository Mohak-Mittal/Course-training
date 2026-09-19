# Step 2: Cleaning

def clean_message(record):

    cleaning_data = "message"
    a = ""

    if cleaning_data in record:
        a = record[cleaning_data].strip().lower().strip().replace("!!!","!")
        return a
    else:
        return False

# Step 3: Counting

def count_message_stats(a):

    Character_Count = len(a)
    word = a.split()
    Word_count = 0

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
            break
        else:
            pass

# Step 6: Extract Keywords
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