import os
os.system('cls' if os.name == 'nt' else 'clear')

option0_1 = {'text': 'left','DSPG': 1}
option0_2 = {'text': 'right','DSPG': 2}
page0 = {'text': 'You are adventurer about to enter a dungeon. As soon as you are in you see that there are two paths.', 'option':[option0_1, option0_2],'type':'normal'}

#left
option1_1 = {'turn back, page: 4': '','DSPG': 3}
option1_2 = {'keep going, page: 5': '','DSPG': 4}
page1 = {'text': 'As you walk down the path, you hear a scraping noise!', 'option':[option1_1, option1_2],'type':'normal'}

#right
option2_1 = {'text': 'open the chest','DSPG': 4}
option2_2 = {'text': 'turn back','DSPG': 5}
page2 = {'text': 'You find yourself at the end of a long hall in a small room. Resting in the center of the room on a small pedastool, you see a large chest!', 'option':[option2_1, option2_2],'type':'normal'}

option3_1 = {'text': '','DSPG': 0}
option3_2 = {'text': '','DSPG': 0}
page3 = {'text': '', 'option':[option3_1, option3_2],'type':'end'}

option4_1 = {'text': '','DSPG': 0}
option4_2 = {'text': '','DSPG': 0}
page4 = {'text': '', 'option':[option4_1, option4_2],'type':'end'}

option5_1 = {'text': '','DSPG': 0}
option5_2 = {'text': '','DSPG': 0}
page5 = {'text': '', 'option':[option5_1, option5_2],'type':'end'}



story = [page0, page1, page2, page3, page4, page5]
current_page_index = 0
current_page = story[current_page_index]

while True:

    #Print page text
    print('\n\rpage: ', current_page_index + 1)
    print("\n\r")
    print(current_page['text'])
    print("\n\r")
    
    #Print page options
    if current_page['type'] != 'end':
        print('1', current_page['option'][0]['text'])
        print('2', current_page['option'][1]['text'])
        #Get user choice
        user_choice = input("Choose your option:")
         #Set new current_page based on choice
        if user_choice == '1':
            current_page_index = current_page['option'][0]['DSPG']
        else:
            current_page_index = current_page['option'][1]['DSPG']

        current_page = story[current_page_index]
            
        #clear terminal
        os.system('cls' if os.name == 'nt' else 'clear')

    else:
        print('Game over!')
        input('hit enter to exit')
        os.system('cls' if os.name == 'nt' else 'clear')
        exit()


