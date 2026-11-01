def fizz_buzz(n):
    resposta = []

    for i in range (1, n+1):
        if i % 15 == 0:
            resposta.append("FizzBuzz")
        elif i % 3 == 0:
            resposta.append("Fizz")
        elif i % 5 == 0:
            resposta.append("Buzz")
        else:
            resposta.append(str(i))
        

    return resposta

print (fizz_buzz(3))
print (fizz_buzz(5))
print (fizz_buzz(15))