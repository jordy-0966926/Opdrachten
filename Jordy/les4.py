import math

def main():
    # lists()
    # tuples()
    dictionaries()


def lists():
    games_list = ['Player\'s Unknown Battle Ground (PUBG) 50 Million 2018',
                  'Fortnite Battle Royale 39 Million 2017',
                  'Apex Legends 50 Million (1 Month) 2019',
                  'Leauge of Legends (LOL) 27 Million 2009',
                  'Counter Strike; Global Offensive 32 Million 2014',
                  'Heartstone 29 Million 20120',
                  'Minecraft 91 Million 2011',
                  'DOTA 2 5 million 2015',
                  'The Division 2 N/A 2019',
                  'The Splatoon 2']

    index = input(
        f'Type a number to pick a game, there are {len(games_list)} games ')
    try:
        index = int(index)
        game = games_list[index-1]
        len_str = len(game)
        print(f'{index}] {game}, length of the str = {len_str}')
        games_list.insert(1, 'Snake')
        print(
            f'List has been updated Snake has been added to the list as the new rank 2, {games_list.pop()} has been removed from the top 10')

        print(games_list)

    except:
        print('that is not a number')
    return


def tuples():

    brands_tuple = (
        'Apple',
        'Asus',
        'Dell',
        'Lenovo',
        'Acer',
        'Samsung',
        'MSI',
        'Hewlett-Packard (HP)',
        'Toshiba',
        'Microsoft',
        'Chuwi',
        'Sony',
    )

    a = f'This tuple contains {len(brands_tuple)} brands'
    b = f'{brands_tuple[7]}\'s name contains {len(brands_tuple[7])} letters'
    c = f'Name of the brand on the 10th place: {brands_tuple[9]}'

    string_tuple = tuple((a, b, c))
    for string in string_tuple:
        print(string)
        print(brands_tuple)


def dictionaries():
    movies_dict = {
        "The Simpsons": "636-555-3226",
        "Vegas Vacation": "555-0100",
        "Ghostbusters": "555-23678",
        "Billy Madison": "555-0840",
        "Swingers": "213-555-4679",
        "Bruce Almighty": "555-0123",
        "Seinfeld": "555-FILK",
        "Arrested Development": "555-0113",
        "Die Hard With a Vengeance": "555-0001",
        "The A-Team": "555-6162"
    }

    a = f'Bruce Almight\'s phone number is {movies_dict["Bruce Almighty"]}'
    movies_dict["Harry Potter"] = "605-475-6961"
    b = f'Harry Potter\'s number has been added'
    movies_dict['Ghostbusters'] = "555-2368"
    c = f'Ghostbusters\'s number has been changed to 555-2368'
    d = f'Seinfeld\'s number has been removed {movies_dict.pop("Seinfeld")}'
    e = f'There are now {len(movies_dict)} phone numbers in the dictionary'

    string_dict = dict(a=a, b=b, c=c, d=d, e=e)
    for values in string_dict.values():
        print(values)
        print(movies_dict)


main()
