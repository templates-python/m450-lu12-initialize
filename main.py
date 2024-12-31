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
    
    """



if __name__ == '__main__':
    dbinitialize()
