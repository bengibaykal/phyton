# import pandas library
import pandas as pd


other_path = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"
df = pd.read_csv(other_path, header=None)

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
 
 #add headers
 df.columns = headers
 
 #drop missing values along the column price
 df.dropna(subset=["price"], axis=0)
 
 #save the dataframe df as automobile.csv
 df.to_csv("automobile.csv", index=False)
