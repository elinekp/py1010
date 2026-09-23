#!/usr/bin/env python
# coding: utf-8

# <h1>Arbeidskrav 1 - Sammenligning av kostnader for elbil og bensinbil</h1>

# In[18]:


'''
Arbeidskrav 1 - Sammenligning av kostnader for elbil og bensinbil

Av Eline Kaupang Petersen (eline.kaupang.petersen@nmbu.no)

Oppdatert 2026 09 23
'''

# Felles utgifter
antall_km_totalt = 10000  # [Kjørte km per år]
trafikkforsikring = 8.38*365  # [Årlig trafikkforsikringsavgift]

# Forsikring
forsikring_elbil = 5000  # [Forsikringspremie elbil, per år]
forsikring_bensinbil = 7500  # [Forsikringspremie bensinbil, per år]

# Drivstoff
strompris = 2  # [Strømpris i kr/kWh]

drivstoffbruk_elbil = 0.2  # [Drivstofforbruk elbil, målt i kWh/km]
drivstoff_pris_elbil_per_km = drivstoffbruk_elbil*strompris  # [Drivstoffpris for elbil per km]
drivstoff_pris_elbil = drivstoff_pris_elbil_per_km*antall_km_totalt  # [Drivstoffpris for elbil per år]

drivstoff_pris_bensinbil_per_km = 1  # [Drivstoffpris for bensinbil per km]
drivstoff_pris_bensinbil = drivstoff_pris_bensinbil_per_km*antall_km_totalt  # [Drivstoffpris for bensinbil per år]

#Bomutgifter
bom_elbil_per_km = 0.1  # [Bomavgift for elbil, målt i kr/km]
bom_elbil = bom_elbil_per_km*antall_km_totalt  # [Bomavgift for elbil per år]

bom_bensinbil_per_km = 0.3  # [Bomavgift for bensinbil, målt i kr/km]
bom_bensinbil = bom_bensinbil_per_km*antall_km_totalt  # [Bomavgift for bensinbil per år]

# Utregninger
pris_elbil = trafikkforsikring + forsikring_elbil + drivstoff_pris_elbil + bom_elbil
pris_bensinbil = trafikkforsikring + forsikring_bensinbil + drivstoff_pris_bensinbil + bom_bensinbil

# Utskrift
print('Årlige utgifter for elbil: ', pris_elbil, 'kr')
print('Årlige utgifter for bensinbil: ', pris_bensinbil, 'kr')

print('Årlig kostnadsdifferanse: ', pris_bensinbil - pris_elbil, 'kr')
