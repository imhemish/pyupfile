# pyupfile
Pyupfile allows you to upload any file to https://file.io site using their API

# Installation
Pyupfile can be installed through python package manager (pip):
```bash
python -m pip install pyupfile
```  
Note: You need to have tkinter installed on the platform on which you are running this.  
Note: On Linux systems, you may need to install additional packages for clipboard function to run correctly. Otherwise, this would result into an error.
Installation (for Ubuntu/Debian based systems)  
```bash
# apt install xclip
```   
For other distros, install xclip through your package manager.

# Usage
Pyupfile can be used in two ways:
- by running directly through command line:  
```bash
pyupfile
```
or 
```bash
python -m pyupfile
```
- by importing the 'main' function from the module and using it in other python program:  
```python
import pyupfile
pyupfile.main()
```  
In both the cases, a window would pop up asking you the location of the file to be uploaded and download link would be copied to clipboard.