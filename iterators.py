# This program will reverse the string that is passed 
# to it from the main function 
class Reverse(object):
    def __init__(self, data):
        self.data = data
        self.index = len(data)
#returns an obect thar can  iterated
    def __iter__(self):
        return self
#__next_gives the next value in the iteration
    def __next__(self):
        if self.index == 0:
            #stops the iteration
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


def Main():
    rev = Reverse('Waithira Kunene')
    for char in rev:
        print(char)


if __name__ == '__main__':
    Main()