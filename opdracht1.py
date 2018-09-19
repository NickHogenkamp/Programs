# Naam:     Nick Hogenkamp
# Opdracht: Euler problem 1
# Datum:    19-9-2018

sum = 0                                 # Make variable sum
              
for j in list(range(0, 1000)):          # for loop range 0..20
    if ((j%5) == 0) | ((j%3) == 0):     # if statement
        sum = sum + j

print(sum)                              # print sum    
