# AnalyticsPortfolio
This is a portfolio to showcase my analytics work using Python to preprocess and building machine learning models.

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
