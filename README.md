# Amazon_Product_Review_Extractor

This script is designed to scrape Amazon product reviews for a list of ASINs (Amazon Standard Identification Numbers) and save the review data to CSV files. It uses BeautifulSoup for parsing HTML, requests for making HTTP requests, and the fake_useragent library to rotate user agents for the requests.

Code Breakdown

Setting Up User Agent Rotation:
```
ua = UserAgent()
```
An instance of UserAgent from the fake_useragent library is created to randomly generate user agent strings for HTTP requests.


Processing Each Product:
```
for jj in lines:
    BSROUTPUT = str(jj) + " Review.csv"
    try:
        os.stat(BSROUTPUT)
        output = codecs.open(BSROUTPUT, 'a', 'utf-8')
    except:
        output = codecs.open(BSROUTPUT, 'a', 'utf-8')
        output.write('ASIN,Reviewer Name,Reviewer Star,Reviewer Date,Year,Reviewer Summary\n')
```
For each ASIN:
A CSV file named <ASIN> Review.csv is created or opened in append mode.
If the file does not exist, it is created with a header row.
