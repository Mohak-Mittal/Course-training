# Step 1: Validation Function

def validate_record(record):

    required_fields = ["message_id", "customer_id", "message", "channel", "language"]

    for field in required_fields:
        if field not in record or record[field] is None or record[field] == "":
            return False
        else:
            return True