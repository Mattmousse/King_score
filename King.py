class JeuDeCartes:
    def __init__(self, nombre_joueurs):
        self.nombre_joueurs = nombre_joueurs
        self.points_totaux = 510
        self.points_par_manche = self.points_totaux // 5

    def repartir_points(self):
        # Initialiser les points pour chaque catégorie
        points_hommes = 0
        points_dames = 0
        points_derniers_plis = 0
        points_roi_de_coeur = 0
        points_coeurs = 0
        points_plis = 0

        # Déterminer le nombre de plis
        if self.nombre_joueurs == 3:
            nombre_de_plis = 17
        elif self.nombre_joueurs == 4:
            nombre_de_plis = 13
            
        else:
            nombre_de_plis = 0  # Ajuster selon les règles spécifiques

        # Calculer les points pour chaque catégorie
        points_hommes = self.points_par_manche * 0.2  # Exemple de ratio
        points_dames = self.points_par_manche * 0.15
        points_derniers_plis = self.points_par_manche * 0.1
        points_roi_de_coeur = self.points_par_manche * 0.05
        points_coeurs = self.points_par_manche * 0.2
        points_plis = self.points_par_manche * 0.3

        # Ajuster les points pour respecter le total de 102 points par manche
        total_points_calcules = (points_hommes + points_dames + points_derniers_plis +
                                 points_roi_de_coeur + points_coeurs + points_plis)

        if total_points_calcules != self.points_par_manche:
            difference = self.points_par_manche - total_points_calcules
            points_plis += difference  # Ajuster les points des plis pour compenser

        return {
            "hommes": points_hommes,
            "dames": points_dames,
            "derniers_plis": points_derniers_plis,
            "roi_de_coeur": points_roi_de_coeur,
            "coeurs": points_coeurs,
            "plis": points_plis
        }

# Exemple d'utilisation
nombre_joueurs = 3
jeu = JeuDeCartes(nombre_joueurs)
repartition_points = jeu.repartir_points()
print(f"Répartition des points pour {nombre_joueurs} joueurs : {repartition_points}")
