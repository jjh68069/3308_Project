#Project Name: Stock Insights

##Team Members:
* Kevin Flynn
* Jason Hill
* Andrew Callahan
* Soham Shah

##Class
CSCI 3308 - Software Development Methods and Tools
Professor: Elizabeth Boese

##About this Project:
This website is a service to inform millennials about an investing strategy by interpreting and visualizing stock market data. 

##Repo Organization
There are three main folders
* Database
  * This contains all the scripts necessary to query Quandl using the API to grab the stock market data.
* Algorithm
  * This is where the momentum algorith for interpreting the stock data is
* Documentation
  * This folder contains all the necessary documentation for the project as assigned by our instructor
  * This folder also contains the Doxygen generated output for the program. To see this, clone the Doxygen folder and run the index.html folder to see the autodoc documentation
* HTML
  * This is the website implementation itself with all assiciated CSS and JS stuff

##Running the program.
* Go into the HTML folder 
* Double click on index.html 
  * This will display the website in your default browser (we recommend Chrome or Firefox)
* Click on the function tab on the top bar
* Query the database by adding a stock market ticker from a stock in the S&P500 like "aapl" into the input box
* The page will now display the data on the stock you requested

##Deployment
* Website has also been deployed to: http://soham-shah.github.io/ for easy access

##Running test code
* Currently we have coded unit tests for the algorithm implementations
* You can run these by cloning the git repo to your local computer and running the Algorithms_Test.py python script using the python interpreter

