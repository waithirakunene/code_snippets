#create a class called MyClass
class Myself():
    #assign values to class Myself attributes
    number = 0
    name = ""

def Main(self):
    #create an object for class Myself 
    me = Myself()
    #access the attributes of Myself class using (.) operator
    me.number = 1928
    me.name = "Waithira Kunene"
    #print the values
    print(me.name + "" + me.number)
#remind Python there is method Main
if __name__ == '__name__':
    Main()
