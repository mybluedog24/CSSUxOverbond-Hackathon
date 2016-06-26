import time
#import sys

def read_result(clique, filename):
    """Read nodes file filename, store nodes in dictionary dic as keys.

    Args:
             dic: dictionary{int : {'name' : str, 'edges' : a set of int}}
        filename: str
    Returns:
        None

    """
    with open(filename, "r") as f:
        for line in f:
            line = line.split()
            clique[int(line[0])] = True

#    for a in clique:
#        dic[a] = {}
#        for b in clique:
#            dic[a][b] = [0,0,0]


def read_edges(clique, filename, PhoneCost, EmailCost, OverbondCost):
    """Read edges file filename, store edge vertices in dictionary dic as values.

        Args:
                 dic: dictionary{int : {'name' : str, 'edges' : a set of int}}
            filename: str
        Returns:
            None
        """
#    price = [OverbondCost, PhoneCost, EmailCost]
    result = 0.0
    
#    keys = dic.keys()
    with open(filename, "r") as f:
        for line in f:
            line = line.split()
            v1 = int(line[1])
            v2 = int(line[2])
            if v1 not in clique or v2 not in clique:
                continue
            connection = line[3]
            # the number of connections of type 0 = Overbond, 1 = Phone, 2 = Email
            # are represented as an integer in the list at position 0,1 or 2
            if (connection == 'Overbond'):
                result += OverbondCost
            elif (connection == 'Phone'):
                result += PhoneCost
            elif (connection == 'Email'):
                result += EmailCost
                
    return result


#=========================================================================

def cost(dic, PhoneCost, EmailCost, OverbondCost):
    """Calculates the cost by summing over all connections in the dictionary dic.
       Note that this time only one of the vertices knows of the connection to
       avoid redundancy.
    """
    price = [OverbondCost, PhoneCost, EmailCost]
    result = 0.0
    for a in dic:   # iterating over all vertices in the clique
        for b in dic[a]: # iterating over all neighbours of the vertex a
            result += sum([x*y for x,y in zip(dic[a][b],price)])

    return result

           
if __name__ == "__main__":

    t = time.time()

#    file_nodes = sys.argv[1]
#    file_edges = sys.argv[2]
    file_edges = "edges_world_2a.clq"
    file_result = "result.txt"

    dic = {}
    clique = {}

    read_result(clique, file_result)
    print read_edges(clique, file_edges,1.0, 0.8, 0.5)

#    result = max_clique(dic)

#    f = open('result.txt', 'w')
#    for i in result:
#        f.write(str(i) + ' ' + dic[i]['name'] + '\n')
#    f.close()

#    print cost(dic, 1.0, 0.8, 0.5)

    print 'run time: ' + str(time.time() - t)

