## SECTION 1 : PROJECT TITLE
## Intelligent carpooling system

<div align=center>
<img src="https://github.com/kaiyangHebert/CyberCaptain/blob/main/img/first%20page.jpg?raw=true" width="347" height="679"> 
</div>


## SECTION 2 : EXECUTIVE SUMMARY
Due to the large number of students at NUS and the fact that the university dormitory is not available to all, students are required to take the bus or MRT or a taxi home after class. Taking the bus or MRT can result in long waiting times and the cost of taking a taxi alone can be expensive. Hence, the need for carpooling between students is generated.

Our project is dedicated to carpooling by grouping student passengers from similar destinations together based on a clustering algorithm and then using the Dijkstra algorithm to figure out the shortest path. As the colleges are relatively far away, but the NUS bus route basically covers all colleges and utown, the default pick-up point for students was chosen as utown. The drop-off location is freely chosen by the passengers, but system will match the existing carpooling points by calculating the relative distance, so that system can give the user a station closer to his/her destination.

## SECTION 3 : CREDITS / PROJECT CONTRIBUTION
| First Header  | Second Header || First Header  | Second Header |
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  || ------------- | ------------- || Content Cell  | Content Cell  || Content Cell  | Content Cell  |
## Install
download [Node.js](https://nodejs.org/en/download/)  
`$ npm install`  
  
download [python3.6](https://www.python.org/downloads/release/python-360/)  
`$ pip install -r requirements.txt`  

## Error and Solution  
In file:.\lib\site-packages\chatterbot\tagging.py  
**Change** `yaml.load()` **to** `yaml.safe_load() `  
  
**Change** `self.nlp = spacy.load(self.language.ISO_639_1.lower())` **to**
`if self.language.ISO_639_1.lower() == 'en': self.nlp = spacy.load('en_core_web_sm')  `
`else: self.nlp = spacy.load(self.language.ISO_639_1.lower())`

