"""Create a command line program to fetch the top news headlines or search for a particular subject using the OpenNews APILinks to an external site..

The application flow should look like the following for identifying top headlines:

Welcome to Command Line News!   

Please make a choice: [1] Top headlines [2] Search   
>> 1  
  
Select which category would you like to headlines for:   
[1] business   
[2] entertainment   
[3] general   
[4] health   
[5] science   
[6] sports   
[7] technology   
  
>> 7   
* Ikea's First Smart Air Purifier Comes Camouflaged as a Side Table - Gizmodo (October 25, 2024)
         The Starkvind will help you breathe easier while also being easy on the eyes.
         
* Freebie alert: Amazon is giving away eight video games (worth over $130) to all Prime members - Yahoo Lifestyle (October 25, 2024)
         Prime Gaming subscribers can get their hands on hits like 'Battlefield V' and indie sensations like 'A Normal Lost Phone.'
Here is the application flow for a search:

Welcome to Command Line News! 
Please make a choice: [1] Top headlines [2] Search 
>> 2  
  
Enter your search term:   
>> Nintendo   

* The next Nintendo Direct is all about Super Nintendo World’s Donkey Kong Country - The Verge 2024-11-10T22:58:58Z
           Nintendo will showcase the Donkey Kong Country area of its Super Nintendo World theme park in a roughly 10-minute Direct video on Monday.

In either mode, present the top 10 results to the command line following the format above. If there is no description for the article or author, print a blank space. You will need to convert the date from the JSON feed to a more readable format that includes only the month, day and year.

Note: There are many Python packages that can help with date formatting.

The program should prompt the user if they would like to get more news after a retrieval. For example:

Would you like to find more news articles? [y/n]  
>> y
Start the application flow over from the beginning.

Welcome to Command Line News! 

Please make a choice: [1] Top headlines [2] Search 
>> 2
...
..."""
from newsapi_demo import NewsApp


def main():
    app = NewsApp()
    app.run()


if __name__ == "__main__":
    main()