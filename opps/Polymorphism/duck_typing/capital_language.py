class India:
    def capital(self):
        print("New Delhi")

    def language(self):
        print("Hindi")


class USA:
    def capital(self):
        print("Washington D.C")

    def language(self):
        print("English")

def display(obj):
    obj.capital()
    obj.language()     

i = India()
display(i)      

u = USA()
display(u)