def details(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")
details(city="Rajahmundry", age=21, name="Sai")