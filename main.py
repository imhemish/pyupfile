import requests
import json
import clipboard
from tkinter import Tk
from tkinter.filedialog import askopenfilename
Tk().withdraw()
filename = askopenfilename()
myfiles = {'file': open(filename ,'rb')}
url = "https://file.io"
postrequest = requests.post(url, files = myfiles)
postrequestresponse = postrequest.text
jsonloadedresponse = json.loads(postrequestresponse)
downloadlink = jsonloadedresponse["link"]
print(downloadlink)
print("Download Link Copied to Clipboard. Press Enter to Exit.")
clipboard.copy(downloadlink)
input()