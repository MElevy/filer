import PySimpleGUI as sg
import os
sg.theme('DarkAmber')
layout=[[sg.In('file to open/old name', key='in'), sg.FileBrowse(target='in')],
               [sg.In('what to write/new name')],
               [sg.Button('write'), sg.Button('append'), sg.Button('read')],
               [sg.Button('rename'), sg.Button('delete', button_color='red')],
               [sg.Output(size=[43,5])]]
window=sg.Window('filer', layout)
while True:
	event, values=window.read()
	if event=='write':
		f=open(values['in'], 'w')
		f.write(values[1])
		f.close()
	elif event==sg.WIN_CLOSED:
		break
	elif event=='append':
		f=open(values['in'], 'a')
		f.write(values[1])
		f.close()
	elif event=='read':
		f=open(values['in'], 'r')
		for line in f:
			print(line, end='')
		f.close()
	elif event=='rename':
		os.rename(values['in'], values[1])
	elif event=='delete' and sg.popup_yes_no('are you sure you want to delete this file?', 'contents will be lost forever')=='Yes':
		os.remove(values['in'])
window.close()