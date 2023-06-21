# Problem Link
# https://infytq.onwingspan.com/web/en/viewer/hands-on/lex_auth_012751861844041728222_shared?collectionId=lex_auth_0125409722749255681063_shared&collectionType=Course&pathId=lex_auth_0127475769196216322339_shared

class Parrot:
    __counter = 7000
    def __init__(self, name, color) :
        self.__name = name
        self.__color = color
        Parrot.__counter += 1
        self.__unique_number = Parrot.__counter
    
    def get_name(self):
        return self.__name
    
    def get_color(self) :
        return self.__color
    
    def get_unique_number(self):
        return self.__unique_number
    
x=Parrot("x","black")
print(x.get_name(), " , ",x.get_color()," , ",x.get_unique_number())
y=Parrot("y","blue")
print(y.get_name(), " , ",y.get_color()," , ",y.get_unique_number())