#!/usr/bin/env python
# coding: utf-8

# <h1>Arbeidskrav 2</h1>

# In[1]:


'''
Arbeidskrav 2

Av Eline Kaupang Petersen (eline.kaupang.petersen@nmbu.no)

Oppdatert 2026 11 12
'''


# <h2>Oppgave 1</h2>

# Brukerinput
alder = int(input("Hvilket år er du født?"))  # input() viser teksten og lager et input-felt for brukeren. int() konverterer strengen til et heltall (integer), og verdien brukeren skriver inn lagres i variabelen alder.

# Utregning
alder = 2026-alder  # Variabelens verdi overskrives og får ny verdi gjennom utregningen 2026-fødselsår=alder i 2026

# Utskrift
print(f"Ved utgangen av 2026 er du blitt {alder} år.")


# <h2>Oppgave 2</h2>

# Import av numpy-pakka
import numpy as np

# Brukerinput
antall_elever = int(input("Skriv inn antall elever:"))

# Utregning
pizza_per_elev = 0.25
antall_pizzaer = int(np.ceil(antall_elever*pizza_per_elev))  # Bruker np.ceil() for å runde opp antallet pizzaer. Bruker int() for å konvertere fra flyttall (float) til heltall (integer). 

# Utskrift
print(f"Det må kjøpes inn {antall_pizzaer} pizzaer til klassefesten.")


# <h2>Oppgave 3</h2>

# Import av numpy-pakka
import numpy as np

# Funksjonsdefinisjon
def fun_grad_til_radian(grad):
    rad = grad*np.pi/180
    return rad

# Brukerinput
v_grad = float(input("Skriv inn gradtallet:"))

# Funksjonskall
v_rad = fun_grad_til_radian(v_grad)  # Kaller funksjonen og tilordner verdien til variabelen v_rad

# Utskrift
print(f"Radianen er {v_rad:.2f}")  # Begrenser til to desimaler


# <h2>Oppgave 4</h2>

# Oppgave 4a

# Dictionary med land som nøkkel (key) og lister med hovedstad og antall innbyggere i millioner som verdier (value)
data = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873]
}

# Oppgave 4b
# Brukerinput
land = input("Skriv inn et land (eksempelvis England) for å se informasjon om landet:").capitalize()  # Bruker capitalize() for å gjøre første bokstav stor og resten små, slik at for eksempel "england" blir "England" og dermed matcher nøkkelen

land_info = data[land]

# Utskrift
print(f"{land_info[0]} er hovedstaden i {land} og det er {land_info[1]} mill. innbyggere i {land_info[0]}")

# Oppgave 4c
# Brukerinput
land_ny = input("Skriv inn navnet på et nytt land:")
hovedstad_ny = input("Skriv nå inn hovedstaden til landet:")
antall_innbyggere_ny = float(input("Skriv til slutt inn antall innbyggere i hovedstaden (oppgi i millioner):"))

# Oppdaterer dictionaryen
data.update({land_ny: [hovedstad_ny, antall_innbyggere_ny]})

# Utskrift
print(data)


# <h2>Oppgave 5</h2>

# Import av numpy-pakka
import numpy as np

# Funksjonsdefinisjon
def fun_areal_og_ytre_omkrets(a, b):
    r = a/2  # Regner ut radius

    A_halvsirkel = (np.pi*r**2)/2  # Deler på 2 for å finne arealet til halvsirkel
    O_halvsirkel = np.pi*r  # Halvparten av 2πr = halvsirkel

    A_rettv_trekant = b*a/2
    c = np.sqrt(a**2 + b**2)  # Hypotenusen

    A_figur = A_halvsirkel + A_rettv_trekant
    O_figur = O_halvsirkel + b + c  # a ligger "inni" figuren, telles derfor ikke med

    return A_figur, O_figur  # Funksjonen returnerer areal og "ytre" omkrets av figuren

# Deklarering av variabler
kat_a = 8.0  # Også diameter i halvsirkelen
kat_b = 15.0

# Funksjonskall
(areal, omkrets) = fun_areal_og_ytre_omkrets(kat_a, kat_b)  # Kaller funksjonen og returargumentet er tuppel med to verdier
print(f"Arealet til figuren: {areal:.2f}")  # Begrenser til to desimaler
print(f"Den 'ytre' omkretsen til figuren: {omkrets:.2f}")  # Begrenser til to desimaler


# <h2>Oppgave 6</h2>

# Import av numpy- og pyplot-pakka
import numpy as np
import matplotlib.pyplot as plt

# Funksjonsdefinisjon
def f(x):
    return -x**2 - 5

x_verdier = np.linspace(-10, 10, 200)  # Lager array med 200 punkter jevnt fordelt på intervallet [-10, 10]. 

# Plotting
plt.figure(1)
plt.plot(x_verdier, f(x_verdier))  # Bruker arrayen for de 200 punktene, disse utgjør x-verdiene (første argument), og funksjonen brukes for å regne ut -x²-5 for hvert datapunkt som gir y-verdiene (andre argument)  
plt.grid()
plt.show()