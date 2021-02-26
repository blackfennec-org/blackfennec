Project Proposal
================

============== ============
Project Name   Date
============== ============
Black Fennec   17.12.2020
============== ============

Team
****

- Leonie Däullary <leonie.daeullary@ost.ch>
- Lara Gubler <lara.gubler@ost.ch>
- Simon Kindhauser <simon.kindhauser@ost.ch>
- Caspar Martens <caspar.martens@ost.ch> 

Beratungs- und Review-Zeitslots
******************************* 

| X   = Slot ist dem Team möglich  
| (X) = Slot ist für das Team nicht optimal, wäre aber möglich  
| O   = Treffen online möglich  
| P   = Treffen physisch (Campus OST-RJ) möglich  
| OP  = Treffen online sowie physisch (Campus OST-RJ) möglich  
|     = Slot ist nicht möglich

 
===============  ======  ========  ========  ==========  =======
*Zeitslot*       Montag  Dienstag  Mittwoch  Donnerstag  Freitag 
===============  ======  ========  ========  ==========  =======
**08:00-09:00**                                          XO      
**09:00-10:00**                                          XO      
**10:00-11:00**                                          (XO)    
**11:00-12:00**                                          (XO)    
**12:00-13:00**                                          (XO)    
**13:00-14:00**                                          XO      
**14:00-15:00**                                          XO      
**15:00-16:00**                                          XO      
**16:00-17:00**                                          XO      
**17:00-18:00**                                          (XO)    
**18:00-19:00**                                                 
===============  ======  ========  ========  ==========  ======= 

Motivation
**********

Es gibt bis dato keine Applikation, zur strukturierten verwaltung von Daten, die aus unstrukturierten Quellen gewonnen wurden (zum Beispiel dem Internet), welches zusätzlich auch die Funktionalität der Versionskontrolle, zu unserer Zufriedenheit unterstützt. Deshalb wollen wir im Rahmen des Engineering Projekts solch eine Applikation entwickeln. Das Tool soll uns in Zukunft als teilbares Informations-strukturierungs Hilfe dienen. Ein Hauptanwendungszweck sehen wir im OSINT Gathering und dem Speichern der entdeckten Daten und mit gewissen Plugins auch zur automatisierten Suche von Daten. 

Typischer Workflow
^^^^^^^^^^^^^^^^^^
Ein Headhunter hat auf GitHub eine Person mit vielversprechenden Repositories gefunden und würde mit dieser gerne in Kontakt treten. Um diese Kontaktaufnahme jedoch möglichst erfolgsversprechend zu gestalten benötigt er gewisse Informationen angefangen mit der Email-Adresse.

Marco, der Headhunter erstellt für diesen Zweck nun ein Projekt in Black Fennec, angefangen mit einem Template für die Daten einer Person. Dort füllt er anfangs einfach die GitHub profil URI hinein. Mit einem Plugin, welche das Herunterladen der wichtigsten Informationen eines GitHub Profils erlaubt, stellt im nun alle relevanten Daten direkt in Black Fennec integriert zu Verfügung, inklusive Daten, die man nicht auf den ersten Blick findet. Ganz alles kann ihm Black Fennec jedoch nicht abnehmen, deshalb geht nun die Suche weiter über Google, indem er das GitHub handle über Google sucht, und ein Steam-Account entdeckt. Wie vorhin will er nun die gefundenen Daten ablegen, jedoch dieses mal ohne Plugin-Unterstützung. Leider findet Marco keine weiteren Informationen über seine Zielperson, und deshalb speichert er sein Projekt und Pusht es in sein Firmen-internes GitHub Repository. Am nächsten Tag kommt er immernoch nicht vorwärts, und deshalb fragt er einen Kollegen um Hilfe, welcher ihm verspricht, auch einmal sein Glück zu versuchen. Dieser kann das Repository wie gewohnt klonen, und sogar für seine gesammelten Erkenntnisse einen eigenen Branch erstellen, welcher Marco dann später anschauen und gegebenenfalls mergen kann.

Projektidee
***********
Black Fennec ist ein versionisierbar, pluggable, dynamisch strukturiertes Informations-verwaltungs Tool,welches visuell ansprechend und angenehm zur Bedienung ist. 

Das Stichwort pluggable ist allgemein sehr wichtig im Projekt, da diese Module einen wichtigen Teil der Arbeit ausmachen. Die Basis des Projekts bietet nur nur sehr Grundlegende funktionalitäten die wir im Rahmen dieser Arbeit auch noch erweitern wollen. Dadurch kann sehr unabhängig gearbeitet, und der Aufwand sehr dynamisch skaliert werden.

Projektidee besprochen mit: Thomas Kälin

Realisierung
************
Die Applikation basiert auf YAML/JSON Dateien (evtl. zusätzlich XML) welche in einem mit Python Client interpretiert und visualisiert werden. Die GUI-Technologie ist noch nicht entschieden, der Plan ist jedoch in die richtung von Deklarativen Frameworks zu gehen (XAML/HTML). Die Plugins welche die Applikation unabhängig beinhalten wird, können beliebige Libraries (Python) verwenden. Der Client ist für Desktop-systeme optimiert.

Technologie
^^^^^^^^^^^

Wie erwähnt werden wir unser Projekt mit Python entwickeln. Wir streben Test Driven Development and was mit Hilfe vom PyTest Modul realisiert werden soll. Unser GUI wird mit dem Modul Kivy implementiert, welches Cross-Plattform unterstützt. Das GUI soll mit einer MVVM Architektur implementiert werden.

Core
^^^^
Der Core ist die Grundlage unseres Projekts und soll ein Framework anbieten, welches den verschiedenen Plugins eine integration ins System ermöglicht. Zusätzlich bietet er bestimmte Core-Features an, die immer benötigt werden. Dies sind insbesondere die Typen String, Number, Referenzen, List und Dictionary. Diese Typen bilden die Basis des dynamischen Objektmodells, welches sich für unser Produkt sehr gut eignet. Das Core-GUI, welches auch die Visualisierung der aufgelisteten Typen enthält ist ebenfalls hier implementiert. Eine Unterstützung für eine Suche auf Basis von einem beliebigen Typen soll ebenfalls implementiert werden im Core.

Base
^^^^
Base ist das einzige direkt eingebaute Plugin. Es bietet Funktionalität, welche von unseren Benutzern erwartet werden, dass sie immer zu verfügung stehen. Zum Beispiel die Typen: Datei, Bild, Datum, Ort. Man kann die Base auch als Minimal Viable Product anschauen. Das Ziel ist es, dieses möglichst schlank zu halten und jegliche zusätzliche Funktionalität in weitere Plugin auszulagern, damit unsere Applikation so Flexibel wie möglich bleibt.

Zusätzliche Plugins
^^^^^^^^^^^^^^^^^^^
Bei diesen Plugins handelt es sich um Beispiel Ideen, damit sich der Betreuer etwas unter den möglichkeiten unserer angestrebten Plugins vorstellen kann, und je nach unseren Zeitmöglichkeiten werden mehr oder weniger dieser Ideen schlussendlich umgesetzt.

GitHub Crawler
""""""""""""""
Automatisiertes Crawling von Benutzerdaten eines GitHub-Account durch die angabe der Profil-URI.

Facebook Crawler
""""""""""""""""
Automatisiertes Crawling von Benutzerdaten eines Facebook-Account durch die angabe der Profil-URI. Hinterlegung von Facebook account?

LinkedIn Crawler
""""""""""""""""
Automatisiertes Crawling von Benutzerdaten eines LinkedIn-Account durch die angabe der Profil-URI. Hinterlegung von LinkedIn account?

Facial Recognition
""""""""""""""""""
Extraktion von Gesichter aus Bildern. Evt. eine Verweisung auf ähnliche Gesichter innerhalb des Projekts.

Google Dorker
"""""""""""""
Generate Google Dorks from selected Types.