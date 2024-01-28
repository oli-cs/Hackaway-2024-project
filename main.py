from taipy.gui import Gui,builder

from pyautogui import press


def on_change(state, var_name, var_value):
    global greenhouse
    if var_name == "mansion_select":
        print(var_value)
        #switch statement
        match var_value :
            case  "Mailbox":  
                state.mansion_text = "You look in the mailbox. There are no letters."
            case "Painting":
                state.mansion_text = "Painting"
            case "Party RSVP":
                state.mansion_text = "Party RSVP"
            case "Lampshade":
                state.mansion_text = "You look under the lampshade. There is nothing but dust and cobwebs."
            case "Rug":
                state.mansion_text = "You look under the rug. The rug is blinking back at you."

        
    if var_name == "garden_select":
        match var_value :
            case  "Greenhouse": 
                state.greenhouse = [["Plant","Family","id"],
                                    ["Tulip","Liliaceae","23"],["Lavender","Lamiaceae","45"],
                                    ["Garlic","Liliaceae","37"],["Water Spinach","Convolvulaceae","36"],
                                    ["Morning Glory","Convolvulaceae","84"],["Lily","Liliaceae","08"],
                                    ["Lettuce","Asteraceae","43"],["Oregano","Lamiaceae","92"],
                                    ["Dahlia","Lamiaceae","26"],["Onion","Liliaceae","75"],
                                    ["Chicory","Asteraceae","28"],["Sweet Potato","Convolvulaceae","54"],
                                    ["Mint","Lamiaceae","64"],["Asparagus","Liliaceae","78"],
                                    ["Aloe Vera","Liliaceae","95"],["Basil","Lamiaceae","04"],
                                    ["Sunflower","Asteraceae","15"],["Thyme","Lamiaceae","33"],
                                    ["Bindweed","Convolvulaceae","86"],["Daisy","Asteraceae","52"]]
                press("f5")
                
            case "Plant pots":
                state.garden_text = "You look under the plant pots. There is nothing there."
            case "Pond":
                state.garden_text = "You look into the pond. Fishes are staring back at you."
            case "Statue":
                state.garden_text = "Statue"
                state.pain = True #SET PAIN TO TRUE HERE
                #PAIN HERE AAAAAAHAHHHAHAHHHHH
            case "Overgrown grass":
                state.garden_text = "You step into the grass. It is too thick to go further."
        return
    
    if var_name == "passcode":
        match var_value :
            case 36845486: 
                state.status = [
                    "S",
                    "UNLOCKED"
                ]
                state.door_text = "You enter the code and hear a door click."

root_md = """
<|navbar|>
# EPIC COL GAME !!!1
"""


status = [
    "E",
    "LOCKED"
]

greenhouse = []
mansion_text = ""
garden_text = ""
door_text = ""
pain = builder.pane(open=False)
value = 0
mansion_select = "Select an Item to Inspect"
garden_select = "Select an Item to Inspect"
passcode = 0


page1_md = "You find yourself locked in a mansion.\n\n <|{mansion_select}|selector|lov=Select an Item to Inspect;Mailbox;Painting;Party RSVP;Lampshade;Rug|dropdown|>\n\n<|{mansion_text}|text|>\n<|{passcode}|number|>\n<|{door_text}|text|>\n"
page2_md = "You enter a garden.\n\n <|{garden_select}|selector|lov=Select an Item to Inspect;Greenhouse;Plant pots;Pond;Statue;Overgrown grass|dropdown|>\n\n<|{garden_text}|text|>\n<|{greenhouse}|table|>\n<|{pain}|pane|open=False|>\n"
page3_md = """  <|{status}|status|> \n

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢖⠲⣶⡒⠒⣲⣶⡒⡲⠖⠚⡶⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠲⣏⣅⠊⠀⠘⠃⠸⣿⣯⠳⠘⠂⠀⠘⣂⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣳⠘⠶⢏⠻⣷⣼⣲⣤⣶⣿⣧⣁⣔⣁⣁⣴⣿⡁⡹⠰⠉⢳⡆⠀⠀⠀⠀⠀⠀⠀⠀\n
⠀⠀⠀⠀⠀⠀⠀⣀⣼⡁⠐⠂⡄⣼⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⣤⢀⣼⣷⢤⡄⠀⠀⠀⠀⠀⠀\n
⠀⠀⠀⠀⠀⢰⢋⠽⡐⠛⠓⢦⣿⣿⣿⣿⣿⢿⣿⣿⣿⠛⡟⣿⣿⣿⣿⣿⣿⣵⠿⠋⢡⡙⢸⣿⠀⠀⠀⠀⠀⠀\n
⠀⠀⠀⠀⠀⠸⣮⣴⣠⡀⣴⣿⣿⣿⣿⣿⠛⡇⣿⠨⠇⠀⣇⠋⢻⡇⣿⣿⣿⣿⣿⣔⢤⣴⣾⣟⠀⠀⠀⠀⠀⠀\n
⠀⠀⠀⠀⠀⣾⣉⠈⠉⢻⣿⣿⣿⣿⠈⣿⠈⠁⡏⠀⡅⢀⣟⠀⢸⡇⠇⡟⠹⣿⣿⡿⢩⡵⠄⢹⣷⠀⠀⠀⠀⠀\n
⠀⠀⠀⠀⠀⣿⠀⠤⠀⢼⣿⣿⡿⢋⠀⣟⠀⠃⡇⠀⡃⠠⡇⢰⠀⡇⠀⡇⠀⡿⣿⡧⠀⠁⢈⣭⣿⡇⠀⠀⠀⠀\n
⠀⠀⠀⠀⠀⣿⠀⠀⣰⣿⣿⣿⣷⠘⠃⡿⠀⡇⣇⢠⣀⣀⡇⠀⠀⣇⡀⡧⠀⡇⣿⣿⣤⣿⡭⢾⣿⠁⠀⠀⠀⠀\n
⠀⠀⠀⠀⠀⢹⡶⠾⠾⣿⣿⣿⣿⠀⠤⢧⠀⠀⣷⣿⣿⢷⣿⣆⢀⡇⡀⡇⠇⣿⣿⢁⡄⠉⠀⢸⣿⠀⠀⠀⠀⠀\n
⠀⠀⠀⠀⠀⣿⠀⢀⠍⢭⣿⣿⣿⣶⣿⣾⣾⣷⣿⣻⡇⢸⣟⣿⣾⣿⣷⣿⣤⡅⣿⣦⣤⡼⣶⣿⡇⠀⠀⠀⠀⠀\n
⠀⠀⠀⠀⠀⣽⠟⠛⠟⢿⣿⣿⣿⡟⠭⣿⠛⠟⣟⢿⣷⣞⣿⡿⢻⠻⠟⡏⠁⣄⡟⠹⠇⢠⠘⢻⡧⠀⠀⠀⠀⠀\n
⠀⠀⠀⠀⠀⣧⢀⣄⠀⠾⣿⣿⣿⡇⠀⡷⠀⠀⣿⡀⠈⠉⡟⠁⢸⠂⠀⡇⡴⣿⣇⣇⣁⣲⣴⣼⡿⠀⠀⠀⠀⠀\n
⠀⠀⠀⠀⠀⡿⠈⠉⡆⣠⣿⣿⣿⠃⠈⢻⠀⠀⡇⠃⠀⠀⡏⠀⢸⣠⣴⡿⣯⣿⣿⠟⢭⠽⠉⢹⡇⠀⠀⠀⠀⠀\n
⠀⠀⠀⠀⠀⢻⡼⠶⢦⣿⣿⣿⢿⠅⠀⢸⣀⠀⡇⠀⠠⠀⡇⠀⢸⠳⡿⣿⣿⣿⣿⣶⠶⠦⢶⣿⠇⠀⠀⠀⠀⠀\n
⠀⠀⠀⠀⠀⢸⠀⢲⢱⡟⣿⣿⣾⡞⠀⢸⠀⢠⡇⠀⠀⡄⡇⠀⢸⢇⡀⡟⢿⢿⣿⠁⠀⢀⠘⣿⡇⠀⠀⠀⠀⠀\n
⠀⠀⠀⠀⠀⢻⣄⣠⣤⣤⣿⣿⣿⡷⣿⣾⣶⣿⣷⣶⡶⣶⣷⣿⣾⣶⣿⣷⣤⢸⣿⣤⣤⣨⣶⣿⠇⠀⠀⠀⠀⠀\n
⠀⠀⠀⣆⣴⢱⡏⡀⠨⢿⣿⣿⣿⣿⣿⣿⢻⡟⡟⠛⢛⡛⡟⠿⢻⣻⠟⣯⢨⢸⣿⠉⠁⠰⡞⣿⡇⠀⠀⠀⠀⠀\n
⠀⠙⢶⣿⣿⣿⢧⣤⣦⣼⣿⣿⣿⡇⢀⢸⠁⢀⡇⠀⠌⠁⣷⠀⢸⡇⢀⣿⠘⣾⣿⢷⣬⣥⣷⣿⡇⠀⠀⠀⠀⠀\n
⠀⢰⣿⠫⢿⣤⣰⠟⠻⣾⣿⣿⣿⣷⣾⣿⣼⣾⣷⣶⣧⣶⣿⣶⣾⣷⣾⣿⣷⣿⢉⣧⣤⠞⠛⣿⣿⣰⡀⡀⠀⠀\n
⠀⢤⣿⣗⡀⣝⢯⣧⣁⢸⣿⣿⣿⠿⠿⠿⢿⡟⣛⢛⡛⢛⣛⣛⣛⠻⠿⢿⣿⡟⣋⢟⣥⡔⣐⢿⣿⣿⣟⢇⡀⠀\n
⠘⠚⠛⠛⠛⠿⠟⠻⠛⠿⠛⠋⣛⣳⠒⡒⢽⠮⠿⠒⠒⠒⠂⠨⣟⡷⠢⣦⣍⣙⣛⡫⠭⠛⠛⠛⠿⠿⠟⠛⠓⠂\n
⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠉⠒⠒⠀⠁⠈⠀⠐⠈⠁⠛⠛⠛⠒⠒⠒⠀⢠⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀\n\n\n

This is BLAHAJ\n\n
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n
⢠⣾⣿⣏⠉⠉⠉⠉⠉⠉⢡⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⢿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡄⠀\n
⠈⣿⣿⣿⣿⣦⣽⣦⡀⠀⠀⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⠀⠀\n
⠀⠘⢿⣿⣿⣿⣿⣿⣿⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⠇⠀⠀\n
⠀⠀⠈⠻⣿⣿⣿⣿⡟⢿⠻⠛⠙⠉⠋⠛⠳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⡟⠀⠀⠀\n
⠀⠀⠀⠀⠈⠙⢿⡇⣠⣤⣶⣶⣾⡉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣰⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠾⢇⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⠃⠀⠀⠀\n
⠀⠀⠀⠀⠀⠀⠀⠱⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠤⢤⣀⣀⣀⣀⣀⣀⣠⣤⣤⣤⣬⣭⣿⣿⠀⠀⠀⠀\n
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣶⣤⣄⣀⣀⣠⣴⣾⣿⣿⣿⣷⣤⣀⡀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣾⣿⣿⣿⣿⡿⠿⠛⠛⠻⣿⣿⣿⣿⣇⠀⠀⠀\n
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣤⣘⡛⠿⢿⡿⠟⠛⠉⠁⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣦⠀⠀\n
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣶⣦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡄⠀\n
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⠿⠛⠉⠁⠀⠈⠉⠙⠛⠛⠻⠿⠿⠿⠿⠟⠛⠃⠀⠀⠀⠉⠉⠉⠛⠛⠛⠿⠿⠿⣶⣦⣄⡀⠀⠀⠀⠀⠀⠈⠙⠛⠂\n
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀\n

"""

pages = {
    "/": root_md,
    "Mansion": page1_md,
    "Garden": page2_md,
    "Exit": page3_md
}


gui = Gui(pages=pages)
gui.run(use_reloader=True)

