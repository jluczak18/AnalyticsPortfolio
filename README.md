# AnalyticsPortfolio
Thank you for coming to my github! I am Jeff Luczak and am a current Master's student at Arizona State University looking to apply
my data analysis skills for a company that values the use of data driven decisions at a high level. Very excited about using
predictive analytics to help drive these decisions. If you have any questions on my background or my attached projects, email me
at jluczak18@gmail.com. Enjoy reading through my code!

# Electriticy Price Forecasting Project
The Nexant2 file is an ongoing project to use information gathered from the California ISO along with weather data 
to create a short term electricity price forecasting model. The current work in the notebook is all the steps we took to gather
the information. It required canvassing all the nodes within the specific region, finding the weather stations near these nodes,
and then aggregating weather data on these nodes to be able to combine with our historical information from the California ISO.

Using this information we will be building a forecasting model to predict prices tomorrow or even a week from now. More to come!

The file named "Model_Input_Data" houses all the information gathered from a seperate code to pull wind and solar generation,
fuel prices, demand, and the LMP prices for electricity in the Pacific Gas & Electric zone in California. 

The other file labeled "PGE_2019_Q4_ElectricUsageByZip" was used to pull zipcodes that the company operated in. Our model will be 
used to predict electricity prices within the PG&E zone.

# PUBG Win Place Percentile Prediction Project
The PUBG-kernel file was a kaggle project I did on my own time to build a machine learning algorithm to predict how someone will
place in the game PUBG based on certain features. The pre-processing identified several factors that had an impact on win placement.
These included boosts, killPlace, walkDistance, and weaponsAcquired. I used these features in my final model.
