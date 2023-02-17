# Case-Study
<p align="center">
 <img src="https://i.imgur.com/rSyq3MW.png" alt="The Documentation Compendium"></a>
</p>

<h3 align="center">The Documentation For Data Analytics</h3>

---

## Table of Contents
1. Tool and python packeges are used
2. High level design
3. Quick first implementation
4. Single processing or mulitprocessing
5. Derived conclusions summary
6. Next steps


## 1. Tool and python packeges are used
As suggested in case study statement we have selected a python as lagauage to complete this project. This case study is extracting the data from various online website and do analysis on same. Hence, we deciced to choose web scrapping libraries of python like selenium and beautifulsoup. After some exploaraiton we decided to go with beautifulsoup to keep the complexiy simple and avoid the installation of web drivers.

Further, since this is very first analysis of this data hence choosed Jupyter notebook as python IDE in order to have simpple and clear visualization of analysis.

Also, this case study is demanding the outputs in CSV formats hence pandas is framework we will use to deal with dataframes and numpy to do numerical operations in python.

Below are the essential python packages/tools that required for this project and can be added in requirnment.txt file while productionizing.
<strong>python packages </strong>
- re
- requests
- numpy
- pandas
- BeautifulSoup

<strong>Tools </strong>
- excel
- jupyter notebook

## 2. High level design
As high level design we can think of below steps,
1. Create a initial code in jupyter notebook
2. Perform result validations
3. Understand the data size, time required for operations
4. Select multiprocessing or sequential method
5. Add Optimization, beautification and logging 
6. Create an API which will take inputs from front end and answer the below questions.

## 3. Problem complexity
As the given case study is of medium level complexity and it in production we might encounter the scenarios which are not covered in this case. Hence as rule of thumb we are focusing on quick implementaion of intial development so that we can do the upgrade, optimize and improvement keeping end goal in mind.

As first step, creating a jupyter notebook for intial analysis which will be followed by code optimization, improvements and beautifications.

## 4. Single processing or mulitprocessing
We have a small amount of data hence we decided to go with sequential operations however we have noticed that it was time consuming. Also there were several factor that can affect the API to respond. Hence if we will plan to deploy this project in production its depolyment should follow the multiprocessing approach to reduce the use waiting time on front end. 

Multiprocess is assigning tasks to multiple processes — workers — to handle tasks alongside other tasks. This is a significant benefit to programmers as it allows you to create more efficient software that can perform tasks and functions.

Link to official documentation <a href="https://docs.python.org/3/library/multiprocessing.html">Visit Mulitprocessing</a>
<br>
<Strong>Mulitprocessing in python</Strong>
```ruby
from multiprocessing import Pool
def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))
==>> [1, 4, 9]
```

## 5. Derived conclusion summary 
### 1. For each URL, look for all href elements
- https://sanctionssearch.ofac.treas.gov/  =  11
- https://home.treasury.gov/  =  289
- https://www.thomsonreuters.com/  =  121
- https://verafin.com/solution/  =  0
- https://www.swift.com/  =  208
- https://anti-fraud.ec.europa.eu/index_en  =  83
- https://www.kroll.com/  =  107
- https://learn.seon.io/  =  4
- total_href =  823

### 2.Out of these hrefs, filter out first 10 which start with http (or https) and those which do not. That is they have format href=”http://…” or href=https://......”
```ruby
filtered_href =  ['https://home.treasury.gov/policy-issues/financial-sanctions/consolidated-sanctions-list-data-files', 'https://home.treasury.gov/policy-issues/financial-sanctions/faqs/287', 'https://home.treasury.gov/policy-issues/financial-sanctions/specially-designated-nationals-list-data-formats-data-schemas', 'https://home.treasury.gov/policy-issues/financial-sanctions/specially-designated-nationals-list-sdn-list/program-tag-definitions-for-ofac-sanctions-lists', 'https://home.treasury.gov/policy-issues/office-of-foreign-assets-control-sanctions-programs-and-information', 'http://www.usajobs.gov/', 'https://home.treasury.gov/subfooter/site-policies-and-notices', 'https://www.irs.gov/forms-pubs/about-form-941', 'https://home.treasury.gov/utility/languages/alrbyt-arabic', 'https://www.treasury.gov/auctions/irs/index.html']
```
### 3.For each href which starts with http or https, find all links which are valid (which return http status code 200 and those which are not valid). Save as a CSV file.
<a href="https://github.com/ShubhPatil95/Case-Study/blob/main/valid_href.csv"> Check valid_href.csv </a>

### 4.Handle those cases where a website does not respond within 20 seconds ( configurable) ( Nice to have, leave if you have no time).
<a href="https://github.com/ShubhPatil95/Case-Study/blob/main/valid_href_timeout.csv"> </a>

### 5.Make a graph which plots each entry in List1 against total number of href links, valid https/https links and invalid https links.
![image](https://user-images.githubusercontent.com/74223025/219590359-6fd7e44e-e73c-4289-b635-402a8b508640.png)

##### Stacked plot
![image](https://user-images.githubusercontent.com/74223025/219592471-1d8bdd97-bb33-4e44-9223-a0cdbbf50a67.png)


### 6. For each valid http/ https links or sub links find the website having the highest number of each keyword form list2 in Appendix. Group them by main link from list 1 and then the sub links. Make a csv file.
<a href="https://github.com/ShubhPatil95/Case-Study/blob/main/Max_freq_keyword.csv" > Check Max_freq_keyword </a>

## 6. Next steps
As next step we should first discuss these results and our future plan with end user/client and take suggestions and improvement. The main challenge that we can face here is use waiting time hence need to explore more on same. Also we can think of two way deployment 1. Real time API 2. Linux Service as per data size hence need to check the end user requirnment accordingly.  
