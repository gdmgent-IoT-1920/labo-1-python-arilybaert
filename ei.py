# LINGO
from random import randint

number = str(9099)
numberBackup = number

# str(randint(1000,9999))
usergues = ' '
tries = 0
def change_char(s, p, r):
    return s[:p]+r+s[p+1:]
while usergues != number:
    usergues = str(input("guess a 4 digit number \n"))
    kippen = 0
    eieren = 0
    tries += 1
    for x in usergues:
        if x in number:
            indexNumber = number.find(x)
            indexGues = usergues.find(x)
            usergues = change_char(number, number.index(x), "X")
            if indexNumber == indexGues:
                kippen += 1
                number = change_char(number, number.index(x), "X")
            else:
                eieren += 1

    print('je hebt ' + str(eieren) + ' eieren en ' + str(kippen) + ' kippen')
    number = numberBackup
    print('secret number: ' + number)

print('Horaaaa!')
print('tries ' + str(tries))

tries = 0


