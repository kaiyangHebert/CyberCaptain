# SECTION 1 : PROJECT TITLE
# Intelligent carpooling system

![Image text]

## 
  
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

