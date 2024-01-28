from taipy.gui import Gui
from pyautogui import press

# user interaction function
def on_change(state, var_name, var_value):
    # declared globally in order to preserve the changes to their value
    global mailbox_locked
    global greenhouse
    global mailbox_created
    global statue_created

    # mansion object selection
    if var_name == "mansion_select":
        match var_value :
            case  "Mailbox": 
                if mailbox_locked == True:
                    state.mansion_text = "You go to the mailbox. It is locked, likely electronically."
                    state.mansion_text2 = "A wire leads out the back of it and into the wall connecting to the garden."
                    return
                
                state.mansion_text = "You look inside the mailbox. There is a single letter written entirely in latin."
                state.mansion_text2 = ""
                state.mailbox_pane = True
                if not mailbox_created:
                    gui.add_page("Mail_Pane",mailbox_text,"main.css")
                return
            case "Painting":
                state.mansion_text = "You walk up to a painting. It depicts a small family posing together; by the appearance of their clothes and the weathered look of the piece it must have been from a time long ago."
                state.mansion_text2 = "You see a small white piece of paper sticking out the bottom of the frame. A note. It reads the number 1001."
                return
            case "Party RSVP":
                state.mansion_text = "You find a pile of ornate RSVP cards stacked neatly on a desk, their finishings glistening in the light."
                state.mansion_text2 = "You pick one up and flip it over. Blank."
                return
            case "Lampshade":
                state.mansion_text = "You stumble across a mangled lamp in the dark. You attempt to turn it on, but nothing happens."
                state.mansion_text2 = "You look under the lampshade. There is nothing but dust and cobwebs. A lone spider scurries across the desk."
                return
            case "Rug":
                state.mansion_text = "Whilst exploring the mansion's rooms, you feel the ground soften. You have stepped on a lavish rug, perhaps made from the skin of a hunted animal."
                state.mansion_text2 = "You look under the rug, but find nothing. The rug is blinking back at you."
                return
            
    # garden object selection
    if var_name == "garden_select":
        match var_value :
            case  "Greenhouse": 
                state.garden_text = "Despite the largley abandoned and uncared for feel of the rest of the house, this greenhouse, standing proudly at the back of the garden, appears to be looked after regularly."
                state.garden_text2 = "A log book for the plants lies by the entrance. For each plant, the latin family name and the code are recorded inside."
                state.greenhouse = {"Plant":["Tulip","Lavender","Garlic","Water Spinach","Morning Glory","Lily","Lettuce","Oregano","Dahlia","Onion","Chicory","Sweet Potato","Mint","Asparagus","Aloe Vera","Basil","Sunflower","Thyme","Bindweed","Daisy"],
                                    "Family":["Liliaceae","Lamiaceae","Liliaceae","Convolvulaceae","Convolvulaceae","Liliaceae","Asteraceae","Lamiaceae","Lamiaceae","Liliaceae","Asteraceae","Convolvulaceae","Lamiaceae","Liliaceae","Liliaceae","Lamiaceae","Asteraceae","Lamiaceae","Convolvulaceae","Asteraceae"],
                                    "ID":["23","45","37","36","84","08","43","92","26","75","28","54","64","78","95","04","15","33","86","52"]}

                press("f5")
                return
            case "Plant pots":
                state.garden_text = "The walls of the garden are littered with plant pots of varying shape and size."
                state.garden_text2 = "Glancing at the plant nearest you, it appears to be withered and dying, the name of its family italicised on a plaque."
                return
            case "Pond":
                state.garden_text = "You look into the pond. Many fish swim around the water, bringing the odd splash of colour to its murky gray."
                state.garden_text2 = "Peering further in, you can barely make out the bottom of the pond behind a cloud of silt and mud. Not somewhere worth searching further."
                return
            case "Statue":
                state.garden_text = "You notice a statue, overrun with vines and clearly not maintained."
                state.garden_text2 = "Upon closer look, you see a control fixed to the back of it with a series of switched lining it."
                
                state.statue_pane = True
                if not statue_created:
                    gui.add_page("Switches",statue_slider)
                return
            case "Overgrown grass":
                state.garden_text = "You step into the grass. It is too thick to go further."
                state.garden_text2 = "The shrill cry of cicadas resonates out from the grass and through the cold air."
                return
    
    # if passcode is correct, unlock door
    if var_name == "passcode":
        match var_value :
            case 36845486: 
                state.status = [
                    "S",
                    "UNLOCKED"
                ]
                state.door_text = "You enter the code and hear the door click open."
                state.door_dialog = True
                gui.add_page("Blahaj",page4_md)
                return

    # if switches are correct then the mail box unlocks
    if var_name == "toggle1" or var_name == "toggle2" or var_name == "toggle3" or var_name == "toggle4":
        if state.toggle1 == "On" and state.toggle2 == "Off" and state.toggle3 == "Off" and state.toggle4 == "On":
            mailbox_locked = False
            return
        else:
            mailbox_locked = True
            return

# root directory - web page title
root_md =  """     
<|navbar|>
# MANSION ESCAPE
"""

# status of the final door - initially locked
status = [
    "E",
    "LOCKED"
]

# initialising values for user interaction and text
greenhouse = []
mansion_text = ""
mansion_text2 = ""
garden_text = ""
garden_text2 = ""
door_text = "The door is heavy, and will not budge. A heavy, gold padlock adornes the front."
door_dialog = False
mailbox_pane = False
statue_pane = False
mailbox_locked = True
value = 0
toggle1 = ""
toggle2 = ""
toggle3 = ""
toggle4 = ""
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

statue_slider = "<|{toggle1}|toggle|lov=On;Off|unselected_value=Off|><|{toggle2}|toggle|lov=On;Off|unselected_value=Off|><|{toggle3}|toggle|lov=On;Off|unselected_value=Off|><|{toggle4}|toggle|lov=On;Off|unselected_value=Off|>"

# page layouts - unchangable other than variables
page1_md = "You find yourself locked in a mansion.\n\n <|{mansion_select}|selector|lov=Select an Item to Inspect;Mailbox;Painting;Party RSVP;Lampshade;Rug|dropdown|>\n<|{mailbox_pane}|pane|anchor=right|page=Mail_Pane|>\n\n<|{mansion_text}|text|>\n\n<|{mansion_text2}|text|>\n"
page2_md = "You enter a garden.\n\n <|{garden_select}|selector|lov=Select an Item to Inspect;Greenhouse;Plant pots;Pond;Statue;Overgrown grass|dropdown|>\n\n<|{garden_text}|text|>\n\n<|{garden_text2}|text|>\n\n<|{statue_pane}|pane|anchor=top|page=Switches|>\n<|{greenhouse}|table|>\n\n"
page3_md = """  <|{door_text}|text|>\n\n<|{passcode}|number|><|{status}|status|>\n<|{door_dialog}|dialog|page=Blahaj|>\n

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

Pushing the door slowly open, you are greeted with a magnificent BLAHAJ waiting on the other side. Freedom. \n\n
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
gui = Gui(pages=pages,css_file="main.css")
gui.run(use_reloader=True)


