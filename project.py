# NPC-Generator
import random

# This tells the user that the npcs will be given certain attributes and asks for how many npcs it wants
print('NPCs Will Be Given Heights, Eye Colors, Hair Colors, Ages and Names\n')
user = int(input('How Many NPCs Do You Want? '))


# These are the different attributes and charcteristics that will be given to each NPC
first_names = ['Star', 'Sky', 'Aris', 'Mars', 'Moon', 'Orion', 'Atlas', 'Luna', 'Nova', 'Andromeda']
last_names = ['Smith', 'Johnson', 'Brown', 'Miller', 'Davis', 'Jones', 'Williams', 'Anderson', 'Jackson', 'Green']
eye_color = ['Brown', 'Brown', 'Hazel', 'Hazel', 'Blue', 'Blue', 'Green', 'Green', 'Gold', 'Gold']
age = random.randint(12, 65)
hair_color = ['Red', 'Green', 'Blue', 'Purple', 'Pink', 'Brown', 'Black']
height = random.randint(152, 198)

# This sets the amount of npcs generated to 0
npcs_generated = 0

# This will generate the amount of npcs the user wants, giving them different chracteristics everytime to ensure that the npcs are different
while npcs_generated <= user:
    print('Name: ', random.choice(first_names), random.choice(last_names), '\n', f'Age: {age}\n' 'Eye Color: ', random.choice(eye_color), '\n', 'Hair Color: ', random.choice(hair_color), '\n', f'Height: {height}cm\n\n')
    age = random.randint(12, 65)
    height = random.randint(152, 198)
    
    npcs_generated += 1
# This adds one to the counter, the loop will continue making npcs until the counter is equal to how many npcs the user wants
    
