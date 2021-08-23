# -*- coding: UTF-8 -*-
# Libraries needed (pandas is not standard and must be installed in Python)
import csv
import requests
import pandas as pd
# from matplotlib import pyplot

grader_liste = []
ar_liste = []
ar_liste_tekst = []

# Insert your own client ID here
client_id = ''


# Define endpoint and parameters
for i in range(90):
    year = 1925 + i
    year_text = str(year)
    ar_liste.append(year)
    ar_liste_tekst.append(year_text)

    endpoint = 'https://frost.met.no/observations/v0.jsonld'
    parameters = {
        'sources': 'SN18700',
        'elements': 'best_estimate_mean(air_temperature P1D)',
        'referencetime': year_text + "-05-17/" + year_text + "-05-18",
    }
    # Issue an HTTP GET request
    r = requests.get(endpoint, parameters, auth=(client_id,''))
    # Extract JSON data
    json = r.json()



    # Check if the request worked, print out any errors
    if r.status_code == 200:
        data = json['data']
        #print('Data retrieved from frost.met.no!')
    else:
        print('Error! Returned status code %s' % r.status_code)
        print('Message: %s' % json['error']['message'])
        print('Reason: %s' % json['error']['reason'])



    # This will return a Dataframe with all of the observations in a table format
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)

    df = pd.DataFrame()
    for i in range(len(data)):
        row = pd.DataFrame(data[i]['observations'])
        row['referenceTime'] = data[i]['referenceTime']
        row['sourceId'] = data[i]['sourceId']
        df = df.append(row)
        #legger til verdien i en liste kalt grader
        grader_liste.append(float(df['value']))

    # These additional columns will be kept
    columns = ['sourceId','referenceTime','elementId','value','unit','timeOffset']
    df2 = df[columns].copy()
    # Convert the time value to something Python understands
    df2['referenceTime'] = pd.to_datetime(df2['referenceTime'])


    print(df2.head())
    #print(df.head())
print(grader_liste)
print(ar_liste)


#pyplot.plot(ar_liste, grader_liste, color="red", linestyle="solid", marker = "o") #tegner grafen
#pyplot.title("Gjennomsnitt grader 04.02....") #hoved-tittel
#pyplot.xlabel("årstall:") #x-akse tittel
#pyplot.ylabel("grader:") #y-akse tittel
#pyplot.show()


with open("Værdata.csv", "w") as tekst_fil:
    filskriver = csv.writer(tekst_fil)
    filskriver.writerow(["Gjennomsnittstemperaturer på 17 mai. Målt på værstasjonen på Blindern."])
    filskriver.writerow(["Dato: ", "Gjennomsnittstemperatur den dagen:"])

    for i in range(len(ar_liste)):
        filskriver.writerow(["17.05."+ ar_liste_tekst[i], grader_liste[i]])
