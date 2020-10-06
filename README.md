# Analytics Portfolio
Thank you for coming to my github! I am Jeff Luczak and am a current Master's student at Arizona State University looking to apply
my data analysis skills for a company that values the use of data driven decisions at a high level. Very excited about using
predictive analytics to help drive these decisions. If you have any questions on my background or my attached projects, email me
at jluczak18@gmail.com. You can also find more of my projects using Tableau, SQL, and other technologies at https://jluczak18.wixsite.com/analytics. Enjoy reading through my code!

# Electricity Price Forecasting Project
The Nexant2 file is an ongoing project to use information gathered from the California ISO along with weather data 
to create a short term electricity price forecasting model. The current work in the notebook includes all the steps we took to gather
the information. It required canvassing all the nodes within the specific region, finding the weather stations near these nodes,
and then aggregating weather data on these nodes to be able to combine with our historical information from the California ISO.
We want to be able to predict prices on an hourly basis which requires hourly weather information which we obtained using an API
from the National Solar Radiation Database.

Using this information we will be building a forecasting model to predict prices tomorrow or even a week from now. The company has asked me not to share further data so this is all I can showcase.

The file named "Model_Input_Data" houses all the information gathered from a seperate code to pull wind and solar generation,
fuel prices, demand, and the LMP prices for electricity in the Pacific Gas & Electric zone in California. 

The other file labeled "PGE_2019_Q4_ElectricUsageByZip" was used to pull zipcodes that the company operated in. Our model will be 
used to predict electricity prices within the PG&E zone.

# Email Bounce List Cleaning
Working as a Social Media Analytics Intern, I approached the President of the company about building a database to house an abundance of data that we collect from multiple platforms. This conversation sparked the task of cleaning up our current database due to it not being updated since inception. One way we utilize our database is to send segmented emails in a platform called SendGrid. Inside of this platform, we noticed we had an abundance of bounced email addresses totaling about 70,000. In an effort to remove these email addresses we needed to identify which bounced emails were a result of a hard or a soft bounce. A hard bounce identifies that the email is not valid where as a soft bounce could be that the server was down momentarily or someone had an out of office on. 

Using Python, I loaded in the list of bounced email addresses with error codes embedded inside a large string value. The task was to pull these values out of this column into a seperate column with just the error code. Once we have the error codes in their own column, we can filter which emails we want to remove from our database. The file labeled Cleaning_BounceList does this process. I cannot share the files due to a breach of confidentiality.

# PUBG Win Place Percentile Prediction Project
The PUBG-kernel file was a kaggle project I did on my own time to build a machine learning algorithm to predict how someone will
place in the game PUBG based on certain features. The pre-processing identified several factors that had an impact on win placement.
These included boosts, killPlace, walkDistance, and weaponsAcquired. I used these features in my final model.
