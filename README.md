# House-Rental-Analysis
1 Project Profile
1.1 Project Definition.
Know Your Rent is a program, where we can check statistical data of  the rents/ rates of various apartments for purchase, rent or lease in Bangalore. The program scrapes commonfloor.com for data and analyzes it to draw relevant conclusions. This program is not specific for apartments but can also be applied to independent houses in various places in Bangalore.


1.2 Project Duration.
The project idea began with thinking about students going to different cities for education and how their accommodation is managed. This program was then designed to help students or employees who travel to Bangalore for work or studies to aid in their apartment searching process.


1.3 Objective.
In the 21 century, as the working population increases, so do their incomes. Thus, we are also seeing a surge in rents/ rates of properties, houses, apartments. The purpose of this program is to know what owners are charging their tenants as rent or how much properties in different areas of Bangalore cost. We also check the amenities, seller, location and rent of the apartment.



2 System Environment
2.1 Frontend Tool.
The frontend of the project was built using HTML, CSS and Javascript. For a user to use this program, all they would need is a functional web browser.

2.2 Backend Tool.
But for the server, they’ll need the following:
Hardware requirements:
Intel i5 7th gen and above or an AMD equivalent
3 GB - 5 GB ROM
8 Gb and above RAM
Software Requirements:
Any modern day operating system
A modern Operating System is one that supports python3 and other libraries mentioned below.

PyCharm or any Python IDE
	PyCharm is an integrated development environment used in computer programming, specifically for the Python language. It is developed by the Czech company JetBrains.
An integrated development environment is a software application that provides comprehensive facilities to computer programmers for software development. An IDE normally consists of at least a source code editor, build automation tools and a debugger.
Python
Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse.
BeautifulSoup
Beautiful Soup is a Python package for parsing HTML and XML documents. It creates a parse tree for parsed pages that can be used to extract data from HTML, which is useful for web scraping.
Matplotlib
Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy. It provides an object-oriented API for embedding plots into applications using general-purpose GUI toolkits like Tkinter, wxPython, Qt, or GTK.

Pandas
pandas is a software library written for the Python programming language for data manipulation and analysis. In particular, it offers data structures and operations for manipulating numerical tables and time series. 
Requests
The requests module allows you to send HTTP requests using Python. The HTTP request returns a Response Object with all the response data (content, encoding, status, etc).




2.3 Tools and Technologies.
The application has these 6 server side modules:

Connection: In this module, we establish connection with the website for scraping.
Extraction: Now that the connection is established, we extract the necessary data from that website.
Storing, We store the extracted information in a pandas dataframe, then we convert it into a CSV file.
Cleaning: We clean the extracted data by converting everything to lowercase and replacing missing values with 0.
Visualization: We used the cleaned extracted data to generate charts and graphs.
Database: We have a database to store client data for authentication purposes.
3 Design Methodology of Proposed Work
3.1 Stages.
Stage 1: The first objective was to successfully scrape data from commonfloor.com and clean it.
The first step included writing python code to scrape data from commonflood.com using BeautifulSoup, a python library that extracts data from HTML or XML code by dividing the attributes into trees. BeautifulSoup does this with existing HTML code that was extracted using requests, a python library that goes to the URL provided in the syntax parameter and retrieves the website’s entire HTML file.

Stage 2:The Second objective is to make a website to host all the visualizations drawn from our scraped data. 
The website was made by using HTML, CSS and Javascript. The website hosts visualizations of Location wise apartment availability frequency, Sellers with high market dominance, Agents who are actively aiding sellers sell their apartments and occupants find their apartments in Bangalore. It also hosts graphs that show popular amenities in apartments in Bangalore and how an increase in carpet area affects rent. All of the above charts are available for 1, 2, 3 Bedroom, hall and kitchen apartments in Bangalore. The website has a login module, which in future can be used to send alerts to users whenever the website has new information, or a new article is published. Users can also request alerts as and when an apartment is available in a certain location in Bangalore.

Stage 3: Perform data analytics on the extracted data to generate graphs/ charts and upload it to our website. 
The data extracted from commonfloor.com was used to generate the following visualization charts using matplotlib, a python library used to produce visualization charts: Location wise apartment availability frequency, Sellers with high market dominance, Agents who are actively aiding sellers sell their apartments and occupants find their apartments in Bangalore. It also hosts graphs that show popular amenities in apartments in Bangalore and how an increase in carpet area affects rent. All of the above charts are available for 1, 2, 3 Bedroom, hall and kitchen apartments in Bangalore.
4 Data Dictionary
4.1 All Tables and Details (CSV files).
This Project uses Python files that generate a CSV file for each type of apartment, i.e, 1 BHK, 2 BHK and 3 BHK. The CSV files store the following data: 
Apartment Details
Agents
Rent
Locations
Sellers
Carpet Area.
We then use these details to generate relevant charts/ Graphs.
This project hosts a login page for both customers and admins. With this, a customer can register themselves with our website for future notifications as and when new details are uploaded. Although this is a simple login page that is made using javascript text validation, in future this can be improved to support php and authenticate using database login. The database will contain two four tables. Admin table, Admin login details table, Customer table, Customer Login Details table, containing Admin ID and name, Admin ID and password, Email ID and name, surname and phone number, Email ID and password respectively.
6.3 Primary Keys and Foreign Keys
In the Customer table, there is one Primary Key and Foreign Key, i,e. Email ID. In order to login as a Customer they must use their Email ID and password.
In the Admin table, there is one Primary Key and Foreign Key, i,e. Admin ID. In order to login as a Customer they must use their assigned Admin ID and password.
6.4 Relations.
The Admin table and admin login details are related by sharing Admin ID field as foreign key.
The Customer Table and Login Details tables are related by having Email ID from Customer table as a Foreign Key in the Login Details table.
7 Future Enhancements:
In future, we can expand the scope of this program from rental rates to purchase rates and make the webpage available for public usage. The program can be  self-sustaining when owners begin posting ads directly to this application. Humans comprehend the differences when they can visually see price, feature differences. Since the program visually represents the seller also, the general public can easily trust a seller based on the number of properties they are selling at any given point of time. The website has a login module, which in future can be used to send alerts to users whenever the website has new information, or a new article is published. Users can also request alerts as and when an apartment is available in a certain location in Bangalore.
