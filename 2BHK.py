
    # Importing all necessary libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt

# List of Locations in Bangalore
location_list = ['Hennur', 'Kempegowda', 'Siddapura', 'Bellandur', 'HSR Layout', 'Chennamanakere Achukattu',
                 'Halasuru', 'Viveknagar', 'Jnanabharathi', 'Hulimavu', 'R T Nagar', 'Basaveshwara Nagar',
                 'Kalasipalya', 'Mahadevapura', 'JC Nagar', 'K G Halli', 'Vyalikaval', 'Jeevan Bhima Nagar',
                 'Bagalgunte', 'Talaghattapura', 'Kumaraswamy Layout', 'JP Nagar', 'Subramanyapura',
                 'Byatarayanapura', 'V V Puram', 'RajaRajeshwari Nagar', 'Mico Layout', 'Basavanagudi',
                 'Thilaknagar', 'Magadi Road', 'Chamrajpet', 'Shivajinagar', 'Banashankari', 'Girinagar', 'Adugodi',
                 'Jayanagar', 'Hanumantha Nagar', 'Upparpet', 'Koramangala', 'Seshadripuram', 'High Grounds',
                 'Subramanya Nagar', 'Bharthinagar', 'Ashoka Nagar', 'Sampangi Rama Nagar', 'Rajajinagar',
                 'Electronic City', 'Pulikeshi Nagar', 'Bandepalya', 'SJ Park', 'Cottonpet', 'Siddapura',
                 'JJR Nagar', 'Basavanagudi', 'Baiyappanahalli', 'Mahalakshmipuram', 'Parappana Agrahara',
                 'Vidyaranyapura', 'Banaswadi', 'Suddaguntepalya', 'Hampi Nagara', 'Kempapura Agrahara',
                 'Upparapete', 'Sampigehalli', 'Jalahalli', 'Hebbal', 'Vijayanagar', 'KG Halli', 'Siddapura',
                 'Lalbagh', 'Kengeri', 'Indiranagar', 'Begur', 'Azad Nagar', 'Krishnarajapura', 'Srirampura',
                 'CITY MARKET', 'Peenya', 'Whitefield', 'Soladevanahalli', 'Rajagopal Nagar', 'Ramamurthinagar',
                 'Kadugudi', 'Raghuvanahalli', 'Uttarahalli', 'Anjanapura', 'ISRO layout', 'Yelachenahalli',
                 'Yelahanka', 'Cubbon Park', 'Bannerghetta', 'Akshayanagar', 'DC halli', 'Gubbalala']

# creating a dictionary for storing the information after scraping
IIBHKHouse_details = {
    "Details": [],
    "Amenities": [],
    "Agent": [],
    "Rent": [],
    "Location": [],
    "Seller": [],
    "Carpet_area": []
}

# requesting sourcecode of the website for data extraction
var = requests.get('https://www.commonfloor.com/bangalore-property/for-rent/apartment-ht/2-bhk').text
soup = BeautifulSoup(var, 'html.parser')
houses = soup.find_all('div', class_='snb-tile')
carpet_area_array = soup.find_all('small', class_ = "smtext")

i = 0

# for each house we will scrape agent, details, rent, seller, location, amenities.
for house in houses:
    agent = house.find('div', class_="infownertext").find("small").text
    details = house.find('div', class_="inforow pull-left graybg").text.replace(' ', '')
    carpet_area = carpet_area_array[i].text
    rent = house.find('span', class_='s_p').text.replace('', '')
    for a in house.findAll('a', attrs={'class': 'gtpnd'}):
        seller = a.text
    location = house.find('a', class_='gtloc').text
    description_of_apartment = house.find('div', class_='inforow pull-left graybg').text
    info_para = house.find('div', class_='info_para').text
    amenities = []
    for ul in house.findAll('ul', class_='i_l clearfix'):
        if ul.find('house'):
            break
        amenities.append(ul)
    for ul in amenities:
        IIBHKHouse_details["Amenities"].append(ul.text)

    # Printing all the extracted data
    print(f'''
            The Details of this apartment are: {details}
            The Rent of this Apartment is {rent}
            The Agent of this Apartment is: {agent}
            The Seller of this Apartment is: {seller}
            The Location of this Apartment is: {location}
            The Carpet Area of this Apartment is: {carpet_area}
        ''')
    print('---------------------------------------------------------------------------------')

    # Saving extracted data in the dictionary created above
    IIBHKHouse_details["Details"].append(details)
    IIBHKHouse_details["Agent"].append(agent)
    IIBHKHouse_details["Rent"].append(rent)
    IIBHKHouse_details["Location"].append(location)
    IIBHKHouse_details["Seller"].append(seller)
    IIBHKHouse_details["Carpet_area"].append(carpet_area)

    i += 1
    # Converting the dictionary into a pandas DataFrame and then to CSV file
df = pd.DataFrame.from_dict(IIBHKHouse_details, orient="index")
df = df.transpose()
df.to_csv("IIBHKHouse_details.csv")
df = pd.read_csv("IIBHKHouse_details.csv", index_col=0)
df.tail(5)

# Checking for null values in our data if any
df.isna().sum()

# lets drop the null values
df = df.dropna()

# Checking for duplicate values in our data if any
var = df[df.duplicated(subset=["Details", "Amenities", "Agent", "Rent", "Location"])].shape

# lets lower case all the strings to avoid redundancy
df = df.apply(lambda x: x.astype(str).str.lower())
df.Amenities = [amenities.split("\n") for amenities in df.Amenities]
df.Details = [details.split("   ") for details in df.Details]
df.Seller = [seller.split("\n") for seller in df.Seller]
variable = df[15:20]

# Plotting a chart for locations with high apartment availability in Bangalore
df.Location.apply(pd.Series).value_counts()[:10].plot.pie(figsize=(12, 10), startangle=50, autopct='%1.1f%%',
                                                          fontsize=15)
plt.title("Location Wise Apartment Availability", fontsize=30)
centre_circle = plt.Circle((0, 0), 0.72, color='gray', fc='white', linewidth=1.25)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.axis('equal')
plt.show()

# Plotting a chart for popular Sellers in Bangalore
df.Seller.apply(pd.Series).value_counts()[:10].plot.pie(figsize=(12, 10), startangle=50, autopct='%1.1f%%',
                                                        fontsize=15)
plt.title("Sellers in Bangalore", fontsize=30)
centre_circle = plt.Circle((0, 0), 0.72, color='gray', fc='white', linewidth=1.25)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.axis('equal')
plt.show()

# Plotting a chart for popular agents in Bangalore
df.Agent.apply(pd.Series).value_counts()[:10].plot.pie(figsize=(12, 10), startangle=50, autopct='%1.1f%%',
                                                       fontsize=15)
plt.title("Agents in Bangalore", fontsize=30)
centre_circle = plt.Circle((0, 0), 0.72, color='gray', fc='white', linewidth=1.25)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.axis('equal')
plt.show()

# Plotting a bar graph for location vs rent
# Plotting a bar graph for carpet area vs rent

# lets convert the amenities column into a separate DataFrame, which makes things easy for pre processing
jj = pd.DataFrame(df.Amenities.apply(pd.Series).stack().value_counts()).reset_index()
jj.columns = ["amenities", "count"]
jj.head()

# lets first find the top amenities in an apartment
AMENITIES = {}
AMENITIES['parking'] = jj["count"][jj['amenities'].str.contains('park', regex=True)].sum()
AMENITIES['power_backup'] = jj["count"][jj['amenities'].str.contains('power', regex=True)].sum()
AMENITIES['swimming_pool'] = jj["count"][jj['amenities'].str.contains('swim', regex=True)].sum()
AMENITIES['security'] = jj["count"][jj['amenities'].str.contains('security', regex=True)].sum()
from operator import itemgetter

AMENITIES = dict(sorted(AMENITIES.items(), key=itemgetter(1), reverse=True))
AMENITIES
plt.bar(AMENITIES.keys(), AMENITIES.values(),
        color=["#FE6363", "#66FA72", "#6B89F9", "c", "y", "pink", "#63FCFE", "#DD63FE"])
plt.xticks(rotation=80, fontsize=15)
plt.title("Available Amenities", fontsize=20)
plt.show()

plt.title("Carpet Area VS Rent")
plt.scatter(df.Rent, df.Carpet_area)
plt.xlabel('rent', fontsize=12)
plt.ylabel('carpet area', fontsize=12)
plt.show()









