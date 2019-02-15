#Test of the fibonacci to practice on Git

def fibonacci():
    old = 1
    new = 1
    print(old)
    print(new)
    for i in range(20):
        new_1 = old + new
        print(new_1)
        old = new
        new = new_1

fibonacci()
