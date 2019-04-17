#ODDN Photos Downloader

##Description
Script Python permettant de télécharger les photos référencées dans le code HTML des pages photos de chaque billet journalier du site __ondonnedesnouvelles.com__ 

##Utilisation

Sauvegarder le code source de chaque page photo dans un fichier nommé YYYYDDMM sous le répertoire ````html/```. Par exemple:

```
20190408.html
20190409.html
```

Lancer le script qui téléchargera les photos et les placera sous le répertoire ```photos/``` en les préfixant par ```YYYYDDAA```

```
Processing: html\20190413.html
Saving:     http://ondonnedesnouvelles.com/uploads/n1/121195/photos_web/abcdefghij.xxxx_yy.jpg as photos/photos/20190413_0001.jpg
Saving:     http://ondonnedesnouvelles.com/uploads/n1/121195/photos_web/abcdefghij.xxxx_yy.jpg as photos/photos/20190413_0002.jpg
Saving:     http://ondonnedesnouvelles.com/uploads/n1/121195/photos_web/abcdefghij.xxxx_yy.jpg as photos/photos/20190413_0003.pg
Saving:     http://ondonnedesnouvelles.com/uploads/n1/121195/photos_web/abcdefghij.xxxx_yy.jpg as photos/photos/20190413_0004.pg
```
