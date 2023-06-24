import time
import copy
import pygame
import sys
import random


class Joc:
    """
    Clasa care defineste jocul.
    """

    NR_COLOANE = 8
    JMIN = None
    JMAX = None
    GOL = "#"

    @classmethod
    def initializeaza(cls, display, NR_COLOANE=8, dim_celula=70):
        cls.display = display
        cls.dim_celula = dim_celula
        cls.n_img = pygame.image.load("black_circle.png")
        cls.n_img = pygame.transform.scale(cls.n_img, (dim_celula, dim_celula))
        cls.n_S_img = pygame.image.load("black_circle_selected.png")
        cls.n_S_img = pygame.transform.scale(cls.n_S_img, (dim_celula, dim_celula))

        cls.a_img = pygame.image.load("white_circle.png")
        cls.a_img = pygame.transform.scale(cls.a_img, (dim_celula, dim_celula))
        cls.a_S_img = pygame.image.load("white_circle_selected.png")
        cls.a_S_img = pygame.transform.scale(cls.a_S_img, (dim_celula, dim_celula))

        cls.N_img = pygame.image.load("black_circle_R.png")
        cls.N_img = pygame.transform.scale(cls.N_img, (dim_celula, dim_celula))
        cls.N_S_img = pygame.image.load("black_circle_R_selected.png")
        cls.N_S_img = pygame.transform.scale(cls.N_S_img, (dim_celula, dim_celula))

        cls.A_img = pygame.image.load("white_circle_R.png")
        cls.A_img = pygame.transform.scale(cls.A_img, (dim_celula, dim_celula))
        cls.A_S_img = pygame.image.load("white_circle_R_selected.png")
        cls.A_S_img = pygame.transform.scale(cls.A_S_img, (dim_celula, dim_celula))

        cls.celuleGrid = []  # este lista cu patratelele din grid
        for linie in range(NR_COLOANE):
            for coloana in range(NR_COLOANE):
                patr = pygame.Rect(
                    coloana * (dim_celula + 1),
                    linie * (dim_celula + 1),
                    dim_celula,
                    dim_celula,
                )
                cls.celuleGrid.append(patr)

    def deseneaza_grid(self, i = -1, j = -1):
        """
        Se deseneaza o tabla de sah de 8x8. Se schimba aspectul piesei pe care se face click.
        Pentru fiecare casuta, in matricea starii, exista fie valoare 'GOL', fie culoarea piesei
        :param i: linia piesei pe care s-a efectuat click-ul
        :param j: coloana piesei pe care s-a efectuat click-ul
        :return:
        """
        for ind in range(len(self.matr)):
            linie = ind // Joc.NR_COLOANE
            coloana = ind % Joc.NR_COLOANE

            if (linie + coloana) % 2 == 0:
                culoare = (255, 255, 255)
            else:
                culoare = (0, 0, 0)
            pygame.draw.rect(
                self.__class__.display, culoare, self.__class__.celuleGrid[ind]
            )
            if self.matr[ind] == "n":
                if ind == i * Joc.NR_COLOANE + j:
                    self.__class__.display.blit(
                        self.__class__.n_S_img,
                        (
                            coloana * (self.__class__.dim_celula + 1),
                            linie * (self.__class__.dim_celula + 1),
                        ),
                    )
                else:
                    self.__class__.display.blit(
                        self.__class__.n_img,
                        (
                            coloana * (self.__class__.dim_celula + 1),
                            linie * (self.__class__.dim_celula + 1),
                        ),
                    )
            elif self.matr[ind] == "a":
                if ind == i * Joc.NR_COLOANE + j:
                    self.__class__.display.blit(
                        self.__class__.a_S_img,
                        (
                            coloana * (self.__class__.dim_celula + 1),
                            linie * (self.__class__.dim_celula + 1),
                        ),
                    )
                else:
                    self.__class__.display.blit(
                        self.__class__.a_img,
                        (
                            coloana * (self.__class__.dim_celula + 1),
                            linie * (self.__class__.dim_celula + 1),
                        ),
                    )
            elif self.matr[ind] == "N":
                if ind == i * Joc.NR_COLOANE + j:
                    self.__class__.display.blit(
                        self.__class__.N_S_img,
                        (
                            coloana * (self.__class__.dim_celula + 1),
                            linie * (self.__class__.dim_celula + 1),
                        ),
                    )
                else:
                    self.__class__.display.blit(
                        self.__class__.N_img,
                        (
                            coloana * (self.__class__.dim_celula + 1),
                            linie * (self.__class__.dim_celula + 1),
                        ),
                    )
            elif self.matr[ind] == "A":
                if ind == i * Joc.NR_COLOANE + j:
                    self.__class__.display.blit(
                        self.__class__.A_S_img,
                        (
                            coloana * (self.__class__.dim_celula + 1),
                            linie * (self.__class__.dim_celula + 1),
                        ),
                    )
                else:
                    self.__class__.display.blit(
                        self.__class__.A_img,
                        (
                            coloana * (self.__class__.dim_celula + 1),
                            linie * (self.__class__.dim_celula + 1),
                        ),
                    )
        pygame.display.flip()

    def __init__(self, tabla=None):
        if tabla is not None:
            self.matr = tabla
        else:
            self.matr = [Joc.GOL, 'n', Joc.GOL, 'n', Joc.GOL, 'n', Joc.GOL, 'n',
                         'n', Joc.GOL, 'n', Joc.GOL, 'n', Joc.GOL, 'n', Joc.GOL,
                         Joc.GOL, 'n', Joc.GOL, 'n', Joc.GOL, 'n', Joc.GOL, 'n',
                         Joc.GOL, Joc.GOL, Joc.GOL, Joc.GOL, Joc.GOL, Joc.GOL, Joc.GOL, Joc.GOL,
                         Joc.GOL, Joc.GOL, Joc.GOL, Joc.GOL, Joc.GOL, Joc.GOL, Joc.GOL, Joc.GOL,
                         'a', Joc.GOL, 'a', Joc.GOL, 'a', Joc.GOL, 'a', Joc.GOL,
                         Joc.GOL, 'a', Joc.GOL, 'a', Joc.GOL, 'a', Joc.GOL, 'a',
                         'a', Joc.GOL, 'a', Joc.GOL, 'a', Joc.GOL, 'a', Joc.GOL]

    @classmethod
    def jucator_opus(cls, jucator):
        if jucator == cls.JMIN:
            return cls.JMAX
        else:
            return cls.JMIN

    def final(self):
        """
        :return: false daca ambii jucatori mai au mutari disponibile, "remiza" daca fiecare jucator are
        cate un singur rege, sau castigatorul, daca este cazul
        """
        aux = copy.deepcopy(self.matr)
        castigator = fara_mutari(aux)
        piese_JMIN = 0
        piese_JMAX = 0
        piese_JMIN_R = 0
        piese_JMAX_R = 0
        for i in self.matr:
            if i == self.JMIN or i.lower() == self.JMIN:
                piese_JMIN += 1
                if i == self.JMIN.upper():
                    piese_JMIN_R += 1
            if i == self.JMAX or i.lower() == self.JMAX:
                piese_JMAX += 1
                if i == self.JMAX.upper():
                    piese_JMAX_R += 1
        if piese_JMIN == piese_JMAX == 1 and piese_JMIN_R == piese_JMAX_R:
            return "remiza"
        return castigator

    def mutari(self, jucator):
        """
        Pentru fiecare piesa a jucatorului se apeleaza mutare_simpla() si mutare_compusa(), cu observatia ca
        daca exista mutari compuse care pot fi efectuate, atunci mutarile simple nu mai sunt valide, deci nu sunt
        returnate in lista de mutari
        :param jucator: JMIN sau JMAX ('a' sau 'n')
        :return: lista de configuratii posibile ale tablei dupa aceasta mutare
        """
        l_mutari = []
        l_mutari_fortate = []
        for i in range(Joc.NR_COLOANE):
            for j in range(Joc.NR_COLOANE):
                if self.matr[i * Joc.NR_COLOANE + j].lower() == jucator:
                    aux = copy.deepcopy(self.matr)
                    for mutare in mutare_compusa(i, j, aux):
                        l_mutari_fortate.append(Joc(mutare[2]))
                    if not mutare_compusa(i, j, copy.deepcopy(self.matr)):
                        for mutare in mutare_simpla(i, j, self.matr):
                            copie_matr = copy.deepcopy(self.matr)
                            copie_matr[i * Joc.NR_COLOANE + j] = Joc.GOL
                            copie_matr[mutare[0] * Joc.NR_COLOANE + mutare[1]] = self.matr[i * Joc.NR_COLOANE + j]
                            if mutare[0] == 0 or mutare[0] == Joc.NR_COLOANE - 1:
                                copie_matr[mutare[0] * Joc.NR_COLOANE + mutare[1]] = \
                                    copie_matr[mutare[0] * Joc.NR_COLOANE + mutare[1]].upper()
                            l_mutari.append(Joc(copie_matr))
        if l_mutari_fortate:
            return l_mutari_fortate
        return l_mutari

    def numar_piese(self, estimare=1):
        """

        :return: Un tuplu cu numarul de piese ale lui JMAX si ale lui JMIN
        """
        piese_JMIN = 0
        piese_JMAX = 0
        zona_JMIN = 1
        zona_JMAX = 9
        if self.JMIN == 'a':
            zona_JMIN = 9
            zona_JMAX = 1

        index = 0
        for i in self.matr:
            if estimare == 1:
                if i == self.JMIN or i.lower() == self.JMIN:
                    piese_JMIN += 1
                if i == self.JMAX or i.lower() == self.JMAX:
                    piese_JMAX += 1
            elif estimare == 2:
                if i == self.JMIN or i.lower() == self.JMIN:
                    piese_JMIN += 1
                if i == self.JMAX or i.lower() == self.JMAX:
                    piese_JMAX += 1
            else:
                if i == self.JMIN:
                    piese_JMIN += 5 + abs((index // 9 + 1) - zona_JMIN) + 1
                elif i == self.JMIN.upper():
                    piese_JMIN += 16
                if i == self.JMAX:
                    piese_JMAX += 5 + abs((index // 9 + 1) - zona_JMAX) + 1
                elif i == self.JMAX.upper():
                    piese_JMAX += 16
                index += 1
        return piese_JMAX, piese_JMIN

    def estimeaza_scor(self, adancime, metoda):
        t_final = self.final()
        if t_final == self.__class__.JMAX:
            return 99999999 + adancime
        elif t_final == self.__class__.JMIN:
            return -99999999 - adancime
        elif t_final == 'remiza':
            return 0
        else:
            piese_JMAX, piese_JMIN = self.numar_piese(metoda)
            '''
            Estimarea 1: Pentru fiecare mutare posibila a lui JMAX adaug 1 + numarul de piese pe care le
            va putea captura in pasul urmator, si scad 1 + numarul de piese pe care JMIN le va putea captura 
            Estimarea 2: Numarul de piese pe care le are JMAX in plus fata de JMIN
            Estimarea 3: Atribui scoruri pentru piese: 5 + numarul liniei pentru un simplu pion si 16 pentru rege. 
            Suma scorurilor calculatorului minus suma jucatorului este estimarea
            '''
            if metoda == 1:
                scor = 0
                for m in self.mutari(self.__class__.JMAX):
                    scor += 1 + (piese_JMIN - m.numar_piese()[1])
                for m in self.mutari(self.__class__.JMIN):
                    scor -= 1 - (piese_JMAX - m.numar_piese()[0])
                return scor
            else:
                return piese_JMAX - piese_JMIN


class Stare:
    """
    Clasa folosita de algoritmii minimax si alpha-beta
    O instanta din clasa stare este un nod din arborele minimax
    Are ca proprietate tabla de joc
    Functioneaza cu conditia ca in cadrul clasei Joc sa fie definiti JMIN si JMAX (cei doi jucatori posibili)
    De asemenea cere ca in clasa Joc sa fie definita si o metoda numita mutari() care ofera lista cu configuratiile
    posibile in urma mutarii unui jucator
    """

    def __init__(self, tabla_joc, j_curent, adancime, parinte=None, estimare=None):
        self.tabla_joc = tabla_joc
        self.j_curent = j_curent

        # adancimea in arborele de stari
        self.adancime = adancime

        # estimarea favorabilitatii starii (daca e finala) sau al celei mai bune stari-fiice (pentru jucatorul curent)
        self.estimare = estimare

        # lista de mutari posibile (tot de tip Stare) din starea curenta
        self.mutari_posibile = []

        # cea mai buna mutare din lista de mutari posibile pentru jucatorul curent
        # e de tip Stare (cel mai bun succesor)
        self.stare_aleasa = None

    def mutari(self):
        # lista de informatii din nodurile succesoare
        l_mutari = self.tabla_joc.mutari(self.j_curent)

        juc_opus = Joc.jucator_opus(self.j_curent)

        # mai jos calculam lista de noduri-fii (succesori)
        l_stari_mutari = [
            Stare(mutare, juc_opus, self.adancime - 1, parinte=self)
            for mutare in l_mutari
        ]
        return l_stari_mutari


def mutare_simpla(i, j, lista):
    """
    O mutare simpla este mutarea cu o casuta pe diagonala, fara capturi
    :param i: linia pe care se afla piesa
    :param j: coloana pe care se afla piesa
    :param lista: configuratia tablei in momentul curent
    :return: o lista cu toate pozitiile in care se poate muta piesa
    """
    m = []

    if lista[i * Joc.NR_COLOANE + j] == 'n':
        """
        Mutare piesă neagră
        """
        if 0 <= j - 1 <= 7 and 0 <= (i + 1) * Joc.NR_COLOANE + j - 1 < 64 and lista[
            (i + 1) * Joc.NR_COLOANE + j - 1] == Joc.GOL:
            m.append((i + 1, j - 1))
        if 0 <= j + 1 <= 7 and 0 <= (i + 1) * Joc.NR_COLOANE + j + 1 < 64 and lista[
            (i + 1) * Joc.NR_COLOANE + j + 1] == Joc.GOL:
            m.append((i + 1, j + 1))

    if lista[i * Joc.NR_COLOANE + j] == 'a':
        """
        Mutare piesă albă
        """
        if 0 <= j - 1 <= 7 and 0 <= (i - 1) * Joc.NR_COLOANE + j - 1 < 64 and lista[
            (i - 1) * Joc.NR_COLOANE + j - 1] == Joc.GOL:
            m.append((i - 1, j - 1))
        if 0 <= j + 1 <= 7 and 0 <= (i - 1) * Joc.NR_COLOANE + j + 1 < 64 and lista[
            (i - 1) * Joc.NR_COLOANE + j + 1] == Joc.GOL:
            m.append((i - 1, j + 1))

    if lista[i * Joc.NR_COLOANE + j] == 'A' or lista[i * Joc.NR_COLOANE + j] == 'N':
        """
        Mutare damă, culoarea nu mai are relevanţă pentru direcţie
        """
        if 0 <= j - 1 <= 7 and 0 <= (i + 1) * Joc.NR_COLOANE + j - 1 < 64 and lista[
            (i + 1) * Joc.NR_COLOANE + j - 1] == Joc.GOL:
            m.append((i + 1, j - 1))
        if 0 <= j + 1 <= 7 and 0 <= (i + 1) * Joc.NR_COLOANE + j + 1 < 64 and lista[
            (i + 1) * Joc.NR_COLOANE + j + 1] == Joc.GOL:
            m.append((i + 1, j + 1))
        if 0 <= j - 1 <= 7 and 0 <= (i - 1) * Joc.NR_COLOANE + j - 1 < 64 and lista[
            (i - 1) * Joc.NR_COLOANE + j - 1] == Joc.GOL:
            m.append((i - 1, j - 1))
        if 0 <= j + 1 <= 7 and 0 <= (i - 1) * Joc.NR_COLOANE + j + 1 < 64 and lista[
            (i - 1) * Joc.NR_COLOANE + j + 1] == Joc.GOL:
            m.append((i - 1, j + 1))

    return m


def mutare_compusa(i, j, lista):
    """
    O mutare compusă se referă la mutările care fac capturi. Am modelat o astfel de mişcare ca o functie recursiva
    care simulează câte o captură. În momentul în care există căi diferite de captură, această funcţie traversează
    fiecare cale şi adaugă la lista de întoarcere configuraţia finală în cazul fiecărei mutări compuse.
    :param i: linia pe care se află piesa
    :param j: coloana pe care se află piesa
    :param lista: configuraţia tablei la un moment dat
    :return: o listă de tupluri de forma (linia nouă a piesei, coloana nouă a piesei, noua configuraţie a tablei)
    """
    m = []

    if lista[i * Joc.NR_COLOANE + j] == 'n':
        """
        Mutare piesă neagră, cu captură a unei piese albe
        """
        if 0 <= j - 2 <= 7 and 0 <= (i + 2) * Joc.NR_COLOANE + j - 2 < 64 and lista[
            (i + 2) * Joc.NR_COLOANE + j - 2] == Joc.GOL:
            if lista[(i + 1) * Joc.NR_COLOANE + j - 1] not in [Joc.GOL, lista[i * Joc.NR_COLOANE + j],
                                                               lista[i * Joc.NR_COLOANE + j].upper()]:
                aux = copy.deepcopy(lista)
                aux[(i + 1) * Joc.NR_COLOANE + j - 1] = Joc.GOL
                aux[(i + 2) * Joc.NR_COLOANE + j - 2] = lista[i * Joc.NR_COLOANE + j]
                if i + 2 == Joc.NR_COLOANE - 1:
                    aux[(i + 2) * Joc.NR_COLOANE + j - 2] = aux[(i + 2) * Joc.NR_COLOANE + j - 2].upper()
                aux[i * Joc.NR_COLOANE + j] = Joc.GOL
                if not mutare_compusa(i + 2, j - 2, aux) or i + 2 == Joc.NR_COLOANE - 1:
                    m.append((i + 2, j - 2, aux))
                else:
                    m.extend(mutare_compusa(i + 2, j - 2, aux))
        if 0 <= j + 2 <= 7 and 0 <= (i + 2) * Joc.NR_COLOANE + j + 2 < 64 and lista[
            (i + 2) * Joc.NR_COLOANE + j + 2] == Joc.GOL:
            if lista[(i + 1) * Joc.NR_COLOANE + j + 1] not in [Joc.GOL, lista[i * Joc.NR_COLOANE + j],
                                                               lista[i * Joc.NR_COLOANE + j].upper()]:
                aux = copy.deepcopy(lista)
                aux[(i + 1) * Joc.NR_COLOANE + j + 1] = Joc.GOL
                aux[(i + 2) * Joc.NR_COLOANE + j + 2] = lista[i * Joc.NR_COLOANE + j]
                if i + 2 == Joc.NR_COLOANE - 1:
                    aux[(i + 2) * Joc.NR_COLOANE + j + 2] = aux[(i + 2) * Joc.NR_COLOANE + j + 2].upper()
                aux[i * Joc.NR_COLOANE + j] = Joc.GOL
                if not mutare_compusa(i + 2, j + 2, aux) or i + 2 == Joc.NR_COLOANE - 1:
                    m.append((i + 2, j + 2, aux))
                else:
                    m.extend(mutare_compusa(i + 2, j + 2, aux))
    elif lista[i * Joc.NR_COLOANE + j] == 'a':
        if 0 <= j - 2 <= 7 and 0 <= (i - 2) * Joc.NR_COLOANE + j - 2 < 64 and lista[
            (i - 2) * Joc.NR_COLOANE + j - 2] == Joc.GOL:
            if lista[(i - 1) * Joc.NR_COLOANE + j - 1] not in [Joc.GOL, lista[i * Joc.NR_COLOANE + j],
                                                               lista[i * Joc.NR_COLOANE + j].upper()]:
                aux = copy.deepcopy(lista)
                aux[(i - 1) * Joc.NR_COLOANE + j - 1] = Joc.GOL
                aux[(i - 2) * Joc.NR_COLOANE + j - 2] = lista[i * Joc.NR_COLOANE + j]
                if i - 2 == 0:
                    aux[(i - 2) * Joc.NR_COLOANE + j - 2] = aux[(i - 2) * Joc.NR_COLOANE + j - 2].upper()
                aux[i * Joc.NR_COLOANE + j] = Joc.GOL
                if not mutare_compusa(i - 2, j - 2, aux) or i - 2 == 0:
                    m.append((i - 2, j - 2, aux))
                else:
                    m.extend(mutare_compusa(i - 2, j - 2, aux))
        if 0 <= j + 2 <= 7 and 0 <= (i - 2) * Joc.NR_COLOANE + j + 2 < 64 and lista[
            (i - 2) * Joc.NR_COLOANE + j + 2] == Joc.GOL:
            if lista[(i - 1) * Joc.NR_COLOANE + j + 1] not in [Joc.GOL, lista[i * Joc.NR_COLOANE + j],
                                                               lista[i * Joc.NR_COLOANE + j].upper()]:
                aux = copy.deepcopy(lista)
                aux[(i - 1) * Joc.NR_COLOANE + j + 1] = Joc.GOL
                aux[(i - 2) * Joc.NR_COLOANE + j + 2] = lista[i * Joc.NR_COLOANE + j]
                if i - 2 == 0:
                    aux[(i - 2) * Joc.NR_COLOANE + j + 2] = aux[(i - 2) * Joc.NR_COLOANE + j + 2].upper()
                aux[i * Joc.NR_COLOANE + j] = Joc.GOL
                if not mutare_compusa(i - 2, j + 2, aux) or i - 2 == 0:
                    m.append((i - 2, j + 2, aux))
                else:
                    m.extend(mutare_compusa(i - 2, j + 2, aux))
    elif lista[i * Joc.NR_COLOANE + j] == 'A' or lista[i * Joc.NR_COLOANE + j] == 'N':
        if 0 <= j - 2 <= 7 and 0 <= (i + 2) * Joc.NR_COLOANE + j - 2 < 64 and lista[
            (i + 2) * Joc.NR_COLOANE + j - 2] == Joc.GOL:
            if lista[(i + 1) * Joc.NR_COLOANE + j - 1] not in [Joc.GOL, lista[i * Joc.NR_COLOANE + j],
                                                               lista[i * Joc.NR_COLOANE + j].lower()]:
                aux = copy.deepcopy(lista)
                aux[(i + 1) * Joc.NR_COLOANE + j - 1] = Joc.GOL
                aux[(i + 2) * Joc.NR_COLOANE + j - 2] = lista[i * Joc.NR_COLOANE + j]
                aux[i * Joc.NR_COLOANE + j] = Joc.GOL
                if not mutare_compusa(i + 2, j - 2, aux):
                    m.append((i + 2, j - 2, aux))
                else:
                    m.extend(mutare_compusa(i + 2, j - 2, aux))
        if 0 <= j + 2 <= 7 and 0 <= (i + 2) * Joc.NR_COLOANE + j + 2 < 64 and lista[
            (i + 2) * Joc.NR_COLOANE + j + 2] == Joc.GOL:
            if lista[(i + 1) * Joc.NR_COLOANE + j + 1] not in [Joc.GOL, lista[i * Joc.NR_COLOANE + j],
                                                               lista[i * Joc.NR_COLOANE + j].lower()]:
                aux = copy.deepcopy(lista)
                aux[(i + 1) * Joc.NR_COLOANE + j + 1] = Joc.GOL
                aux[(i + 2) * Joc.NR_COLOANE + j + 2] = lista[i * Joc.NR_COLOANE + j]
                aux[i * Joc.NR_COLOANE + j] = Joc.GOL
                if not mutare_compusa(i + 2, j + 2, aux):
                    m.append((i + 2, j + 2, aux))
                else:
                    m.extend(mutare_compusa(i + 2, j + 2, aux))
        if 0 <= j - 2 <= 7 and 0 <= (i - 2) * Joc.NR_COLOANE + j - 2 < 64 and lista[
            (i - 2) * Joc.NR_COLOANE + j - 2] == Joc.GOL:
            if lista[(i - 1) * Joc.NR_COLOANE + j - 1] not in [Joc.GOL, lista[i * Joc.NR_COLOANE + j],
                                                               lista[i * Joc.NR_COLOANE + j].lower()]:
                aux = copy.deepcopy(lista)
                aux[(i - 1) * Joc.NR_COLOANE + j - 1] = Joc.GOL
                aux[(i - 2) * Joc.NR_COLOANE + j - 2] = lista[i * Joc.NR_COLOANE + j]
                aux[i * Joc.NR_COLOANE + j] = Joc.GOL
                if not mutare_compusa(i - 2, j - 2, aux) or i - 2 == 0:
                    m.append((i - 2, j - 2, aux))
                else:
                    m.extend(mutare_compusa(i - 2, j - 2, aux))
        if 0 <= j + 2 <= 7 and 0 <= (i - 2) * Joc.NR_COLOANE + j + 2 < 64 and lista[
            (i - 2) * Joc.NR_COLOANE + j + 2] == Joc.GOL:
            if lista[(i - 1) * Joc.NR_COLOANE + j + 1] not in [Joc.GOL, lista[i * Joc.NR_COLOANE + j],
                                                               lista[i * Joc.NR_COLOANE + j].lower()]:
                aux = copy.deepcopy(lista)
                aux[(i - 1) * Joc.NR_COLOANE + j + 1] = Joc.GOL
                aux[(i - 2) * Joc.NR_COLOANE + j + 2] = lista[i * Joc.NR_COLOANE + j]
                aux[i * Joc.NR_COLOANE + j] = Joc.GOL
                if not mutare_compusa(i - 2, j + 2, aux):
                    m.append((i - 2, j + 2, aux))
                else:
                    m.extend(mutare_compusa(i - 2, j + 2, aux))
    return m


def fara_mutari(lista):
    """
    O functie simpla care verifica daca exista vreun jucator care nu mai poate muta nicio piesa.
    Testeaza implicit si cazul in care jucatorul nu mai are nicio piesa pe tabla.
    :param lista: configuratia tablei
    :return: false daca ambii jucatori mai au mutari disponibile, sau castigatorul, daca este cazul
    """
    mutari_n = 0
    mutari_a = 0
    for i in range(Joc.NR_COLOANE):
        for j in range(Joc.NR_COLOANE):
            if lista[i * Joc.NR_COLOANE + j] in 'nN':
                mutari_n += len(mutare_simpla(i, j, lista)) + len(mutare_compusa(i, j, copy.deepcopy(lista)))
            elif lista[i * Joc.NR_COLOANE + j] in 'aA':
                mutari_a += len(mutare_simpla(i, j, lista)) + len(mutare_compusa(i, j, copy.deepcopy(lista)))
    if mutari_a == 0:
        return 'n'
    if mutari_n == 0:
        return 'a'
    return False


""" 
Algoritmul MinMax 
"""


def min_max(stare, NODURI_CURENT, metoda=1):
    NODURI_CURENT += 1
    # daca sunt la o frunza in arborele minimax sau la o stare finala
    if stare.adancime == 0 or stare.tabla_joc.final():
        stare.estimare = stare.tabla_joc.estimeaza_scor(stare.adancime, metoda)
        return stare, NODURI_CURENT

    # calculez toate mutarile posibile din starea curenta
    stare.mutari_posibile = stare.mutari()

    # aplic algoritmul minimax pe toate mutarile posibile (calculand astfel subarborii lor)
    mutariCuEstimare = [
        min_max(x, NODURI_CURENT)[0] for x in stare.mutari_posibile
    ]  # expandez(constr subarb) fiecare nod x din mutari posibile
    if stare.j_curent == Joc.JMAX:
        # daca jucatorul e JMAX aleg starea-fiica cu estimarea maxima
        stare.stare_aleasa = max(mutariCuEstimare, key=lambda x: x.estimare)
    else:
        # daca jucatorul e JMIN aleg starea-fiica cu estimarea minima
        stare.stare_aleasa = min(mutariCuEstimare, key=lambda x: x.estimare)

    stare.estimare = stare.stare_aleasa.estimare
    return stare, NODURI_CURENT


def alpha_beta(alpha, beta, stare, NODURI_CURENT, metoda=1):
    NODURI_CURENT += 1
    if stare.adancime == 0 or stare.tabla_joc.final():
        stare.estimare = stare.tabla_joc.estimeaza_scor(stare.adancime, metoda)
        return stare, NODURI_CURENT

    if alpha > beta:
        return stare, NODURI_CURENT  # este intr-un interval invalid deci nu o mai procesez

    stare.mutari_posibile = stare.mutari()

    if stare.j_curent == Joc.JMAX:
        estimare_curenta = float("-inf")

        for mutare in stare.mutari_posibile:
            # calculeaza estimarea pentru starea noua, realizand subarborele
            stare_noua, NODURI_CURENT = alpha_beta(
                alpha, beta, mutare, NODURI_CURENT
            )  # aici construim subarborele pentru stare_noua

            if estimare_curenta < stare_noua.estimare:
                stare.stare_aleasa = stare_noua
                estimare_curenta = stare_noua.estimare

            if alpha < stare_noua.estimare:
                alpha = stare_noua.estimare
                if alpha >= beta:
                    break

    elif stare.j_curent == Joc.JMIN:
        estimare_curenta = float("inf")

        for mutare in stare.mutari_posibile:

            stare_noua, NODURI_CURENT = alpha_beta(
                alpha, beta, mutare, NODURI_CURENT
            )  # aici construim subarborele pentru stare_noua

            if estimare_curenta > stare_noua.estimare:
                stare.stare_aleasa = stare_noua
                estimare_curenta = stare_noua.estimare
            if beta > stare_noua.estimare:
                beta = stare_noua.estimare
                if alpha >= beta:
                    break

    stare.estimare = stare.stare_aleasa.estimare
    return stare, NODURI_CURENT


def game_over(stare_curenta):

    final = stare_curenta.tabla_joc.final()
    if final:
        if final == "remiza":
            print("Remiza!")
        else:
            print("A castigat " + final)
        return True

    return False


def main():
    metoda = 3
    global t_star, tip_algoritm
    t_start = int(round(time.time() * 1000))
    # initializare algoritm
    global linie1, coloana1, linie2, coloana2
    NR_NODURI_PER_MUTARE = []

    calc_timp_minim = 99999999999999
    calc_timp_maxim = 0
    calc_timp_total = 0
    calc_mutari = 0
    calc_timpi = []
    juc_mutari = 0
    raspuns_valid = False

    while not raspuns_valid:
        tip_algoritm = input(
            "Algoritmul folosit? (raspundeti cu 1 sau 2)\n 1.Minimax\n 2.Alpha-beta\n "
        )
        if tip_algoritm in ["1", "2"]:
            raspuns_valid = True
        else:
            print("Nu ati ales o varianta corecta.")

    raspuns_valid = False
    global ADANCIME_MAX
    while not raspuns_valid:
        dificultate = input("Ce dificultate doriti? Variante: usor(u), mediu(m) sau dificil(d)").lower()
        if dificultate == 'u':
            raspuns_valid = True
            ADANCIME_MAX = 4
        elif dificultate == 'm':
            raspuns_valid = True
            ADANCIME_MAX = 5
        elif dificultate == 'd':
            raspuns_valid = True
            ADANCIME_MAX = 7
        else:
            print("Raspunsul trebuie sa fie usor(u), mediu(m) sau dificil(d).")
    # initializare jucatori
    raspuns_valid = False
    while not raspuns_valid:
        Joc.JMIN = input("Doriti sa jucati cu alb(a) sau cu negru(n)? ").lower()
        if Joc.JMIN in ["a", "n"]:
            raspuns_valid = True
        else:
            print("Raspunsul trebuie sa fie alb(a) sau negru(n).")
    Joc.JMAX = "n" if Joc.JMIN == "a" else "a"
    # expresie= val_true if conditie else val_false  (conditie? val_true: val_false)

    # initializare tabla
    tabla_curenta = Joc()

    # creare stare initiala
    stare_curenta = Stare(tabla_curenta, "n", ADANCIME_MAX)

    pygame.init()
    pygame.display.set_caption("Ganea Carina - Dame")

    ecran = pygame.display.set_mode(size=(567, 567))  # N *70+ N-1
    Joc.initializeaza(ecran)

    tabla_curenta.deseneaza_grid()
    clicks = []
    while not game_over(stare_curenta):

        if len(clicks) == 1:
            stare_curenta.tabla_joc.deseneaza_grid(clicks[0][0], clicks[0][1])
        else:
            stare_curenta.tabla_joc.deseneaza_grid()
        if stare_curenta.j_curent == Joc.JMIN:
            # muta jucatorul
            print("Acum muta utilizatorul cu simbolul", stare_curenta.j_curent)
            t_inainte = int(round(time.time() * 1000))
            raspuns_valid = False
            while not raspuns_valid:
                if len(clicks) == 1:
                    stare_curenta.tabla_joc.deseneaza_grid(clicks[0][0], clicks[0][1])
                else:
                    stare_curenta.tabla_joc.deseneaza_grid()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()  # coordonatele clickului
                        for np in range(len(Joc.celuleGrid)):
                            if Joc.celuleGrid[np].collidepoint(pos):
                                linie1 = np // Joc.NR_COLOANE
                                coloana1 = np % Joc.NR_COLOANE
                                if stare_curenta.tabla_joc.matr[linie1 * Joc.NR_COLOANE + coloana1].lower() != Joc.JMIN \
                                        and not clicks:
                                    print("Casuta selectata nu contine o piesa care sa va apartina.")
                                    print("Reluati mutarea.")
                                elif stare_curenta.tabla_joc.matr[linie1 * Joc.NR_COLOANE + coloana1].lower() != Joc.GOL \
                                        and clicks:
                                    print("Casuta selectata nu este libera.")
                                    print("Reluati mutarea.")
                                    clicks = []
                                else:
                                    clicks.append((linie1, coloana1))
                                if len(clicks) == 2:
                                    (linie1, coloana1) = clicks[0]
                                    (linie2, coloana2) = clicks[1]
                                    clicks = []
                                    mutari_fortate = []
                                    for i in range(Joc.NR_COLOANE):
                                        for j in range(Joc.NR_COLOANE):
                                            if stare_curenta.tabla_joc.matr[i * Joc.NR_COLOANE + j].lower() == Joc.JMIN:
                                                y = mutare_compusa(i, j, copy.deepcopy(stare_curenta.tabla_joc.matr))
                                                if y:
                                                    mutari_fortate.extend(y)

                                    ok = False
                                    nou = ''
                                    for x in mutari_fortate:
                                        if x[0] == linie2 and x[1] == coloana2:
                                            ok = True
                                            nou = x[2]
                                    if ok:
                                        raspuns_valid = True
                                        juc_mutari += 1
                                        stare_curenta.tabla_joc.matr = copy.deepcopy(nou)
                                    elif (linie2, coloana2) in mutare_simpla(linie1, coloana1,
                                                                             stare_curenta.tabla_joc.matr):
                                        if mutari_fortate:
                                            print("Mutarea nu este valida, sunteti fortat sa capturati.")
                                            clicks = []
                                            continue
                                        else:
                                            raspuns_valid = True
                                            juc_mutari += 1

                                            stare_curenta.tabla_joc.matr[linie2 * Joc.NR_COLOANE + coloana2] = \
                                                stare_curenta.tabla_joc.matr[linie1 * Joc.NR_COLOANE + coloana1]
                                            stare_curenta.tabla_joc.matr[linie1 * Joc.NR_COLOANE + coloana1] = Joc.GOL
                                            if linie2 == 0 or linie2 == Joc.NR_COLOANE - 1:
                                                stare_curenta.tabla_joc.matr[
                                                    linie2 * Joc.NR_COLOANE + coloana2] = Joc.JMIN.upper()
                                    else:
                                        print("Mutare invalida. Reluati.")
                                        continue
                                    # dupa iesirea din while sigur am valide atat linia cat si coloana
                                    # deci pot plasa simbolul pe "tabla de joc"
                                    if len(clicks) == 1:
                                        stare_curenta.tabla_joc.deseneaza_grid(clicks[0][0], clicks[0][1])
                                    else:
                                        stare_curenta.tabla_joc.deseneaza_grid()
                                    # S-a realizat o mutare. Schimb jucatorul cu cel opus
                                    stare_curenta.j_curent = Joc.jucator_opus(stare_curenta.j_curent)

                                    t_dupa = int(round(time.time() * 1000))
                                    print(
                                        'Jucatorul a "gandit" timp de '
                                        + str(t_dupa - t_inainte)
                                        + " milisecunde."
                                    )
            if game_over(stare_curenta):
                print("Timp maxim de gandire pentru calculator:", calc_timp_maxim)
                print("Timp minim de gandire pentru calculator:", calc_timp_minim)
                print("Timp mediu de gandire pentru calculator:", calc_timp_total / calc_mutari)
                print("Mediana timpului de gandire pentru calculator:", calc_timpi[(len(calc_timpi) - 1) // 2])
                print()
                print("Timp total al jocului:", int(round(time.time() * 1000)) - t_start)
                print("Numarul de mutari calculator:", calc_mutari)
                print("Numarul de mutari jucator:", juc_mutari)
                print()
                print("Numar maxim de noduri generate la o mutare:", NR_NODURI_PER_MUTARE[-1])
                print("Numar minim de noduri generate la o mutare:", NR_NODURI_PER_MUTARE[0])
                print("Numar mediu de noduri generate la o mutare:", sum(NR_NODURI_PER_MUTARE) / len(NR_NODURI_PER_MUTARE))
                print("Mediana numarului de noduri generate la o mutare:", NR_NODURI_PER_MUTARE[(len(NR_NODURI_PER_MUTARE) - 1) // 2])
                break

        # --------------------------------
        else:  # jucatorul e JMAX (calculatorul)
            # Mutare calculator

            print("Acum muta calculatorul cu simbolul", stare_curenta.j_curent)
            # preiau timpul in milisecunde de dinainte de mutare
            t_inainte = int(round(time.time() * 1000))

            if tip_algoritm == 1:
                stare_actualizata, NODURI_CURENT = min_max(stare_curenta, 0, metoda)
            else:
                stare_actualizata, NODURI_CURENT = alpha_beta(-500, 500, stare_curenta, 0, metoda)

            NR_NODURI_PER_MUTARE.append(NODURI_CURENT)
            NR_NODURI_PER_MUTARE.sort()

            # aici se face de fapt mutarea !!!
            stare_curenta.tabla_joc = stare_actualizata.stare_aleasa.tabla_joc

            stare_curenta.tabla_joc.deseneaza_grid()
            # preiau timpul in milisecunde de dupa mutare
            t_dupa = int(round(time.time() * 1000))
            print(
                'Calculatorul a "gandit" timp de '
                + str(t_dupa - t_inainte)
                + " milisecunde."
            )
            calc_timp_maxim = max(calc_timp_maxim, t_dupa - t_inainte)
            calc_timp_minim = min(calc_timp_minim, t_dupa - t_inainte)
            calc_timp_total += t_dupa - t_inainte
            calc_timpi.append(t_dupa - t_inainte)
            calc_timpi.sort()
            calc_mutari += 1
            print("Estimare:", stare_curenta.estimare)

            if game_over(stare_curenta):
                print("Timp maxim de gandire pentru calculator:", calc_timp_maxim)
                print("Timp minim de gandire pentru calculator:", calc_timp_minim)
                print("Timp mediu de gandire pentru calculator:", calc_timp_total / calc_mutari)
                print("Mediana timpului de gandire pentru calculator:", calc_timpi[(len(calc_timpi) - 1) // 2])
                print()
                print("Timp total al jocului:", int(round(time.time() * 1000)) - t_start)
                print("Numarul de mutari calculator:", calc_mutari)
                print("Numarul de mutari jucator:", juc_mutari)
                print()
                print("Numar maxim de noduri generate la o mutare:", NR_NODURI_PER_MUTARE[-1])
                print("Numar minim de noduri generate la o mutare:", NR_NODURI_PER_MUTARE[0])
                print("Numar mediu de noduri generate la o mutare:",
                      sum(NR_NODURI_PER_MUTARE) / len(NR_NODURI_PER_MUTARE))
                print("Mediana numarului de noduri generate la o mutare:",
                      NR_NODURI_PER_MUTARE[(len(NR_NODURI_PER_MUTARE) - 1) // 2])
                break
            # S-a realizat o mutare.  jucatorul cu cel opus
            stare_curenta.j_curent = Joc.jucator_opus(stare_curenta.j_curent)


if __name__ == "__main__":
    main()