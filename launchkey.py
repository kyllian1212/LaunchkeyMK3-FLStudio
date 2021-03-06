'''
every launchkey param!
'''

#fl imports
import ui
import playlist
import channels
import mixer
import patterns
import arrangement
import transport
import device
import general
import launchMapPages
import midi

#ext imports
import launchkeyConsts as lkc
import screenSysex as s
import lighting as l
import programConsts as prog

#python imports
import sys
import time

programMode = prog.MODE_OFF

'''which state every launchkey params have!'''
#DAW mode state on the launchkey
dawMode = False

#which color each pad has rn
padsColor = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
]

#which state each pad has rn
padsState = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
]

#which color each fader button has rn
faderButtonsColor = [0,0,0,0,0,0,0,0,0]

#which state each fader button has rn
faderButtonsState = [0,0,0,0,0,0,0,0,0]

lightingDict = {
    lkc.PAD_1: [padsColor[0][1],padsState[0][1]], #0
    lkc.PAD_2: [padsColor[0][2],padsState[0][2]], #1
    lkc.PAD_3: [padsColor[0][3],padsState[0][3]], #2
    lkc.PAD_4: [padsColor[0][4],padsState[0][4]], #3
    lkc.PAD_5: [padsColor[0][5],padsState[0][5]], #4
    lkc.PAD_6: [padsColor[0][6],padsState[0][6]], #5
    lkc.PAD_7: [padsColor[0][7],padsState[0][7]], #6
    lkc.PAD_8: [padsColor[0][8],padsState[0][8]], #7
    lkc.PAD_9: [padsColor[1][1],padsState[1][1]], #8
    lkc.PAD_10: [padsColor[1][2],padsState[1][2]], #9
    lkc.PAD_11: [padsColor[1][3],padsState[1][3]], #10
    lkc.PAD_12: [padsColor[1][4],padsState[1][4]], #11
    lkc.PAD_13: [padsColor[1][5],padsState[1][5]], #12
    lkc.PAD_14: [padsColor[1][6],padsState[1][6]], #13
    lkc.PAD_15: [padsColor[1][7],padsState[1][7]], #14
    lkc.PAD_16: [padsColor[1][8],padsState[1][8]], #15
    lkc.PAD_UPARROW: [padsColor[0][0],padsState[0][0]], #16
    lkc.PAD_DOWNARROW: [padsColor[1][0],padsState[1][0]], #17
    lkc.PAD_RIGHTARROW: [padsColor[0][9],padsState[0][9]], #18
    lkc.PAD_STOPSOLOMUTE: [padsColor[1][9],padsState[1][9]], #19
    lkc.FADERBUTTON_1: [faderButtonsColor[0], faderButtonsState[0]], #20
    lkc.FADERBUTTON_2: [faderButtonsColor[1], faderButtonsState[1]], #21
    lkc.FADERBUTTON_3: [faderButtonsColor[2], faderButtonsState[2]], #22
    lkc.FADERBUTTON_4: [faderButtonsColor[3], faderButtonsState[3]], #23
    lkc.FADERBUTTON_5: [faderButtonsColor[4], faderButtonsState[4]], #24
    lkc.FADERBUTTON_6: [faderButtonsColor[5], faderButtonsState[5]], #25
    lkc.FADERBUTTON_7: [faderButtonsColor[6], faderButtonsState[6]], #26
    lkc.FADERBUTTON_8: [faderButtonsColor[7], faderButtonsState[7]], #27
    lkc.FADERBUTTON_ARMSELECT: [faderButtonsColor[8], faderButtonsState[8]] #28
}

'''launchkey functionment'''
#enable daw mode
def enableDAW():
    global dawMode
    dawMode = True
    device.midiOutMsg(0x9F, 0x0F, 0x0C, 0x7F)

#disable daw mode
def disableDAW():
    global dawMode
    dawMode = False
    device.midiOutMsg(0x9F, 0x0F, 0x0C, 0x00)

def modeChange(mode):
    global programMode
    programMode = mode