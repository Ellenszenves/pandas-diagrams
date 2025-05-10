# pandas-diagrams

#Függőségek  
Szükséges library-k, indítás előtt kérlek ellenőrizd, hogy telepítve vannak-e:  
pandas, matplotlib.pyplot, requests, csv, seaborn, tkinter

#Használat  
Indítás: python3 solution.py  
Egy interaktív menü segítségével érhetjük el a funkciókat.
1. Letöltés
   Ez a funkció letölti a KSH oldaláról a legfrissebb népességi adatokat, ezután automatikusan létrehoz egy analizáláshoz alkalmas tisztított fájlt is.
2. Tisztítás
   Ha esetleg már a mappánkban van a megfelelő fájl az adatokkal, ez a funkció megtisztítja a további használathoz.
3. Statisztika
   Ez a funkció megmutatja az oszlopok korrelációját.
4. Pont-diagram
   Ez a funkció létrehoz egy pont diagramot, a teljes népesség értékeivel.
5. Vonal-diagram
   Egy vonal diagramot kapunk, melyen a teljes népesség mellett a női és férfi népességi adatok is szerepelnek.
6. Grafikus felülfet
   Egy egyszerű grafikus felület, melyen a funkciók a gombok megnyomása után érhetőek el.
7. Kilépés
   Ezzel a funkcióval kiléphet a programból.
