# OpenClassrooms AI Engineer training : Project 1
Detect a language using Azure Cognitive Services. 
* The solution should retrieve the model prediction. 
* The text in the body of the request should be easily editable. 
* The solution should be secure: authentification keys should not be visible in the script.
* The script should be contained in one file.

Files in this repository:
* /detect.py/ contains the main script
* /config.py/ is the file I call on in my script to retrieve the API key, endpoint and location
* /.gitignore/ tells Git which fies to ignore when committing to avoid sharing my keys
* /script.bat/ is the initial cURL script I wrote to query Azure Cognitive Services before switching to Python and VSCode

```
Please enter a string: Anton (or Antonius) Maria Schyrleus (also Schyrl, Schyrle) of Rheita (1604–1660) ((in Czech) Antonín Maria Šírek z Reity) was an astronomer and optician.
[{'language': 'en', 'score': 0.91, 'isTranslationSupported': True, 'isTransliterationSupported': False}]
The text is in en with a confidence score of 100%

Please enter a string: 近幾年來，由於氣候變遷對人類帶來的警訊，讓各國政府紛紛思考如何減碳節能。
[{'language': 'zh-Hant', 'score': 1.0, 'isTranslationSupported': True, 'isTransliterationSupported': True}]
The text is in zh-Hant with a confidence score of 100%

Please enter a string: बांग्लादेश के मुख्य न्यायाधीश का पद, बांग्लादेश सर्वोच्च न्यायिक पद है। 
[{'language': 'hi', 'score': 1.0, 'isTranslationSupported': True, 'isTransliterationSupported': True}]The text is in hi with a confidence score of 100%

Please enter a string: 2014 debía de ser la temporada de la consagración de Elissonde, pero no fue así.
[{'language': 'es', 'score': 1.0, 'isTranslationSupported': True, 'isTransliterationSupported': False}]
The text is in es with a confidence score of 100%

Please enter a string: Les supporters de l'ASM Clermont Auvergne ont reçu en 2007, 2008 et 2009 le prix de l’Éthique et de la convivialité (challenge des meilleurs supporters) du Top 14.
[{'language': 'fr', 'score': 1.0, 'isTranslationSupported': True, 'isTransliterationSupported': False}]
The text is in fr with a confidence score of 100%
```
