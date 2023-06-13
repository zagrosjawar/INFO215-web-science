# SPARQL Queries on Wikidata

This directory contains SPARQL queries to fetch specific information from [Wikidata](https://www.wikidata.org/). Below are the queries for different tasks:

## 2.1 Find all American Politicians whose fathers were also politicians

```sparql
SELECT ?politician ?father ?politicianLabel
WHERE 
{
  ?politician wdt:P31 wd:Q5;         # instance of Human
              wdt:P27 wd:Q30;        # country of citizenship United States of America
              wdt:P106 wd:Q82955;    # occupation Politician
              wdt:P22 ?father.       # father 
  ?father wdt:P106 wd:Q82955.        # occupation Politician
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
```

## 2.2 Find all Norwegian Poets whose date of birth is after 1950

```sparql
SELECT ?poet ?poetLabel ?birthdate ?BirthdateLabel
WHERE
{
  ?poet wdt:P31 wd:Q5.               # instance of Human
  ?poet wdt:P106 wd:Q49757.          # occupation Poet
  ?poet wdt:P27 wd:Q20.              # country of citizenship Norway
  ?poet wdt:P569 ?birthdate.
  FILTER(?birthdate > "1950-12-31T23:59:59"^^xsd:dateTime)
  
SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
```

## 2.3 Count the number of universities in Wikidata

```sparql
SELECT (COUNT(*) AS ?NumUniversities)
WHERE
{
  ?NumUniversities wdt:P279 wd:Q38723.  # subclass of Higher Education Institution
}
```

## 2.4 Find all Norwegian Poets who are also politicians. Show their birthplace in a map

```sparql
#defaultView:Map
SELECT *
WHERE
{
  ?item wdt:P31 wd:Q5.               # instance of Human
  ?item wdt:P106 wd:Q49757.          # occupation Poet
  ?item wdt:P106 wd:Q82955.          # occupation Politician
  ?item wdt:P27 wd:Q20.              # country of citizenship Norway
  ?item wdt:P19 ?birthplace.
  ?birthplace wdt:P625 ?geo.
}
```

## 2.5 Show the birthplace of all people in a map who received Nobel prizes

```sparql
#defaultView:Map
SELECT *
WHERE
{
  ?person wdt:P31 wd:Q5;             # instance of Human
          wdt:P166 ?prize;           # award received ?prize
          wdt:P19 ?birthplace.       # place of birth ?birthplace
  ?birthplace wdt:P625 ?geo.         # coordinate location ?geo
  FILTER ((?prize in (wd:Q35637,  wd:Q37922, wd:Q44585, wd:Q80061, wd:Q38104, wd:Q47170)))
}
```

Please note that these queries are provided as examples and may require adjustments or additional filtering based on your specific needs.

For more information on SPARQL and Wikidata, please refer to the [Wikidata Query Service](https://query.wikidata.org/) and the [Wikidata Query Help](https://www.wikidata.org/wiki/Wikidata:SP
