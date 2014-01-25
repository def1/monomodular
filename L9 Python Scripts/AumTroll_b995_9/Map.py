#!/usr/bin/env python
# encoding: utf-8
"""
Cntrlr_Map.py

Created by amounra on 2010-10-05.
Copyright (c) 2010 __aumhaa__. All rights reserved.
http://www.aumhaa.com

This file allows the reassignment of the controls from their default arrangement.  The order is from left to right; 
Buttons are Note #'s and Faders/Rotaries are Controller #'s
"""

CHANNEL = 0		#main channel (0 - 15)

CNTRLR_BUTTONS = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]  #there are 16x2 of these

CNTRLR_GRID = [0, 4, 8, 12, 1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15]	#there are 4x4 of these

CNTRLR_FADERS = [4, 8, 12, 16, 20, 24, 28, 32]		#there are 8 of these

CNTRLR_KNOBS_LEFT = [1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15]	#there are 12 of these

CNTRLR_KNOBS_RIGHT = [17, 21, 25, 29, 18, 22, 26, 30, 19, 23, 27, 31]		#there are 12 of these

CNTRLR_DIALS = [48, 51, 54, 57, 49, 52, 55, 58, 50, 53, 56, 59]		#there are 12 of these

CNTRLR_DIAL_BUTTONS = [48, 51, 54, 57, 49, 52, 55, 58, 50, 53, 56, 59]		#there are 12 of these

PAD_TRANSLATION =	((0, 0, 0, 9), (0, 1, 1, 9), (0, 2, 2, 9), (0, 3, 3, 9),		#this is used by DrumRacks to translate input to one of the visible grid squares for triggering
					(1, 0, 4, 9), (1, 1, 5, 9), (1, 2, 6, 9), (1, 3, 7, 9),			#the format is (x position, y position, note-number, channel)
					(2, 0, 8, 9), (2, 1, 9, 9), (2, 2, 10, 9), (2, 3, 11, 9),
					(3, 0, 12, 9), (3, 1, 13, 9), (3, 2, 14, 9), (3, 3, 15, 9))

FOLLOW = True		#this sets whether or not the last selected device on a track is selected for editing when you select a new track

CHOPPER_ENABLE = False		#when set True, this enables the Python ClipChopperComponent in modSlot 4 when a mod isn't present there

AUMPUSH_LINK = True

USE_PEDAL = True

MONOHM_LINK = True			#when set True, this enables an alternate configuration to be used for the controls to better suit use with the MonOhm script

TROLL_RIGHT_MODE = 2		#this is the initial mode that MixerRight on the MonOhm will be set to when first detected by the CNTRLR

TROLL_MAIN_OFFSET = 0		#this is the initial offset that MixerLeft on the MonOhm will be set to when first detected by the CNTRLR

TROLL_OFFSET = 4			#this is the offset that the CNTRLR uses when linked to the MonOhm script

#	The default assignment of colors within the OhmRGB is:
#	Note 2 = white
#	Note 4 = cyan 
#	Note 8 = magenta 
#	Note 16 = red 
#	Note 32 = blue 
#	Note 64 = yellow
#	Note 127 = green
#	Because the colors are reassignable, and the default colors have changed from the initial prototype,
#		MonOhm script utilizes a color map to assign colors to the buttons.	 This color map can be changed 
#		here in the script.	 The color ordering is from 1 to 7.	 

COLOR_MAP = [2, 64, 4, 8, 16, 127, 32]

#	In addition, there are two further color maps that are used depending on whether the RGB or Monochrome 
#		Ohm64 is detected.	The first number is the color used by the RGB (from the ordering in the COLOR_MAP array),
#		the second the Monochrome.	Obviously the Monochrome doesn't use the colors.  
#	However, the flashing status of a color is derived at by modulus.  Thus 1-7 are the raw colors, 8-14 are a fast
#		flashing color, 15-21 flash a little slower, etc.  You can assign your own color maps here:


###	 the first number is Livid(OhmModes) standard, the second is Monomdular standard, the third is Monochrome
MUTE = [2, 2, 127]
SOLO = [3, 9, 127]
ARM = [5, 5, 8]
SEND_RESET = [7, 7, 7]
STOP_CLIPS = [127, 1, 1]
STOP_CLIPS_OFF = [127, 127, 127]
SELECT = [127, 127, 127]
SELECT_ALT = [5, 5, 5]
SCENE_LAUNCH = [7, 3, 17]
USER1_COLOR = [4, 4, 29]
USER2_COLOR = [5, 5, 29]
USER3_COLOR = [6, 6, 29]
CROSSFADE_TOGGLE = [4, 4, 127]
TRACK_STOP = [127, 127, 127]
DEVICE_SELECT = [1, 1, 8]
BANK_BUTTONS = [1, 1, 1]
STOP_ALL = [127, 127, 15]
SESSION_NAV = [2, 2, 32]
SESSION_NAV_OFF = [3, 3, 33]
OVERDUB = [4, 4, 127]
LOOP = [3, 3, 127]
STOP = [127, 127, 127]
STOP_OFF = [127, 127, 127]
RECORD = [5, 5, 15]
RECORD_ON = [11, 11, 15]
PLAY = [6, 6, 127]
PLAY_ON = [18, 18, 127]
DEVICE_BANK = [127, 127, 127]
DEVICE_NAV = [1, 1, 127]
DEVICE_ON = [127, 127, 127]
DEVICE_LOCK = [4, 4, 127]
CLIP_RECORDING = [5, 11, 8] 
CLIP_STARTED = [6, 6, 32]
CLIP_STOP = [1, 127, 127]
CLIP_TRG_REC = [11, 4, 8]
CLIP_TRG_PLAY = [12, 2, 15]
ZOOM_STOPPED = [1, 127, 127]
ZOOM_PLAYING = [6, 6, 15]
ZOOM_SELECTED = [8, 1, 8]
STOP_CLIP = [127, 127, 2]

DEVICE_COLORS = {'midi_effect':2,
				'audio_effect':5,
				'instrument':7,
				'Operator':3,
				'DrumGroupDevice':6,
				'MxDeviceMidiEffect':4,
				'MxDeviceInstrument':4,
				'MxDeviceAudioEffect':4,
				'InstrumentGroupDevice':1,
				'MidiEffectGroupDevice':1,
				'AudioEffectGroupDevice':1}




"""'Operator':5
'UltraAnalog':2
'OriginalSimpler':2
'MultiSampler':2
'LoungeLizard':2
'StringStudio':2
'Collision':2
'InstrumentImpulse':2
'NoDevice':0"""

## a  http://www.aumhaa.com
