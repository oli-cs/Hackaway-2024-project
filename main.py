from taipy.gui import Gui
from pyautogui import press

# user interaction function
def on_change(state, var_name, var_value):
    # mansion object selection
    global mailbox_locked
    global greenhouse
    global mailbox_created
    global statue_created


    if var_name == "mansion_select":
        match var_value :
            case  "Mailbox": 
                if mailbox_locked == True:
                    state.mansion_text = "You go to the mailbox. It is locked."
                    return
                
                state.mansion_text = "You look in the mailbox. There is a single letter."
                state.mailbox_pane = True
                if not mailbox_created:
                    gui.add_page("Mail_Pane",mailbox_text)
                return
            case "Painting":
                state.mansion_text = "You walk up to a painting. You see a note sticking out of its frame. It reads 42."
                return
            case "Party RSVP":
                state.mansion_text = "You flip over an invite. Blank."
                return
            case "Lampshade":
                state.mansion_text = "You look under the lampshade. There is nothing but dust and cobwebs."
                return
            case "Rug":
                state.mansion_text = "You look under the rug. The rug is blinking back at you."
                return
            
    # garden object selection
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
                return
            case "Plant pots":
                state.garden_text = "You look under the plant pots and there is nothing there. The name of the plant is italicised."
                return
            case "Pond":
                state.garden_text = "You look into the pond. Fishes are staring back at you."
                return
            case "Statue":
                state.garden_text = "You notice a statue. Upon closer look, you see a control fixed to the back of it."
            
                state.statue_pane = True
                if not statue_created:
                    gui.add_page("Statue_Slider",statue_slider)
                return
            case "Overgrown grass":
                state.garden_text = "You step into the grass. It is too thick to go further."
                return
    
    # if passcode is correct, unlock door
    if var_name == "passcode":
        match var_value :
            case 36845486: 
                state.status = [
                    "S",
                    "UNLOCKED"
                ]
                state.door_text = "You enter the code and hear the door click."
                state.door_dialog = True
                gui.add_page("Blahaj",page4_md)
                return

    # if slide value is correct then the mail box unlocks
    if var_name == "slideVal":
        if var_value == 100:
            mailbox_locked = False
            return
        else:
            mailbox_locked = True
            return

# root directory - web page title
root_md =  """     
<|navbar|>
# EPIC COL GAME !!!1
"""

# status of the final door - initially locked
status = [
    "E",
    "LOCKED"
]

# initialising values for user interaction and text
rsvp = "words !!"
greenhouse = []
mansion_text = ""
garden_text = ""
door_text = ""
door_dialog = False
mailbox_pane = False
statue_pane = False
mailbox_locked = True
value = 0
slideVal = 0
mansion_select = "Select an Item to Inspect"
garden_select = "Select an Item to Inspect"
passcode = 0
mailbox_created = False
statue_created = False


# pane window text/slider
mailbox_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
                Quisque facilisis vehicula scelerisque.
                *Convolvulaceae* et pharetra dui, auctor faucibus diam. Suspendisse potenti. 
                Sed ac finibus purus, ac euismod ipsum. 
                Cras bibendum turpis ac purus cursus, mattis tristique dui pellentesque. 
                Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. 
                Mauris condimentum rhoncus ante sit amet hendrerit. 
                Quisque sit amet risus neque. 
                Ut suscipit neque ac quam rhoncus, varius tincidunt purus sollicitudin. 
                Cras in dignissim tortor, sit amet maximus tortor."""
statue_slider = "<|{slideVal}|slider|width=1600px|height=250px|id='statueSlider'|text_anchor=bottom|>"

# page layouts - unchangable other than variables
page1_md = "You find yourself locked in a mansion.\n\n <|{mansion_select}|selector|lov=Select an Item to Inspect;Mailbox;Painting;Party RSVP;Lampshade;Rug|dropdown|>\n<|{mailbox_pane}|pane|anchor=right|page=Mail_Pane|>\n<|{mansion_text}|text|>\n"
page2_md = "You enter a garden.\n\n <|{garden_select}|selector|lov=Select an Item to Inspect;Greenhouse;Plant pots;Pond;Statue;Overgrown grass|dropdown|>\n\n<|{garden_text}|text|><|{statue_pane}|pane|anchor=top|page=Statue_Slider|>\n<|{greenhouse}|table|>\n\n"
page3_md = """  \n<|{passcode}|number|><|{status}|status|>\n<|{door_text}|text|>\n<|{door_dialog}|dialog|page=Blahaj|>

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
⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠉⠒⠒⠀⠁⠈⠀⠐⠈⠁⠛⠛⠛⠒⠒⠒⠀⢠⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀\n

"""

# blahaj hidden page
page4_md = """ <|{status}|status|> \n

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

# list of all pages (minus hidden pages)
pages = {
    "/": root_md,
    "Mansion": page1_md,
    "Garden": page2_md,
    "Exit": page3_md,
}

# generates the graphical user interface
gui = Gui(pages=pages)
gui.run(use_reloader=True)


