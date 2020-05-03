from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
#root.geometry('100x100')
#Display the GUI at the center of the screen
windowWidth     = root.winfo_reqwidth()
windowHeight    = root.winfo_reqheight()
positionRight   = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown    = int(root.winfo_screenheight()/2 - windowHeight/2)
root.geometry("+{}+{}".format(positionRight, positionDown))
root.title('DropDowns')
root.iconbitmap('./Icon_File.ico')

try:
    global city,quality,category
    api_request = requests.get('http://www.airnowapi.org/aq/observation/zipCode/current/?format=text/csv&zipCode=83530&distance=25&API_KEY=-687A-4B16--')
    api         =   json.loads(api_request.content)
    city        =   api[0]['ReportingArea']
    quality     =   str(api[0]['AQI'])
    category    =   api[0]['Category']['Name']
    #output      =   'City' + '\t' + city + '\nAir Qality' + '\t' +  quality + '\nCategory' + '\t' +  category
except Exception as e:
    api         =   'Error During load'

font    =   ('Helvetica',12)
bg      =   ''

if category ==  'Good':
    bg      =   '#00E400'
elif category == 'Moderate':
    bg      =   '#ffff00'
elif category == 'Unhealthy for Sensitive Groups':
    bg      =   '#ff7e00'
elif category == 'Unhealthy':
    bg      =   '#ff0000'
elif category == 'Very Unhealthy':
    bg      =   '#99004c'
elif category == 'Hazardous':
    bg      =   '#7e0023'


city_label  = Label(root, text='City', font=font, bg=bg)
aqi_label  = Label(root, text='AQI', font=font, bg=bg)
category_label  = Label(root, text='City', font=font, bg=bg)

cityVal     =   Label(root,text=city, font=font, bg=bg)
aqiVal     =   Label(root,text=quality, font=font, bg=bg)
categoryVal     =   Label(root,text=category, font=font, bg=bg)

city_label.grid(row=0, column=0, pady=10)
aqi_label.grid(row=1, column=0)
category_label.grid(row=2, column=0)

cityVal.grid(row=0, column=1)
aqiVal.grid(row=1, column=1)
categoryVal.grid(row=2, column=1)

root.config(background=bg)

#myLabel     =   Label(root,text=output, font=('Helvetica',12), bg='green')

#myLabel.pack()

root.mainloop()