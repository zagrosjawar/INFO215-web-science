## spaCy
SpaCyis a free, open-source library for advanced Natural Language Processing (NLP) in python.
Installations instructions: https://spacey.io/usage

<code>pip install spacy</code>

## Text Summarization steps:  
	1. Initialization                          
	2. Filtering tokens 
	3. Normalization                            
	4. Weighing sentences      
	5. Summarizing Sentences


## The Global Database of Events, Language, and Tone (GDELT)

GDELT 2.0 (https://blog.gdeltproject.org/gdelt-2-0-our-global-world-in-realtime/ ), also known as the Global Database of Events, Language, and Tone, 
is a big data platform that monitors news media worldwide. 
You can access to the latest news articles by following the hyperlink 'Last 15 Minutes CSV Data File List – English.  (Updated every 15 minutes).' 
from GDelt website. 
The file contains a URL to a zip file that ends with 'export.CSV.zip’. 
The zip file contains a csv file with multiple lines where each line contains a url to news articles (see last column of the csv file). 

This program extracts information following links to the news articles (using python library called spaCy and  Newspaper3k) (https://newspaper.readthedocs.io/en/latest/ ) for extracting & curating the news articles. 

gdelt_summary_named_entities.py is python program that takes a csv file (with links to news articles) as input and produces another csv file as output. 
It makes a summary of the news article and then extract named-entities from the article summary. 
The output file consist of the following information (seperated by comma): 

- Link to the source news article 
- Named entities
  
The source csv file may contain redundant news-article links, therefore, the program keeps tract of already visited news article pages. 
For named entity recognition you may use spacy library or DBPedia Spotlight (https://www.dbpedia-spotlight.org/api ).

