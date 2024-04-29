from datetime import datetime # Import Datetime-Bibliothek, für den Umgang mit Daten und Zeiten
from folder import * # Import folder.py
from camera import * # Import camera.py
from transfer import * #Import transfer.py
import logging # Import Logging-Bibliothek zum Erstellen einer Logdatei

class Process():
        
    class __init__(): # Ausführung beim Programmaufruf
                                                                                          # dd-mm-YYYY_HH-MM-SS
        time = datetime.now(  ).strftime("%d-%m-%Y--%H:%M:%S") # Erstellung der aktuell Uhrzeit im Format "03-10-2022_20-13-23" 
        print(time)
        year = datetime.now().strftime("%Y") # Erstellung des Jahres als Text
        #print(year)
        month = datetime.now().strftime("%Y-%m") # Erstellung des Monates und Jahres als Text
        day = datetime.now().strftime("%m-%d") # Erstellung des Monates und Jahres als Text
        hour = datetime.now().strftime("Stunde-%H") # Erstellung des Monates und Jahres als Text
        print(month)
        path1 = '/home/pi/Desktop/Birdwatcher' # Ordnerpfad 1
        path2 = '/home/pi/Desktop/Birdwatcher/%s' %year #Ordnerpfad 2
        path3 = '/home/pi/Desktop/Birdwatcher/%s/%s' % (year, month) # Ordnerpfad 3
        path4 = '/home/pi/Desktop/Birdwatcher/%s/%s/%s' % (year, month, day) # Ordnerpfad 4
        path5 = '/home/pi/Desktop/Birdwatcher/%s/%s/%s/%s' % (year, month, day,hour) # Ordnerpfad 5
        pFile = path5 +'/image_'+ time + '.jpg' #Dateipfad für die Aufnahme
        filename = time # Dateiname für den Mail-Versand
        print("account")
        pSubject = 'Vogelbeobachtung ' + time # Betreff der E-Mail
        pFrom = 'max.musterman@hsbi.de' # Absenderadresse der Mail [zu ergänzen]
        pTo = 'birdwatcher.ium@hsbi.de' # Empfaengeradresse [zu ergänzen]
        Cc = '' # Empfaengeradresse(ZUSATZ) [zu ergänzen]
        pContent = 'Birdwatcher' # E-Mailtext [zu ergänzen]
        host = 'smtp.hsbi.de' # SMTP-Url des Mailproviders [zu ergänzen]
        Port = 587 # Port der SMTP-URL
        password = '' # Passwort des Mail-Kontos
        
        pTransfer = '/home/pi/Desktop/Birdwatcher/transfer' # Ordnerpfad für den Transferordner
        logging.basicConfig(filename="process_log.txt", format="%(asctime)s %(message)s") # Erstellung und Konfiguration der Log-Datei
            
        #folder.delFolder('/home/pi/Desktop/Birdwatcher'     
        folder.createFolder(path1) # Erstellung des Orners an Pfad 1
        folder.createFolder(path2) # Erstellung des Orners an Pfad 2
        folder.createFolder(path3) # Erstellung des Orners an Pfad 3
        folder.createFolder(path4) # Erstellung des Orners an Pfad 3
        folder.createFolder(path5) # Erstellung des Orners an Pfad 3
        folder.createFolder(pTransfer) # Erstellung des Transferordners   
        camera.takePhoto(pFile) # Aufnahme und Speicherung unter dem Dateipfad
        folder.transfer(pFile, pTransfer) # Kopieren der Aufnahme in den Transferordner
        transfer.sendMail(pSubject, pFrom, pTo, Cc, pContent, pTransfer, filename, host, Port, password) # Versand der Datei per E-Mail in einer .zip-Datei
        
        


