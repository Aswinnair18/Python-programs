class Time:
    def __init__(self,hour,min,sec):
        self.__hour=hour
        self.__min=min
        self.__sec=sec

    def __add__(self, other):
        s=self.__sec + other.__sec
        m=self.__min + other.__min
        h=self.__hour + other.__hour
        if s >= 60:
            m += 1
            s -= 60
        
        if m >= 60:
            h += 1
            m -= 60
        
        return Time(h, m, s)

    def display(self):
        print(self.__hour, ":", self.__min, ":", self.__sec)

t1 = Time(2, 45, 50)
t2 = Time(1, 30, 20)

t3 = t1 + t2

print("Sum of two time :")
t3.display()