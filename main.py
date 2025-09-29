#### Imports et définition des variables globales

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    with open(filename, mode='r') as f :
        l = []
        csv = f.readlines()
        for line in csv :
            nombres = [int(n) for n in line.strip().split(';')]
            l.append(nombres)
    f.close()
    return l

def get_list_k(data, k):
    return data[k]

def get_first(l):
    return l[0]

def get_last(l):
    return l[-1]

def get_max(l):
    return max(l)

def get_min(l):
    return min(l)

def get_sum(l):
    return sum(l)


#### Fonction principale


def main():
    pass
    data = read_data(FILENAME)
    print(data)
    #for i, l in enumerate(data):
        #print(i, l)
    #k = 37
    #print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
