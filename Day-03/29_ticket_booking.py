prices = {
    "child": 100,
    "adult": 200,
    "senior": 150
}

child_tickets = int(input("Enter number of Child tickets: "))
adult_tickets = int(input("Enter number of Adult tickets: "))
senior_tickets = int(input("Enter number of Senior Citizen tickets: "))

total = (child_tickets * prices["child"] +
         adult_tickets * prices["adult"] +
         senior_tickets * prices["senior"])

print("\n--- Ticket Booking Summary ---")
print(f"Child Tickets: {child_tickets} × ₹{prices['child']} = ₹{child_tickets * prices['child']}")
print(f"Adult Tickets: {adult_tickets} × ₹{prices['adult']} = ₹{adult_tickets * prices['adult']}")
print(f"Senior Tickets: {senior_tickets} × ₹{prices['senior']} = ₹{senior_tickets * prices['senior']}")
print("Total Amount: ₹", total)
