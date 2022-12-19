.. _usability_test_template:

========================
Usability Test Templates
========================

This template can be used to conduct usability tests of the black-fennec application. It contains multiple tasks that can be used to the the systems usability. These tasks are dedicated to personas that have little to none experience with the application, in order to be representative of users that use our application for the first time.

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
<Name>          <Observation>
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
<Name>          <Observation>
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
<Name>          <Observation>
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
<Name>          <Observation>
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
<Name>          <Observation>
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
<Name>          <Observation>
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
<Name>          <Observation>
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
<Name>          <Observation>
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
<Name>          <Observation>
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
<Name>          <Observation>
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
<Name>          <Observation>
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
<Name>          <Observation>
==============  =================


Run an Action
"""""""""""""
Run an action.

Preconditions
~~~~~~~~~~~~~
- Black Fennec is started.
- The main UI is loaded.
- Presenter is configured.
- A file is open.

Goals
~~~~~
The user finds the action and can run it.

Observation
~~~~~~~~~~~

==============  =================
 Tester          Observation
==============  =================
 <Name>          <Observation>
==============  =================


Open File from File Manager
"""""""""""""""""""""""""""
From the file manager, open a file in Black Fennec.

Preconditions
~~~~~~~~~~~~~
- Black Fennec is NOT started.
- The file manager displays a JSON file.

Goals
~~~~~
The file is opened in Black Fennec when double clicked.

Observation
~~~~~~~~~~~

==============  =================
 Tester          Observation
==============  =================
 <Name>          <Observation>
==============  =================


Missing Extension Dialog
""""""""""""""""""""""""
Install the missing recommended extensions.

Preconditions
~~~~~~~~~~~~~
- Black Fennec is installed correctly.
- A recommended extension is missing.
- Black Fennec is started.
- The missing extensions dialog is displayed.

Goals
~~~~~
The recommended extensions are installed.

Observation
~~~~~~~~~~~

==============  =================
 Tester          Observation
==============  =================
 <Name>          <Observation>
==============  =================

The missing recommended extensions dialog does not inform the user that Black Fennec must be restarted to use newly installed extensions.


Notes
~~~~~
Add notes here.

Conclusion
~~~~~~~~~~
Add conclusion here.
