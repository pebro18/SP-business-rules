# SP-business-rules
We gaan aan het werk met het opzetten van een rule-based systeem ten behoeve van de recommendation engine.


### Fork van Stan Haakman versie
wij hebben voor deze opdracht een verbeterde versie gemaakt van opdracht 2

### opzetten van DB
prerequities: 
1. verbonden met mongodb met een db genaam huwebshop die gevult is met sessions, products en visitors
2. database.ini aanmaken in het project map met deze info er in:
![afbeelding](https://user-images.githubusercontent.com/35180025/111664177-ccfebc00-8811-11eb-994a-a407041a08fa.png)

3. als de DB niet bestaat commenteer de drop_database functie in main.py

dan alleen main.py runnen

### Run content filter rule
voor deze regel moet je content_rules.py runnen

#### resultaat van content rule
![afbeelding](https://user-images.githubusercontent.com/35180025/111662977-ac823200-8810-11eb-8746-9d261fea31d2.png)

### Run collab filter rule
voor deze regel moet je collab_rules

#### resultaat van collab rule
