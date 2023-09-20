import math 
# Integers
print('INTEGERS:\n')

people = 7_861_304_740
# Calculations with big numbers
meals = 3
people_eat = people * meals
print(f'people_eat: {people_eat}')

days = 365
meals_per_year = people_eat * days
print(f'meals_per_year: {meals_per_year}')

# What is the data type?
print(f'type: {type(meals_per_year)}\n')  # int


# Float
print('FLOAT:\n')

# Ethernet capacity
ethernet_speed_mbps = 1000
efficiency = 0.7
maximum_capacity = ethernet_speed_mbps * efficiency
print(f'maximum_capacity: {maximum_capacity}')

# Print capacity used on the ethernet
ethernet_speed_mbps = 1000
download_speed_average = 96.25
usage = ethernet_speed_mbps / download_speed_average
print(f'usage: {usage}')


# Speed of light in m/s
speed_of_light = 299_792_458

# Distance Rotterdam / New York in km
distance_Rotterdam_NewYork = 5_862.03
# Distance Rotterdam to New York in meters divided by the speed of light
time_to_reach_NYC = (distance_Rotterdam_NewYork * 1000) / speed_of_light
print(
    f'Time to reach New York is: {time_to_reach_NYC} seconds => {time_to_reach_NYC * 1000.0} milliseconds.')

# What is the data type?
print(f'type: {type(time_to_reach_NYC)}\n')


# String
print(f'STRING:\n')

ship = 'Titanic'
print(ship)
ship = "Titanic"
print(ship)
ship = """Titanic"""
print(ship)

# Vaak zul je quotes in een string moeten gebruiken. Dit kan met de escape character \, of door de string met enkele quotes te omringen
zonder_escape = 'This is a "good" plan'
print(zonder_escape)
met_escape = "This is a \"good\" plan"
print(met_escape)

# Gebruik """ """ als je meerdere regels tekst moet tonen
paragraph = """Computer Technology means all designs, drawings, procedures (including design, manufacturing, test and maintenance procedures), specifications, software (other than as described within the meaning of the term "Software" defined elsewhere herein), printed circuit board art work, integrated circuit masks, test equipment, tools, fixtures, documentation, training materials, and information, in whatever form, related to, useful, utilizable or necessary in the design, manufacture, test and/or maintenance of the computer system, or relate to any Technology Licenses."""
print(paragraph)
# With the len() function you can ask how many characters the string has
characters_in_paragraph = len(paragraph)
print(f"{paragraph}\n\nThe paragraph has {characters_in_paragraph} characters.")


year = 1936
inventor = "Alan Turing"
name_of_machine = "automatic machine"
# Note: Within the text double quotes are used. We need to use single quotes to embrace the string
invention = f'The Turing machine was invented in {year} by {inventor}, who called it an "a-machine" ({name_of_machine}).'
print(invention)

# What is the data type?
print(f'type: {type(invention)}\n')


# Boolean
print('BOOLEAN:\n')

logged_in = False
print(logged_in)

netwerk_activity = True
print(f'netwerk_activity: {netwerk_activity}\n')


# Logische operatoren
print('LOGISCHE OPERATOREN')
# | Operator | Betekenis |
# | --- | --- |
# | == | Is gelijk aan |
# | != | Is niet gelijk aan |
# | < | Is kleiner dan |
# | <= | Is kleiner dan of gelijk aan |
# | > | Is groter dan |
# | >= | Is groter dan of gelijk aan |


user_name = "John Doe"
entered_name = input("User name, please: ")
size_user_name = len(user_name)
size_entered_name = len(entered_name)
user_name_is_bigger = size_user_name > size_entered_name
entered_name_is_bigger = size_entered_name > size_user_name
print(
    f"The user name {user_name} has more characters then the entered name {entered_name} is: {user_name_is_bigger}")
print(
    f"The entered name {entered_name} has more characters then the user name {user_name} is: {entered_name_is_bigger}")

lights_on = False
lock_closed = True


# Not keert de waarde van een boolean om not True is hetzelfde als False
# Andersom is not False dus True
alarm_activated = not lights_on and lock_closed
print(f"The alarm is activated, is: {alarm_activated}")


# Containers
print('CONTAINERS:\n')

# Op een terminal worden schepen gelost en geladen. Tijdens het lossen worden 331 containers gelost in 441 minuten. Na het lossen wordt het schip geladen met 287 containers in 295 minuten.
# Bedenk een goede representieve variabele naam voor de * geloste * containers en ken het aantal geloste containers toe aan de variabele.
# Bedenk een goede representieve variabele naam voor de * geladen * containers en ken het aantal geladen containers toe aan de variabele.
# Bereken van zowel het laden als lossen de gemiddelde laad/lostijd. Geef deze weer op in een volzin: De gemiddelde tijd die het laden of lossen duurt.

laad_count = 287
laad_tijd = 295
los_count = 331
los_tijd = 441



print(f'De gemiddelde tijd die het laden of lossen duurt. Laden: {laad_tijd / laad_count} minuten, lossen: {los_tijd / los_count} minuten \n')


# Berekening
# Zet de volgende formule om naar Python code:

# ![Formule 1](./Images/Formule_1.png)

def formule_1(num):
    y = math.sqrt((3 * num)) + (1 + num)**2
    return y


# Bereken het antwoord als 
x = 9.1
# Geef het antwoord weer in de volzin:

print(f'De waarde van y = {formule_1(x)} als x = {x}.')

# # Output
# ![Antwoord 13](./Images/Les2-Antwoord_Source_1.png)

# Uitwerking
# Een voorbeeld uitwerking: [Les2_Source1.py](Uitwerkingen % 2FLes2_Source1.py)

# Berekening
print('BEREKENING:\n')
# Een belangrijke vaardigheid om op te doen is het opsplitsen van een groot probleem naar kleine deelproblemen. Dat ga je in de volgende twee opdrachten doen.

# Zet de volgende formule om naar Python code. Bedenk dat je alle tussenstapjes in variabelen kunt vangen:

# ![Formule 2](./Images/Formule_2.png)

def formule_2(num_a, num_b, num_c):
    discriminant = (num_b**2) - 4 * num_a * num_c
    teller = -1 * num_b + math.sqrt(discriminant)
    noemer = 2*num_a
    y = teller / noemer

    return y
# Bereken het antwoord als:
a = 0.87
b = 22.7
c = 5.03

# Geef het antwoord weer in een volzin:

print(f'De waarde van y = {formule_2(a, b, c)} als a = {a}, b = {b} en c = {c}')
# Output
# ![Antwoord 14](./Images/Les2-Antwoord_Source_2.png)

# # Uitwerking
# Een voorbeeld uitwerking: [Les2_Source2.py](Uitwerkingen % 2FLes2_Source2.py)


# Berekening
print('BEREKENING:\n')
# Tijd en ruimte zijn geen absolute concepten, maar relatief en afhankelijk van de snelheid van de waarnemer.
# Met behulp van onderstaande formule kan worden berekend hoeveel de tijd versneld of vertraagd afhankelijk van de snelheid van de waarnemer.
# U kijkt vanaf uw tuinstoel gedurende t = 4 uur naar een passeerde komeet die met een snelheid van v = 179875474.8 m/s langs de hemel trekt.
# Hoeveel tijd zou er gepasseerd zijn als u op de komeet zou zitten en naar uw tuinstoel op de aarde keek, gegeven dat de lichtsnelheid c = 299792458 m/s?
# Gegeven de formule:

# ![Formule 3](./Images/Formule_3.png)

# Bereken de delta en druk het berekende antwoord af op het scherm in de zin:

t = 4
v = 179875474.8 
c = 299792458

def formule_3(t, v , c):
    delta = t / (v * (1 - ((v**2)/(c**2))))
    return delta

print(f'Vanaf een komeet gezien zit u {formule_3(t, v, c)} uur op de tuinstoel.')

# # Output
# ![Antwoord 16](./Images/Les2-Antwoord_Source_4.png)

# # Uitwerking
# Een voorbeeld uitwerking: [Les2_Source4.py](Uitwerkingen % 2FLes2_Source4.py)
