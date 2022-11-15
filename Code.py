import usaddress

def main():
    address_list = [
    " Winterallee 3",
    "Musterstrasse 45",
    "Blaufeldweg 123B",
    "Am Bächle 23",
    "Auf der Vogelwiese 23 b",
    "4, rue de la revolution",
    "Calle Aduana, 29",
    "Calle 39 No 1540"
    ]

    for addr in address_list:
        data = usaddress.tag(addr)
        if "PlaceName" in data[0].keys():
            print(data[0]["PlaceName"])
        else:
            print("no streetnames/Numbers")

main()
