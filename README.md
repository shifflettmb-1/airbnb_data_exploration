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

There were three main focuses I had for this project. I wanted to see how listing name played apart in how likely the Airbnb would be to be booked (reviewed), how to determine an appropriate price for listing based on the market, and finally if I could display this data on a map to see what hidden geographical influences played a part in success of these hosts.

For my visualization I wanted to look deeper at the top performers in the dataset, the listings that were in the Top 10 percent of total number of reviews AND the Top 10 percent of monthly reviews. Comparisons also needed to be geographically based, meaning I'm taking the data and breaking it down into the top performers by region to see results. There were five distinct regions for this exploration which included the Bronx, Brooklyn, Manhattan, Queens, and Staten Island.

## Listing

When analyzing the listing names of the properties I decided that common conjunctions and prepositions may not be too relevant for this context so I decided to remove them from the results.
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

Trends that we can gather from listing names is that good listing normally contain the type of listing. Such as private bedroom or apartment, adding in proximity to local attractions or airports is beneficial.
Adding adjectives such as spacious, or cozy may slightly increase chance for the listing to stand out.

[Back to Top](#Table-of-Contents)

## Price vs Reviews

When analyzing the price comparison to the number of total and monthly reviews, one must consider the difference in the listing. Is the listing a single private room or is the entire house or apartment available for short-term lease?
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

From this data we can see that as one might suspect that entire homes are listed at higher price than private rooms. However an unexpected trend of top performers only booking 3 to 9 times per month on average.
Looking at particular neighborhood regions, one can make observations. Brooklyn, for example, amjority of private rooms tend to average around $50 per night and the average home or apartment starts at $125 to $250 per night.

[Back to Top](#Table-of-Contents)

## Graphical Map

The last visual I wanted to display for the dataset was map for each particular neighborhood region. Each map contains green and red house based on the locational data. The green house signifies that the listing is a top performer in the area while the red house signifies that the listing is a standard performer outside the top 10 percent. The image below brief example of what is displayed in the html file generated from the code.

Image taken from output html file stored locally using Folium Comparing Top Performers and Standard Performer In Bronx
<img width="1419" height="841" alt="graphical map bronx" src="https://github.com/user-attachments/assets/4cc0fb87-2a24-4190-ab9f-6e154cf72741" />

These files allow for users to explore and compare real data (ex. Price, Listing, Name, Reviews) for neighborhoods quickly and get a range of ideas of a starting point for becoming an airbnb host themselves.

[Back to Top](#Table-of-Contents)

# Conclusion

Based on the data I recommend the following for listing name:

* Choose specific keywords for what you are offering like “private room”, “2-bedroom apt”
* Mention local tourist attraction or airport if they are close by (Example 10 mins from JFK, LaGuardia - LGA, Times Square)
* Mention pools or playgrounds nearby
* Adding an adjective like “cozy”, “spacious” to help it stand out in listing

Based on the data I recommend the following for price setting:

* Compare neighborhood of property to look for price that has most monthly reviews as starting point based on whether private room or entire home/apt
* Lower prices tend to lead to more reviews (more bookings) 

Bookings To Expect:

* Some areas Top Performers only average 3 to 9 bookings per month so it would be important have realistic expectations

# Photo and Data Credits
I did not create nor do I own any images/data from airbnb nor am I affliated with airbnb

This data can be accessed from [here](https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data/data)
