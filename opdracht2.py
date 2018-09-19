# Naam:     Nick Hogenkamp
# Opdracht: Euler problem 1
# Datum:    19-9-2018

term1 = 0                       # Make variable term1
term2 = 1                       # Make variable term2
som = 0                         # Make variable som
fibonacci = term1 + term2       # Make variable fibonacci

while fibonacci < 4000000:      # Zolang fibonacci kleiner is dan 4miljoen
    term1 = term2
    term2 = fibonacci
    fibonacci = term1 + term2
    if (fibonacci%2) == 0:      # if statement
        som = som + fibonacci

print(som)
