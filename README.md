# AirBnB Data Exploration
<img width="822" height="547" alt="image" src="https://github.com/user-attachments/assets/75b8fcd0-96d5-4df0-92bf-e4b22ab5cc0e" />


## Table Of Contents
- [Overview](#overview)
- [Questions](#questions)
- [Visualization](#visualization)
  - [Listing](#listing)
  - [Price vs Reviews](#price-vs-reviews)
  - [Graphical Map](#graphical-map)
- [Conclusion](#conclusion)
- [Photo and Data Credits](#photo-and-data-credits)

# Overview

Airbnb is an online marketplace that connects hosts offering short-to-long-term stays, experiences, and services with guests worldwide. The company operates on a peer-to-peer model, allowing individuals to rent out a wide variety of properties like private rooms, entire houses or apartments, and even unique spaces like castles. Airbnb allows hosts to set their price, availability, decide whether to rent their whole home or just a single room as well as decide on what listing name they want for their property. This exploration is for educational purposes only and meant to see what can be discovered through diving deeper into the data.

The dataset was pulled from [kaggle](https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data/data) and contains information of close to 50,000 hosts during the 2019 calendar year. The analysis is based on data collected from the public Airbnb platform that is verified, aggregated and publicly available.

# Questions

* What factors would make an AirBnB location have the highest chance to be the most profitable?
* If I’m new to being an airbnb host or wanted to become on, how should I go about setting my price, choosing my listing?
* What is a realistic number of bookings that I can expect per month?

# Visualization

There were three main focuses I had for this project. First, I wanted to see how listing name played a part in how likely an Airbnb would be booked. Second based on market, determine an appropriate price for listings. Finally I wanted to display this data on a map to see if other influences played a part in success of these hosts.

For my visualization I decided to look deeper at the Top Performers in the dataset. "Top Performer" is refering to the listings that were in the Top 10 percent of Total Number of Reviews AND the Top 10 percent of Monthly Reviews. Comparisons also needed to be geographically based, meaning I'm taking the data and breaking it down into the Top Performers by region to see results. There were five distinct regions for this exploration which included the Bronx, Brooklyn, Manhattan, Queens, and Staten Island. I also provided information on Top Performers Overall in New York for general insight.

## Listing

When analyzing the listing names of the Airbnb Hosts, I decided that common conjunctions and prepositions may not be too relevant for this context so I decided to remove them from the results.
Results are shown below.

Bronx
<img width="1189" height="390" alt="common_words_bronx" src="https://github.com/user-attachments/assets/2ecdbdea-520a-4036-85a9-4b9aa7fa303b" />

Brooklyn
<img width="1189" height="390" alt="common_words_brooklyn" src="https://github.com/user-attachments/assets/775924fa-d626-4ad5-a60a-d41bd3a1e75e" />

Manhattan
<img width="1189" height="390" alt="common_words_manhattan" src="https://github.com/user-attachments/assets/fb651a84-af48-41f6-a953-d099ec610767" />

Queens
<img width="1189" height="390" alt="common_words_queens" src="https://github.com/user-attachments/assets/245c040f-f7f3-4b75-85de-12df16e5af1f" />

Staten Island (limited amount of active top performers from Staten Island)
<img width="1189" height="390" alt="common_words_staten_island" src="https://github.com/user-attachments/assets/e246d203-f53b-4b12-85d8-1945ddc1f10a" />

Top Performers Overall
<img width="1189" height="390" alt="common_words_overall" src="https://github.com/user-attachments/assets/00d1eeac-1e1c-4d15-85e8-f3c205e4acd5" />

Whole Dataset
<img width="1189" height="390" alt="common_words_whole" src="https://github.com/user-attachments/assets/db29af17-ba78-4971-b4a8-85ab9d9c0f2b" />

### Trends
* Good listings normally contain the type of listing (private room, 2-bedroom apartment)
* Adding in proximity to local attractions or airports is beneficial (Yankee Stadium, Times Square).
* Adding adjectives such as spacious, or cozy may slightly increase chance for the listing to stand out.

[Back to Top](#Table-of-Contents)

## Price vs Reviews

When analyzing the Rrice Comparison to the Number of Total and Monthly Reviews it is important to consider the difference in the listing type. Is the listing a single private room or is the entire house or apartment available for short-term lease?
Results are shown below.

Bronx
<img width="1390" height="390" alt="price_vs_reviews_bronx" src="https://github.com/user-attachments/assets/cbec55af-51fe-47cb-890f-e65280544941" />

Brooklyn
<img width="1390" height="390" alt="price_vs_reviews_brooklyn" src="https://github.com/user-attachments/assets/2e3d6111-5963-4e25-8d6e-d8930df7fd6f" />

Manhattan
<img width="1390" height="390" alt="price_vs_reviews_manhattan" src="https://github.com/user-attachments/assets/7e493367-4eb2-47b2-98ea-8c3592579ce7" />

Queens
<img width="1390" height="390" alt="price_vs_reviews_queens" src="https://github.com/user-attachments/assets/f6942fec-7231-43e6-8f3f-0a23d8136a39" />

Staten Island (limited amount of active top performers from Staten Island)
<img width="1390" height="390" alt="price_vs_reviews_staten_island" src="https://github.com/user-attachments/assets/48d738be-d860-40f6-bfe8-00dc2357a0b3" />

Top Performers Overall
<img width="1390" height="390" alt="price_vs_reviews_overall" src="https://github.com/user-attachments/assets/9ef0d1b3-04d5-4e44-a972-c5171cab51e0" />

### Trends
* Overall we see that the price of entire home listings are listed at a higher average price than single private rooms as might be expected.
  
<ins>Top Performing Private Room Listings</ins>
  * Bronx, Brooklyn, and Queens average  listing price is ~$50 per night
  * Manhattan average listing price is ~$75-$125.
  * Staten Island doesn't appear to have any current Top Performing private room listings which could provide a potential opportunity or a caution.

<ins>Top Performing Entire Home/Apt Listings</ins>
  * Bronx average listing price is ~$100
  * Brooklyn average listing price ~$100-$200
  * Manhattan average listing price ~150-$350
  * Queens average listing price ~$100-$200
  * Staten Island average listing price ~$75-$125

> [!Note]
> Majority of Top Performers average between 3 to 9 bookings per month. 

[Back to Top](#Table-of-Contents)

## Graphical Map

For further analysis, I chose to display a map of all the airbnb listing for each region (Bronx, Brooklyn, Manhattan, Queens, Staten Island). Each map has either a Green or Red House at a current Airbnb host location. The Green House signifies that the listing is a Top Performer in the area while the Red House signifies that the listing is a standard performer outside the top 10 percent. The image below is a brief example of what is displayed in the html files generated from the code. These output files are located [here](https://github.com/shifflettmb-1/airbnb_data_exploration/tree/main/output)

Image taken from output html file using Folium Comparing Top Performers and Standard Performer In Bronx
<img width="1419" height="841" alt="graphical map bronx" src="https://github.com/user-attachments/assets/4cc0fb87-2a24-4190-ab9f-6e154cf72741" />

* These files allow for users to explore and compare real data for neighborhoods quickly (ex. Price, Listing, Name, Number of Reviews).
* Provide a range of ideas of a starting point for becoming an airbnb host themselves by viewing nearby listings. 
* Potentially allows future hosts to see things that might have been overlooked like proximity to the zoo or playground in the area which might intice potential clients.

> [!WARNING]
> The HTML output files can get pretty large depending on the number of given airbnb host for the region

[Back to Top](#Table-of-Contents)

# Conclusion

Based on the data I recommend the following for listing name:

* Choose specific keywords for what you are offering like “private room”, “2-bedroom apt”
* Mention local tourist attraction or airport if they are close by (Example 10 mins from JFK, LaGuardia - LGA, Times Square)
* Adding an adjective like “cozy”, “spacious” to help it stand out in listing

Based on the data I recommend the following for price setting:

* Is it a private room? entire home?
* Compare neighborhood of property to look for price that has most monthly reviews as starting point based on whether private room or entire home/apt
* Lower prices tend to lead to more reviews (more bookings) 

Bookings To Expect:

* Some areas Top Performers only average 3 to 9 bookings per month so it would be important have realistic expectations

# Photo and Data Credits
I did not create nor do I own any images/data from airbnb nor am I affliated with airbnb

Using this information as a basis for creating an airbnb listing doesn't guarantee success or failure.

This data can be accessed from [here](https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data/data).

The coding for this repo can be found [here](https://github.com/shifflettmb-1/airbnb_data_exploration/tree/main/src).
