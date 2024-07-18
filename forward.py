import os
import FreeSimpleGUI as psg
import sys
import subprocess

listing = {
	"1": "Hero",
	"2": "Rosie",
	"3": "Diggins",
	"4": "Vivian",
	"5": "Snivels",
	"6": "Rex",
	"7": "McJunker",
	"8": "Duna",
	"9": "Human Duna",
	"10": "Bea Ginner",
	"11a": "Devolved Rosie",
	"11b": "Devolved Rosie with Hat",
	"12": "Beth",
	"13": "Denture Shark",
	"14": "Nevada",
	"15": "Saurhead",
	"16": "Samurai",
	"17": "KL-33N",
	"18": "Mole Man",
	"19": "Raptin",
	"20": "Mr. Richmond",
	"21": "Digadig Chieftain",
	"22": "B.B. Bullwort",
	"23": "Police Bullwort",
	"24": "Medal-Dealer Joe",
	"25": "Captain Woolbeard",
	"26": "Nick Nack",
	"27": "Oonga Oonga",
	"28": "Shopkeeper",
	"29": "Dynal",
	"30": "Digadig Tribesman",
	"31": "Holt",
	"32": "Blambeau",
	"33": "Dinaurian",
	"34": "B.B. Bandit (Boy)",
	"35": "B.B. Bandit (Girl)",
	"36": "Police Officer",
	"37": "Staff Member",
	"38": "Small Boy",
	"39": "Jenna",
	"40": "Captain Travers",
	"41": "Mask Lady",
	"42": "Laurence",
	"43": "Old Woman",
	"44": "Miner",
	"45": "Tipper",
	"46": "Cold Person",
	"47": "Margaret"
}

layout = [[psg.DropDown(list(listing.values()), key = "drop", default_value = "Hero"), psg.Button("Submit")]]
window = psg.Window("", layout, grab_anywhere = True, font = "-size 12")
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if (event == psg.WINDOW_CLOSED) or (event == "Quit"):
        break
    elif (event == "Submit"):
        for k in list(listing.keys()):
            if (listing[k] == values["drop"]):
                number = k
                break
        subprocess.run(["swap.exe", sys.argv[1], "output", number])
        break
