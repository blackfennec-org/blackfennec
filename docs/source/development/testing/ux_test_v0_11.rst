.. _usability_study_0.11.0:

=============================
Usability Study Release v0.11
=============================

This usability test was conducted for version 0.11.0. This is the release preceding version 1.0 which optimally can address some of the recognized shortcomings.

It contains multiple tasks that can be used to the the systems usability. These tasks are dedicated to personas that have little to none experience with the application, in order to be representative of users that use our application for the first time.

Personas
--------

2 personas have participated in this study. We mapped each of them to a :ref:`persona <personas>` which most closely fits their background and potential usage.

==============  =================
 Tester          Persona
==============  =================
 TW              :ref:`Alan`
 MB              :ref:`Sun`
==============  =================

Tasks
-----
The tasks are to be read to the user that is testing the application. The tester is encouraged to think aloud by the test supervisor, by asking them to whenever necessary.

Open a Project
""""""""""""""
Open the folder `examples` which is located under `$BLACK_FENNEC_HOME/examples`.

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
 TW              Intuitively correct
 MB              Intuitively correct; suggested to remove empty list pattern
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
 TW              Intuitively correct
 MB              Intuitively correct; expected context menu in file tree (e.g. rename file)
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
 TW              "empty" list is not intuitive; suggests showing a preview. Is concerned that new columns might be missed by user; could be solved with auto-scrolling.
 MB              "empty" list is not intuitive; suggests showing a preview.
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
 TW              Intuitively correct
 MB              Intuitively correct; expected tab switch when "opening" same file multiple times
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
 TW              Intuitively correct
 MB              Intuitively correct
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
 TW              Intuitively correct. Not sure if the change is saved automatically; suggests change indicator (e.g. asterisk) and a warning on close.
 MB              Intuitively correct; expects save button or change indicator
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
 TW              Intuitively correct
 MB              Intuitively correct
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
 TW              double click, right click, edit button
 MB              right click, edit button; expected check mark to save entire file
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
 TW              first tried using the delete key, then edit button; noted it to be intuitive but would like to see more short cuts like this.
 MB              Intuitively correct
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
 TW              Intuitively correct
 MB              expected enter to add item. entered unknown type in type field; was not stopped from doing so.
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
 TW              Intuitively correct
 MB              Intuitively correct
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
 TW              Intuitively correct; right click on tab
 MB              Intuitively correct; expected 'save changes' warning on close
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
 TW              Intuitively correct
 MB              Expected to run action from field of string
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
 TW              Intuitively correct
 MB              Intuitively correct
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
 TW              Intuitively correct and restarted Black Fennec.
 MB              Did not read error fully, expected 'install' to just install the missing extensions, did not immediately find extensions in software center. Suggested better error message and to rename the 'install' button to 'open software center'
==============  =================

The missing recommended extensions dialog does not inform the user that Black Fennec must be restarted to use newly installed extensions.


Notes
~~~~~

Some of the subjects whished for a more keyboard friendly UX. The argument is, that users are more productive with keyboard shortcuts. Some of the suggested shortcuts are:

- Delete: Delete a row in a list or map
- Keyboard navigation through the structure

It was also noted, that changing the key of a map item is somewhat cumbersome as the user has to click on the edit button located at the very top of the column. Suggested alternatives include:

- Double click on the key
- Right click on the row

It was also noted that users tend to ignore error messages and just click the most suggestive button. We should consider to change the error message to something more informative and to rename the button to something more descriptive of what actually happens.

Conclusion
~~~~~~~~~~

Although the test subjects were not familiar with Black Fennec, they were able to use it mostly intuitively. However, the study has also shown that there is room for improvement.
