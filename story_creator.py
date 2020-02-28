print("use command:give_page(pgnum, pgtext, op1text, DSPG, op2text, DSPG,type) for text")
def give_page(pgnum=int, pgtext=str, op1text=int, DSPG1=int, op2text=str, DSPG2=int, ty=str):
    print("option"+ pgnum,"_1 = {'text': '"+ op1text,"','DSPG':"+ SDPG1,"}")
    print("option"+ pgnum,"_2 = {'text': '"+ op2text,"','DSPG':"+ SDPG2,"}")
    print("page"+ pgnum," = {'text': '"+ pgtext,"', 'option':[option"+ pgnum,"_1, option"+ pgnum,"_2],'type':"+ ty,"'}")