#Importing the libraries

import pyttsx3
engine=pyttsx3.init() 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from textblob import TextBlob
import wikipedia
import pyaudio
from textblob import TextBlob as tb
import pywhatkit


while True:
	#Documentation
	print("Choose the mode of output you want , \n chat is the text conversion between the user and the AI whereas voice conversion is the vocal or sound conversion between human and AI\n Choose ==-> \n ::1:: for chat \n\n ::2:: for voice \n \n ::3:: for exit \n \n ::4:: to get back \n")
	#Configuration
	config_type_output=int(input('enter here: '))
	#Logic


#Chat section
	if config_type_output==1:
		print('welcome user, lets chat :)')
		print('Please enter the number according to the type of chatting you want to perform \n\n Options ==-> \n\n ::1:: for Tchat \n\n ::2:: for RaudioIchat \n\n ::3:: for IaudioRchat \n\n ::4:: for exit \n\n ::5:: to get back')
		config_type_chat=int(input('enter here: '))
		if config_type_chat==1:
			print("Welcome user , Let's start Total chat , Tchat conversation")

			print('enter the number next to the option, according to your need, \n Options==-> \n::1:: for Chatting \n\n ::2:: for Wiki \n\n ::3:: for Math \n\n ::4:: for Search/Browse \n\n ::5:: for Data Science')
			main = int(input(': '))
			if main==1:
				#coding area
				print('Welcome to the chatting section')
			elif main==2:
				#coding area
				print('Welcome to the Wiki section')
				w=input(': ')
				result=wikipedia.summary(w,2)
				print(result + '\n\n')
			elif main==3:
				#coding area
				print('Welcome to the Math section')
				print("This is the mathematics section")
				print("Normal \n Advance \n Extra-Ordinary")
				config2 = input("config: ").lower()
				if config2 == "normal":
					print("This is the normal section")
					main1A = float(input("first number: "))
					op = input("operator: ")
					main1B = float(input("second number: "))
					if op == '+':
						print(main1A + main1B)
					elif op == '-':
						print(main1A - main1B)
					elif op == '*':
						print(main1A * main1B)
					elif op == '/':
						print(main1A / main1B)
					else:
						print("INVALID OPERATOR")
				elif config2 == "advance":
					print("This is the advance section")
					main2A = float(input("first number: "))
					op = input("operator: ")
					main2B = float(input("second number: "))
					if op == '+':
						print(main2A + main2B)
					elif op == '-':
						print(main2A - main2B)
					elif op == '*':
						print(main2A * main2B)
					elif op == '/':
						print(main2A / main2B)
					elif op == '%':
						print(main2A % main2B)
					elif op == 'square':
						print(main2A * main2A)
						print(main2B * main2B)
					else:
						print("INVALID OPERATOR")
				elif config2 == "extra-ordinary":
					print("This is the extra ordinary section")
				else:
					print("INVALID INPUT")
			elif main==4:
				#coding area
				print('Welcome to the Search OR Borwsing section')
				print('Enter the number according to the required options \n ::1::youtube \n\n ::2::whatsapp \n\n::3::google_search \n\n::4::Information_with_keywords \n')
				c11=int(input(': '))
				if c11==1:
					c=input('enter the keyword to search on YT: ')
					pywhatkit.playonyt(c)
					print('Playing...')
				elif c11==2:
					n = input('enter rcv number including +91 : ')
					msg = input('enter the message to send: ')
					h = int(input('hours in 24 format : '))
					m = int(input('minutes: '))
					pywhatkit.sendwhatmsg(n , msg , h , m)
				elif c11==3:
					g=input('enter the keyword to search: ')
					pywhatkit.search(g)
					print('searching...')
				elif c11==4:
					i=input('enter the keyword to get info: ')
					pywhatkit.info(i,int(input(': ')))
				else:
					print("INVALID INPUT")


			elif main==5:
				#coding area
				print('Welcome to the Data Science section')
				config3 = input("choose the option you want to use: ")
				if config3 == 'sentiment':
					text = tb(input("enter the sentence for analysis: "))
					result = text.sentiment
					print(result)
				else:
					print('INVALID INPUT')


		elif config_type_chat==2:
			print("Welcome user , Let's start Return audio Input chat , RaudioIchat conversation")
			engine.say('Welcome user , lets start return audio input chat , RaudioIchat conversation')
			engien.runAndWait()
		elif config_type_chat==3:
			print("Welcome user , Let's start Input audio Return chat , IaudioRchat conversation")
			engine.say('welcome user, lets start input audio return chat , IaudioRchat conversation')
			engine.runAndWait()
		elif config_type_chat==4:
			exit
		elif config_type_chat==5:
			break
		else:
			print('INVALID INPUT')


#Voice section

	elif config_type_output==2:
		print('welcome user, lets start a vocal conversation')
		#Coding area
		#Documentation
		print('You have successfully selected the option voice option .\n But for more clarity please mention any \n from the given options \n \n')
		voices=engine.getProperty('voices')
		print('Enter ::1:: for female voice \n\n ::0:: for male voice \n')
		engine.setProperty('voice',voices[int(input('enter here: '))].id)

		print('Options are here ==-> \n\n ::1:: for Taudio \n\n ::2:: for RaudioIchat \n\n ::3:: for IaudioRchat \n\n ::4:: for exit \n\n ::5:: to get back \n')
		
		#Configuration
		config_type_voice=int(input('enter here: '))
		#Logic
		if config_type_voice==1:
			engine.say('WELCOME, Lets Start Total audio , Taudio conversation')
			engine.runAndWait()

		elif config_type_voice==2:
			engine.say('WELCOME, Lets Start Return audio and Input chat , RaudioIchat conversation')
			engine.runAndWait()

		elif config_type_voice==3:
			engine.say('WELCOME, Lets Start Input audio and Return chat , IaudioRchat conversation')
			engine.runAndWait()

		elif config_type_voice==4:
			exit

		elif config_type_voice==5:
			break

		else:
			print('INVALID INPUT')



	#Negative input cases
	elif config_type_output==3:
		exit
	elif config_type_output==4:
		break
	else:
		print('INVALID INPUT')