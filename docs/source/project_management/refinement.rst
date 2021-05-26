**********
Refinement
**********
After each sprint, a review meeting was held to discuss the current status of the project. The checklist of the individual milestones was discussed and it was ensured that all items on the list were fulfilled. During the meetings, we received some suggestions for improvement from our supervisor, which we implemented during the course of the project.

This document provides an overview of all these improvement suggestions and how they were implemented in our project.

Project Plan
============
- Projektorganisation: PL explizit als Rolle aufführen
- Phasen, Iterationen und Meilensteine: Grobplanung fehlt

 - --> Wie lange dauern die 4 RUP-Phasen?
 - --> Wann starten, bzw. Enden die 2-wöchigen Iterationen?
 - --> Wann finden die Milestones, bzw. zugehörigen Reviews statt?
 - --> All das kann mit wenig Aufwand mit einem groben (!) Plan beantwortet werden.
 - Dieser Plan kann und soll dann iterativ verfeinert werden.

- Risk Management: Tipp - Berechnung von Zeitreserven aufgrund von Risikoanalyse (Gewichteter Schaden; siehe Vorlage) --> Zeitreserve in Grobplan berücksichtigen (verteilt auf Iterationen oder als Puffer am Projektende)
- Ausgewogene Beiträge der Teammitgliedern: Range etwas gross, für R1 aber gerade noch okay --> Für R2 sollte eine Tendenz zum Ausgleich erkennbar sein

Improvements
------------

**Role Project Lead / Project Manager must be added in the documentation**
The description of this role was added in the document :ref:`project plan <Project Organisation>`

**Rough plan of the project must be created and added in the documentation**
We created a project timeline in the document :ref:`project plan <Project Timeline>`

**Add the time needed to respond to the risk to the risk analysis and the rough plan of the project**
The time needed to respond to a risk is included in the project timeline.

Requirements Engineering & Domainanalysis
=========================================
- FA mit schönen UI Skizzen unterstützt

 - Gedanke #1: wenn möglich immer mit realen Daten arbeiten zwecks einfacherer Kommunikation mit Stakeholdern
 - Gedanke #2: für Schlusspräsentation mit konkretem Beispiel beginnen - Abstraktionen sind tendenziell schwieriger verständlich

- NFA sehr systematisch und umfangreich erfasst

 - Gedanke: Aufgrund der Vielzahl an Kriterien (riecht etwas nach Over Engineering) Priorisierung vornehmen

- Domäne aufgrund komplexer Problemstellung in alternativem Format auf verschiedenen Stufen / Ansichten beschrieben - Top!

 - Gedanke #1: ggf. Umfang kritisch hinterfragen ("Könnte dieselbe Information mit weniger Text / Diagrammen erklärt werden?")
 - Gedanke #2: Warum haben die "Klassen" im Domain Model keine Attribute / Eigenschaften? Hätte dies einen Mehrwert?

- Das Domänen Modell soll das Verständnis der Anforderungen des Auftraggebers in "visueller Form" abbilden. Es dient als gemeinsame Diskussionsgrundlage und längerfristig als Ausgangslage für den "Kern unserer Software". ==> Das Domänen Modell beschreibt, was unsere Software macht.
- Während der Architektur entsteht meist ein Design Modell. In dieser Phase geht es darum, die Erkenntnisse aus dem Domänen Modell in einer lauffähigen Software zu verpacken. Oft endet das Domänen Modell als eine Komponente innerhalb des Design Modells. Das Design Modell umfasst aber noch ganz viel mehr (Persistenz, UI, Kommunikation, etc.). Bei der Clean Architecture bildet die Domäne beispielsweise den technologie-neutralen Kern der Architektur. ==> Das Design Modell beschreibt, wie unsere Software das macht, was sie macht.

Improvements
------------
**Explain the rhombus sign in the domain model with pseudocode**


**Prioritize the important non-functional requirements**


**Use the personas in the use-cases**
We did this by relating the user stories to specific personas. An example of this can be found :ref:`here. <https://gitlab.ost.ch/epj/2021-FS/g01_blackfennec/black-fennec/-/issues/131>`_

**Add sketches from extensions as soon as they exist**


Architecture Prototype & End of Elaboration
===========================================
- Architektur-Dokumentation in aktueller Form hilft noch nicht besonders, sich im Code der Applikation zurecht zu finden

 - Abweichung von Diagrammen zu Code
 - Fehlende Kommentare zu logischer Strukturierung (Wieso wurde so strukturiert? Was finde ich in diesen «Hauptelementen»? Etc.)

- Feedbacks aus Review #2 bzgl. RE wurden – zumindest soweit ich das erkennen konnte – nur «zögerlich» umgesetzt

Improvements
------------
**It is hard to make a connection between the architecture documentation and our structure in the code. We should therefore consider either adapting the documentation or the folder structure**


**Mention in the documentation that in our project everything is done in a process and we do not have a backend**


**The diagram of the architecture and source documentation should be matched to each other**


**Consider changing the title 'Documentation'**

Software Architecture
=====================
- Das prüfen von Performance-Szenario könnte ggf. technische Risiken mit Einfluss auf die Architektur hervorbringen
- Einige Texte in der Doku sind für meinen Geschmack etwas «ausführlich» formuliert
- Eine dynamische Sicht auf das System fehlt in der Dokumentation völlig (wichtige Use Cases à Interaktion zwischen Komponenten, bzw. Klassen)

Improvements
------------
**Consider adding a performance test. E.g. insertion of large files**


**The document contains only static views of the system. Consider adding a dynamic view of the system**


Quality Ensurance Measurements & Code Quality
=============================================
- Ein Usability Test könnte nützliche Verbesserungen für die Applikation ergeben. Eine informelle Durchführung benötigt auch nicht viel Zeit, die Erkenntnisse sind aber oft vergleichsweise wertvoll.

Improvements
------------

**Consider adding usability tests**


