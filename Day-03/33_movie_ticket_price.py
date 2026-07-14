def calculate_price(age, ticket_type):
    ticket_type = ticket_type.lower()
    
    if age < 12:
        if ticket_type == "regular":
            return 100
        elif ticket_type == "premium":
            return 150
    elif age >= 60:
        if ticket_type == "regular":
            return 150
        elif ticket_type == "premium":
            return 200
    else:  
        if ticket_type == "regular":
            return 200
        elif ticket_type == "premium":
            return 300
    
    return None


# Main program
age = int(input("Enter your age: "))
ticket_type = input("Enter ticket type (Regular/Premium): ")

price = calculate_price(age, ticket_type)

if price:
    print(f"Ticket Price: ₹{price}")
else:
    print("Invalid ticket type entered! Please choose Regular or Premium.")
