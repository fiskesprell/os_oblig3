# Oblig 3 - Github Actions

## Hvordan jeg fikk det til å fungere:
### 1. Lage et repository  
Jeg har allerede filene lagret på maskinen min, så alt jeg 
gjorde her var å logge inn på github.com, og under taben "repositories"
trykke på "New" og skrive inn navnet jeg ville ha på repositoriet.
Etter dette gikk jeg inn på pycharm, commited alle filene fra oblig 2
til til dette repositoriet ved å lime in lenken til det, og trykke på "push".

### 2. Lage readme.md
Readme.md lages lett ved å opprette en ny fil i prosjektet ditt og
kalle den "readme.md". Jeg brukte lenken https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
for basic syntax og formattering av tekst. Commit og push.  
Lager mappen .github/workflows på samme måte.  

### 3. Lage .github/workflows/testing.yml
1. Gå inn på "Actions" tabben i repositoriet ditt på Github.
2. Trykk på "Configure" under "Simple Workflow" for å opprette en .yaml fil under .github/workflows/
3. Følg denne dokumentasjonen for å sette opp python testing: https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python#caching-dependencies
og https://vilisimo.com/blog/setting-up-pytest-with-github-actions/
5. Commit og push.

### 4. Sjekke at tester faktisk blir gjennomført og bestått:
Når jeg pusher til github repositoriet blir det automatisk kjørt en test.
Her er forrige test som ble kjørt. Under "Testing with Pytest" står det at
100% av test_leap_year.py er bestått, "4 passed in 0.02 seconds."
https://github.com/fiskesprell/softeng_oblig3/actions/runs/6631254900/job/18014377393
