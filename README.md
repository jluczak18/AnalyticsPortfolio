# Analytics Portfolio
Thank you for coming to my github! My name is Jeff Luczak and I am a Senior Business Analyst at CCC Intelligent Solutions. As a Senior Business Analyst, it is my job to translate business requirements to technical jobs to be done for our developers. I also work directly with the business side of CCC to answer questions from our data through the use of ad-hoc data preparation on visualizations. In order to do this, I use SQL, Tableau, and Python extensively.

How have I used these technologies?
- SQL: Running ad-hoc queries to build reporting. Creating data sources through complex queries across different environments and schemas. Publishing custom SQL queries to Tableau
- Tableau: Create internal and external facing dashboards to visualize the data to drive customer insights
- Python: Utilized Python in numerous ways in my current and prior jobs. By using python, I have built algorithms to find meaning in data, created dummy data sets with existing data to show the development team how we should model our warehouse, used python to call Rest APIs for use in reporting and for process improvement practices.

Other skills I have learned on the job
- Reading XML, JSON files
- How to connect Python to Tableau to publish data into a server
- How to move data across different servers utilizing the XML behind Tableau workbooks

Outside of work I have taken it upon myself to keep pushing myself to learn new skills around Python and coding in general. One of the ways I have pushed myself is through what is called Advent of Code. This is a 25 day set of puzzles released in December to challenge your coding skills. I have a branch on my github devoted to some of these challenges. 

If you have any questions on my background or my attached projects, email me
at jluczak18@gmail.com. You can also find more of my projects using Tableau, SQL, and other technologies at https://jluczak18.wixsite.com/analytics. Enjoy reading through my code!

# Advent of Code
The Advent of Code project is an open source set of puzzles set to test coding/problem solving skills. At CCC we created our own leaderboard for our team to track our progress. These challenges certainly tested my problem solving skills, but at the end of the day I was able to answer the problems correctly and further my knowledge of Python. I will continue to update this file as I go through the challenges. As of this writing, I completed through Day 7 and part 1 of days 8,9,10,13, and 14.

# CCC Hackathon
At CCC Intelligent Solutions every year we have a company wide challenge to come up with new ideas for products and provide some sort of proof of concept on what that may look like. This section highlights all the entries I have worked on with my team.

  ## 2023
  In 2023, my team identified that there was a large need for our internal account teams to be able to understand how threshold changes to an existing CCC product impacts Insurance customers line of business. The    end goal was for a Tableau dashboard that helps the team understand how a change to a given threshold increases productivity across the insurance landscape. I was a project lead on this as well as one of the   
  main developers. I helped gather requirements from stakeholders and then translated those to the team. From there I created python code that helped us simulate individual changes and how that impacted volume. 
  Our team took home a trophy for Best Strategic Value out of the 30 teams that participated.

  ## 2022
  For 2022 we decided to work on building a scorecard that helped us understand casualty providers and how the services they provide compare to similar providers in the same geographic location. Our goal was to 
  look to identify potential fraud by seeing providers charging for similar services at an elevated cost relative to the market. This project I was both the designer and BI developer. Was extremely proud of my 
  work. We ended up losing by 1 vote to the overall winner in 2022.
  
  ![Provider Scorecard Screen 2](https://github.com/jluczak18/AnalyticsPortfolio/blob/7bc65af020a552497d7f0743d99f33b145385bc3/ProviderScorecardScreen2.PNG)
  
  ## 2021
  As an analytics team we decided to bring in external data around extreme weather and join it to our internal data around motor vehicle accidents to see how extreme weather plays a factor in increased volumes or    higher severity. This is a future roadmap for our company so we thought building a POC would be a great idea. My role in this project included helping identify different APIs we could use to gather the data, 
  joining the data together across multiple different environments (Oracle, Haddop Hive, and Amazon EMR), and build a visualization in Tableau. The outcome was that our team brought hom the trophy for top overall 
  winning team!

  ![2021 Hackathon](https://github.com/jluczak18/AnalyticsPortfolio/blob/89d202c309dae4f62c4c3e425e60a53a1f9acc65/CCC_Hackathon.png)

# Edward Jones Capstone Project
For my capstone project in my Master's program, I worked with my colleague who is a Business Support Specialist at Edward Jones to analyze the application process for their life insurance programs. Given data on applications from the last 12 months, we build predictive models to understand our data better and what features affect the overall cycle time. From here we communicated to Edward Jones what expected time on an application will be from start to finish and how certain aspects of an application add time to the overall process.

Our overall findings was that there was too much variation in our datasets to build an accurate predictive model. This was due to having 6 different carriers who all have a large range of cycle times in our dataset. See the file MSBA_JupyterNotebook for the code created.

For background and more information on this project, see the pdf file "Team 10 MSBA Applied Project Report." I worked in a team of 3 on this project, but I built all the code for this project.

# Electricity Price Forecasting Project
During my Masters program I approached one of my professors about getting additional experience and he pointed me to a colleague at a company called Nexant. I recruited a few colleagues and we helped Nexant build out a price forecasting model using different machine learning models. 

The Nexant2 file is a project that uses information gathered from the California ISO along with weather data to create a short term electricity price forecasting model. The current work in the notebook includes all the steps we took to gather the information. It required canvassing all the nodes within the specific region, finding the weather stations near these nodes, and then aggregating weather data on these nodes to be able to combine with our historical information from the California ISO.

We wanted to be able to predict prices on an hourly basis which required hourly weather information which we obtained using an API from the National Solar Radiation Database. Using this information we built a forecasting model that predicted prices tomorrow and even a week from now. The company has asked me not to share further data so this is all I can showcase.

The file named "Model_Input_Data" houses all the information gathered from a seperate code to pull wind and solar generation,
fuel prices, demand, and the LMP prices for electricity in the Pacific Gas & Electric zone in California. 

The other file labeled "PGE_2019_Q4_ElectricUsageByZip" was used to pull zipcodes that the company operated in. Our model will be used to predict electricity prices within the PG&E zone.

# ProMark Planners Stock Code
While finishing up my Masters degree and preparing to enter the job market, I worked part time at ProMark Planners which is a financial advisor firm located in Palatine, IL. My work here revolved around analyzing different fund objectives to enhance client portfolios. This included reallocation of current portfolios, finding new investment strategies, building optimization and simulation models to maximize performance, and more. While working in this role, I was tasked with finding some more aggressive approaches by investing in the stock market. Noticing some issues with current tools like MorningStar I wanted a quick way to be able to analyze the performance of multiple stocks at once. This is how the file Stock_Code was born. Using a Rest API called Finnhubb.io I was able to load in stock prices for multiple stocks and analyze them together whether this be analyzing percent returns from day to day or looking at overall stock price trends month over month. The output was used to start discussions and swap in different tickers at once.

![Stock Trends](https://github.com/jluczak18/AnalyticsPortfolio/blob/576e67f80060c9b0d3b96efe5245d362d8e80234/Ticker.jpg)

# Email Bounce List Cleaning
Working as a Social Media Analytics Intern, I approached the President of the company about building a database to house an abundance of data that we collect from multiple platforms. This conversation sparked the task of cleaning up an existing database that houses member email addresses used to send segmented emails in a platform called SendGrid. Inside of this platform, we noticed we had an abundance of bounced email addresses totaling about 70,000. In an effort to remove these email addresses we needed to identify which bounced emails were a result of a hard or a soft bounce. A hard bounce identifies that the email is not valid where as a soft bounce could be that the server was down momentarily or someone had an out of office on. 

Using Python, I loaded in the list of bounced email addresses with error codes embedded inside a large string value. The task was to pull these values out of this column and into a seperate column with just the error code. Once we had the error codes in their own column, we were able to filter which emails we wanted to remove from our database. The file labeled Cleaning_BounceList does this process. I cannot share the files due to a breach of confidentiality.

# PUBG Win Place Percentile Prediction Project
The PUBG-kernel file was a kaggle project I did on my own time to build a machine learning algorithm to predict how someone will place in the game PUBG based on certain features. The pre-processing identified several factors that had an impact on win placement. These included boosts, killPlace, walkDistance, and weaponsAcquired. I used these features in my final model.
