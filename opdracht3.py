# Naam:     Nick Hogenkamp
# Opdracht: Euler problem 3
# Datum:    19-9-2018

n = 600851475143              # Make variable n
i = 2

while i*i <= n:               # 
    if n%i:
        i = i + 1
    else:
        n //= i

print(n)
