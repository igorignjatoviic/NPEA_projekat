# Projektni zadatak br. 1 – Genetski algoritam: Problem putujućeg trgovca

## Predmet
Nelinearno programiranje i evolutivni algoritmi

## Tema
Implementacija genetskog algoritma za rešavanje problema putujućeg trgovca (TSP).

---

## Opis problema
Problem putujućeg trgovca (TSP) zahteva pronalaženje optimalnog redosleda obilaska svih gradova iz zadatog skupa tako da:

- Svaki grad bude obiđen **tačno jednom**  
- Ukupan pređeni put bude **najmanji mogući**  
- Putovanje se **završava u gradu odakle je počelo**

Koordinate gradova su date u fajlu `data_tsp.txt`. Udaljenost između dva grada se računa pomoću Euklidske distance:

\[
d(g_1, g_2) = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}
\]

---

## Struktura programa
Program je implementiran u Python-u i sastoji se od sledećih modula/funkcija:

- `loadCities(filename)` – učitava gradove i njihove koordinate iz fajla  
- `generateInitialPopulation(size)` – kreira inicijalnu populaciju ruta (permutaije gradova)  
- `totalDistance(route, cities)` – računa ukupnu udaljenost rute  
- `tournamentSelection(cities, population, chromosomes)` – bira roditelje pomoću turnirske selekcije  
- `orderCrossover(parent1, parent2)` – pravi dete iz dva roditelja pomoću order crossover operatora  
- `swapMutation(route, mutationRate)` – menja mesta dva grada u ruti sa određenom verovatnoćom  
- `elitis(cities, population)` – čuva najbolju jedinku (elitizam)  
- `generateNewPopulation(cities, population)` – kreira novu generaciju iz postojeće populacije  
- `generateGenerations(numGenerations, cities)` – glavni loop algoritma koji iterira kroz generacije i prati najbolje rešenje  

---

## Kriterijum optimalnosti
Kriterijum optimalnosti je **minimalna ukupna pređena distanca** svih gradova u ruti. Najbolja jedinka je ruta sa najmanjom vrednošću `totalDistance`.

---

## Implementacija operatora
### Mutacija
- Implementirana kao **swap mutation**  
- Dva grada u ruti se nasumično zamene sa verovatnoćom `mutationRate`  
- Ovo omogućava istraživanje novih ruta bez gubitka permutacije

### Ukrštanje (Crossover)
- Implementiran **order crossover (OX)**  
- Deo rute prvog roditelja se kopira, a preostale pozicije se popunjavaju redom iz drugog roditelja bez duplikata  
- Obezbeđuje validnu permutaciju gradova  

---

## Strategija odabira jedinki za ukrštanje
- Koristi se **turnirska selekcija**  
- Nasumično se bira `k` jedinki iz populacije  
- Najbolja jedinka iz turnira postaje roditelj  
- Proces se ponavlja za oba roditelja svakog crossover-a  

---

## Odabir parametara algoritma
- Veličina populacije: npr. 100 ruta  
- Broj generacija: npr. 500  
- Mutation rate: 0.2 (20% šanse za swap po jedinki)  
- Turnirska selekcija: 3–10 kandidata po turniru  
- Elitizam: 1 najbolja jedinka po generaciji se čuva  

---

## Rezultati algoritma
- Program ispisuje najbolju rutu po generaciji:  
