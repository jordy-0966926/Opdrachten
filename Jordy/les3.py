def main():

    internet_verbinding_selectie()
    flowchart_TB()
    flowchart_shopping()
    mcdonalds()


def internet_verbinding_selectie():

    def print_verbinding(keuze):
        print(f"U bent verbonden via {keuze}!")
        return

    keuze = input(
        'Waarmee wilt u verbinden? Kies uit: \n 4G\n 5G\n Wifi open\n Verbind met: ')
    if keuze.lower() in ['4g', '5g']:
        print_verbinding(keuze)

    elif keuze.lower() == "wifi open":
        print(f"U heeft de voor de Wifi open gekozen, wij wijzen u erop dat de data door de eigenaar van dit netwerk is te lezen.")
        confirm = input(" Wilt U nogsteeds verbinding maken? ja/nee ")
        if confirm == "ja":
            print_verbinding(keuze)
        else:
            print("U bent niet verbonden!")
    else:
        print("Onbekende invoer, er wordt geen verbinding tot stand gebracht.")


def flowchart_TB():

    def wrong_input():
        print("Please answer with \"Yes\" or \"No\"")
        exit()

    patient = input('Is the patient exposed to TB an Adult or Child? ')
    if patient.lower() == "adult":
        symptoms = input('Does the patient have common TB symptoms? Yes / No ')
        if symptoms.lower() in ['yes', 'y']:
            print('Treat as likely TB patient and perform full TB exam')
        elif symptoms.lower() in ['no', 'n']:
            print('Have patient report back if unwell; return in 1 month for checkup')
        else:
            wrong_input()
    elif patient.lower() == "child":
        eligible = input('Can TB test be given? Yes / No ')
        if eligible.lower() in ['yes', 'y']:
            print('Administer TB test \n Assess TB test results and child\'s condition')
        elif eligible.lower() in ['no', 'n']:
            wellness = input('Is the child well? ')
            if wellness.lower() in ['yes', 'y']:
                print(
                    "6 months preventive isoniazid \nHave parent bring in if child's shows any symptoms")
            elif wellness.lower() in ['no', 'n']:
                print("Take full history. Examine for TB \n If TB likely diagnosis, treat for TB \n If other diagnosis more likely, treat as needed and watch for TB symptoms")
            else:
                wrong_input()
        else:
            wrong_input()
    else:
        print("Please answer with \"Adult\" or \"Child\"")


def flowchart_shopping():

    def approved(payment_method):
        if payment_method.lower() == 'online':
            print('Enter payment details')
            print('Place Order.')
        elif payment_method.lower() == 'offline':
            print('Order created automatically')
        else:
            wrong_input()
        return

    def rejected():
        print('Purchase order rejected')
        return

    def wrong_input():
        print('Abort unknown input')
        exit()

    payment_method = input('Payment method? [Online/Offline] ')
    if payment_method not in ['online', 'offline']:
        wrong_input()
    print(f'{payment_method}, place purchase order.')
    admin_check = input("Admin? [Yes/No] ")
    if admin_check.lower() in ['yes', 'y']:
        approved(payment_method)
    elif admin_check.lower() in ['no', 'n']:
        rejected()
    else:
        wrong_input()


def mcdonalds():

    # Zoek een string in een array van strings, hoofdletterongevoelig
    def find_item(array, search_string):
        try:
            index = [item.lower() for item in array].index(search_string)
            print(array[index])
        except:
            wrong_input()

    # Print op basis van hier opeten of meenemen
    def end_of_order(dine_in):
        if dine_in.lower() == 'opeten':
            print('Bedankt voor uw bestelling en eet smakelijk in ons restaurant.')
        elif dine_in.lower() == 'meenemen':
            print('Bedankt voor uw bestelling, goede reis en eet smakelijk.')
        else:
            wrong_input()

    # Error handler
    def wrong_input():
        print('Abort unknown input')
        exit()

    burgers_arr = ['Hamburger', 'Cheese burger', 'Big Mac', 'Quarter Pounder']
    warm_arr = ['Koffie', 'Cappucino', 'Chocolademelk']
    koud_arr = ['Coca Cola', 'Cola Zero', '7-up', 'Fanta', 'Fristi']
    menu_arr = burgers_arr + koud_arr + warm_arr

    dine_in = input('Hier opeten of meenemen? [Opeten/Meenemen] ')
    if dine_in.lower() not in ['opeten', 'meenemen']:
        wrong_input()

    print(dine_in)
    order = input('Burgers of drankjes? ')
    print(order)

    if order.lower() in ['burgers', 'burger']:
        menu_item = input(f'Burgers {burgers_arr} ')

    elif order.lower() in ['drankjes', 'drankje']:
        drank_type = input('Warme of koude drankjes? [Warme/Koude] ')
        if drank_type.lower() in 'warme':
            menu_item = input(f'Warme drank {warm_arr} ')
        elif drank_type.lower() in 'koude':
            menu_item = input(f'Koude drank {koud_arr} ')
        else:
            wrong_input()

    else:
        wrong_input()

    find_item(menu_arr, menu_item)
    end_of_order(dine_in)


main()
