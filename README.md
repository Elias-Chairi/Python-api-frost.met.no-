# Python-api-frost.met.no

Dette er et programm som bruker frost.met.no sin api til å hente ut gjennomsnitts temperaturer på 17.mai fra 1925 til 2014.

Fungerer slik:
  * Henter ut dataene i en loop som hver gang legger det i en liste.
  * Til slutt så skriver den ut lista i csv dokumentet.


Du må også gå in på frost.met.no og generere en client ID som du putter inn i koden.

Python modules som trengs (bruker python3):
  * import csv
  * import requests
  * import pandas as pd


