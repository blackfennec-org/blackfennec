Usability Tests
===============

Release v0.6
************

This usability test was conducted for the release of version 0.6.0. It contains multiple tasks that can be used to the the systems usability. These tasks are dedicated to personas that have little to none experience with the application, in order to be representative of users that use our application for the first time.

Personas
--------
In this study four persons participated. We mapped three of the testers to a :ref:`persona <personas>`, which fits their background and potential usage best.
The last tester was not in the target group and had a non technical background.

========  =========
 Tester    Persona
========  =========
 CC         :ref:`Matthew`
 YH         :ref:`Sun`
 MB         :ref:`Alan`
 CH         Not in target group
========  =========

Tasks
-----
The tasks are to be read to the user that is testing the application. The tester is encouraged to think aloud by the test supervisor, by asking them to whenever necessary.

Open a Project
""""""""""""""
Open the project `examples` which is located under `$BLACK_FENNEC_HOME/examples`.

Preconditions
~~~~~~~~~~~~~
- Black Fennec is started.
- The main UI is loaded.
- Presenter is configured.

Goals
~~~~~
The project is loaded and the associated files are accessible through the `Project File Tree`.

Observation
~~~~~~~~~~~

==============  =================
 Tester          Observation
==============  =================
CC               Intuitively Correct
YH               Intuitively Correct
MB               Intuitively Correct
CH               Double clicked folders, and was unsure how to open project, because in folder with only files nothing could be selected.
==============  =================

Open a File
"""""""""""
Open the file named `black_fennec.json`.

Preconditions
~~~~~~~~~~~~~
- Black Fennec is started.
- The main UI is loaded.
- Presenter is configured.
- The project `examples` is open.

Goals
~~~~~
The presenter displays the file.

Observation
~~~~~~~~~~~

==============  =================
 Tester          Observation
==============  =================
CC               Intuitively Correct
YH               Intuitively Correct
MB               Intuitively Correct
CH               Single click tried first, then double click
==============  =================


Navigate Structure
""""""""""""""""""
In the file `black_fennec.json`, find and navigate to the `Person` called `Lara`.

Preconditions
~~~~~~~~~~~~~
- Black Fennec is started.
- The main UI is loaded.
- Presenter is configured.
- The project `examples` is open.
- The file `black_fennec.json` is open.

Goals
~~~~~
The user recognises the correct location.

Observation
~~~~~~~~~~~

==============  =================
 Tester          Observation
==============  =================
CC               N/A
YH               N/A
MB               Intuitively Correct; List is not immediately obvious.
CH               Intuitively Correct; Thinks whole list item should be clickable
==============  =================


Open two Files
""""""""""""""
Open the files named `black_fennec.json` and `user_db.json`.

Preconditions
~~~~~~~~~~~~~
- Black Fennec is started.
- The main UI is loaded.
- Presenter is configured.
- The project `examples` is open.

Goals
~~~~~
The main ui opened two tabs, each with a presenter displaying one file.

Observation
~~~~~~~~~~~

==============  =================
 Tester          Observation
==============  =================
CC               Intuitively Correct; Did not expect file to open in background.
YH               Intuitively Correct; Did not expect file to open in background.
MB               Intuitively almost Correct; Did not immediately see newly opened file and reopened file; Did not expect file to open in background.
CH               Intuitively Correct; Did not expect file to open in background.
==============  =================

Switch Tabs
"""""""""""
Switch between to opened files.

Preconditions
~~~~~~~~~~~~~
- Black Fennec is started.
- The main UI is loaded.
- Presenter is configured.
- The project `examples` is open.
- Two files have been opened.

Goals
~~~~~
The content of the two files can be displayed at will.

Observation
~~~~~~~~~~~

==============  =================
 Tester          Observation
==============  =================
CC               Intuitively Correct
YH               Intuitively Correct
MB               Intuitively Correct
CH               Intuitively Correct
==============  =================

Edit Text
"""""""""
Edit the text in a text field.

Preconditions
~~~~~~~~~~~~~
- Black Fennec is started.
- The main UI is loaded.
- Presenter is configured.
- The project `examples` is open.
- The file `black_fennec.json` has been opened.

Goals
~~~~~
The text in any text field has changed.

Observation
~~~~~~~~~~~

==============  =================
 Tester          Observation
==============  =================
CC               Intuitively Correct
YH               Intuitively Correct
MB               Intuitively Correct
CH               Intuitively Correct; Noticed that language differed when right clicking text field
==============  =================

Edit Truth Value
""""""""""""""""
Edit the value of a true/false question.

Preconditions
~~~~~~~~~~~~~
- Black Fennec is started.
- The main UI is loaded.
- Presenter is configured.
- The project `examples` is open.
- The file `black_fennec.json` has been opened.

Goals
~~~~~
The truth value in any switch has changed.

Observation
~~~~~~~~~~~

==============  =================
 Tester          Observation
==============  =================
CC               Intuitively Correct
YH               Intuitively Correct
MB               Intuitively Correct
CH               Intuitively Correct; Not immediately clear what was meant with truth value
==============  =================

Edit Field Name
"""""""""""""""
Edit the name of a filed/row.

Preconditions
~~~~~~~~~~~~~
- Black Fennec is started.
- The main UI is loaded.
- Presenter is configured.
- The project `examples` is open.
- The file `black_fennec.json` has been opened.
- A map is presented to the user.

Goals
~~~~~
The key in a map item has changed.

Observation
~~~~~~~~~~~

==============  =================
 Tester          Observation
==============  =================
CC               Intuitively almost Correct; first tried Double Click, then Right Click; Expected current key value in the text field
YH               Intuitively almost Correct; first tried Singe Click, then Double Click then Right Click; Did not know which row he is editing; Expected row to be highlighted
MB               Intuitively almost Correct; Did not intuitively expect key to be editable; First tried Double Click, then Right Click; No further comments
CH               Intuitively Correct
==============  =================

Remove Field
"""""""""""""""
Remove a filed/row.


Preconditions
~~~~~~~~~~~~~
- Black Fennec is started.
- The main UI is loaded.
- Presenter is configured.
- The project `examples` is open.
- The file `black_fennec.json` has been opened.
- A map or list is presented to the user.

Goals
~~~~~
The row in a map/list item is removed.

Observation
~~~~~~~~~~~

==============  =================
 Tester          Observation
==============  =================
CC               Intuitively Correct
YH               Intuitively Correct
MB               Intuitively Correct
CH               Intuitively Correct
==============  =================

Add Field to List
"""""""""""""""""
Add a item of type `String` to a list.

Preconditions
~~~~~~~~~~~~~
- Black Fennec is started.
- The main UI is loaded.
- Presenter is configured.
- The project `examples` is open.
- The file `black_fennec.json` has been opened.
- A list is presented to the user.

Goals
~~~~~
A row in a list item of type `String` was added.

Observation
~~~~~~~~~~~

==============  =================
 Tester          Observation
==============  =================
CC               Intuitively almost Correct; Expected Right Click in empty Space; Expected Add Button;
YH               Intuitively almost Correct; Expected Right Click in empty Space; Expected Add Button; First entered random text, then inspects dropdown menu; Expected behaviour not clearly communicated.
MB               Intuitively almost Correct; Purpose of Template Text Filed not intuitively clear
CH               Intuitively almost Correct; Expected Right Click in empty Space; Expected Add Button;
==============  =================

Add Field to Map
""""""""""""""""
Add a item of type `String` to a map.

Preconditions
~~~~~~~~~~~~~
- Black Fennec is started.
- The main UI is loaded.
- Presenter is configured.
- The project `examples` is open.
- The file `black_fennec.json` has been opened.
- A map is presented to the user.

Goals
~~~~~
A row in a map item of type `String` was added.

Observation
~~~~~~~~~~~

==============  =================
 Tester          Observation
==============  =================
CC               Intuitively Correct; Same issues as with `Add Field to List`
YH               Intuitively Correct; Same issues as with `Add Field to List`
MB               Intuitively Correct; Same issues as with `Add Field to List`
CH               Intuitively Correct; Same issues as with `Add Field to List`
==============  =================

Save File
"""""""""

Save changes made to a file.

Preconditions
~~~~~~~~~~~~~

Black Fennec is started.
- The main UI is loaded.
- Presenter is configured.
- The project `examples` is open.
- A file is open.
- The file was edited.

Goals
~~~~~
Changes made to file are persisted.

Observation
~~~~~~~~~~~

==============  =================
 Tester          Observation
==============  =================
CC               Intuitively Correct; Expected Auto Save; No Feedback on Action; Unexpected behaviour: saves all files => Rename button to "save all"?
YH               Intuitively Correct
MB               Intuitively Correct; Expected entire project to be saved (which is what happens); Expected Feedback on Action
CH               Intuitively Correct
==============  =================
