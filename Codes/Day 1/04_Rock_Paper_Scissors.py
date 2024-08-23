import random

# rock_paper_scissors = random.randint(1,3)
# print(rock_paper_scissors)

# 1 = rock, 2 = paper, 3 = scissors

user_choose = int(input('choose 0 for rock 1 for paper and 2 for scissors '))

if user_choose == 0:
    print('you chose rock')
    print('''
        ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"''')
elif user_choose == 1:
    print('you chose paper')
    print('''       
    _.-._
    | | | |_
    | | | | |
    | | | | |
  _ |  '-._ |
  \`\`-.'-._;
   \    '   |
    \  .`  /
     |    |''')
elif user_choose == 2:
    print('you chose scissors')
    print('''
    .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/''')
    
computer_choose=random.randint(0,2)
if computer_choose == 0:
    print('Computer chose rock')
    print('''
        ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"''')
elif computer_choose == 1:
    print('Computer chose paper')
    print('''       
    _.-._
    | | | |_
    | | | | |
    | | | | |
  _ |  '-._ |
  \`\`-.'-._;
   \    '   |
    \  .`  /
     |    |''')
elif computer_choose == 2:
    print('Computer chose scissors')
    print('''
    .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/''')

# print(user_choose)
# print(computer_choose)

if(computer_choose  == 0 and user_choose == 1):
    print('You win')
elif(computer_choose  == 0 and user_choose == 2):
    print('Computer wins')
elif(computer_choose  == 1 and user_choose == 0):
    print('Computer wins')
elif(computer_choose  == 1 and user_choose == 2):
    print('You win')
elif(computer_choose  == 2 and user_choose == 0):
    print('You win')
elif(computer_choose  == 2 and user_choose == 1):
    print('Computer wins')
elif(computer_choose==0 and user_choose==0):
    print('DRAW!')
elif(computer_choose==1 and user_choose==1):
    print('DRAW!')
elif(computer_choose==2 and user_choose==2):
    print('DRAW!')
    

