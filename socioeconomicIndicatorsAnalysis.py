#Analyzing a real world data-set with SQL and Python

%load_ext sql
# Remember the connection string is of the format:
# %sql ibm_db_sa://my-username:my-password@my-hostname:my-port/my-db-name
# Enter the connection string for your Db2 on Cloud database instance below
# i.e. copy after db2:// from the URI string in Service Credentials of your Db2 instance. Remove the double quotes at the end.
%sql ibm_db_sa://rjg23325:6mb%5Exsj5kgklzblz@dashdb-txn-sbox-yp-lon02-01.services.eu-gb.bluemix.net:50000/BLUDB

import pandas
chicago_socioeconomic_data = pandas.read_csv('https://data.cityofchicago.org/resource/jcxq-k9xf.csv')
%sql PERSIST chicago_socioeconomic_data

You can verify that the table creation was successful by making a basic query like:
%sql SELECT * FROM chicago_socioeconomic_data limit 5;

#How many rows are in the dataset?
%sql SELECT COUNT(*) FROM chicago_socioeconomic_data

#How many community areas in Chicago have a hardship index greater than 50.0?
%sql SELECT COUNT(community_area_name) FROM chicago_socioeconomic_data WHERE hardship_index > 50.0

%sql SELECT MAX(hardship_index) FROM chicago_socioeconomic_data;

#Which community area which has the highest hardship index?
%sql SELECT community_area_name FROM chicago_socioeconomic_data WHERE hardship_index = MAX(hardship_index)
%sql select community_area_name from chicago_socioeconomic_data where hardship_index = ( select max(hardship_index) from chicago_socioeconomic_data )

#Create a scatter plot using the variables per_capita_income_ and hardship_index. Explain the correlation between the two variables.
import matplotlib.pyplot as plt
import seaborn as sns
income_vs_hardship = %sql SELECT per_capita_income_, hardship_index FROM chicago_socioeconomic_data;
plot = sns.jointplot(x='per_capita_income_',y='hardship_index', data=income_vs_hardship.DataFrame())
