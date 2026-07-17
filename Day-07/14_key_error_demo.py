try:
    dici={"Name":"Saivinay","rollno":21}
    key=input("Enter the key value:")
    if key not in dici:
        raise KeyError("Key not in Dictionary")
except KeyError as k:
    print("Key error:",k)
else:
    print(f"{key} : {dici[key]}")
finally:
    print("============================")