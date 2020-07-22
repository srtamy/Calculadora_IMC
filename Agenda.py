# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 09:12:29 2020
#minha agenda

@author: amand
"""
import pysimplegui as sg
class TelaPython:
    def _init_(self):
        #layout
        layout = [
                [sg.Text('tempo'),sg.Input()],
                [sg.Text('dolar'),sg.Input()],
                [sg.Text('atividades'),sg.Input()],
                [sg.Text('calendário google'),sg.Input()],
                ]
        #janela
        #dados
        
