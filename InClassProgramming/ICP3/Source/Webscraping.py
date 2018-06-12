# Import the libraries
import urllib.request
from bs4 import BeautifulSoup

# Defining a variable and assigned the link to it
inputLink = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
# Get the url
getData=urllib.request.urlopen(inputLink)
# parsing using beautiful soup
parseSoup = BeautifulSoup(getData,  "html.parser")
print(parseSoup.h1.text)

# iterating the parsed content and finding the "anchor" tags
for i in parseSoup.findAll('a'):
    # retrieve the href elements from a tags
    print(i.get('href'))

    # create a table variable and retrive table elements from class 'wikitable sortable plainrowheaders'
table = parseSoup.find("table", { "class" : "wikitable sortable plainrowheaders" })

#  Iterate over table variable using for loop and "tr" attribute of the table for rows "td" for columns
for row in table.findAll('tr'):
    for column in row.findAll('td'):

        columnData = column.text
# print the column data
        print(columnData)
# print the row data
rowData = row.find('th')
print(rowData.text)