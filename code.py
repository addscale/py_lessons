# -*- coding: utf-8 -*- 

import random

import requests

def point(event, context):
    print(event)
    if event["message"]["text"][0] == "/":
        words = event["message"]["text"].split()
        command = words[0][1:]
        if command == "echo":
            send_message(event["message"]["from"]["id"], event["message"]["text"])
        elif command == "help":
            help_text = ''' Длиномер - Д3 @dd3bot — это бот для измерения расстояния от стойки A до стойки B. 
            
            Отправьте боту номер первой стойки, второй стойки и в ответ он отправит для Вас результат расчета с расстоянием между этими стойками, а также подскажет через какой лоток оптимальнее проложить кроссировку.'''
            send_message(event["message"]["from"]["id"], help_text)
        elif command == "support":
            support = ''' Нашли ошибку? Расскажите мне о ней как можно подробнее, чтобы я смог исправить её.
            Контакт: @verceti''' 
            send_message(event["message"]["from"]["id"], support)
        elif command == "start":
            start = ''' Ладно, давай начнём! 
			Вводи номера стоек: '''
            send_message(event["message"]["from"]["id"], start)
            send_message(event["message"]["from"]["id"], ''' Принимаю только формат:
		 
        =x=y
		 
        x  — № первой стойки, y  — № второй стойки
		 
        пример: =123=234 ''')
        else:
            send_message(event["message"]["from"]["id"], "Я не знаю эту команду")
            
    elif event["message"]["text"][0] == "=":
        p1 = str(event["message"]["text"][1:])
        temp=p1.find('=')
        index = temp
        p1 = p1 [index:]
        p1 = p1 [1:]
        
        
        p2 = str(event["message"]["text"][1:])
        temp=p2.find('=')
        index = temp
        p2 = p2 [:index]
        p2 = p2 [0:]
        
        if 243 >= int(p1) >= 1:
            s1 = int(p1)
        else:
            send_message(event["message"]["from"]["id"], ''' Я знаю, что ничего не знаю про вторую введенную стойку
            ¯\_(ツ)_/¯''')
        if 243 >= int(p2) >= 1:
            s2 = int(p2)
        else:
            send_message(event["message"]["from"]["id"], ''' Я знаю, что ничего не знаю про первую введенную стойку 
            ¯\_(ツ)_/¯''')
            
        if 20 >= s1 >= 1:
            s1R = 1
        elif 40 >= s1 >= 21:
            s1R = 2
        elif 60 >= s1 >= 41:
            s1R = 3
        elif 80 >= s1 >= 61:
            s1R = 4
        elif 100 >= s1 >= 81:
            s1R = 5
        elif 120 >= s1 >= 101:
            s1R = 6
        elif 140 >= s1 >= 121:
            s1R = 7
        elif 160 >= s1 >= 141:
            s1R = 8
        elif 180 >= s1 >= 161:
            s1R = 9
        elif 200 >= s1 >= 181:
            s1R = 10
        elif 220 >= s1 >= 201:
            s1R = 11
        elif 240 >= s1 >= 221:
            s1R = 12
        elif 243 >= s1 >= 241:
            s1R = 13
	
	
        if 20 >= s2 >= 1:
            s2R = 1
        elif 40 >= s2 >= 21:
            s2R = 2
        elif 60 >= s2 >= 41:
            s2R = 3
        elif 80 >= s2 >= 61:
            s2R = 4
        elif 100 >= s2 >= 81:
            s2R = 5
        elif 120 >= s2 >= 101:
            s2R = 6
        elif 140 >= s2 >= 121:
            s2R = 7
        elif 160 >= s2 >= 141:
            s2R = 8
        elif 180 >= s2 >= 161:
            s2R = 9
        elif 200 >= s2 >= 181:
            s2R = 10
        elif 220 >= s2 >= 201:
            s2R = 11
        elif 240 >= s2 >= 221:
            s2R = 12
        elif 243 >= s2 >= 241:
            s2R = 13
        
        long_st1 = s1R * 20 - 9
        long_st2 = s2R * 20 - 9

        if s1R == s2R:
            if s1R == 13:	    
                v1 = ((abs(s1-s2)+1)*0.6) + 0.2
                send_message(event["message"]["from"]["id"], "Расстояние (м):")
                send_message(event["message"]["from"]["id"], v1)
                send_message(event["message"]["from"]["id"], "(без запаса)")
                exit()
            else:
                if (s1 >= long_st1 >= s2) or (s2 >= long_st1 >= s1):
                    v1 = ((abs(s1-s2)+1)*0.6) + 0.2
                    send_message(event["message"]["from"]["id"], "Расстояние (м):")
                    send_message(event["message"]["from"]["id"], v1)
                    send_message(event["message"]["from"]["id"], "(без запаса)")
                    exit()
                else:
                    v1 = (abs(s1-s2)+1)*0.6
                    send_message(event["message"]["from"]["id"], "Расстояние (м):")
                    send_message(event["message"]["from"]["id"], v1)
                    send_message(event["message"]["from"]["id"], "(без запаса)")
                    exit()
                    
        if int(p1) > 240:
            s1 = 240
            s1R = 12
        if int(p2) > 240:
            s2 = 240
            s2R = 12			
			
        dlr = abs(s1R - s2R)
        do_mid_s1 = abs(s1-(s1R * 20 - 9))
        do_cr_s1 = abs(s1-(s1R * 20 - 1))
        do_mid_s2 = abs(s2-(s2R * 20 - 9))
        do_cr_s2 = abs(s2-(s2R * 20 - 1))
        
        if do_mid_s1 + do_mid_s2 >= do_cr_s1 + do_cr_s2:
            send_message(event["message"]["from"]["id"], "Наиболее оптимально проложить кабель через КРАЙНИЙ ЛОТОК:")
            if (s1 >= long_st1 >= s2) or (s2 >= long_st1 >= s1):
                best = ((do_cr_s1 + do_cr_s2) * 0.6) + 0.8
            else:
                best = ((do_cr_s1 + do_cr_s2) * 0.6) + 0.6
        else:
            best = ((do_mid_s1 + do_mid_s2) * 0.6) + 0.8
            send_message(event["message"]["from"]["id"], "Наиболее оптимально проложить кабель через СРЕДНИЙ ЛОТОК:")
        
        if int(s1R) > int(s2R):
            if dlr == 1:
                if s1R % 2 == 0:
                    dlot = 3
                else:
                    dlot = 2.4
            elif s1R % 2 == 0:
                if dlr % 2 == 0:
                    dlot = dlr / 2 * (5.4)
                else:
                    dlot = (dlr-1) / 2 * (5.4) + 3
            else:
                if dlr % 2 == 0:
                    dlot = dlr / 2 * (5.4)
                else:
                    dlot = (dlr-1) / 2 * (5.4) + 2.4
                
        if int(s1R) < int(s2R):
            if dlr == 1:
                if s2R % 2 == 0:
                    dlot = 3
                else:
                    dlot = 2.4
            elif s2R % 2 == 0:
                if dlr % 2 == 0:
                    dlot = dlr / 2 * (5.4)
                else:
                    dlot = (dlr-1) / 2 * (5.4) + 3
            else:
                if dlr % 2 == 0:
                    dlot = dlr / 2 * (5.4)
                else:
                    dlot = (dlr-1) / 2 * (5.4) + 2.4
                
        if int(p1) > 240:
            trnc = ((abs(int(p1)-241)+1)*0.6) + 0.2
            rezU = dlot + best + trnc + 3.4
            send_message(event["message"]["from"]["id"], "Расстояние (м):")
            send_message(event["message"]["from"]["id"], rezU)
            send_message(event["message"]["from"]["id"], "(без запаса)")
        elif int(p2) > 240:
            trnc = ((abs(int(p2)-241)+1)*0.6) + 0.2
            rezU = dlot + best + trnc + 3.4
            send_message(event["message"]["from"]["id"], "Расстояние (м):")
            send_message(event["message"]["from"]["id"], rezU)
            send_message(event["message"]["from"]["id"], "(без запаса)")
        else:
            rezU = dlot + best
            send_message(event["message"]["from"]["id"], "Расстояние (м):")
            send_message(event["message"]["from"]["id"], rezU)
            send_message(event["message"]["from"]["id"], "(без запаса)")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    else:
        send_message(event["message"]["from"]["id"], ''' Принимаю только формат:
		 
        =x=y
		 
        x  — № первой стойки, y  — № второй стойки
		 
        пример: =123=234 ''')
        
        
