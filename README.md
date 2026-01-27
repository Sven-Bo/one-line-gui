# Make a GUI with just ONE LINE of code using Python

In this Python tutorial, I'm going to show you how to make a GUI with just one line of code - and it's really easy! GUI stands for Graphical User Interface. It is the visual part of a system that a user interacts with. In this video, I will show you how to create GUI with ONE LINE OF CODE using Python and the PySimpleGUI library.

## Video Tutorial
[![YouTube Video](https://img.youtube.com/vi/_H5hsUwv8lE/0.jpg)](https://youtu.be/_H5hsUwv8lE)

## Examples
```python
import PySimpleGUI as sg
```
| Code | Window |
| -- | -- |
| ``` sg.popup_get_folder("Select Folder") ``` |  ![popup_get_folder](demos/popup_get_folder.jpg) |
| ``` sg.popup_get_file("Choose Excel file", multiple_files=True, file_types=(("Excel Files", "*.xls*"),),) ``` |  ![popup_get_file](demos/popup_get_file.jpg) |
| ``` sg.popup_get_date() ``` |  ![popup_get_date](demos/popup_get_date.jpg) |
| ``` sg.popup_get_text("Please enter a text:") ``` |  ![popup_get_text](demos/popup_get_text.jpg) |
| ``` sg.popup_no_buttons("You cannot click any buttons") ``` |  ![popup_no_buttons](demos/popup_no_buttons.jpg) |
| ``` sg.popup_no_titlebar("A very simple popup") ``` |  ![popup_no_titlebar](demos/popup_no_titlebar.jpg) |
| ``` sg.popup_ok("You can only click on 'OK'") ``` |  ![popup_ok](demos/popup_ok.jpg) |
| ``` sg.popup_error("Something went wrong") ``` |  ![popup_error](demos/popup_error.jpg) |
| ``` sg.popup_notify("Task done!") ``` |  ![popup_notify](demos/popup_notify.jpg) |
| ``` sg.popup_yes_no("Do you like this video?") ``` |  ![popup_yes_no](demos/popup_yes_no.jpg) |
| ``` sg.Window("Continue?",[[sg.T("Do you want to subscribe to this channel?")], [sg.Yes(s=10), sg.No(s=10), sg.Button('Maybe', s=10)]],disable_close=True,).read(close=True) ``` |  ![custom_popup](demos/custom_popup.jpg) |

## Requirements
```
xlwings==0.25.3
PySimpleGUI==4.59.0
```

## More Solutions
Explore my tools and templates for Excel, automation, and more.

**[View all solutions](https://pythonandvba.com/solutions)**
## Connect with Me
- **YouTube:** [CodingIsFun](https://youtube.com/c/CodingIsFun)
- **Website:** [PythonAndVBA](https://pythonandvba.com)
- **LinkedIn:** [Sven Bosau](https://www.linkedin.com/in/sven-bosau/)
- **Contact:** [Get in Touch](https://pythonandvba.com/contact)
## Support
If you find this project helpful, consider buying me a coffee. 

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://pythonandvba.com/coffee-donation)
