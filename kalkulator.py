import logging

logging.basicConfig(level=logging.DEBUG)

def menu():
    run = True
    while run:
        print("1. Dodawanie")
        print("2. Odejmowanie")
        print("3. Mnożenie")
        print("4. Dzielenie")
        choice = input("Wybierz funkcje wpisując jej numer, bądź 'Q' aby wyjść: ")

        if choice.upper() == "Q":
            run = False
        elif choice.isdigit() and int(choice) in range(1, 5):
            f = eval(f'f{choice}')
            f()
        else:
            print("Ta funkcja nie istnieje. Spróbuj ponownie.")

def f1():
    print("Wybrałeś/aś funkcje 'dodawanie'.")
    print("Ma ona zadanie dodawać liczby podawane przez użytkownika kolejno do siebie.")
    initial_number = int(input("Podaj liczbę początkową: "))
    breaker = True
    for i in range(0,1):
        middle_number = int(input("Podaj liczbę, która będzie dodana do tej liczby: "))
        end_number = initial_number + middle_number
        logging.info(f"Dodaje {middle_number} do {initial_number}.")
        print("Wynik:", end_number)
        tn = input("Czy chcesz kontynuować dodawanie? (t/n): ")
        if tn.lower() == "n":
            break
        elif tn.lower() == "t":
            while breaker == True:
                middle_number = int(input("Podaj liczbę, która będzie dodana do tej liczby: "))
                end_number2 = end_number + middle_number
                logging.info(f"Dodaje {middle_number} do {end_number}.")
                print("Wynik:", end_number2)
                end_number = end_number2
                tn = input("Czy chcesz kontynuować dodawanie? (t/n): ")
                if tn.lower() == "n":
                    breaker = False
                elif tn.lower() == "t":
                    continue
                else:
                    logging.error("Wprowadzono niepoprawne dane.")
                    breaker = False
        else:            
            logging.error("Wprowadzono niepoprawne dane.")
            breaker = False


def f2():
    print("Wybrałeś/aś funkcje 'odejmowanie'.")
    print("Ma ona zadanie odejmować liczby podawane przez użytkownika kolejno od siebie.")
    initial_number = int(input("Podaj liczbę początkową: "))
    breaker = True
    for i in range(0,1):
        middle_number = int(input("Podaj liczbę, która będzie odjęta tej liczby: "))
        end_number = initial_number - middle_number
        logging.info(f"Odejmuje {middle_number} od {initial_number}.")
        print("Wynik:", end_number)
        tn = input("Czy chcesz kontynuować odejmowanie? (t/n): ")
        if tn.lower() == "n":
            break
        elif tn.lower() == "t":
            while breaker == True:
                middle_number = int(input("Podaj liczbę, która będzie odjęta od tej liczby: "))
                end_number2 = end_number - middle_number
                logging.info(f"Odejmuje {middle_number} od {end_number}.")
                print("Wynik:", end_number2)
                end_number = end_number2
                tn = input("Czy chcesz kontynuować odejmowanie? (t/n): ")
                if tn.lower() == "n":
                    breaker = False
                elif tn.lower() == "t":
                    continue
                else:
                    logging.error("Wprowadzono niepoprawne dane.")
                    breaker = False
        else:            
            logging.error("Wprowadzono niepoprawne dane.")
            breaker = False


def f3():
    print("Wybrałeś/aś funkcje 'mnożenie'.")
    print("Ma ona zadanie mnożyć liczby podawane przez użytkownika kolejno przez siebie.")
    initial_number = int(input("Podaj liczbę początkową: "))
    breaker = True
    for i in range(0,1):
        middle_number = int(input("Podaj liczbę, która będzie pomnożona przez tą liczbę: "))
        end_number = initial_number * middle_number
        logging.info(f"Mnożę {middle_number} razy {initial_number}.")
        print("Wynik:", end_number)
        tn = input("Czy chcesz kontynuować mnożenie? (t/n): ")
        if tn.lower() == "n":
            break
        elif tn.lower() == "t":
            while breaker == True:
                middle_number = int(input("Podaj liczbę, która będzie pomnożona przzez tą liczbę: "))
                end_number2 = end_number * middle_number
                logging.info(f"Mnożę {middle_number} razy {end_number}.")
                print("Wynik:", end_number2)
                end_number = end_number2
                tn = input("Czy chcesz kontynuować mnożenie? (t/n): ")
                if tn.lower() == "n":
                    breaker = False
                elif tn.lower() == "t":
                    continue
                else:
                    logging.error("Wprowadzono niepoprawne dane.")
                    breaker = False
        else:            
            logging.error("Wprowadzono niepoprawne dane.")
            breaker = False


def f4():
    print("Wybrałeś/aś funkcje 'dzielenie'.")
    print("Ma ona zadanie dzielić liczby podawane przez użytkownika kolejno przez siebie.")
    initial_number = int(input("Podaj liczbę początkową: "))
    breaker = True
    for i in range(0,1):
        middle_number = int(input("Podaj liczbę, przez którą ma zostać podzielona ta liczba: "))
        end_number = initial_number / middle_number
        logging.info(f"Dodaje {middle_number} do {initial_number}.")
        print("Wynik:", end_number)
        tn = input("Czy chcesz kontynuować dzielenie? (t/n): ")
        if tn.lower() == "n":
            break
        elif tn.lower() == "t":
            while breaker == True:
                middle_number = int(input("Podaj liczbę, przez którą ma zostać podzieloiny wynik: "))
                end_number2 = end_number / middle_number
                logging.info(f"Dzielę {end_number} przez {middle_number}.")
                print("Wynik:", end_number2)
                end_number = end_number2
                tn = input("Czy chcesz kontynuować dzielenie? (t/n): ")
                if tn.lower() == "n":
                    breaker = False
                elif tn.lower() == "t":
                    continue
                else:
                    logging.error("Wprowadzono niepoprawne dane.")
                    breaker = False
        else:            
            logging.error("Wprowadzono niepoprawne dane.")
            breaker = False

print("Witam Cię w kalkulatorrze 4 podstawowych działań matematycznych.")
print("UWAGA, PROGRAM ZOSTAŁ STWORZONY DO DZIAŁANIA NA LICZBACH CAŁKOWITYCH!!!")
print("Wpisując kolejno liczby do funkcji należy posługiwać się tylko nimi.")
menu()