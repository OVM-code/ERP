<!-- pack: food-manufacturing v1 — fork naar clients/<slug>/bpa/content/ en vervang <placeholders> -->
# 4. Voorraad

Volledige lottracering met THT-bewaking is in food niet onderhandelbaar
(<certificering — IFS/BRC> + FAVV-recallplicht). De inrichting steunt op de Aptean
Food & Beverage-laag: lot management voor tracering, expiration management voor
THT/FEFO. Waardering typisch FIFO.

## BS50.100 Artikelen beheren
- **Invulling:** standaard

Grondstoffen, verpakkingen en eindproducten met artikelcategorieën per
productgroep; traceerplichtige artikelen krijgen een traceringscode en een
houdbaarheidsformule. Waarderingsmethode: <FIFO>.

## BS50.104 Artikeltraceringscodes beheren
- **Invulling:** standaard

Twee codes volstaan meestal: `LOT-VOLLEDIG` (lotverplicht bij ontvangst, verbruik,
productie én verzending) en `GEEN` (hulpstoffen zonder voedselcontact).

## BS45.904 Lot management
- **Invulling:** add-on: Aptean Food & Beverage

Traceringscockpit: elk lot in beide richtingen traceerbaar (grondstof → afnemers,
eindproduct → leveranciers). De FAVV-recalltest wordt een rapport van minuten.
Lotnummers automatisch per <nummerlogica>; leverancierslot mee geregistreerd.

## BS45.902 Expiration management
- **Invulling:** add-on: Aptean Food & Beverage

THT automatisch bij productie/ontvangst; picken FEFO; per klant(groep) een
minimale resthoudbaarheid (<retailregel — typisch 2/3 of 3/4>) waaronder loten
voor dat kanaal niet meer aangeboden worden.
<!-- vraag: verschillende resthoudbaarheidsregels per keten? -->

## BS45.200 Artikelen blokkeren
- **Invulling:** workaround
<!-- vraag: is een QC-labomodule in scope? zo ja: invulling wordt add-on, dit blok herschrijven -->

Zonder QC-module: kwaliteitsvrijgave via lotstatussen (Aptean status management) —
productieloten automatisch `GEBLOKKEERD-QC`, digitale vrijgave door kwaliteit met
gelogde gebruiker/tijdstip (audittrail vervangt het papieren formulier). Labo-
meetwaarden blijven in het labosysteem; alleen de beslissing komt in BC.
