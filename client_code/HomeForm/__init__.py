from ._anvil_designer import HomeFormTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

#
# This is the Python code that makes this feedback form work.
# It's a Python class, with a method that runs when the user
# clicks the SUBMIT button.
#
# When the button is clicked, we send the contents of the
# text boxes to our Server Module. The Server Module records
# the feedback in the database, and sends an email to the
# app's owner (that's you!).
#
# To find the Server Module, look under "Server Code" on the
# left.
#
import tkinter as tk
from huggingface_hub import InferenceClient

# Replace with your model and token
client = InferenceClient(
    "meta-llama/Meta-Llama-3.1-8B-Instruct",
    token="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",
)





def GUI():
    global chatlog, textbox, send_button

    # Initialize Tkinter window
    gui = tk.Tk()
    gui.title("PolicyPro Chat")
    gui.geometry("900x750")

#############----MENU-----################
    
    # Create a menu bar
    menu_bar = tk.Menu(gui)
    gui.config(menu=menu_bar)

    # Create a file menu
    file_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="File", menu=file_menu)


    # Add "Open File" and "Save File" commands
    file_menu.add_command(label="Open File", command="")
    file_menu.add_command(label="Save File", command="")

    
    
#############---CHAT AREA---#############

    
    # Text area to display messages
    chatlog = tk.Text(gui, bg="#2C3E50", fg='white')
    chatlog.config(state=tk.DISABLED)
    chatlog.pack(fill=tk.BOTH, expand=True)

    # Input frame
    input_frame = tk.Frame(gui)
    input_frame.pack(fill=tk.X, side=tk.BOTTOM)
    
    # Textbox for user input
    textbox = tk.Text(gui, bg="#ABB2B9", fg='white', width=50, height=3)
    textbox.pack(fill=tk.X)

    
    
############---SEND BUTTON--################
    
    # Button to send messages
    send_button = tk.Button(input_frame, text="Send")
    send_button.pack(side=tk.RIGHT)
    
    



############--- MAIN ----############

 # Create a new frame for the buttons on the right
    button_frame = tk.Frame(gui)
    button_frame.pack(side=tk.TOP, fill=tk.Y)

    # Add buttons to the frame
    button1 = tk.Button(button_frame, text="Button 1", command=open_file)
    button1.pack(pady=10)
    button2 = tk.Button(button_frame, text="Button 2", command=save_file)
    button2.pack(pady=10)

    

    gui.mainloop()


   






        
if __name__ == "__main__":
    GUI()
