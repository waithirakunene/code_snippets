#functions in classes
#requires self parameters
#def keyword creates a new method
class Vector():
    #attributes for class vector
    x = 0.0
    y = 0.0

    #methods for class vector
    def Assign(self,x, y):
        self.x = x
        self.y = y

def Main():
    vec = Vector()
    vec.Assign(4,6)
    print("X:" + str(vec.x) +  " , Y:" + str(vec.y))

if __name__ == "__main__":
    Main()
