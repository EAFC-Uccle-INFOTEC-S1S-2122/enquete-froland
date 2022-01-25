def poser_question(question):
    return input(question)

def confirmer():
    confirmation = input("Confirmez-vous vos choix ? (o/n)")
    return confirmation == "o"

def poser_questions_jusqua_confirmation(questions):
    reponses = []
    for question in questions:
        reponse = poser_question(question)
        reponses.append(reponse)
    confirmation_recue = confirmer()
    if confirmation_recue:
        return reponses
    else:
        return poser_questions_jusqua_confirmation(questions)

def ecrire_reponses(questions, reponses):
    with open("reponses.txt", "w", encoding="utf-8") as fichier_reponse:
        for i in range(len(questions)):
            ma_question = questions[i]
            ma_reponse = reponses[i]
            fichier_reponse.write(ma_question)
            fichier_reponse.write(ma_reponse + "\n")
            fichier_reponse.write("\n")

def lire_questions():
    questions = []
    with open("questions.txt", "r", encoding="utf-8") as fichier_questions:
        for ligne in fichier_questions:
            questions.append(ligne)
    return questions


mes_questions = lire_questions()
mes_reponses = poser_questions_jusqua_confirmation(mes_questions)
ecrire_reponses(mes_questions, mes_reponses)
