print("")
# Jour à trouver. Ecrivez votre date 

jour = 6
mois = 6
an = 3593


print("On va afficher le jour du %d/%d/%d" %(jour,mois,an))

date = [jour,mois,an]

# Ref : 1 mai 2022 : dimache
jour_ref = 1
mois_ref = 5
an_ref = 2022
an_bisextile_ref = 2020 # annee la plus proche en dessous de an
siecle_ref = 2000
# dico de réf attention
jour_sem = {0:"Dimanche", 1:"Lundi", 2:"Mardi", 3:"Mercredi", 4:"Jeudi", 5:"Vendredi", 6:"Samedi"}
Njour_mois = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

def est_multiple_100(n):
  if n % 100 == 0:
    return True
  return False 

def est_multiple_400(n):
  if n % 400 == 0:
    return True
  return False 

def est_multiple_4(n):
  if n % 4 == 0:
    return True
  return False 

def est_bisextile(n): # si multiple de 4 mais pas de 100 ou multiple de 400
  if est_multiple_100(n):
    if est_multiple_400(n):
      return True
  else:
    if est_multiple_4(n):
      return True
  return False 


def print_jour():

  # Combien d'années à compter ?

  N_ans = -(an_ref - an)
  # Signe - car on enlève les jours de la semaine quand an_ref>an
  # La formule marche pour an > .. ou an < ..

  print("Nombre d'années à compter :", N_ans)
                            
  # Années bissextiles ?
  
  if an > an_bisextile_ref:   
    Nbisextile = (an - an_bisextile_ref)//4 
    Nbisextile -= (an - siecle_ref)//100
    Nbisextile += (an - siecle_ref)//400
  else:
    print(1)
    Nbisextile = -((an_bisextile_ref - an)//4 + 1)
    print(Nbisextile)
    Nbisextile += (siecle_ref - an)//100
    Nbisextile -= (siecle_ref - an)//400
    

  if est_bisextile(an)%4 == True : # si c'est une annee bisextile
    print("Année bissextile !")
    if (an_bisextile_ref>an and mois > 2 ):
      Nbisextile += 1 # pas d'effet du mois de février, on a compté un jour en trop donc on enlève en positif
    if (an_bisextile_ref<an and mois < 3 ):
      Nbisextile -= 1 # meme chose on a compté en trop
  
  
  print("Nombre d'années bissextiles impactant la date :",Nbisextile)

  # Saut dû au changement de calendrier en 1582
  # En Europe, le lendemain du jeudi 4 octobre fut le vendredi 15 octobre 1582, donc noter 11 jours
  # (c'est cette version qui est utilisée sur dCode).
  # Si on ne modifie rien ca serait un lundi 4 oct, il faut donc ajouter 3=14-11 jours pour avoir jeudi
  Ngreg = 0
  if an <= 1582 and mois <= 10 :
    if 5 <= jour <= 14:
      print("ATTENTION : jour inexistant, souci du calendrier grégorien à cette époque")
    if jour <= 4:
      Ngreg = 3

  # On s'occupe des mois. Bisextile déjà pris en compte.
  Nmois = 0 #initialisation..

  # Cas 1
  if mois > mois_ref:
    Nmois += Njour_mois[mois_ref] - jour_ref + 1
    for _mois in range(mois_ref+1,mois):
      Nmois += Njour_mois[_mois]
    Nmois += jour-1

  # Cas 2
  elif mois == mois_ref:
    if jour == jour_ref:
      None # Rien à faire
    if jour > jour_ref:
      Nmois += jour - jour_ref
    else:
      Nmois -= jour - jour_ref
  
  # Cas 3
  else:
    Nmois -= Njour_mois[mois] - jour + 1
    for _mois in range(mois+1,mois_ref):
      Nmois -= Njour_mois[_mois]
    Nmois -= jour_ref - 1
  
  # Résultat
  le_jour = jour_sem[(Nbisextile + N_ans + Nmois + Ngreg)%7]

  # Affichage
  print("Le jour cherché est :",le_jour)


print_jour()






print("")