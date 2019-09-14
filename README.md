### PairPiperWeb 1.5.4

##
#### Versionshistorik<br>
**0.0.1** - Grundläggande Django-projekt <br>
**0.0.2** - Formulär för pardata, fungerande returnering <br>
**0.0.3** - Appen 'piperdatabase' tillagd, endast funktionen 'update live' är i drift <br>
**0.0.4** - Uppdateringsfunktioner för livedb.csv och fulldb.csv är nu fullt fungerande <br>
**0.0.5** - Pairsdata visar nu graf i samma template <br>

**0.1.0** - Förbättrad layout samt interface för att växla mellan pairsdata och piperdatabase <br>
**0.1.1** - Piperdatabase genererar nu statusmeddelande vid databasuppdatering <br>
**0.1.2** - Problemet "List index out of range" vid webscraping löst <br>
**0.1.3** - Graf-layout förändrad och förinställd end date i pairs data <br>
**0.1.4** - Förinställd start date <br>

**1.1.5** - Körs skarpt på lokal webbserver synkad via Dropbox

**1.2.0** - Portfolio och Add Position tillagd, delvis fungerande, kopplad till sqlite-databas<br>
**1.2.1** - Uppdaterad tickerlist i samtliga appar (CAST, HUFV-A, FABG, SHB-A, SECU-B)<br>

**1.3.2** - piperdatabase kopplad till db.sqlite3, Add Position och Portfolio kopplade till modelforms, tradelogg tillagd (ej funktionell)<br>
**1.3.3** - Startsida (127.0.0.1:8000) tillagd. Länk till admin-sida i headern <br>
**1.3.4** - AddPosition baserad på modelforms. Skriver till portfolio-model. Main position fortfarande ej komplett <br>
**1.3.5** - Portfolio-appen kan nu redigera och lägga till data till en position  <br>

**1.4.0** - Positioner skrivs nu till tradelogg när de stängs på portfolio-sidan  <br>
**1.4.1** - Både singel- och flerbenspositioner kan nu öppnas och stängas via interface  <br>

**1.5.0** - Portfolio-appen kan nu visa samtliga och stänga valda positioner <br>
**1.5.1** - Open price / close price borttaget från main position vid flerbenstrades <br>
**1.5.2** - La till /autoscraper till repository <br>
**1.5.3** - Uppdaterade requirements och gitignore <br>
**1.5.4** - Piperdatabase borttaget då Autoscraper fyller samma funktion. Admin-static flyttade till ordinarie static-mapp.
