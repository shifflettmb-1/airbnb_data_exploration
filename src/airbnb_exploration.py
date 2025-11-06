import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import plotly.express as px
import re
import matplotlib.patches as mpatches
import folium
from folium.plugins import MarkerCluster

#methods to remove punctuation re more efficient
def remove_punctuation(text):
    """ 
    Removes punctuation from text using regular expression function
    
    Parameters
    ----------
    text: string
    
    Returns
    -------
    text without punctuation
    
    """   
    return re.sub(r'[^\w\s]', '',text)

# method that finds top ten percent of reviews overall and per month
# aka top performers of reviews
def find_top_ten_percent(df):
    """ 
    Finds top 10 percent of airbnb host based on
    number_of_reviews, reviews_per_month

    Parameters
    ----------
    df: DataFrame of airbnb information
    
    Returns
    -------
    top_ten_month: DataFrame that has top performers in the top 10 percent 
    by number_of_reviews AND reviews_per_month
    """
    percentile_90_nor = df['number_of_reviews'].quantile(0.90)
    percentile_90_nor_m = df['reviews_per_month'].quantile(0.90)
    top_ten = df[df['number_of_reviews']> percentile_90_nor]
    top_ten_month = top_ten[top_ten['reviews_per_month'] > percentile_90_nor_m]
    return top_ten_month

#method that retrieves the top fifteen most used words in the listing
#after cleaning the data 
def get_top_fifteen_words(df):
    """ 
    Retrieves the top fifteen most common words (excluding stopwords)
    
    Remove cases and punctuation from listing creating a new column in def
    called listing processed. Then take the listing processed column and 
    expands into a single column of strings. Then get value counts.
    Remove stopwords from consideration. Sort the counts in descending order.
    Return top 15.


    Parameters
    ----------
    df: dataFrame of airbnb information

    Returns
    -------
    top_15_words: Series of the 15 most common words (index) and their count (values)

    """
    #removes punctuation
    df.loc[:,"listing_processed"] = df["listing"].str.lower().apply(remove_punctuation)
    
    #stacks all the words in listing_processed into a Panda Series
    all_words = df["listing_processed"].str.split(expand=True).stack()

    #records the value_counts of each word as a Series
    word_counts = all_words.value_counts()
    
    #applies the remove_stop_words() functions on the word_counts Series
    word_counts = pd.DataFrame(word_counts).apply(remove_stop_words, axis=1)

    #sorts the word counts Series in descending order
    sorted_word_counts = word_counts.sort_values(ascending=False)
    
    #retrieves top 15 words
    top_15_words = sorted_word_counts.head(15)
    return top_15_words

def remove_stop_words(x):
    """ 
    Changes the count value to 0 if index is in stopwords
    to remove it from consideration as part of most common
    due to the words being conjunctions, prepositions

    Parameters
    ----------
    x: a word(str) in the listing
    
    Returns
    -------
    0 if index is in stopwords
    x["count"] if index not in stopwords
    
    """
    stopwords = ["and", "in", "on", "the", "to", "by", "with", "near", "1", "2", "of", "from"]
    if x.name in stopwords:
        return 0
    else:
        return x["count"]
    
def get_top_performers_top_fifteen_words(df):
    """ 
    Combining the two methods of find top performers and top 15 words in listing

    Parameters
    ----------
    df: dataFrame of airbnb information
    
    Returns
    -------
    top_ten_df, top_fifteen_words: a tuple where first element is df of top performers
    and the second is a Series which has 15 most common words and their counts
    
    """
    top_ten_df = find_top_ten_percent(df)
    top_fifteen_words = get_top_fifteen_words(top_ten_df)
    return top_ten_df, top_fifteen_words

def get_non_top_performers(df, top_performers_df):
    """ 
    Filters out the ids of the top_performers from the df and returns the rows which the ids are not in 
    top_performers_df. IDs are unique for each airbnb listing in df

    Parameters
    ----------
    df: dataFrame of airbnb information that is unfiltered, possibly specific to neighborhood
    toptop_performers_df: dataFrame of top performing airBnBs
    
    Returns
    -------
    non_top_performers_df: DataFrame of airbnb information that filters out top performers
    from original df
    
    """
    ids_in_top_performers_df = top_performers_df["id"]
    non_top_performers_df = df[~df['id'].isin(ids_in_top_performers_df)]
    return non_top_performers_df


def make_bar_graph_word_counts(series, name_str):
    """ 
    Create bar graph of most common 15 words in the airbnb series

    Parameters
    ----------
    series: Series that has information about top 15 most common words
    name_str: name of the Title for the graph 
    
    """
    #creates horizontal bar graph, set labels, title
    fig, axs = plt.subplots(figsize = (12,4))
    axs.barh(series.index, series.values, color = "lightblue", edgecolor = "black")
    axs.set_xlabel('Top 15 Words')
    axs.set_ylabel('Frequency')
    axs.set_title(f"Top 15 Most Common Words In Top Performers In {name_str}")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()

def make_scatter_reviews_price(df, name_str):
    """ 
    Create scatterplot comparing the total number of reviews
    and price of listing

    Parameters
    ----------
    df: Dataframe that has airbnb information
    name_str: string for the name of the Title for the graph 
    
    """
    #Seperate Colors based on room type
    color_array = np.where(df["room_type"] == "Private room", "blue", "orange")
    
    #Create handles for legend bars that correspond to the colors of the bar
    blue_patch = mpatches.Patch(color='blue', label='Private Room')
    orange_patch = mpatches.Patch(color='orange', label='Entire Home/Apt')

    #creates scatterplot, set labels, tickmarks, title, legend
    fig, axs = plt.subplots(figsize = (12,4))
    axs.scatter(df["price"], df["number_of_reviews"], color=color_array)
    axs.set_xlabel('Price Per Night In $')
    axs.set_ylabel('Number 0f Reviews (Total)')
    axs.set_xticks(range(0, df["price"].max()+100, 50))
    axs.set_yticks(range(0, df["number_of_reviews"].max()+100, 50))
    axs.set_title(f"Top Performers Price VS Number Of Reviews {name_str}")
    plt.legend(handles=[blue_patch, orange_patch])
    plt.tight_layout()
    plt.show()

def make_scatter_reviews_per_month_price(df, name_str):
    """ 
    Creates a scatter plot showing relationship between
    Reviews per month and price

    Parameters
    ----------
    df: Dataframe of airbnb data
    name_str: string for the name of the Title for the graph
    """
    #Seperate Colors based on room type blue for private room, orange for entire home/apt
    color_array = np.where(df["room_type"] == "Private room", "blue", "orange")
    
    #Create handles for legend bars that correspond to the colors of the bar
    blue_patch = mpatches.Patch(color='blue', label='Private Room')
    orange_patch = mpatches.Patch(color='orange', label='Entire Home/Apt')
    
    #creates scatterplot, set labels, tickmarks, title, legend
    fig, axs = plt.subplots(figsize = (12,4))
    axs.scatter(df["price"], df["reviews_per_month"], color=color_array)
    axs.set_xlabel('Price Per Night In $')
    axs.set_ylabel('Number 0f Monthly Reviews')
    axs.set_xticks(range(0, df["price"].max()+100, 50))
    axs.set_yticks(range(0, int(df["reviews_per_month"].max())+6, 3))
    axs.set_title(f"Top Performers Price VS Monthly Reviews {name_str}")
    plt.legend(handles=[blue_patch, orange_patch])
    plt.tight_layout()
    plt.show()

def combine_scatters_reviews_price(df, name_str):
    """ 
    Creates a scatter plot showing relationship between
    Reviews and price side by side with reviews per month and
    price.

    Parameters
    ----------
    df: Dataframe of airbnb data
    name_str: string for the name of the Title for the graph
    """    
    #Seperate Colors based on room type
    color_array = np.where(df["room_type"] == "Private room", "blue", "orange")
    
    #Create handles for legend bars that correspond to the colors of the bar
    blue_patch = mpatches.Patch(color='blue', label='Private Room')
    orange_patch = mpatches.Patch(color='orange', label='Entire Home/Apt')

    #creates scatterplot, set labels, tickmarks, title, legend for number of reviews vs price to axs[0] for side by side
    fig, axs = plt.subplots(1,2,figsize = (14,4))
    axs[0].scatter(df["price"], df["number_of_reviews"], color=color_array)
    axs[0].set_xlabel('Price Per Night In $')
    axs[0].set_ylabel('Number 0f Reviews (Total)')
    axs[0].set_xticks(range(0, df["price"].max()+100, 50))
    axs[0].set_yticks(range(0, df["number_of_reviews"].max()+100, 50))
    axs[0].set_title(f"Top Performers Price VS Total Reviews {name_str}")
    axs[0].legend(handles=[blue_patch, orange_patch])

    #creates scatterplot, set labels, tickmarks, title, legend for review per month vs price to axs[1] for side by side
    axs[1].scatter(df["price"], df["reviews_per_month"], color=color_array)
    axs[1].set_xlabel('Price Per Night In $')
    axs[1].set_ylabel('Number 0f Monthly Reviews')
    axs[1].set_xticks(range(0, df["price"].max()+100, 50))
    axs[1].set_yticks(range(0, int(df["reviews_per_month"].max())+6, 3))
    axs[1].set_title(f"Top Performers Price VS Monthly Reviews {name_str}")
    axs[1].legend(handles=[blue_patch, orange_patch])
    plt.tight_layout()
    plt.show()

def make_ny_folium_map(ntp_df, tp_df, name_str):
    """ 
    Create a folium map with lat, long data from the two dataframes.
    Green House represent top performers
    Red House represent under performers
    Map Centers on New York

    Provides review information and listing information in pop-up text

    Parameters
    ----------
    ntp_df: DataFrame of underperforming airbnb of a particular area
    tp_df: DataFrame of top performing airbnb of a particular area
    name_str: name of the neighborhood for the saving to file
    
    Output
    ---------
    html file output of map
    """
    # Create a map centered in New York
    m = folium.Map(location=[40.7306, -73.9352], zoom_start=12)

    #creates two categories based on performancy
    top_group = folium.FeatureGroup(name="Top Performers")
    ntp_group = folium.FeatureGroup(name="Non Top Performers")

    #gathers lat, long, and display data
    for index, row in tp_df.iterrows():
        location = [row['latitude'], row['longitude']]
        popup_text = f"""Top Performing AirBnB In {row['neighbourhood_group']},
        Number Of Reviews: {row['number_of_reviews']}, 
        Reviews Per Month: {row['reviews_per_month']}, 
        Price: ${row['price']} Per Night,
        Type: {row['room_type']}, 
        Listing: {row["listing"]}""" 

        #Builds a green house icon at lat long symbolizing top performer and adds to top_group
        folium.Marker(
            location=location,
            popup=folium.Popup(popup_text, min_width=200, max_width=200),
            icon=folium.Icon(color='green', icon='home') # Custom icon/color
            ).add_to(top_group)
    
    #gathers lat, long, and display data
    for index, row in ntp_df.iterrows():
        location = [row['latitude'], row['longitude']]
        popup_text = f"""Standard {row['neighbourhood_group']} AirBnB,
        Number Of Reviews: {row['number_of_reviews']}, 
        Reviews Per Month: {row['reviews_per_month']},
        Price: ${row['price']} Per Night,
        Type: {row['room_type']},
        Listing: {row["listing"]}"""

        #Builds a marker of a red house icon at lat long symbolizing standard performer and adds to ntp_group
        folium.Marker(
            location=location,
            popup=folium.Popup(popup_text, min_width=200, max_width=200),
            icon=folium.Icon(color='red', icon='home') # Custom icon/color
        ).add_to(ntp_group)

    #places groups on map
    top_group.add_to(m)
    ntp_group.add_to(m)

    folium.LayerControl().add_to(m)
    
    # Custom HTML for the legend
    legend_html = """
    <div style="position: fixed;
            bottom: 50px; left: 50px; width: 150px; height: 100px;                
            border:2px solid grey; z-index:9999; font-size:14px;
            background-color:white; opacity:0.9;">
      &nbsp; <b>Legend</b> <br>
      &nbsp; <i class="fa fa-home fa-lg" style="color:red;"></i>&nbsp; Standard <br>
      &nbsp; <i class="fa fa-home fa-lg" style="color:green;"></i>&nbsp; Top Performers <br>
    </div>
    """
    #adds the legend to the map
    m.get_root().html.add_child(folium.Element(legend_html))

    #filename for output
    filename = '../output/ny_top_performers_' + name_str +'.html'
    
    #saves map to the file path
    m.save(filename)

if __name__ == "__main__":

    #Load in data from csv
    airbnb_df = pd.read_csv("../data/airbnb.csv")

    #data cleaning dropping rows where no reviews are known
    airbnb_df = airbnb_df.dropna(subset=["last_review", "reviews_per_month"])

    #fill in null values of host_name and name
    airbnb_df.fillna({"host_name": "Unknown", "name": "Unknown"}, inplace=True)

    #rename name column to listing to better define
    airbnb_df.rename(columns={"name": "listing"}, inplace=True)

    #Creating sub dfs based on the neighborhood group for better comparisons
    bronx_airbnb_df = airbnb_df[airbnb_df["neighbourhood_group"] == "Bronx"]
    brooklyn_airbnb_df = airbnb_df[airbnb_df["neighbourhood_group"] == "Brooklyn"]
    manhattan_airbnb_df = airbnb_df[airbnb_df["neighbourhood_group"] == "Manhattan"]
    queens_airbnb_df = airbnb_df[airbnb_df["neighbourhood_group"] == "Queens"]
    staten_island_airbnb_df = airbnb_df[airbnb_df["neighbourhood_group"] == "Staten Island"]

    #retrieve top performers and their most common words for all neighborhood groups
    top_performers_bronx, top_15_words_bronx = get_top_performers_top_fifteen_words(bronx_airbnb_df)
    top_performers_brooklyn, top_15_words_brooklyn = get_top_performers_top_fifteen_words(brooklyn_airbnb_df)
    top_performers_manhattan, top_15_words_manhattan = get_top_performers_top_fifteen_words(manhattan_airbnb_df)
    top_performers_queens, top_15_words_queens = get_top_performers_top_fifteen_words(queens_airbnb_df)
    top_performers_staten_island, top_15_words_staten_island = get_top_performers_top_fifteen_words(staten_island_airbnb_df)
    top_performers_overall, top_15_words_overall = get_top_performers_top_fifteen_words(airbnb_df)

    #retrieve non top performers for graphing purposes later
    non_tp_bronx = get_non_top_performers(bronx_airbnb_df, top_performers_bronx)
    non_tp_brooklyn = get_non_top_performers(brooklyn_airbnb_df, top_performers_brooklyn)
    non_tp_manhattan = get_non_top_performers(manhattan_airbnb_df, top_performers_manhattan)
    non_tp_queens = get_non_top_performers(queens_airbnb_df, top_performers_queens)
    non_tp_staten_island = get_non_top_performers(staten_island_airbnb_df, top_performers_staten_island)
    non_tp_overall = get_non_top_performers(airbnb_df, top_performers_overall)


    #Create the bar graphs for most common words in each neighborhood group
    make_bar_graph_word_counts(top_15_words_bronx, "Bronx")
    make_bar_graph_word_counts(top_15_words_brooklyn, "Brooklyn")
    make_bar_graph_word_counts(top_15_words_manhattan, "Manhattan")
    make_bar_graph_word_counts(top_15_words_queens, "Queens")
    make_bar_graph_word_counts(top_15_words_staten_island, "Staten Island")
    make_bar_graph_word_counts(top_15_words_overall, "Overall In New York")

    #Create scatter plots to see relationship between number of reviews/price
    make_scatter_reviews_price(top_performers_bronx, "Bronx")
    make_scatter_reviews_price(top_performers_brooklyn, "Brooklyn")
    make_scatter_reviews_price(top_performers_manhattan, "Manhattan")
    make_scatter_reviews_price(top_performers_queens, "Queens")
    make_scatter_reviews_price(top_performers_staten_island, "Staten Island")
    make_scatter_reviews_price(top_performers_overall, "Overall In New York")

    #Create scatter plots to see relationship between reviews per month/price
    make_scatter_reviews_per_month_price(top_performers_bronx, "Bronx")
    make_scatter_reviews_per_month_price(top_performers_brooklyn, "Brooklyn")
    make_scatter_reviews_per_month_price(top_performers_manhattan, "Manhattan")
    make_scatter_reviews_per_month_price(top_performers_queens, "Queens")
    make_scatter_reviews_per_month_price(top_performers_staten_island, "Staten Island")
    make_scatter_reviews_per_month_price(top_performers_overall, "Overall In New York")

    #Creates scatter plots to see relationship between number of reviews/price
    #Creates scatter plots to see relationship between reviews per month/price
    #Side by side for comparison purposes
    combine_scatters_reviews_price(top_performers_bronx, "Bronx")
    combine_scatters_reviews_price(top_performers_brooklyn, "Brooklyn")
    combine_scatters_reviews_price(top_performers_manhattan, "Manhattan")
    combine_scatters_reviews_price(top_performers_queens, "Queens")
    combine_scatters_reviews_price(top_performers_staten_island, "Staten Island")
    combine_scatters_reviews_price(top_performers_overall, "Overall In New York")

    #Create NY Folium Maps that are sent to output folder for each neighborhood
    make_ny_folium_map(non_tp_bronx, top_performers_bronx, "Bronx")
    make_ny_folium_map(non_tp_brooklyn, top_performers_brooklyn, "Brooklyn")
    make_ny_folium_map(non_tp_manhattan, top_performers_manhattan, "Manhattan")
    make_ny_folium_map(non_tp_queens, top_performers_queens, "Queens")
    make_ny_folium_map(non_tp_staten_island, top_performers_staten_island, "Staten Island")
    make_ny_folium_map(non_tp_overall, top_performers_overall, "Overall_In_New_York")