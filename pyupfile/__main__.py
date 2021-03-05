import requests
import json
import clipboard
import time
def main():
	temp = None
	try:
		import tkinter
		temp = 1
	except:
		temp = 0
	if temp == 0:
		print("No Valid Tkinter installation found. Either tkinter is not installed or tkinter is not supported on this platform.")
	if temp == 1:
		try:
			from tkinter import Tk
			from tkinter.filedialog import askopenfilename
			Tk().withdraw()
			filename = askopenfilename()
			myfiles = {'file': open(filename ,'rb')}
			url = "https://file.io"
			postrequest = requests.post(url, files = myfiles)
			jsonloadedresponse = json.loads(postrequest.text)
			downloadlink = jsonloadedresponse["link"]
			print(downloadlink)
			clipboard.copy(downloadlink)
			time.sleep(1)
		except:
			print("Error")
if __name__ == "__main__":
	main()