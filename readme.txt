#####################README##########################

AUTOR: 		Frank Chen, Lennart Döppenschmitt
VERSION:	1.0.0
DATE:		19 June, 2016



The graph G is stored in a dictionary with the structure 

        {int : {'name' : str, 'edges' : set of int}}

First the function read_nodes(dic, filename) is called to initialize the value dictionaries within the outermost dictionary for every node in the file “filename”.
This dictionary dic is then filled with the information using the function read_edges(dic, filename) with the information contained in “filename”.

The main function is max clique(dic) which returns a sorted list containing the nodes belonging to the maximum clique in the graph G represented by dic.
For every node in the graph this function creates the maximum clique containing this particular initial node.
While performing this search it constantly checks which nodes don’t have to be considered to be part of this maximal clique due to their degrees (=number of neighbours) which has to be at least n-1 where n is the current number of elements in the clique since every clique has to be a complete subgraph.
