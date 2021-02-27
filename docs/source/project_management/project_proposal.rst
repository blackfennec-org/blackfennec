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

Consulting and Review Times
*************************** 
===============  ======  =======  =========  =========  ======
*Time Slots*     Monday  Tuesday  Wednesday  Thursday   Friday 
===============  ======  =======  =========  =========  ======
**08:00-09:00**                                         XO      
**09:00-10:00**                                         XO      
**10:00-11:00**                                         (XO)    
**11:00-12:00**                                         (XO)    
**12:00-13:00**                                         (XO)    
**13:00-14:00**                                         XO      
**14:00-15:00**                                         XO      
**15:00-16:00**                                         XO      
**16:00-17:00**                                         XO      
**17:00-18:00**                                         (XO)    
**18:00-19:00**                                                 
===============  ======  =======  =========  =========  ======

| X   = Team is available
| (X) = Team is available if need be  
| O   = Meeting online is possible
| P   = Meeting physically at Campus OST-RJ is possible
|     = Team is unavailable

Motivation
**********

We personally require an application that is able to manage unstructured data in a dynamically structured way. Additionally it ought to be possible to use versioning and collaborative tools such as git. This is why we want to develop such an application as our Engineering Project. We will use Black Fennec to help us organize and share unstructured data.

Typical Use Case
^^^^^^^^^^^^^^^^
A headhunter tasked with employing a software engineer for a company found a Github repository of a promising candidate. He will contact the candidate but first wants to know more about her in order to better influence her into taking the job.

For this Marco, the headhunter, creates a new Black Fennec Project. There he can add information already gathered from the Github profile into a pre-existing template. A extension might allow automatic crawling of additional information based on what was previously entered, automating a repetitive task. Some of the new information can now be used to further research the target. All additional data can be added to the project, even if no specific template exists. Once he is done the project can be pushed to a remote server where others can continue working.

Project Idea
************
Black Fennec is a versionable, extendable, dynamically structured information management tool that is visually appealing and pleasant to use. 


Extensibility is generally very important to the project, because these modules are an important part of the work. The base of the project offers only very basic functionalities which we want to extend in the context of this work. This allows us to work independently and scale the effort dynamically.

Project idea discussed with: Thomas Kälin

Implementation
**************
The application is based on YAML/JSON files which are interpreted and visualized in a Python client. The GUI technology is not decided yet, but the plan is to go in the direction of declarative frameworks (XAML/HTML). The extensions will have their own dependencies which need to be installed automatically. The client is optimized for desktop systems.

Technology
^^^^^^^^^^
As mentioned, we will develop our project using Python. We strive for Test Driven Development and this will be realized with the help of the PyTest module. Our GUI will be implemented using GTK3, which supports Linux, MacOS and Windows. We will use MVVM to separate UI from logic.

Core
^^^^
The core is the basis of our project and should provide a framework that allows the various extensions to integrate into the system. In addition, it offers certain core features that are generally required. These are in particular the types String, Number, References, List and Dictionary. These types form the basis of the dynamic object model, which is very well suited for our product. The core GUI, which also contains the visualization of the listed types, is also implemented here. Support for the search feature must also be implemented in the core.

Base
^^^^
Base is the only directly built-in extension. It provides functionality that our users are frequently relaying on. For example the types: File, Image, Date, Location. You can also think of Base as a Minimal Viable Product. The goal is to keep it as lean as possible and to outsource any additional functionality to other extensions, so that our application remains as flexible as possible.

Additional Extensions
^^^^^^^^^^^^^^^^^^^^^
This list is a incomplete collection of extensions that could be implemented in the future. They are mainly listed here for you to get a feel what might be coming, if we find the time to implement more then just of Black Fennec.

==================      ======================================================
Extension Name          Description
==================      ======================================================
GitHub Crawler          Automated crawling of user data of a GitHub account by specifying the profile URI.
Facebook Crawler        Automated crawling of user data of a Facebook account by specifying the profile URI.
LinkedIn Crawler        Automated crawling of user data of a LinkedIn account by specifying the profile URI.
Facial Recognition      Extraction of faces from images. Possibly referencing to similar faces within the project.
Google Dorks            Generate Google Dorks from selected Types.
==================      ======================================================