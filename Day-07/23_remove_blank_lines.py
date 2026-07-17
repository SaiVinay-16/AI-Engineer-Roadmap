with open("sample_05.txt","r") as f:
    data=f.readlines()
    cleaned_data=[line for line in data if line.strip() !=""]
    with open("sample_05.txt","w") as fh:
        fh.writelines(cleaned_data)