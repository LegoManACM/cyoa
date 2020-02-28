import time
import os
os.system('cls' if os.name == 'nt' else 'clear')

print('+---------------+')
print('|  Candy World  |')
print('+---------------+')

#begining
option0_1 = {'text': 'Gumbal planet','DSPG': 1}
option0_2 = {'text': 'Loli-pop planet','DSPG': 4}
page0 = {'text': 'You must start your space adventure somewhere', 'option':[option0_1, option0_2],'type':'normal'}

#page1
option1_1 = {'text': 'A robot mech suit','DSPG': 2}
option1_2 = {'text': 'A car rover','DSPG': 3}
page1 = {'text': 'This planet has hard terrain to navigate. You can change your ship into either:', 'option':[option1_1, option1_2],'type':'normal'}

#page2
option2_1 = {'text': 'Take samples of the gum','DSPG': 5}
option2_2 = {'text': 'Explore the famed candy rainbow','DSPG': 11}
page2 = {'text': "As you land your landing gear fold out. They are two legs. The ship's parts shift and turn. Finnally they resemble a humanoid robot!", 'option':[option2_1, option2_2],'type':'normal'}

#page3
option3_1 = {'text': 'Find a ramp','DSPG': 15}
option3_2 = {'text': 'Have a snack(gum)','DSPG': 20}
page3 = {'text': 'Your craft unfolds. Four hatches open to reveal wheels! You can either:', 'option':[option3_1, option3_2],'type':'normal'}

#page4
option4_1 = {'text': 'Near the candy rainbow','DSPG': 11}
option4_2 = {'text': 'Near the vilage','DSPG': 10}
page4 = {'text': 'Gum is to sticky for your taste! This planet will be hard to land on. There are two landing sites.(your vehicle wil become a robot mech!)', 'option':[option4_1, option4_2],'type':'normal'}

#page5
option5_1 = {'text': 'Grab the controls and pull the arm back','DSPG': 6}
option5_2 = {'text': 'Get out and unstick the claw by hand','DSPG': 7}
page5 = {'text': "Your robot's arm extends dow to the gound and grabs a chunk. Its arm is stuck!", 'option':[option5_1, option5_2],'type':'normal'}

#page6
option6_1 = {'text': "Fly to loli-pop planet's village and get repaired",'DSPG': 8}
option6_2 = {'text': 'Repair this youirself','DSPG': 12}
page6 = {'text': 'You grab the joystick and pull back. The robot pulls so hard that its arm rips off! You can:', 'option':[option6_1, option6_2],'type':'normal'}

#page7
option7_1 = {'text': '','DSPG': 0}
option7_2 = {'text': '','DSPG': 0}
page7 = {'text': 'You press a button and the capsul opens. You get your plasma torch and blast off some of the gum. It seems to work! You continue and soon your vehicle is free! But now your sinking quickly. Seconds later you have sunk!', 'option':[option7_1, option7_2],'type':'end'}

#page8
option8_1 = {'text': 'Continue the transformation','DSPG': 9}
option8_2 = {'text': 'Get out and fix it','DSPG': 7}
page8 = {'text': 'Your ship starts transforming. !ERROR! It seems the other claw is stuck now. You can still make it with no arms', 'option':[option8_1, option8_2],'type':'normal'}

#page9
option9_1 = {'text': 'To the village','DSPG': 10}
option9_2 = {'text': 'To the nearest space station','DSPG': 18}
page9 = {'text': 'You flip a few swiches and press a button to overide the warning. You burst free! Your computer alerts you that you may not be able to return to robot mode.', 'option':[option9_1, option9_2],'type':'normal'}

#page10
option10_1 = {'text': 'The quest','DSPG': 11}
option10_2 = {'text': 'Or go to another planet','DSPG': 0}
page10 = {'text': 'When you land, your landing gear colaps from under you! You give the repair men some chocolate coins. Once your ship is repaired the man tells you of a quest:', 'option':[option10_1, option10_2],'type':'normal'}

#page11
option11_1 = {'text': '','DSPG': 0}
option11_2 = {'text': '','DSPG': 0}
page11 = {'text': 'You see the rainbow is made of pure chocolate(gold)! Making history. you explore this unseen marvel! You hire some help and build an amusment park around the rainbow. Three years later you are famous in the whole galaxy! $The End$', 'option':[option11_1, option11_2],'type':'good'}

#page12
option12_1 = {'text': 'Join him, be adventerous','DSPG': 13}
option12_2 = {'text': 'Continue your research','DSPG': 14}
page12 = {'text': 'As your getting out of your ship, a spacecraft zooooooooms over head then circles back to help you! Once your fixed he says that he is going to jaw breaker planet. You can:', 'option':[option12_1, option12_2],'type':'normal'}

#page13
option13_1 = {'text': '','DSPG': 0}
option13_2 = {'text': '','DSPG': 0}
page13 = {'text': "He gives you the cordinace and your punch it in. Your ship locks on target and zips away. Seconds later you relize that you've made a grave mistake! The directions he gave you led strait into a warhead. There is no escape! You are doomed! The second your ship touches it, it disinegrates!", 'option':[option13_1, option13_2],'type':'end'}

#page14
option14_1 = {'text': 'Continue','DSPG': 11}
option14_2 = {'text': 'Continue','DSPG': 11}
page14 = {'text': 'This area of the planet is rich with chocolate! as you continue to explore a gigantic rainbow appears!', 'option':[option14_1, option14_2],'type':'normal'}

#page15
option15_1 = {'text': 'Go off of the jumps','DSPG': 16}
option15_2 = {'text': 'Grab asnack first','DSPG': 20}
page15 = {'text': 'For a few minuets you drive around until you finally see a lumpy part of the planet!', 'option':[option15_1, option15_2],'type':'normal'}

#page16
option16_1 = {'text': 'Melt your way out','DSPG': 7}
option16_2 = {'text': 'Drive out','DSPG': 17}
page16 = {'text': "You drive a ways away then shoot strait at the biggest jump! Your car flies into the air! Upon landing your wheel hits a sticky patch and you're stuck", 'option':[option16_1, option16_2],'type':'normal'}

#page17
option17_1 = {'text': 'Use the emergency engine to fly to the village','DSPG': 10}
option17_2 = {'text': 'Fix the ship yourself','DSPG': 12}
page17 = {'text': "'You put the pedle to the candy!' The wheels spin, FASTER, FASTER, FASTER! Boom! You engine explodes! You're hurtled out and see a village", 'option':[option17_1, option17_2],'type':'normal'}

#page18
option18_1 = {'text': 'Get your ship repaied','DSPG': 10}
option18_2 = {'text': 'Sell your ship and live there','DSPG': 19}
page18 = {'text': 'You fly your damaged ship off the planet and send out a distress signal. A space station soon sends a tug ship which pulls you back to the station.', 'option':[option18_1, option18_2],'type':'normal'}

#page19
option19_1 = {'text': '','DSPG': 0}
option19_2 = {'text': '','DSPG': 0}
page19 = {'text': "All your belonging sold for a great price. You buy a luxery room at the station and live there the rest of your life. Sometimes you wish you could go back to your old life and regret your choice. You'll never know", 'option':[option19_1, option19_2],'type':'end'}

#page20
option20_1 = {'text': '','DSPG': 0}
option20_2 = {'text': '','DSPG': 0}
page20 = {'text': "You get out and grab a handful of gum. Once you're back in your car you take a bite. A few minuets later your stomack feels weird. you skin is turning pink! You can't feel anything! You've turned into gum... Forever! The End!", 'option':[option20_1, option20_2],'type':'end'}


#page tracker and story
story = [page0, page1, page2, page3, page4, page5, page6, page7, page8, page9, page10, page11, page12, page13, page14, page15, page16, page17, page18, page19, page20]
current_page_index = 0
current_page = story[current_page_index]

#game controler
while True:

    #Print page text
    print('\n\rpage: ', current_page_index + 1)
    print("\n\r")
    print(current_page['text'])
    print("\n\r")
    
    #Print page options
    if current_page['type'] == 'normal':
        print('1', current_page['option'][0]['text'])
        print('2', current_page['option'][1]['text'])
        print('x to quit')
        
        #Get user choice
        user_choice = input("Choose your option:")
        
        #Set new current_page based on choice
        if user_choice == '1':
            current_page_index = current_page['option'][0]['DSPG']
        
        elif user_choice == '2':
            current_page_index = current_page['option'][1]['DSPG']
        
        elif user_choice == 'x':
            exit()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Please re-enter')
            time.sleep(2)
        current_page = story[current_page_index]
        
            
        #clear terminal
        os.system('cls' if os.name == 'nt' else 'clear')

    #Print bad end
    elif current_page['type'] == 'end': 
       print('Game over!')
       input('hit enter to exit')
       os.system('cls' if os.name == 'nt' else 'clear')
       exit()

    #Print good end
    else:
       print('Yay, you made it! Good job!')
       input('hit enter to exit')
       os.system('cls' if os.name == 'nt' else 'clear')
       exit()

