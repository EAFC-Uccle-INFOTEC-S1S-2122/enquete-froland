# Enquête

Le programme que vous allez développer ce soir pose des questions à partir d'un fichier texte et collecte les réponses dans un autre fichier texte.

## Étapes de l'exercice

1. Écrivez une fonction pour poser une question et retourner la réponse sous la forme d'une chaine de caractères.
   La question est passée à la fonction en paramètre sous la forme d'une chaine de caractères.
2. Écrivez une fonction pour demander une confirmation et retourner la réponse sous la forme d'un booléen.
   Cette fonction ne prend pas de paramètre.
3. Écrivez une fonction pour poser plusieurs questions et retourner les réponses après confirmation de l'utilisateur.
   Les questions à poser sont fournies à la fonction sous la forme d'un tableau de chaines de caractères.
   Les réposes sont retournées sous la forme d'un tableau de chaines de caractères.
   Si l'utilisateur ne confirme pas, la fonction repose les mêmes questions et ainsi de suite jusqu'à ce que l'utilisateur confirme.
   Cette fonction utilise les deux première fonctions que vous aurez développées.
4. Écrivez une fonction pour écrire les questions et les réponses dans un fichier texte `reponses.txt`.
   Dans le fichier, on écrit d'abord la question sur une ligne puis la réponse sur la ligne suivante et enfin une ligne vide avant de passer à la question et à la réponse suivante.
   Cette fonction reçoit 2 paramètres : un tableau de questions et un tableau de réponses.
   Elle ne retourne rien.
5. Écrivez une fonction pour lire les questions depuis un fichier texte `questions.txt`.
   Chaque question est écrite sur une seule ligne.
   La fonction ne prend pas de paramètre et retourn un tableau de chaines de caractères.
   Les lignes vides sont ignorées.
6. Écrivez un programme qui utilise les fonctions créées pour :
   1. Lire les questions dans le fichier texte `questions.txt`;
   2. Poser les questions à l'utilisateur, collecter ses réponses et lui demander de confirmer;
   3. Ecrire les questions et les réponses dans le fichier `reponses.txt`.
