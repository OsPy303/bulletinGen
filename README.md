# bulletinGen
C'est un programme qui calcule et genere des bulletin de nots d'une classe
à partir des fichier excel contenant les notes des eleves separé dans 
des fichier excel par matiere comme dans le dossier "note_prelmiere_a1"
en utilisant pandas et utilise pdfkit pour generer les bulletin dans un 
fichier pdf à partir d'un fichier html generé par le programme.

requirement:
Pandas
pdfkit

dependece:
wkhtmltopdf
  installation:
    -Ubuntu: sudo apt-get install wkhtmltopdf
    -Windows: installer l'executable das le dossier requirements
    et si necéssaire ajouter l'excécutable du fichier installé dans 
    le variable d'environnement windows
