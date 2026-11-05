# Music Production Manager

## Apžvalga

„Music Production Manager“ - tai naudojant „Django“ sukurtas žiniatinklio taikymas, skirtas muzikos kūrybos projektams organizuoti ir valdyti.

Taikymas leidžia valdyti muzikinius projektus nuo pradinės idėjos iki galutinio išleidimo, kurti užduotis ir pastabas, saugoti kūrinių versijas bei analizuoti kūrybinę veiklą.

## Funkcijos

- Kurti, peržiūrėti, redaguoti ir ištrinti muzikinius projektus.
- Saugoti projekto informaciją: pavadinimą, žanrą, būseną, BPM, muzikinę tonaciją, išleidimo datą, trukmę, aprašymą ir viršelio paveikslėlį.
- Organizuoti projektus pagal žanrą ir gamybos būseną.
- Ieškoti projektų pagal pavadinimą.
- Filtruoti projektus pagal žanrą ir būseną.
- Naudoti puslapiavimą patogesnei projektų peržiūrai.
- Kurti ir valdyti kiekvieno projekto užduotis.
- Kurti ir tvarkyti projekto pastabas.
- Saugoti ir valdyti skirtingas kūrinio versijas.
- Peržiūrėti projektų ir užduočių statistiką valdymo skydelyje.
- Analizuoti projektų pasiskirstymą pagal būsenas ir žanrus.
- Generuoti diagramas naudojant „Matplotlib“.
- Analizuoti projektų duomenis naudojant „Pandas“.

## Naudojamos technologijos

- Python
- Django
- SQLite
- HTML
- CSS
- Bootstrap 5
- Pandas
- Matplotlib

## Projekto struktūra

- `config/` – pagrindiniai „Django“ projekto nustatymai.
- `projects/` – muzikinių projektų modeliai, formos, peržiūros funkcijos, šablonai ir testai.
- `analytics/` – statistikos valdymo skydelis ir muzikinių projektų analizė.
- `templates/` – bendri HTML šablonai.
- `static/` – statiniai failai, įskaitant CSS.
- `media/` – įkelti projektų viršelių paveikslėliai.
- `manage.py` – „Django“ projekto valdymo įrankis.
- `requirements.txt` – projekto priklausomybės.

## Įdiegimas ir paleidimas

### 1. Atsisiųskite projekto kodą

```bash
git clone YOUR_REPOSITORY_URL
cd MusicProductionManager
```

Pakeiskite `YOUR_REPOSITORY_URL` tikruoju repozitorijos adresu.

Jeigu projekto failai jau yra jūsų kompiuteryje, atidarykite projekto katalogą terminale.

### 2. Sukurkite virtualiąją aplinką

```bash
python -m venv .venv
```

### 3. Aktyvuokite virtualiąją aplinką

„Windows PowerShell“ aplinkoje:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Įdiekite priklausomybes

```bash
python -m pip install -r requirements.txt
```

### 5. Sukonfigūruokite aplinkos kintamuosius

Projekto pagrindiniame kataloge sukurkite `.env` failą ir nurodykite reikalingus aplinkos kintamuosius, įskaitant `SECRET_KEY`.

Neskelbkite slaptųjų raktų ir kitos konfidencialios konfigūracijos versijų valdymo sistemoje.

### 6. Atnaujinkite duomenų bazę

```bash
python manage.py migrate
```

### 7. Paleiskite kūrimo serverį

```bash
python manage.py runserver
```

Atidarykite naršyklėje:

http://127.0.0.1:8000/

## Testavimas

Paleisti visus automatinius testus:

```bash
python manage.py test
```

Paleisti `projects` programėlės testus:

```bash
python manage.py test projects
```

Paleisti `analytics` programėlės testus:

```bash
python manage.py test analytics
```

## Projekto tikslas

Šis projektas sukurtas kaip kursinis darbas, siekiant praktiškai pritaikyti „Django“, reliacinių duomenų bazių modelius, CRUD operacijas, formų validaciją, paiešką, filtravimą, duomenų vizualizavimą ir automatizuotą testavimą žiniatinklio programoje.

## Galimi patobulinimai

- Išplėsti analitikos ir ataskaitų galimybes.
- Tobulinti muzikinių projektų valdymo procesus.
- Pridėti daugiau muzikos kūrybos statistikos.
- Įdiegti duomenų eksportavimo funkciją.
