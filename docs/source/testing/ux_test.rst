Usability Test Template
=======================


Tasks
-----

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

Save File
---------

Save changes made to a file.

Preconditions
~~~~~~~~~~~~~-

Black Fennec is started.
- The main UI is loaded.
- Presenter is configured.
- The project `examples` is open.
- A file is open.
- The file was edited.

Goals
~~~~~
Changes made to file are persisted.