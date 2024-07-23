try:
  print('Welcome to Harry Potter Trivia! In this game, you will be asked questions about the Harry Potter books and movies. You will recieve points depending on whether you answer correctly or not. You can press Ctrl C to quit at any time. Good Luck!')
  
  while True:
    points = 0
    
    print('Where did in his uncle\'s house did Harry live before he went to Hogwarts?')
    print()
    print('1. The largest bedroom.\t2. The cupboard under the stairs.\t3. The attic.')
    answer = int(input())
    if answer == 2:
      print('Correct!')
      points += 1
    else:
      print('Nope, that\'s not it.')
    
    print('What creature was traveling throuhg the Hogwarts pipes and petrifying students during Harry\'s second year?')
    print()
    print('1. A centaur.\t2. A mermaid.\t3. A basilisk.')
    answer = int(input())
    if answer == 3:
      print('Correct!')
      points += 1
    else:
      print('Nope, that\'s not it.')
    
    print('What was the name of the prison that Harry\'s stepfather, Sirius Black, escaped from in Harry\'s third year?')
    print()
    print('1. Azkaban.\t2. Alkatraz.\t3. Alkazab.')
    answer = int(input())
    if answer == 1:
      print('Correct!')
      points += 1
    else:
      print('Nope, that\'s not it.')
    
    print('What was the dance called that Harry and his friends attended on his fourth year at Hogwarts?')
    print()
    print('1. The Bule Yall.\t2. The Hogwarts Waltz.\t3. The Yule Ball.')
    answer = int(input())
    if answer == 3:
      print('Correct!')
      points += 1
    else:
      print('Nope, that\'s not it.')
    
    print('Who was the defense against the dark arts teacher during Harry\'s fifth year?')
    print()
    print('1. Dolores Umbrige.\t2. Remus Lupin.\t3. Harry Potter.')
    answer = int(input())
    if answer == 1:
      print('Correct!')
      points += 1
    else:
      print('Nope, that\'s not it.')
    
    print('Who murdered Albus Dumbledore?')
    print()
    print('1. Harry Potter.\t2. Severus Snape.\t3. Tom Riddle (Voldemort).')
    answer = int(input())
    if answer == 2:
      print('Correct!')
      points += 1
    else:
      print('Nope, that\'s not it.')
    
    print('How many Deathly Hallows were there?')
    print()
    print('1\t2\t3')
    answer = int(input())
    if answer == 3:
      print('Correct!')
      points += 1
    else:
      print('Nope, that\'s not it.')
    
    if points > 2:
      print('You got ' + str(points) + ' points! Congratulations!')
    elif points == 1:
      print('You got 1 point.')
    else:
      print('You missed every single question. Better luck next time!')
  
    input('Press ENTER to try again, or hit Ctrl C to quit.')
    print()
    print()
    print()

except:
  print('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Thanks for playing!')