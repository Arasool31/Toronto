#Import Libraries 
import pandas as pd
import numpy as np

#Getting data from wikipedia website
Neigh = pd.read_html('https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M')

#Cleaning Data
Neigh_df = pd.DataFrame(Neigh[0])

#Removing all cells that don't have a value of Borough
Neigh_df = Neigh_df[Neigh_df["Borough"] != "Not assigned"]
print(Neigh_df)

#Checking if there are any not assigned values in Neighbourhoods
sum = Neigh_df.Neighbourhood.str.count("Not assigned").sum()
print(sum)
#All Neighbourhoods have a value so we dont have to do anything to that column

#Printing the shape of the data frame
Neigh_df_shape = Neigh_df.shape
print(Neigh_df_shape)