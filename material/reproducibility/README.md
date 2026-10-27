
## Implementeren van een gepubliceerd model

Agentic AI kan een artikel lezen, en een beschreven statistisch model implementeren, uitvoeren, en
de gepubliceerde resultaten controleren.  Hiermee is "reproducible science" echt haalbaar - mits 
natuurlijk alle data vrij beschikbaar is.

Hier is een voorbeeld van een recent paper waar de onderliggende data vrij beschikbaar zijn, en waar
de resultaten reproduceren inderdaad mogelijk is.

Het gaat om een model om het risico op all-cause mortality te voorspellen.  Data zijn 24,000 personen
die gedurende 8 jaar gevolgd zijn, samen met een groot aantal predictievariabelen.

Bij het implementeren blijken er toch een aantal keuzes niet precies beschreven te zijn, wat leidde
tot kleine verschillen.  De AI vond ook een paar keuzes die niet optimaal waren:

- er is geen rekening gehouden met verschillende follow-up intervallen
- er is geen imputatie gedaan; en missingness bleek informatief voor bepaalde variabelen

Een model dat deze aspecten ook  meeneemt blijkt een klein beetje meer voorspellende waarde te hebben,
en laat ook betere calibratie zien.


## Praktische zaken

Copilot kan geen gegevens van het internet downloaden.  Ik heb het paper als .pdf dus bijgevoegd.

Ook de data kan niet gedownload worden, deze is ook toegevoegd, als .zip file.  De interface die wij
gebruiken (Copilot 365?) laat het niet toe .zip files te uploaden, dus ik heb het hernoemd als
data.zip.txt - daar kan Copilot vervolgens prima mee om gaan.

De taak zelf is in Task.md uitgelegd.  Dit kan natuurlijk ook in een prompt worden meegegeven.


## Uitvoeren

Upload de 3 files "Agogo-et-al-2025.pdf", "data.zip.txt", "Task.md"

Typ dan als prompt "Voer taak 1 uit", en vervolgens "Voer taak 2 uit".


## Hoe goed werkt het

Ik heb Copilot vergeleken met Claude.  Claude kan zelf data downloaden (niet het paper zelf, dat zit
achter een paywall).  Dat Copilot niet mag downloaden is wat lastig maar niet een echt probleem.

Claude zet de data en tussenresultaten in folders op je eigen computer.  Dat vind ik prettig werken,
je kunt ook zelf makkelijk bij de data en resultaten.

Copilot maakt meer foutjes, en geeft minder detail over de keuzes die het maakt.  Bijvoorbeeld, 
missing data en "0" waarden worden op een bijzondere manier gedoceerd, en Claude kon hier goed mee 
werken, maar bij Copilot ging dit eerst mis.  Ook voegde Copilot eerst de follow-up time toe als 
voorspellende variabelen in een Cox model, wat zorgde voor convergentieproblemen.  Ik moest Copilot
vragen het convergentieprobleem op te lossen, en zonder meer aanwijzingen vond het zelf het probleem
en lostte het op.

