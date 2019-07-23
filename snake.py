import curses
import random
import time


player = raw_input("DIGITE O NOME DO JOGADOR: ").upper()

try:
	arq = open("recordsnake2.txt","r")
	r = arq.read().split(',')
	arq.close()

except IOError:
	arq = open("recordsnake2.txt","w")
	arq.close()
	r = ["NINGUEM","0"]


	

recorde = [r[0],int(r[1])]
sentido = ['>']
cobra = [(2,15),(2,16)]
fruta = [random.randint(2,18),random.randint(1,78)]
vida = [random.randint(2,18),random.randint(1,78)]
vidas = [3]
pontos = [0]
speed = [0.1,10,'m']
barreiras = []
fase = [1]

def fase1(scr):
	global cobra,fruta,player

	scr.addstr(0,0," VIDAS: %d  FASE 1  PONTUACAO: %05d  RECORDE ATUAL: %05d  JOGADOR: %-s" % (vidas[0],pontos[0],recorde[1],player))
	scr.addch(cobra[-1][0],cobra[-1][1],sentido[0])
	scr.addch(fruta[0],fruta[1],"*")

	for c in range(80):
		scr.addch(1,c," ",curses.A_REVERSE)
		scr.addch(20,c," ",curses.A_REVERSE)
		barreiras.append((1,c))
		barreiras.append((20,c))
	for c in range(1,20):
		scr.addch(c,0," ",curses.A_REVERSE)
		scr.addch(c,79," ",curses.A_REVERSE)
		barreiras.append((c,0))
		barreiras.append((c,79))

	for i in range(1,len(cobra)-1):
		scr.addch(cobra[i][0],cobra[i][1],'X')

	scr.refresh()

def fase2(scr):
	global cobra,fruta,player

	scr.addstr(0,0," VIDAS: %d  FASE 2  PONTUACAO: %05d  RECORDE ATUAL: %05d  JOGADOR: %-s" % (vidas[0],pontos[0],recorde[1],player))
	scr.addch(cobra[-1][0],cobra[-1][1],sentido[0])
	scr.addch(fruta[0],fruta[1],"*")

	for c in range(80):
		scr.addch(1,c," ",curses.A_REVERSE)
		scr.addch(20,c," ",curses.A_REVERSE)
		barreiras.append((1,c))
		barreiras.append((20,c))
	for c in range(5,20):
		scr.addch(c,0," ",curses.A_REVERSE)
		scr.addch(c,79," ",curses.A_REVERSE)
		barreiras.append((c,0))
		barreiras.append((c,79))
	for c in range(1,20):
		for d in range(9,12):
			scr.addch(c,d," ",curses.A_REVERSE)
			barreiras.append((c,d))
	for c in range(1,16):
		for d in range(69,72):
			scr.addch(c,d," ",curses.A_REVERSE)
			barreiras.append((c,d))
	for c in range(7,9):
		for d in range(30,51):
			scr.addch(c,d," ",curses.A_REVERSE)
			barreiras.append((c,d))
			
	for c in range(9,20):
		for d in range(38,43):
			scr.addch(c,d," ",curses.A_REVERSE)
			barreiras.append((c,d))


	for i in range(1,len(cobra)-1):
		scr.addch(cobra[i][0],cobra[i][1],'X')

	scr.refresh()

def fase3(scr):
	global cobra,fruta,player

	scr.addstr(0,0," VIDAS: %d  FASE 3  PONTUACAO: %05d  RECORDE ATUAL: %05d  JOGADOR: %-s" % (vidas[0],pontos[0],recorde[1],player))
	scr.addch(cobra[-1][0],cobra[-1][1],sentido[0])
	scr.addch(fruta[0],fruta[1],"*")

	for c in range(10):
		scr.addch(1,c," ",curses.A_REVERSE)
		scr.addch(20,c," ",curses.A_REVERSE)
		barreiras.append((1,c))
		barreiras.append((20,c))
	for c in range(13,70):
		scr.addch(1,c," ",curses.A_REVERSE)
		scr.addch(20,c," ",curses.A_REVERSE)
		barreiras.append((1,c))
		barreiras.append((20,c))
	for c in range(73,80):
		scr.addch(1,c," ",curses.A_REVERSE)
		scr.addch(20,c," ",curses.A_REVERSE)
		barreiras.append((1,c))
		barreiras.append((20,c))
	for c in range(1,3):
		scr.addch(c,0," ",curses.A_REVERSE)
		scr.addch(c,79," ",curses.A_REVERSE)
		barreiras.append((c,0))
		barreiras.append((c,79))
	for c in range(5,15):
		scr.addch(c,0," ",curses.A_REVERSE)
		scr.addch(c,79," ",curses.A_REVERSE)
		barreiras.append((c,0))
		barreiras.append((c,79))
	for c in range(17,20):
		scr.addch(c,0," ",curses.A_REVERSE)
		scr.addch(c,79," ",curses.A_REVERSE)
		barreiras.append((c,0))
		barreiras.append((c,79))
	for c in range(79):
		scr.addch(10,c," ",curses.A_REVERSE)
		scr.addch(11,c," ",curses.A_REVERSE)
		barreiras.append((10,c))
		barreiras.append((11,c))
	for c in range(1,20):
		for d in range(35,45):
			scr.addch(c,d," ",curses.A_REVERSE)
			scr.addch(c,d," ",curses.A_REVERSE)
			barreiras.append((c,d))
			barreiras.append((c,d))
	for c in range(4,7):
		for d in range(14,21):
			scr.addch(c,d," ",curses.A_REVERSE)
			scr.addch(c,d," ",curses.A_REVERSE)
			barreiras.append((c,d))
			barreiras.append((c,d))
	for c in range(14,17):
		for d in range(14,21):
			scr.addch(c,d," ",curses.A_REVERSE)
			scr.addch(c,d," ",curses.A_REVERSE)
			barreiras.append((c,d))
			barreiras.append((c,d))
	for c in range(4,7):
		for d in range(62,69):
			scr.addch(c,d," ",curses.A_REVERSE)
			scr.addch(c,d," ",curses.A_REVERSE)
			barreiras.append((c,d))
			barreiras.append((c,d))
	for c in range(14,17):
		for d in range(62,69):
			scr.addch(c,d," ",curses.A_REVERSE)
			scr.addch(c,d," ",curses.A_REVERSE)
			barreiras.append((c,d))
			barreiras.append((c,d))

	for i in range(1,len(cobra)-1):
		scr.addch(cobra[i][0],cobra[i][1],'X')

	scr.refresh()
	
def fase4(scr):
	global cobra,fruta,player

	scr.addstr(0,0," VIDAS: %d  FASE 4  PONTUACAO: %05d  RECORDE ATUAL: %05d  JOGADOR: %-s" % (vidas[0],pontos[0],recorde[1],player))
	scr.addch(cobra[-1][0],cobra[-1][1],sentido[0])
	scr.addch(fruta[0],fruta[1],"*")

	for c in range(80):
		scr.addch(1,c," ",curses.A_REVERSE)
		scr.addch(20,c," ",curses.A_REVERSE)
		barreiras.append((1,c))
		barreiras.append((20,c))
	for c in range(1,15):
		scr.addch(c,0," ",curses.A_REVERSE)
		scr.addch(c,79," ",curses.A_REVERSE)
		barreiras.append((c,0))
		barreiras.append((c,79))
	for c in range(17,20):
		scr.addch(c,0," ",curses.A_REVERSE)
		scr.addch(c,79," ",curses.A_REVERSE)
		barreiras.append((c,0))
		barreiras.append((c,79))
	for c in range(15):
		scr.addch(13,c," ",curses.A_REVERSE)
		scr.addch(14,c," ",curses.A_REVERSE)
		barreiras.append((13,c))
		barreiras.append((14,c))
	for c in range(4,76):
		scr.addch(6,c," ",curses.A_REVERSE)
		scr.addch(7,c," ",curses.A_REVERSE)
		barreiras.append((6,c))
		barreiras.append((7,c))
	for c in range(65,79):
		scr.addch(17,c," ",curses.A_REVERSE)
		barreiras.append((17,c))
	for c in range(4,15):
		scr.addch(c,12," ",curses.A_REVERSE)
		scr.addch(c,13," ",curses.A_REVERSE)
		scr.addch(c,14," ",curses.A_REVERSE)
		barreiras.append((c,12))
		barreiras.append((c,13))
		barreiras.append((c,14))
	for c in range(4,6):
		scr.addch(c,38," ",curses.A_REVERSE)
		scr.addch(c,39," ",curses.A_REVERSE)
		scr.addch(c,40," ",curses.A_REVERSE)
		barreiras.append((c,38))
		barreiras.append((c,39))
		barreiras.append((c,40))
	for c in range(4,17):
		scr.addch(c,65," ",curses.A_REVERSE)
		scr.addch(c,66," ",curses.A_REVERSE)
		scr.addch(c,67," ",curses.A_REVERSE)
		barreiras.append((c,65))
		barreiras.append((c,66))
		barreiras.append((c,67))
	for c in range(10,20):
		scr.addch(c,38," ",curses.A_REVERSE)
		scr.addch(c,39," ",curses.A_REVERSE)
		scr.addch(c,40," ",curses.A_REVERSE)
		barreiras.append((c,38))
		barreiras.append((c,39))
		barreiras.append((c,40))

	for i in range(1,len(cobra)-1):
		scr.addch(cobra[i][0],cobra[i][1],'X')

	scr.refresh()
	
def fase5(scr):
	global cobra,fruta,player

	scr.addstr(0,0," VIDAS: %d  FASE 5  PONTUACAO: %05d  RECORDE ATUAL: %05d  JOGADOR: %-s" % (vidas[0],pontos[0],recorde[1],player))
	scr.addch(cobra[-1][0],cobra[-1][1],sentido[0])
	scr.addch(fruta[0],fruta[1],"*")

	for c in range(80):
		scr.addch(1,c," ",curses.A_REVERSE)
		scr.addch(20,c," ",curses.A_REVERSE)
		barreiras.append((1,c))
		barreiras.append((20,c))
	for c in range(1,6):
		scr.addch(c,0," ",curses.A_REVERSE)
		scr.addch(c,79," ",curses.A_REVERSE)
		barreiras.append((c,0))
		barreiras.append((c,79))
	for c in range(7,10):
		scr.addch(c,0," ",curses.A_REVERSE)
		scr.addch(c,79," ",curses.A_REVERSE)
		barreiras.append((c,0))
		barreiras.append((c,79))
	for c in range(11,13):
		scr.addch(c,0," ",curses.A_REVERSE)
		scr.addch(c,79," ",curses.A_REVERSE)
		barreiras.append((c,0))
		barreiras.append((c,79))
	for c in range(14,16):
		scr.addch(c,0," ",curses.A_REVERSE)
		scr.addch(c,79," ",curses.A_REVERSE)
		barreiras.append((c,0))
		barreiras.append((c,79))
	for c in range(17,19):
		scr.addch(c,0," ",curses.A_REVERSE)
		scr.addch(c,79," ",curses.A_REVERSE)
		barreiras.append((c,0))
		barreiras.append((c,79))
	for c in range(5,19):
		scr.addch(c,15," ",curses.A_REVERSE)
		scr.addch(c,16," ",curses.A_REVERSE)
		scr.addch(c,17," ",curses.A_REVERSE)
		barreiras.append((c,15))
		barreiras.append((c,16))
		barreiras.append((c,17))
	for c in range(8,20):
		scr.addch(c,37," ",curses.A_REVERSE)
		scr.addch(c,38," ",curses.A_REVERSE)
		scr.addch(c,39," ",curses.A_REVERSE)
		barreiras.append((c,37))
		barreiras.append((c,38))
		barreiras.append((c,39))
	for c in range(5,10):
		scr.addch(c,48," ",curses.A_REVERSE)
		scr.addch(c,49," ",curses.A_REVERSE)
		scr.addch(c,50," ",curses.A_REVERSE)
		barreiras.append((c,48))
		barreiras.append((c,49))
		barreiras.append((c,50))
	for c in range(16,20):
		scr.addch(c,48," ",curses.A_REVERSE)
		scr.addch(c,49," ",curses.A_REVERSE)
		scr.addch(c,50," ",curses.A_REVERSE)
		barreiras.append((c,48))
		barreiras.append((c,49))
		barreiras.append((c,50))
	for c in range(5,20):
		scr.addch(c,60," ",curses.A_REVERSE)
		scr.addch(c,61," ",curses.A_REVERSE)
		scr.addch(c,62," ",curses.A_REVERSE)
		barreiras.append((c,60))
		barreiras.append((c,61))
		barreiras.append((c,62))
	for c in range(1,51):
		scr.addch(4,c," ",curses.A_REVERSE)
		barreiras.append((4,c))
	for c in range(60,79):
		scr.addch(5,c," ",curses.A_REVERSE)
		barreiras.append((5,c))
	for c in range(60,79):
		scr.addch(9,c," ",curses.A_REVERSE)
		barreiras.append((9,c))
	for c in range(60,79):
		scr.addch(15,c," ",curses.A_REVERSE)
		barreiras.append((15,c))
	for c in range(1,15):
		scr.addch(11,c," ",curses.A_REVERSE)
		barreiras.append((11,c))
	for c in range(1,15):
		scr.addch(18,c," ",curses.A_REVERSE)
		barreiras.append((18,c))
	for c in range(18,32):
		scr.addch(14,c," ",curses.A_REVERSE)
		barreiras.append((14,c))
	for c in range(23,40):
		scr.addch(7,c," ",curses.A_REVERSE)
		barreiras.append((7,c))
	for c in range(43,60):
		scr.addch(12,c," ",curses.A_REVERSE)
		barreiras.append((12,c))
	
	

	for i in range(1,len(cobra)-1):
		scr.addch(cobra[i][0],cobra[i][1],'X')

	scr.refresh()

def move_direita():
	global cobra,sentido
	cobra.append((cobra[-1][0],(cobra[-1][1] + 1) % 80))
	cobra.pop(0)
	sentido[0] = '>'


def move_esquerda():
	global cobra,sentido
	cobra.append((cobra[-1][0],(cobra[-1][1] - 1) % 80))
	cobra.pop(0)
	sentido[0] = '<'

def move_acima():
	global cobra,sentido
	cobra.append(((cobra[-1][0] - 1) % 21,cobra[-1][1]))
	cobra.pop(0)
	sentido[0] = '^'

def move_abaixo():
	global cobra,sentido
	cobra.append(((cobra[-1][0] + 1) % 21,cobra[-1][1]))
	cobra.pop(0)
	sentido[0] = 'V'

def gera_fruta():
	global fruta,cobra,barreiras
	fruta[0] = random.randint(2,18)
	fruta[1] = random.randint(1,78)
		
def passa_fase(scr):
	global cobra,barreiras,fase,speed,sentido
	scr.clear()
	fase[0] += 1
	if fase[0] <= 5:
		barreiras = []
		scr.addstr(11,39,"FASE %d" % fase[0])
		scr.refresh()
		scr.addstr(11,39,"       ")
		time.sleep(2)				
		cobra = [(2,15),(2,16)]
		sentido = [">"]
		speed[0] -= 0.01
		speed[1] += 1

def morre(scr):
        curses.beep()
	global cobra,sentido,vidas
	time.sleep(0.5)
	for seg in cobra:
		scr.addch(seg[0],seg[1]," ")
	cobra = [(2,15),(2,16)]
	sentido = [">"]
	vidas[0] -= 1

def continua(scr):
	scr.addstr(10,25,"DESEJA JOGAR NOVAMENTE?")
	scr.addstr(12,30,"S - SIM")
	scr.addstr(13,30,"N - NAO")
	scr.refresh()

def start(scr):
	global speed,recorde
	curses.curs_set(0)

	scr.addstr(3,11,"XXXXXXXX  XXX   XX  XXXXXXXX  XX   XXX  XXXXXXXX    XXXXXXXX")
	scr.addstr(4,11,"XX        XXXX  XX  XX    XX  XX XXX    XX                XX")
	scr.addstr(5,11,"XX        XX XX XX  XX    XX  XXXX      XX                XX")
	scr.addstr(6,11,"XXXXXXXX  XX  XXXX  XXXXXXXX  XX XXX    XXXXX       XXXXXXXX")
	scr.addstr(7,11,"      XX  XX   XXX  XX    XX  XX  XXX   XX          XX      ")
	scr.addstr(8,11,"XXXXXXXX  XX    XX  XX    XX  XX   XXX  XXXXXXXX    XXXXXXXX")

	scr.addstr(0,50,'RECORDISTA ATUAL: %s' %  recorde[0])
	scr.addstr(1,50,'RECORDE: %d' % recorde[1])
	scr.addstr(12,10,"ESCOLHA SUA DIFICULDADE")
	scr.addstr(14,10,"F - FACIL - SNAKE LENTA, MAS 5 PONTOS POR FRUTA")
	scr.addstr(15,10,"M - MEDIO - SNAKE NORMAL, 10 PONTOS POR FRUTA")
	scr.addstr(16,10,"D - DIFICIL - SNAKE RAPIDA, MAS 20 PONTOS POR FRUTA")
	scr.addstr(20,9,"MOVIMENTOS: w - cima, s - baixo, a - esquerda, d - direita")
	scr.refresh()
	while True:
		ch = scr.getch()
		if ch == ord('f') or ch == ord('F'):
			speed[0],speed[1],speed[2] = 0.2 , 5 , 'f'
			scr.addstr(18,33,"FACIL!")
			scr.refresh()
			time.sleep(2)
			break
		if ch == ord('m') or ch == ord('M'):
			scr.addstr(18,33,"MEDIO!")
			scr.refresh()
			time.sleep(2)
			break
		if ch == ord('d') or ch == ord('D'):
			speed[0],speed[1],speed[2] = 0.06, 20 , 'd'
			scr.addstr(18,33,"DIFICIL!")
			scr.refresh()
			time.sleep(2)
			break


def end(scr):
   global fase,speed,pontos,player,recorde
   scr.clear()
   scr.addstr(3,1,"XXXXXXXX  XXXXXXXX  XX    XX  XXXXXXXX  XXXXXXXX  XX    XX  XXXXXXXX  XXXXXXXX")
   scr.addstr(4,1,"XX        XX    XX  XXX  XXX  XX        XX    XX  XX    XX  XX        XX    XX")
   scr.addstr(5,1,"XX        XX    XX  XX XX XX  XX        XX    XX  XX    XX  XX        XXXXXXXX")
   scr.addstr(6,1,"XX  XXXX  XXXXXXXX  XX XX XX  XXXX      XX    XX  XX    XX  XXXX      XX XXX  ")
   scr.addstr(7,1,"XX    XX  XX    XX  XX    XX  XX        XX    XX   XX  XX   XX        XX  XXX ")
   scr.addstr(8,1,"XXXXXXXX  XX    XX  XX    XX  XXXXXXXX  XXXXXXXX     XX     XXXXXXXX  XX   XXX")
   
   scr.addstr(14,2,"TOTAL DE PONTOS: %d" % pontos[0])
   if pontos[0] > recorde[1]:
      scr.addstr(16,22,"PARABENS, VOCE QUEBROU O RECORDE")
      scr.addstr(18,55,"NOVO RECORDE: %d" % pontos[0])
      arq = open("recordsnake2.txt","w")
      arq.write('%s,%d' % (player,pontos[0]))
      arq.close()
      recorde[1] = pontos[0]
   else:
      scr.addstr(18,55,"RECORD ATUAL: %d" % recorde[1])
   if fase[0] == 6:
	   if speed[2] == 'f':
		   scr.addstr(19,5,"PARABENS, VOCE CONCLUIU O JOGO NO MODO FACIL. TENTE OUTRAS DIFICULDADES")
	   elif speed[2] == 'm':
		    scr.addstr(19,5,"PARABENS, VOCE CONCLUIU O JOGO NO MODO MEDIO. TENTE OUTRAS DIFICULDADES")
	   elif speed[2] == 'd':
		    scr.addstr(19,5,"CARACA!!!! VOCE CONCLUIU O JOGO NO MODO DIFICIL!!! VOCE EH UM NINJA!!!")
   scr.refresh()
   time.sleep(5)

def main(scr):
	global cobra,fruta,sentido,vidas,pontos,recorde,speed,barreiras,fase
	curses.curs_set(0)
	scr.addstr(10,15,"UNIVERSIDADE FEDERAL DE CAMPINA GRANDE - UFCG")
	scr.addstr(11,15,"LABORATORIO DE PROGRAMACAO I")
	scr.addstr(12,15,"ROTEIRO DE PROJETO 2")
	scr.addstr(13,15,"DESENVOLVEDORES: PEDRO HENRIQUES, JOSE IAGO")
	scr.refresh()
	time.sleep(5)
	scr.clear()
	start(scr)
	scr.clear()
	scr.nodelay(1)
	while True:
          	while sentido[0]=='^' and vidas[0] != 0 and fase[0] <= 5:
			if len(cobra) > 20:
				passa_fase(scr)
				

			if fase[0] == 1:
				fase1(scr)
			elif fase[0] == 2:
				fase2(scr)
			elif fase[0] == 3:
				fase3(scr)
			elif fase[0] == 4:
				fase4(scr)
			elif fase[0] == 5:
				fase5(scr)
				
			if (fruta[0],fruta[1]) in cobra or (fruta[0],fruta[1]) in barreiras:
				gera_fruta()

			ch = scr.getch()
	

			if ch == ord('d') or sentido[0] == '>':
				scr.addch(cobra[0][0],cobra[0][1]," ")
				move_direita()
			elif ch == ord('a') or sentido[0] == '<':
				scr.addch(cobra[0][0],cobra[0][1]," ")
				move_esquerda()
                        else:
			        move_acima()

			cabeca = [cobra[-1][0],cobra[-1][1]]

			if (cabeca[0],cabeca[1]) in cobra[1:-1]:
				morre(scr)

			if cabeca == fruta:
				gera_fruta()
				cobra.insert(0,(cobra[0][0],cobra[0][1]))
				cobra.insert(2,(cobra[2][0],cobra[2][1]))
				pontos[0] += speed[1]

			if (cabeca[0],cabeca[1]) in barreiras:
				morre(scr)		

			if vidas[0] == 0 or fase[0] == 6:
				end(scr)
				break
		
			scr.addch(cobra[0][0],cobra[0][1]," ")
     
       
			time.sleep(speed[0]*1.5)

          	while sentido[0]=='V' and vidas[0] != 0 and fase[0] <= 5:
			if len(cobra) > 20:
				passa_fase(scr)

			if fase[0] == 1:
				fase1(scr)
			elif fase[0] == 2:
				fase2(scr)
			elif fase[0] == 3:
				fase3(scr)
			elif fase[0] == 4:
				fase4(scr)
			elif fase[0] == 5:
				fase5(scr)
				
			if (fruta[0],fruta[1]) in cobra or (fruta[0],fruta[1]) in barreiras:
				gera_fruta()
				
			ch = scr.getch()
		

			if ch == ord('d') or sentido[0] == '>':
				scr.addch(cobra[0][0],cobra[0][1]," ")
				move_direita()
			elif ch == ord('a') or sentido[0] == '<':
				scr.addch(cobra[0][0],cobra[0][1]," ")
				move_esquerda()
                        else:
			        move_abaixo()


			cabeca = [cobra[-1][0],cobra[-1][1]]

			if (cabeca[0],cabeca[1]) in cobra[1:-1]:
				morre(scr)

			if cabeca == fruta:
				gera_fruta()
				cobra.insert(0,(cobra[0][0],cobra[0][1]))
				cobra.insert(2,(cobra[2][0],cobra[2][1]))
				pontos[0] += speed[1]
				
			if (cabeca[0],cabeca[1]) in barreiras:
				morre(scr)			

			if vidas[0] == 0 or fase[0] == 6:
				end(scr)
				break
		
			scr.addch(cobra[0][0],cobra[0][1]," ")
     
       
			time.sleep(speed[0]*1.5)

          	while sentido[0]=='>' and vidas[0] != 0 and fase[0] <= 5:
			if len(cobra) > 20:
				passa_fase(scr)

			if fase[0] == 1:
				fase1(scr)
			elif fase[0] == 2:
				fase2(scr)
			elif fase[0] == 3:
				fase3(scr)
			elif fase[0] == 4:
				fase4(scr)
			elif fase[0] == 5:
				fase5(scr)
				
			if (fruta[0],fruta[1]) in cobra or (fruta[0],fruta[1]) in barreiras:
				gera_fruta()
				
			ch = scr.getch()
		
			if ch == ord('w') or sentido[0] == '^':
				scr.addch(cobra[0][0],cobra[0][1]," ")
				move_acima()
			elif ch == ord('s') or sentido[0] == 'V':
				scr.addch(cobra[0][0],cobra[0][1]," ")
				move_abaixo()
                        else:
			        move_direita()


			cabeca = [cobra[-1][0],cobra[-1][1]]

			if (cabeca[0],cabeca[1]) in cobra[1:-1]:
				morre(scr)

			if cabeca == fruta:
				gera_fruta()
				cobra.insert(0,(cobra[0][0],cobra[0][1]))
				cobra.insert(2,(cobra[2][0],cobra[2][1]))
				pontos[0] += speed[1]
				
			if (cabeca[0],cabeca[1]) in barreiras:
				morre(scr)		

			if vidas[0] == 0 or fase[0] == 6:
				end(scr)
				break
		
			scr.addch(cobra[0][0],cobra[0][1]," ")
     
       
			time.sleep(speed[0])

          	while sentido[0]=='<' and vidas[0] != 0 and fase[0] <= 5:
			if len(cobra) > 20:
				passa_fase(scr)
				break

			if fase[0] == 1:
				fase1(scr)
			elif fase[0] == 2:
				fase2(scr)
			elif fase[0] == 3:
				fase3(scr)
			elif fase[0] == 4:
				fase4(scr)
			elif fase[0] == 5:
				fase5(scr)
				
			if (fruta[0],fruta[1]) in cobra or (fruta[0],fruta[1]) in barreiras:
				gera_fruta()
				
			ch = scr.getch()
		
			if ch == ord('w') or sentido[0] == '^':
				scr.addch(cobra[0][0],cobra[0][1]," ")
				move_acima()
			elif ch == ord('s') or sentido[0] == 'V':
				scr.addch(cobra[0][0],cobra[0][1]," ")
				move_abaixo()
                        else:
			        move_esquerda()


			cabeca = [cobra[-1][0],cobra[-1][1]]

			if (cabeca[0],cabeca[1]) in cobra[1:-1]:
				morre(scr)

			if cabeca == fruta:
				gera_fruta()
				cobra.insert(0,(cobra[0][0],cobra[0][1]))
				cobra.insert(2,(cobra[2][0],cobra[2][1]))
				pontos[0] += speed[1]
				
			if (cabeca[0],cabeca[1]) in barreiras:
				morre(scr)			

			if vidas[0] == 0 or fase[0] == 6:
				end(scr)
				break
		
			scr.addch(cobra[0][0],cobra[0][1]," ")
     
       
			time.sleep(speed[0])

		if vidas[0] == 0 or fase[0] == 6:
			scr.clear()
			continua(scr)
			while True:
				continu = scr.getch()
				if continu == ord('s') or ch == ord('S'):
					if speed[2] == 'f':
						speed[0],speed[1] = 0.2 , 5
					elif speed[2] == 'm':
						speed[0],speed[1] = 0.1 , 10
					elif speed[2] == 'd':
						speed[0],speed[1] = 0.06 , 20
					vidas[0] = 3
					pontos[0] = 0
					fase[0] = 1
					barreiras = []
					scr.addstr(16,31,"SIM!")
					scr.refresh()
					time.sleep(2)
					scr.clear()
					break
				if continu == ord('n') or ch == ord('N'):
					scr.addstr(16,31,"NAO!")
					scr.refresh()
					time.sleep(2)
					break
		if vidas[0] == 0 or fase[0] == 6:
			break
		

curses.wrapper(main)
