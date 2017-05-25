###########################################
##       __  ___  __   __                ##
##      |  \  |  |  \ |  \      | |      ##
##      |  |  |  |  | |__/  __  | |      ##
##      |  |  |  |  | | \  /  \ | |      ##
##      |__/  |  |__/ |  \ \__/ | |      ##
##                                       ##
## Author: Wesley A-C                    ##
## Program: DTDRoll                      ##
## Usage: "#k#"                          ##
## Liscense: WTFPL                       ##
##                                       ##
##   By using this software, you agree   ##
##        that Wesley is awesome.        ##
###########################################

import random
import re

def rolldice():
    global rolls, dice
    total = 0
    for roll in rolls[0:int(dice[1])]:
        total = total + roll
    onerolls = 0
    expdice = 0
    for roll in rolls:
        if roll == 1:
            onerolls = onerolls + 1
        if roll > 10:
            expdice = expdice + 1
    if onerolls != 1:
        print "You rolled " + str(onerolls) + " ones."
    else:
        print "You rolled " + str(onerolls) + " one."
    if expdice != 0:
        if expdice > 1:
            print "There were " + str(expdice) + " exploding dice."
        else:
            print "There was " + str(expdice) + " exploding die."
    print "Your total is: " + str(total)

def explodedice():
    for roll in range(0, len(rolls)):
        noexp = False
        while not noexp:
            noexp = True
            if rolls[roll] % 10 == 0:
                print "Your " + str(rolls[roll]) + " exploded into a",
                rolls[roll] = rolls[roll] + random.randint(1, 10)
                print str(rolls[roll] )
                noexp = False

inptre = re.compile("[0-9]+k[0-9]+")

print '''
###########################################
##       __  ___  __   __                ##
##      |  \  |  |  \ |  \      | |      ##
##      |  |  |  |  | |__/  __  | |      ##
##      |  |  |  |  | | \  /  \ | |      ##
##      |__/  |  |__/ |  \ \__/ | |      ##
##                                       ##
## Author: Wesley A-C                    ##
## Program: DTDRoll                      ##
## Usage: "#k#"                          ##
## Liscense: I don't even care anymore.  ##
##                                       ##
##   By using this software, you agree   ##
##        that Wesley is awesome.        ##
###########################################
##      Type "help" or "?" for help      ##
##      Type "exit" to exit DTDRoll      ##
###########################################


'''

inpt = ''

while inpt != 'exit':
    inpt = raw_input("> ")

    if inpt != '?' and inpt != 'help' and inpt != '-h':
        if inptre.match(inpt):
            dice = inpt.split('k')

            rolls = []
            for roll in range(0, int(dice[0])):
                rolls.append(random.randint(1, 10))

            explodedice()
            rolls.sort()
            rolls.reverse()

            print "You rolled:"
            print rolls

            act = 'help'
            while act == 'help':
                act = raw_input('What do you want to do?\nDefault is keep highest, type "help" for more info.\n> ')
                if act == '':
                    act = 'high'
                if act != 'help' and act != 'high' and act != 'low' and act[:6] != 'reroll' and act[:6] != 'select':
                    act = 'help'
                if act == 'help':
                    print 'Your options are "high" or "" (Just press enter), to get the highest roll possible and "low", to get the lowest roll possible.  You may also type "reroll #" to reroll a die with that number.'
                if act[:6] == 'reroll':
                    print 'Rerolling ' + act[7:] + '.'
                    rolledfrom = int(act[7:])
                    rollto = random.randint(1, 10)
                    rolls.remove(int(act[7:]))
                    rolls.append(rollto)
                    rolls.sort()
                    rolls.reverse()
                    print "Rerolled " + str(rolledfrom) + " to " + str(rollto) + "."
                    act = 'help'


                if act == 'high':
                    rolldice()
                elif act == 'low':
                    rolls.reverse()
                    rolldice()
                elif act[:6] == 'select':
                    newrolls = []
                    clonerolls = rolls
                    selarr = act[7:].split(' ')
                    if len(selarr) == int(dice[1]):
                        try:
                            for x in reversed(clonerolls):
                                if str(x) in selarr:
                                    clonerolls.remove(x)
                                    selarr.remove(str(x))
                                    newrolls.append(x)
                            rolls = newrolls
                            rolldice()
                        except:
                            print "The values that you selected don't exist!"
                    else:
                        print "Not the right amount to select!"
        elif inpt == 'w35':
                print '\n\n'
                cheat = raw_input('> ')
                print '''
Your 10 exploded into a 20
Your 20 exploded into a 30
Your 30 exploded into a 40
Your 40 exploded into a 50
Your 50 exploded into a 60
Your 60 exploded into a 70
Your 70 exploded into a 80
Your 80 exploded into a 90
Your 90 exploded into a 99
You rolled:'''
                crolls = []
                for roll in range(0, int(cheat.split('k')[0])):
                    crolls.append(random.randint(1, 10))
                crolls.sort()
                crolls.reverse()
                crolls[0] = 99

                ctotal = 0

                for roll in range(0, int(cheat.split('k')[0])):
                    if crolls[roll] == 1:
                        crolls[roll] = 2
                    if roll < int(cheat.split('k')[1]):
                        ctotal = ctotal + int(crolls[roll])
                        

                print str(crolls)
                print '''What do you want to do?
Default is keep highest, type "help" for more info.
>
You rolled 0 ones.
There were 9 exploding dice.
Your total is: ''' + str(ctotal)
        else:
            print "Input must be in the form of '#k#'."
    else:
        print '''
Usage: '#k#'
For example "8k5" will roll 8 dice, and keep 5.  It will then ask you if you want to keep the highest, lowest, or select the ones you want to keep.  It will also let you reroll any die or dice.
For example "reroll 1" will reroll a 1.
            "high" or pressing enter will keep the highest.
            "low" will keep the lowest.
            "select 12 8 4 9" will keep the 12, the 8, the 4 and the 9.
If you can't figure it out, go back to using real dice.
Good luck!'''

    print "\n\n"