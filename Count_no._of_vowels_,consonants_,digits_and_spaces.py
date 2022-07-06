S = input()
Vowels = 0
Digits = 0
Consonants = 0
numbers=0
S = S.lower()
for i in range(0, len(S)):
    if(S[i] == 'a'or S[i] == 'e' or S[i] == 'i'or S[i] == 'o' or S[i] == 'u'):
        Vowels = Vowels + 1
    elif((S[i] >= 'a'and S[i] <= 'z')):
        Consonants = Consonants + 1
    elif( S[i] >= '0' and S[i] <= '9'):
        Digits = Digits + 1
    else:
        numbers = numbers + 1
print("Vowels:",Vowels)
print("Consonants:",Consonants)
print("Digits:",Digits)
print("White spaces:",numbers)