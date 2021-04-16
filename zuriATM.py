# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 22:58:47 2021

@author: Immanuel
"""

import datetime
import random

print("WELCOME TO BANK OF OJI!!!")
print("Insert Your Card Here")
atmpin = 3005
#we will store the atm pin here#
transaction = ["Check Balance","Deposit Money","Withdrawal", 
               "Transfer","Change Your Pin", "Quit"   ]
#we are storing all the tramsactions here#
activebal = 500000
#we are storing a fix amount as the money the person has
pin = int(input("Enter in your pin: "))


print()

def login():
    if pin == 3005:
        now = datetime.datetime.now()
    print ("Current date and time : ")
    print (now.strftime("%Y-%m-%d %H:%M:%S"))

login()

print('Choose your transaction: ')
print('1. Withdrawal')
print('2. Deposit')
print('3. Complaint')
print('4. Register')
print('5. Recharge')

trans = input("transaction: ")

def generateAccountNumber():
    print('Generating Account Number')
    generated_num = random.randrange(1111111111,9999999999)
    print(f'{generated_num}')

def withdraw():
        withdraw = input('How much would you like to withdraw: ')
        print (f'You withdrew {withdraw} succesfully')
        
def deposit():
        depo = int(input('How much would you like to deposit?: '))
        currentbal = (activebal) + (depo)
        print (f'Current balance is {currentbal}')        

def complaint():
        comp = input('What issue will you like to report?: ')
        print(f'your complaint {comp} has been taken')
        print ('Thank you for contacting us')

def register():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    password = input('Enter your password: ')
    print(f'{first_name}  {last_name}  with the password {password} has been added')
    generateAccountNumber()

def recharge():
    print('Choose a network')
    print('1. MTN')
    print('2. GLO')
    print('3. AIRTEL')
    print('4. 9MOBILE')

net_work = input('Enter the Network: ')
print(f'{net_work}')

def MTN():
    amount = int(input("Enter amount you want to buy: "))
    print(f'{amount} recharged')
    
def GLO():
    amount = int(input("Enter amount you want to buy: "))
    print(f'{amount} recharged')

def AIRTEL():
    amount = int(input("Enter amount you want to buy: "))
    print(f'{amount} recharged')

def MOBILE():
    amount = int(input("Enter amount you want to buy: ")) 
    print(f'{amount} recharged')

        
if trans == ('1'):
    withdraw()       
       
if trans == ('2'):    
    deposit()        
        
if trans == ('3'):
    complaint()    

if trans == ('4'):
    register()    

if trans == ('5'):
    recharge()
    
if net_work == ('1'):
    MTN() 

if net_work == ('2'):
    GLO()

if net_work == ('3'):
    AIRTEL()

if net_work == ('4'):
    MOBILE()    
    
    