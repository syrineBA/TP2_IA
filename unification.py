# Une liste est un atome si elle est vide ou si elle a un seul élément.
def est_atome(expr):
    if len(expr) == 1:
        return True
    return False

# ------------------------------------------------------------------------------------------------------------------

# la methode unifieratomes
def unifieratomes(expr1, expr2):
    e1 = expr1[0]
    e2 = expr2[0]
    # si e1 et e2 sont identiques
    if e1 == e2:
        return ""
    # e1 est une variable
    if e1[0] == "?":
        if e1 in e2:
            return "echec"
        else:
            return e1 + "/" + e2
    # e2 est une variable
    if e2[0] == "?":
        return e2 + "/" + e1
    # e1 et e2 sont des fonctions
    if "(" in e1 and "(" in e2:
        l1 = extract_expression(e1)
        l2 = extract_expression(e2)
        return unifier(l1, l2)
    # echec
    return "echec"


# --------------------------------------------------------------------------------------------------------------------

# elle permet d'extraire e1 en cas ou e1 est une fonction , et la stocker dans la liste l
def extract_expression(e1):
    a = len(e1) - 1
    s = e1[2:a]
    # creation de la liste
    l = list()
    # separer e1 selon le critere ",""
    tab = e1.split(",")
    for i in tab:
        if "(" in i:
            ch = i
            # enlever l'espace
            ch = ch.replace(" ", "")
            ch = ch[1:]
            # ajouter a la liste chaque element
            l.append(ch)
        elif ")" in i:
            ch = i
            ch = ch.replace(" ", "")
            ch = ch.replace(")", "")
            l.append(ch)
    return l

# -------------------------------------------------------------------------------------------------------------------

# Cette méthode permet de changer les occurrences d’une variable par sa substitution.
def changer(t1, z1):
    chg = z1.replace("\\s+", "")
    b = list()
    i = 0
    while i < len(chg):
        b.append(chg[i].split("/"))
        i = i + 1
    j = 0
    k = 0
    while j < len(t1):
        k = 0
        while k < len(b):
            t1[i] = t1[i].replace("\\" + b[k], b[k + 1])
            k = k + 2
        j = j + 1
    return t1


# -------------------------------------------------------------------------------------------------------------------

def change(t1, z1):
    # \s+ permet de Mettre en correspondance un ou plusieurs caractères d’espace blanc.
    chg = z1.split("\s+")
    b = list()
    for i in range(0, len(chg)):
        b.append(chg[i].split("/"))
    if z1 != "":
        for j in range(0, len(t1)):
            for k in range(0, len(b)):
                t1[i] = t1[i].replace(b[k][0], b[k][1])
    return t1


# -------------------------------------------------------------------------------------------------------------------
def unifier(expr1, expr2):
    # tester si l'une des expressions est un atome
    if est_atome(expr1) or est_atome(expr2):
        return unifieratomes(expr1, expr2)
     # recuperer le premier element de la premiere expression
    f1 = expr1[0]
    # sauvegarder les termes non traités de la premiere expression
    del expr1[0]
    t1 = expr1
    # recuperer le premier elemment de la deuxieme expression
    f2 = expr2[0]
    # sauvegarder les termes non traités de la deuxieme expression
    del expr2[0]
    t2 = expr2
    # e1 est une liste qui va contenir l'entete de chaque expression
    e1 = list()
    e1.append(f1)
    e2 = list()
    e2.append(f2)
    # unifier les tetes des deux expressions
    z1 = unifier(e1, e2)
    # echec d'unification
    if z1 == "echec":
        return "echec"
    # application des changements sur les termes non traités des expressions
    g1 = change(t1, z1)
    g2 = change(t2, z1)
    # unifier les termes non traités de deux expressions
    z2 = unifier(g1, g2)
    # echec d'unification
    if z2 == "echec":
        return "echec"
    return z1 + "  " + z2


# -------------------------------------------------------------------------------------------------------------------

def tests():

    e1 = "p(B,C,?x,?z,f(A,?z,B))"
    e2 = "p(?y,?z,?y,C,?w)"
    e3 = "P(?x,f(g(?x)),a)"
    e4 = "P(b,?y,?z)"
    e5 = "q(f(A,?x),?x)"
    e6 = "q(f(?z,f(?z,D)),?z)"
    e7 = "(?x)"
    e8 = "(g(?x))"
    k = extract_expression(e1)
    k1 = extract_expression(e2)
    k2 = extract_expression(e3)
    k3 = extract_expression(e4)
    k4 = extract_expression(e5)
    k5 = extract_expression(e6)
    k6 = extract_expression(e7)
    k7 = extract_expression(e8)

    print("Les exemples de l'enoncé TP2  :\n")
    print("                 * * *                          \n")

    print("Exemple 1:\n")
    print("unifier(p(B,C,?x,?z,f(A,?z,B)),p(?y,?z,?y,C,?w)):\n")
    print(unifier(k, k1))
    print("--------------------------------------------------------- :\n")
    print("Exemple 2:\n")
    print("unifier(P(?x,f(g(?x)),a),P(b,?y,?z)) : \n")
    print(unifier(k2, k3))
    print("--------------------------------------------------------- :\n")
    print("Exemple 3:\n")
    print("unifier(q(f(A,?x),?x),q(f(?z,f(?z,D)),?z)) : \n")
    print(unifier(k4, k5))
    print("--------------------------------------------------------- :\n")
    print("Exemple 4:\n")
    print("unifier((?x),(g(?x)) : \n")
    print(unifier(k6, k7))

    fichier = open("C:/Users/HP/Desktop/traceUnification.txt", "w")
    fichier.write("Exemple 1:\n" + "unifier(p(B,C,?x,?z,f(A,?z,B)),p(?y,?z,?y,C,?w)):\n" +
                  unifier(k, k1) + "\n" + "Exemple 2:\n" + "unifier(P(?x,f(g(?x)),a),P(b,?y,?z)) : \n" +
                  unifier(k2, k3) + "\n" + "Exemple 3:\n" + "unifier(q(f(A,?x),?x),q(f(?z,f(?z,D)),?z)) : \n" +
                  unifier(k4, k5) + "\n" + "Exemple 4:\n" + "unifier((?x),(g(?x)) : \n" +
                  unifier(k6, k7) + "\n")


    print("--------------------------------------------------------- :\n")
    print("Tester d'autres exemples :\n")
    expr1=input('\x1b[50;10;5m' + "expression 1 = " + '\x1b[0m')
    expr2=input('\x1b[50;10;5m' + "expression 2 = " + '\x1b[0m')


    kexp1 = extract_expression(expr1)
    kexp2 = extract_expression(expr2)
    print("Resultat de :\n")
    print("unifier("+expr1+","+expr2+") : \n" )
    print(unifier(kexp1, kexp2))

    fichier.write("Exemple X :\n" + "unifier("+expr1+","+expr2+") : \n" +
                  unifier(kexp1, kexp2) + "\n")

tests()
