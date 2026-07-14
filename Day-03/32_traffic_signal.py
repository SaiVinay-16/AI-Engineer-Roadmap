signal = input("Enter traffic signal color (Red/Yellow/Green): ").strip().lower()

if signal == "red":
    print("Stop")
elif signal == "yellow":
    print("Wait")
elif signal == "green":
    print("Go")
else:
    print("Invalid input! Please enter Red, Yellow, or Green.")