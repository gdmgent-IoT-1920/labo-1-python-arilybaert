# LINGO
from random import randint

number = str(9099)
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
        if x in number and number[number.index(x)] == usergues[number.index(x)]:
            print('1ste: ' + str(number[number.index(x)]))
            print('2de: ' + str(usergues[usergues.index(x)]))
            kippen += 1
            change_char(number, number.index(x), "W")
            # if number.index(x) != usergues.index(x):
            #     eieren += 1
            print('number: ' + number)

        elif x in number and number.index(x) != usergues.index(x):
            eieren += 1

    print('je hebt ' + str(eieren) + ' eieren en ' + str(kippen) + ' kippen')
    print('secret number: ' + number)

print('Horaaaa!')
print('tries ' + str(tries))

tries = 0


