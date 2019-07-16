#generator generates background code next() and iter() methods
def Reverse(data):
    # this is like counting from 100 to 1 by taking one(-1)
    # step backward.
    for index in range(len(data) - 1, -1, -1):
        yield data[index]


def Main():
    rev = Reverse("Waithira Kunene")
    for char in rev:
        #print(char)
        data = 'Waithira Kunene'
    print(list(data[i] for i in range(len(data) - 1, -1, -1)))


if __name__ == "__main__":
    Main()