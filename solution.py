import time
import sys

def read_nodes(dic, filename):
    """Read the nodes file with name "filename" and initialize a
    key with a dictionary as a value for every node.
    The dictionary in the dictionary dic contains a key "name" to
    access the name of the node and a key "edges" to access a list of neighbours of the node.
    The dictionary dic is used as a reference.

    Args:
            dic: dictionary{int : {'name' : str, 'edges' : a set of int}}
            filename: str
    Returns:
            None

    """

    with open(filename, "r") as f:
        for line in f:
            line = line.split()
            dic[int(line[0])] = {'name': line[1], 'edges': set()}


def read_edges(dic, filename):
    """Read edges using the file "filename" and store the edge information in the dictionary of the dictionary dic.
       The dictionary dic is again used as a reference.

        Args:
                 dic: dictionary{int : {'name' : str, 'edges' : a set of int}}
            filename: str
        Returns:
            None

        """

    with open(filename, "r") as f:
        for line in f:
            line = line.split()
            v1 = int(line[1])
            v2 = int(line[2])
            dic[v1]['edges'].add(v2)
            dic[v2]['edges'].add(v1)


#=========================================================================


def max_clique(dic):
    """Return the maximum clique in the given graph represented by dic.
       See readme for detailed description.

        Args:
            dic: dictionary{int : {'name' : str, 'edges' : a set of int}}
        Returns:
            list of int

    """
    max_c = []
    V = dic.keys()

    for vi in V:
        #  pruning vertices that have fewer neighbours than the size of the maximum clique already computed
        if len(dic[vi]['edges']) >= len(max_c):     # only considers this vertex if it is able to span a clique that is maximal
            
            U = {vi}        # list of neighbours who can potentially be part of the clique
            # pruning neighbors of vi that cannot form a clique of size larger than current maximum clique
            for vj in dic[vi]['edges']:
                if len(dic[vj]['edges']) >= len(max_c):
                    U.add(vj)

            size = 0
            temp_max_c = []

            while len(U) != 0:      # keep adding nghs of vi as long as there are potential nghs.
                # break if current U is impossible to form a larger clique than current maximum clique
                # i.e if the maximal size of the clique that we are trying to create ( = nodes already in the clique + potential nodes which are still
                # possible to be added). This is the limes superior.
                if size+len(U) <= len(max_c):
                    break
                
                # choose a random element u in U and add it.
                u = U.pop()             
                temp_max_c.append(u)
                N_u = dic[u]['edges']       # nghs of u
                U = U.intersection(N_u)     # restrict the potential nodes in U considering that u is now in the clique
                size += 1

            # if the size of this maximal clique created by starting with vi exceeds the size of so far globally biggest clique,
            # redefine the new globally largest clique.
            if size > len(max_c):
                max_c = temp_max_c

    # sort the result and return it!
    max_c.sort()
    return max_c


if __name__ == "__main__":

    t = time.time()

    file_nodes = sys.argv[1]
    file_edges = sys.argv[2]


    dic = {}

    read_nodes(dic, file_nodes)
    read_edges(dic, file_edges)

    print 'parsing done in : ' + str(time.time() - t)

    result = max_clique(dic)

    f = open('result.txt', 'w')
    for i in result:
        f.write(str(i) + ' ' + dic[i]['name'] + '\n')
    f.close()

    print 'completely done in : ' + str(time.time() - t)

