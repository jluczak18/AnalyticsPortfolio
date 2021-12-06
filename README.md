# Analytics Portfolio
Thank you for coming to my github! I am Jeff Luczak and am a Business Analyst at CCC Intelligent Solutions. As a Business Analyst, it is my job to translate business requirements to work for our developers as well as work directly with the business side of CCC to answer questions from our data through the use of visualizations or reports. In order to do this, I use SQL, Tableau, and Python extensively.

How have I used these technologies?
- SQL: Running ad-hoc queries to build reporting
- Tableau: Created internal and external facing dashboards to visualize the data to our customers to drive insights
- Python: Created dummy datasets for demo versions of our client facing dashboards, called company APIs to pull in new data as a POC before passing work to our developers, and conducting regression testing in an effort to become predictive with some of our data.

Other skills I have learned on the job
- Reading XML, JSON files
- How to connect Python to Tableau to publish data into a server
- How to move data across different servers utilizing the XML behind Tableau workbooks

If you have any questions on my background or my attached projects, email me
at jluczak18@gmail.com. You can also find more of my projects using Tableau, SQL, and other technologies at https://jluczak18.wixsite.com/analytics. Enjoy reading through my code!

# Advent of Code
The Advent of Code project is an open source set of puzzles set to test coding/problem solving skills. At CCC we created our own leaderboard for our team to track our progress. These challenges certainly tested my problem solving skills, but at the end of the day I was able to answer the problems correctly and further my knowledge of Python. I will continue to update this file as I go through the challenges. As of this writing, I completed through Day 4. 

# Wells Fargo Capstone Project
For my capstone project in my Master's program, I worked with my colleague who is a Business Support Specialist at Edward Jones to analyze the application process for their life insurance programs. Given data on applications from the last 12 months, we build predictive models to understand our data better and what features affect the overall cycle time. From here we communicated to Edward Jones what expected time on an application will be from start to finish and how certain aspects of an application add time to the overall process.

Our overall findings was that there was too much variation in our datasets to build an accurate predictive model. This was due to having 6 different carriers who all have a large range of cycle times in our dataset. See the file MSBA_JupyterNotebook for the code I built. 

For background and more information on this project, see the pdf file "Team 10 MSBA Applied Project Report." I worked in a team of 3 on this project, but I built all the code for this project.

# Electricity Price Forecasting Project
The Nexant2 file is a project that uses information gathered from the California ISO along with weather data 
to create a short term electricity price forecasting model. The current work in the notebook includes all the steps we took to gather the information. It required canvassing all the nodes within the specific region, finding the weather stations near these nodes, and then aggregating weather data on these nodes to be able to combine with our historical information from the California ISO.

We want to be able to predict prices on an hourly basis which requires hourly weather information which we obtained using an API
from the National Solar Radiation Database.

Using this information we will be building a forecasting model to predict prices tomorrow or even a week from now. The company has asked me not to share further data so this is all I can showcase.

The file named "Model_Input_Data" houses all the information gathered from a seperate code to pull wind and solar generation,
fuel prices, demand, and the LMP prices for electricity in the Pacific Gas & Electric zone in California. 

The other file labeled "PGE_2019_Q4_ElectricUsageByZip" was used to pull zipcodes that the company operated in. Our model will be 
used to predict electricity prices within the PG&E zone.

# ProMark Planners Stock Code
I currently work part time as a Financial Analyst at ProMark Planners. ProMark Planners is a financial advisor firm located in Palatine, IL. My work here is revolved around analyzing different fund objectives to enhance client portfolios. This includes reallocation of current portfolios, finding new investment strategies, building optimization and simulation models to maximize performance, and more. While working in this role, I have been tasked with finding some more aggressive approaches by investing in the stock market. Noticing some issues with current tools like MorningStar I wanted a quick way to be able to analyze the performance of multiple stocks at once. This is how the file Stock_Code was born. Using a rest API called Finnhubb.io I am able to load in stock prices for multiple stocks and analyze them together whether this be analyzing percent returns from day to day or looking at overall stock price trends month over month. As this code is still in development, I hope this will help drive some decisions we make on investment strategies at ProMark Planners. It already is sparking good conversations among the financial advisors in the office.

# Email Bounce List Cleaning
Working as a Social Media Analytics Intern, I approached the President of the company about building a database to house an abundance of data that we collect from multiple platforms. This conversation sparked the task of cleaning up our current database due to it not being updated since inception. One way we utilized our database is to send segmented emails in a platform called SendGrid. Inside of this platform, we noticed we had an abundance of bounced email addresses totaling about 70,000. In an effort to remove these email addresses we needed to identify which bounced emails were a result of a hard or a soft bounce. A hard bounce identifies that the email is not valid where as a soft bounce could be that the server was down momentarily or someone had an out of office on. 

Using Python, I loaded in the list of bounced email addresses with error codes embedded inside a large string value. The task was to pull these values out of this column and into a seperate column with just the error code. Once we had the error codes in their own column, we were able to filter which emails we wanted to remove from our database. The file labeled Cleaning_BounceList does this process. I cannot share the files due to a breach of confidentiality.

# PUBG Win Place Percentile Prediction Project
The PUBG-kernel file was a kaggle project I did on my own time to build a machine learning algorithm to predict how someone will
place in the game PUBG based on certain features. The pre-processing identified several factors that had an impact on win placement.
These included boosts, killPlace, walkDistance, and weaponsAcquired. I used these features in my final model.
