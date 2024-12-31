import mysql.connector

def dbinitialize():

    # Verbindungskonfiguration
    # Hier müssen Sie Angaben von Ihrer lokalen MySQL-Instanz angeben und der Dienst muss gestartet sein
    config = {
        'user': 'root',
        'password': 'hello12345',
        'host': 'localhost'
    }

    # Verbindung erstellen
    cnx = mysql.connector.connect(**config)

    """
    TODO
    
    Erstellen Sie hier nun Ihren Code zum einlesen/ausführen des im vorherigen Auftrag ergänzten SQL-Skripts
    
    Ergänzen Sie den Code um eine Funktion, welche die Anzahl Kunden (customer) lesen und zurückgeben kann
    
    Ergänzen Sie den Code um eine Funktion, welche die Anzahl Buchungen (debit) lesen und zurückgeben kann
    
    Ergänzen Sie den Code um eine Funktion, welche die Summe aller Buchungen (debit) lesen und zurückgeben kann




    """


if __name__ == '__main__':
    dbinitialize()
