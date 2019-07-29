# **Google Play web-scraper**

My first scraper using selenium. Scraping information and reviews of apps on Google Play market. 
Reviews are saving to csv file for further exploration. 

## Csv file preview:

![alt text](https://github.com/yngalxx/Web_Scraping/blob/master/Csv_file_preview.png)

## Using: 

To use scraper, change url. It's important that it has to be a url with app’s details view. 
Scraper will print basic information about app and then reviews will save in a csv file. 
I also use a ‘tqdm’ package to have a progress bar and estimated scraping time. 
Some lines of code are not needed but it was a learning for me and I wanted to try a lot of selenium's functionalities.

### Important:

In csv file one column is named usefulness. Value in a field of this column means how many people like this review.
