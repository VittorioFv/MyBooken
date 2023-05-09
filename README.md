# MyBooken

MyBooken è una webapp che ha come scopo promuovere la lettura attraverso lo scambio di libri tra gli utenti tramite Topen digitali, senza dover necessariamente dare un altro libro in cambio o pagare, promuovendo così il libero scambio virtuale.

## Attivare l'ambiente virtuale di python

apri il terminale in ```DJANGO\sito```.
Poi eseguire il seguente comando:

	source myworld/bin/activate

## Far partire il server in locale

Con l'ambiente virtuale attivato (opzionale) apri il terminale in ```DJANGO\sito\myBooken```.

Se è la prima volta che esegui il programma ricordati di eseguire una migrazione ed di istallare tutte le dependency (Le istruzioni le trovi più avanti).

Poi eseguire il seguente comando:

	python3 manage.py runserver
	
Andare sul browser alla pagina ```http://127.0.0.1:8000/libri/```


## Dependency necessarie

Token conferma email:

	pip install six
 
Gestione immagini immagini:
	
	pip install Pillow 

Mappe e distanze tra punti:

	pip install geopy
	
QR code:

	pip install django-qr-code




## Migration:
Per eseguruire un migrazione aprire il terminale in ```DJANGO\sito\myBooken``` e eseguire questi 2 comandi:

	py manage.py makemigrations
	python manage.py migrate