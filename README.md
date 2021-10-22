# guideAppUtils

Auteur : Aurélien MASSON

Ce projet réunit 4 petits scripts de type Utilitaires pour l'application du musée NAM-IP. Il sont tous liés et écrit pour fonctionner avec la base de données NAMIP.db.

1 - Script database.py :

Ce script contient deux fonctions : connection() et update(), et utilise les bibliothèques sqlite3 et pathlib.

La première comme son nom l'indique permet de créer la connexion à la base de données en prenant comme argument le chemin de cette dernière, la connexion se fait si le chemin existe et est bien celui de la base de données se nommant "NAMIP.db". Ensuite elle renvoie deux objets : con (objet connexion) et cur (objet curseur qui permet de faire les exécutions SQL) ou None,None si la connexion n'a pas marché.

La deuxième fonction permet de faire les update/insert dans la BD et de sauvegarder ces changements. Elle prend en arguments le con et le cur mais aussi la requête à exécuter ainsi que le tableau des arguments de la requête. Elle utilise la fonction executemany() pour effectuer plusieurs update à partir d'un tableau contenant lui même des tableaux d'arguments.

2 - Script translate.py :

Ce script contient une fonction : translate() et utilise les bibliothèques sqlite3 et google_translate_py.

La fonction translate récupère la descriptions FR,EN et NL de chaque objet présent dans la BD. Elle traduit ensuite les descriptions EN et NL à partir de la description FR si ces deux dernières n'existe pas dans la BD. Elle enregistre ensuite les deux descriptions ainsi que l'ID de l'objet dans un tuple qui est ensuite ajouté dans une liste qui est renvoyé à la fin de l'exécution.

Un script permet d'appeler cette fonction et de faire l'update à partir de la fonction update() du script database.py.

3 - Script keyWord.py :

Ce script contient 3 fonctions : listeAllMotCléPossible(),changementWordbyIndexMotCle() et traiterDescMoClé(), il utilise la bibliothèque sqlite3 et re.

La première fonction permet de récupérer tous les mots clés actuellement possible, à savoir le nom de chaque objet présent dans la BD. Ces mots clés sont ensuite stockées dans une liste avec leur ID et le mots clé en question. La liste est ensuite retournée.

La deuxième fonction permet de modifier une description qui contient des mots clé. Elle prend en argument la description a modifié ainsi que l'ID de l'objet possédant cette description et enfin la liste de tous les mots clé. Elle cherche ensuite pour chaque mot clé si il apparaisse dans la description et remplace ce dernier par |IDMotClé|. Le mot clé n'est pas remplacé si son ID est égal à l'ID de l'objet passé en paramètre.

La troisième fonction permet de traiter le changement de descriptions pour chaque objet de la BD avec un appelle à la fonction changementWordbyMotClé(), les descriptions modifiées sont ensuite ajoutés à une liste avec l'ID de l'objet pour pouvoir ensuite les charger dans la BD. La fonction sauvegarde aussi dans une liste des tuples unique comprenant l'ID de l'objet modifié, l'ID du mot clé ainsi que le mot clé cette liste est aussi renvoyé.

Un script permet d'appeler la première et troisième fonction pour effectuer le traitement. Ensuite un premier appel à la fonction update() du script database.py pour sauvegarder les descriptions et un deuxième pour insérer les mots clé utilisé par chaque description.

4 - Script spreadSheet.py :

Ce script contient 4 fonctions : initTableau(),ajouterData(),saveData() et recupData(), il utilise les bibliothèques sqlite3, openpyxl et pathlib.

La première fonction permet d'initialiser le tableau en créant le fichier Excel et le nom des colonnes en gras. Elle retourne le tableau et la WorkSheet.

La deuxième fonction permet de récupérer les données de la BD et de les ajouter dans la WorskSheet du tableau Excel. Elle prend en paramètre la WorkSheet.

La troisième fonction permet de sauvegarder les changements effectuer dans la WorkSheet. Elle prend en paramètre la WorkSheet et le chemin d'enregistrement du fichier.

La quatrième fonction permet de récupérer les données du fichier Excel, de les mettre dans une liste qui est ensuite retourné pour mettre à jour la BD. Elle prend en paramètre la WorkSheet.

Un script permet ensuite à l'utilisateur de choisir entre écrire dans la BD à partir d'un fichier Excel ou inversement.
Pour le premier cas, on demande à l'utilisateur le chemin de l'Excel, on vérifie que le chemin existe et correspond à un fichier de type .xlsx. Ensuite on charge l'Excel, récupère les données et update la BD avec la fonction update du script database.py.
Pour le deuxième cas, on créé le fichier Excel, on y ajoute les données, et on demande à l'utilisateur où il veut enregistrer le fichier en vérifiant que le chemin données existe et correspond bien à un répertoire et non un fichier. 







