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
jsonloadedresponse = json.loads(postrequest.text)
downloadlink = jsonloadedresponse["link"]
clipboard.copy(downloadlink)