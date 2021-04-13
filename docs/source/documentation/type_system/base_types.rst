.. _definition_base_types:

Base Types
==========
Base types are structures built on core types. They are not special compared to any other type a type extension might provide but are so commonly used that they are pre-installed with Black Fennec.

Time
""""
Represents a time without specifying a date. Can also deal with inaccuracies.

TimeRange
"""""""""
Includes start time and end time.

DateTime
""""""""
Represents a data and a time. Can also deal with inaccuracies via Time.

DateTimeRange
"""""""""""""
Includes start date time and end date time.

Location
""""""""
Represents a physical location. Can be specified in different formats including coordinates or addresses. Can also deal with inaccuracies via Distance.

Distance
""""""""
Represents distance between objects or locations, or size of objects.

File
""""
Represents a file pointed to by a URL (e.g. file url: "file://file.csv")

Image
"""""
Represents a image and can render it within Black Fennec. Inherits properties from File.


