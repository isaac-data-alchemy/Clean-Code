from seek import search_v4 as search
def main():
    names_1d = ['ella', 'david', 'tipulate', 'sharon', 'amaka', 'jordana']
    names_2d = [['ella', 'david'], ['tipulate', 'sharon'], ['amaka', 'jordana']]
    text = "Enter a name to search: "
    search(names_1d, text=text)


if __name__ == "__main__":
    main()