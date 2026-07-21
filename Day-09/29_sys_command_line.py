import sys
if len(sys.argv) != 3:
    print("Usage: python sum_cli.py <num1> <num2>")
else:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    result = num1 + num2
    print(sys.argv)
    print(f"The sum of {num1} and {num2} is: {result}")