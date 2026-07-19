class cal:
    @staticmethod
    def check_num(num):
        if num%2==0:
            print("Even")
        else:
            print("Odd")
obj=cal()
obj.check_num(5)