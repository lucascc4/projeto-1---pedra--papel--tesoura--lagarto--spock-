# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 13:09:17 2015

@author: LUCAS C
"""
from random import randint
pedra = 1
papel = 2
tesoura = 3
lagarto = 4
spock = 5
while True:
	x = str(input("Voce quer jogar um jogo?:"))
	if x == "sim" :
		wins = 0
		losses = 0
		while wins<3 and losses<3:
			computer = randint(1,5)
			print("estou pronto")
			player = (str(input("escolha pedra, papel, tesoura, lagarto ou spock: "))).lower()
			if computer == 1 and player == "pedra":
				print("empate")
				wins = 0
				losses = 0
			elif computer == 1 and (player == "papel" or player == "spock"):
				print("ganhou")
				wins += 1
				losses = 0
			elif computer == 1 and (player == "tesoura" or player == "lagarto"):
				print("perdeu")
				wins = 0
				losses += 1
			elif computer == 2 and player == "papel":
				print("empate")
				wins = 0
				losses = 0
			elif computer == 2 and (player == "tesoura" or player == "lagarto"):
				print("ganhou")
				wins += 1
				losses = 0
			elif computer == 2 and (player == "pedra" or player == "spock"):
				print("perdeu")
				wins = 0
				losses += 1
			elif computer == 3 and player == "tesoura":
				print("empate")
				wins = 0
				losses = 0
			elif computer == 3 and (player == "pedra" or player == "spock"):
				print("ganhou")
				wins += 1
				losses = 0
			elif computer == 3 and (player == "papel" or player == "lagarto"):
				print("perdeu")
				wins = 0
				losses += 1
			elif computer == 4 and player == "lagarto":
				print("empate")
				wins = 0
				losses = 0
			elif computer == 4 and (player == "pedra" or player == "tesoura"):
				print("ganhou")
				wins += 1
				losses = 0
			elif computer == 4 and (player == "papel" or player == "spock"):
				print("perdeu")
				wins = 0
				losses += 1
			elif computer == 5 and player == "spock":
				print("empate")
				wins = 0
				losses = 0
			elif computer == 5 and (player == "papel" or player == "lagarto"):
				print("ganhou")
				wins += 1
				losses = 0
			elif computer == 5 and (player == "pedra" or player == "tesoura"):
				print("perdeu")
				wins = 0
				losses += 1
		if losses == 3:
			print("voce perdeu, tente de novo")
		if wins == 3:
			print("Parabens, voce ganhou")
	if x == "nao":
		print("Voce nao é pareo para mim mesmo")
	
	