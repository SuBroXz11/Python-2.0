import random;

# own logic
# head_tails = 2 * random.random()

# if(head_tails >= 1):
#     print("Head")
# else:
#     print("Tails")
    
# learned one
# random_side = random.choice(['Head', 'Tails'])
# print(random_side)

random_side= random.randint(0,1)
if(random_side == 1):
    print("Head")
else:
    print('Tails')

