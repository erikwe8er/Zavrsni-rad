# ROBOTSKA ŠAKA

Robotska šaka napravljena uz pomoć 3D printanih modela ruke, te mikrokontrolera Arduino MEGA i Raspberry Pi 3.

## Dijelovi potrebni za izradu

### Modeli

Modeli ruke preuzeti su sa stranice [InMoov](https://inmoov.fr/inmoov-stl-parts-viewer/?bodyparts=Right-Hand), 
kućišta mikrokontrolera su preuzeta sa stranica [Arduino](https://www.thingiverse.com/thing:2709747) i [Raspberry](https://makerworld.com/en/models/579053-raspberry-pi-3-4-case-gpio-ribbon-cable-cutout#profileId-499808).

### Elektronika
Za upravljanje rukom zaslužni su **TowerPro SG90** servo motori, kojih ima pet, jedan za svaki prst. Njima upravlja **Arduino MEGA** mikrokontroler koji signale dobija
od **Raspberry Pi** kontrolera. Komunikacija između kontrolera odvija se preko UART protokola. Osim toga potrebno nam je i jedno napajanje kako bi motori imali dovoljno snage.
Kako bi spojili sve navedene komponente potrebne su nam i žice te jedan _breadboard_. Uz sve navedeno potrebna nam je i **Web kamera** te **tipkovnica** kako bi mogli pokrenuti
samu šaku.

## Korištenje

### Spajanje
Kako bi šaka radila potrebno ju je prvo odgovarajuće spojiti.  
Spajanje motora:  
- Palac: **Siva žica - Ulaz 6 na Arduinu**
- Kažiprst: **Plava žica - Ulaz 5 na Arduinu**
- Srednji prst: **Žuta žica - Ulaz 2 na Arduinu**
- Prstenjak: **Ljubičasta žica - Ulaz 12 na Arduinu**
- Mali prst: **Zelena žica - Ulaz 11 na Arduinu**

Osim žica za signale potrebno je spojiti i crvenu žicu na pozitivni, te smeđu žicu i **GND** pin na **Arduinu** na negativni izlaz napajanja.

Time smo spojili motore, zatim je potrebno spojiti **Arduino** i **Raspberry**, kameru i tipkovnicu na **Raspberry** te napajanje, sve navedeno spaja se preko USB-a.
Kako bi vidjeli na koji način radi prepoznavanje ruke i pokreta poželjno je **Raspberry** spojiti na monitor preko HDMI kabla.

## Pokretanje i korištenje
Kako bi pokrenuli šaku potrebno je upaliti **Raspberry**, prijaviti se u njega (_lozinka:1234_) i otvoriti terminal.  
U terminal je potrebno unijeti sljedeće:  
```
source myenv/bin/activate
python3 GestureControl.py
```
Nakon unešenih naredbi otvoriti će se prozor koji prikazuje sliku s kamere, kako bi upravljali šakom potrebno je staviti ruku u područje koje kamera vidi,
zatim ju držati u raširenom položaju i kliknuti slovo **Q** kako bi kalibrirali ruku, kada ju uspješno kalibriramo doći će do promjene prozora i biti će omogućeno
upravljanje šakom.  
Za prestanak rada potrebno je kliknuti slovo **E**.

