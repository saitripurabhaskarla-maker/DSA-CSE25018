n = int(input("Please enter the number of seconds you want to count: "))

def roc(n):
    for i in range(n, -1, -1):
        print(i)

    print("LAUNCH")

if n <= 0:
    print("Numbers can't be counted as the rocket has already launched.")
else:
    roc(n)
