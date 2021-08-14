import queue
import PySimpleGUI as sg
from libhs import checksum
import threading
from queue import Queue
from libhs import getico

#windows Layout
layout = [  [sg.Text("File:", size=(8,1), justification = 'right'), sg.Input(key='-FILE-'), sg.FileBrowse(size=(6,1))],
            [sg.Text('Checksum:', size=(8,1), justification = 'right'), sg.InputText(key = '-PRESUM-'), sg.Button('Clear',size=(6,1))],
            [sg.Text('Algorithm:', size=(8,1), justification = 'right'), sg.Combo(['SHA1', 'SHA256', 'MD5'], key = 'algo', default_value='SHA1', size=(9,1)), sg.Button('Run', size=(6,1)),sg.Button('Stop', size = (6,1))],
            [sg.Text(key = '-ERROR-', size = (57,1), justification='centre')],
            [sg.ProgressBar(100, orientation='h', size=(43, 6), key='-PGBAR-')]
         ]

# Create the Window
window = sg.Window('harium gui', layout, icon="./assets/logo.ico")
#define variables
processing = False
q = Queue()

#main
while True:
    event, values = window.read(timeout = '10')
    
    #exit window or stop
    if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Stop':
        if processing == True:
            processing = False
            window['-ERROR-'].update('Processing Stopped!')
        else:
            window['-ERROR-'].update('Nothing is running to stop!')
        

        if event == sg.WIN_CLOSED or event == 'Cancel':
            break

    elif event == 'Clear':
        window['-PRESUM-'].update("",background_color = 'snow' )

    elif event == 'Run':

        if processing:
            window['-ERROR-'].update('Wait until the current process is completed.')
        else:
            #input sanitisation
            q = Queue()

            if values['-FILE-'] == '':
                window['-FILE-'].update(background_color = 'salmon')
                window['-ERROR-'].update('Enter a filepath!')
            else:
                window['-FILE-'].update(background_color = 'snow')

                t = threading.Thread(target = checksum, args=(values['-FILE-'], values['-PRESUM-'], values['algo'].lower(), q))
                t.start()
                processing = True
                
                numofReads = q.get()

    if processing:

        i = q.get()
        try:
            i = int(i)
            if i < numofReads:
                window['-PGBAR-'].UpdateBar(i, max = numofReads)
        except:
            if i == 'match':
                window['-PRESUM-'].update(background_color = 'SeaGreen1')
                window['-ERROR-'].update('Checksum matches!')

            elif i == 'not match':
                window['-PRESUM-'].update(background_color = 'salmon')
                window['-ERROR-'].update('Checksum does not match!')
            
            else:
                window['-PRESUM-'].update(i,background_color = 'snow')
            
            processing = False