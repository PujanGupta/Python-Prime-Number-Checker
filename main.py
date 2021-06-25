def checkIfPrime(n):
    if n == 1:
        return 'Neither Prime or Composite"
    prime = True
    for i in range(2, n - 1):
        if n % i == 0:
            prime = False
            break
        else:
            pass
        
    if prime == True:
        return "Prime"
    elif prime == False:
        return "Composite"

while True:
    userInput = int(input("Enter a Number: "))
    userInputStatus = checkIfPrime(userInput)

    print(str(userInput) + " a " + userInputStatus + " Number !!")

