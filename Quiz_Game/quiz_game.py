print('Welcome to my computer quiz')

playing = input('Do you want to play? ')


if playing.lower()!= "yes" :
    quit()

print("Okay! Let's play :)")
score = 0

answer = input('What is the name of the fairy in Peter Pan?')
if answer.lower() == 'tinkerbell':
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


answer = input('What is the colour on the star in the somali flag?')
if answer.lower() == 'White':
    print('Correct!')
    score += 1

else:
    print("Incorrect!")

answer = input('How many planets are in our solar system?')
if answer.lower == 'eight':
    print('Correct!')
    score += 1

else:
    print("Incorrect!")


answer = input('Which Disney movie is Elsa in??')
if answer.lower() == 'frozen':
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%. ")


