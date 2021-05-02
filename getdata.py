import json
import openpyxl
from datetime import date



def getDate():
    todays_date = date.today()

    dateString = ''
    if(len(str(todays_date.day)) == 1):
        dateString += '0'+str(todays_date.day)+'_'
    else:
        dateString += str(todays_date.day)+'_'

    if(len(str(todays_date.month)) == 1):
        dateString += '0'+str(todays_date.month)+'_'
    else:
        dateString += str(todays_date.month)+'_'

    dateString += str(todays_date.year)

    return dateString





def getData(filename):

    wb = openpyxl.load_workbook(filename)

    sheet = wb.active

    class1 = sheet['C11']
    class2 = sheet['D11']
    class3 = sheet['E11']
    class4 = sheet['F11']

    data = {
            'class1':class1.value,
            'class2':class2.value,
            'class3':class3.value,
            'class4':class4.value
             }

    with open('data.txt','w') as outfile:
        json.dump(data,outfile)


    print('done')



filename = 'IV SEM AI_ZOOM_CLASS_LINK_'+getDate()+'.xlsx'


try:
    getData(filename)
except Exception as e:
    print('no such file, provide a valid file')
    print(filename)
    print(e)
