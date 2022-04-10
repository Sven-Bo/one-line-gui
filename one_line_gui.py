import PySimpleGUI as sg  # pip install pysimplegui

# Reference:
# https://pysimplegui.readthedocs.io/en/latest/call%20reference/#popups-pep8-versions


### -- Display popup with text entry field and browse button so that a folder can be chosen.
# dir_path = sg.popup_get_folder("Select Folder")
# if not dir_path:
#     sg.popup("Cancel", "No folder selected")
#     raise SystemExit("Cancelling: no folder selected")
# else:
#     sg.popup("The folder you chose was", dir_path)



### -- Display popup window with text entry field and browse button so that a file can be chosen by user.
# file_types=Tuple[Tuple[str,str]]
# fname = sg.popup_get_file("Choose Excel file", multiple_files=True, file_types=(("Excel Files", "*.xls*"),),)
# if not fname:
#     sg.popup("Cancel", "No filename supplied")
#     raise SystemExit("Cancelling: no filename supplied")
# else:
#     sg.popup("The filename you chose was", fname)



# ### -- Display a calendar window, get the user's choice, return as a tuple (mon, day, year)
# date = sg.popup_get_date()
# if not date:
#     sg.popup("Cancel", "No date picked")
#     raise SystemExit("Cancelling: no date picked")
# else:
#     sg.popup("The date you chose was", date)


# ### -- Display Popup with text entry field. Returns the text entered or None if closed / cancelled
# text = sg.popup_get_text("Please enter a text:")
# if not text:
#     sg.popup("Cancel", "No text was entered")
#     raise SystemExit("Cancelling: no text entered")
# else:
#     sg.popup("You have entered", text)


# ### -- Show a Popup but without any buttons
# sg.popup_no_buttons("You cannot click any buttons")
#
#
# ### -- Display a Popup without a titlebar. Enables grab anywhere so you can move it
# sg.popup_no_titlebar("A very simple popup")
#
#
#
### -- Display Popup with OK button only
# sg.popup_ok("You can only click on 'OK'")
#
#
#
# ### -- Popup with colored button and 'Error' as button text
# sg.popup_error("Something went wrong")
#
#
#
# ### -- Displays a "notification window", usually in the bottom right corner of your display.
# ###    The window will slowly fade in and out if desired.
# sg.popup_notify("Task done!")
#
#
#
# ### -- Display Popup with Yes and No buttons
# answer = sg.popup_yes_no("Do you like this video?")
# sg.popup("You have selected", answer)
#
#
#
# ### -- You can easily make your own popup. Popups can be accomplished in 1 line of code:
choice, _ = sg.Window(
    "Continue?",
    [[sg.T("Do you want to subscribe to this channel?")], [sg.Yes(s=10), sg.No(s=10), sg.Button('Maybe', s=10)]],
    disable_close=True,
).read(close=True)
sg.popup("Your choice was", choice)
