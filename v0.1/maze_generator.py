import random

def create_maze(height,width):
    tree = []
    frontier = []
    max_node = height*width
    edge_list = []
    node_list = []
    for i in range(height):
        node_row = []
        for j in range(width):
            node_row.append([i,j])
        node_list.append(node_row)
    #return node_list
    # create first node
    first_node_x = random.randint(0,width-1)
    first_node_y = random.randint(0,height-1)
    tree.append(node_list[first_node_y][first_node_x])
    #print("tree_node is",tree)
    if first_node_x > 0:
        frontier.append([first_node_y,first_node_x-1])
    if first_node_x < width-1:
        frontier.append([first_node_y,first_node_x+1])
    if first_node_y > 0:
        frontier.append([first_node_y-1,first_node_x])
    if first_node_y < height-1:
        frontier.append([first_node_y+1,first_node_x])
        # print("before iteration")
        # print('current tree nodes:',tree)
        # print('current frontier is',frontier)
    while len(tree) < max_node:
        #select a random list
        #tree_lottery = random.randint(0,len(tree)-1)
        # node_to_develop_edge = tree[tree_lottery]
        if len(frontier)-1 == 0:
            frontier_lottery = 0
        else:
            frontier_lottery = random.randint(0,len(frontier)-1)
        frontier_to_connect = frontier[frontier_lottery]
        #print("frontier is",frontier_to_connect)
        tree.append(frontier_to_connect)
        frontier.pop(frontier_lottery)
        #if frontier_to_connect:
        #edge_list.append([node_to_develop_edge,frontier_to_connect])
        new_treenode_y = frontier_to_connect[0]
        new_treenode_x = frontier_to_connect[1]
        node_to_develop_edge = []
        if new_treenode_y > 0 and [new_treenode_y-1,new_treenode_x] not in tree and [new_treenode_y-1,new_treenode_x] not in frontier:
            frontier.append([new_treenode_y-1,new_treenode_x])
        elif [new_treenode_y-1,new_treenode_x] in tree:
            #pass
            node_to_develop_edge.append([new_treenode_y-1,new_treenode_x])
        if new_treenode_y < height-1 and [new_treenode_y+1,new_treenode_x] not in tree and [new_treenode_y+1,new_treenode_x] not in frontier:
            frontier.append([new_treenode_y+1,new_treenode_x])
        elif [new_treenode_y+1,new_treenode_x] in tree:
            node_to_develop_edge.append([new_treenode_y+1,new_treenode_x])
        if new_treenode_x > 0 and [new_treenode_y,new_treenode_x-1] not in tree and [new_treenode_y,new_treenode_x-1] not in frontier:
            frontier.append([new_treenode_y,new_treenode_x-1])
        elif [new_treenode_y,new_treenode_x-1] in tree:
            node_to_develop_edge.append([new_treenode_y,new_treenode_x-1])
        if new_treenode_x < width-1 and [new_treenode_y,new_treenode_x+1] not in tree and [new_treenode_y,new_treenode_x+1] not in frontier:
            frontier.append([new_treenode_y,new_treenode_x+1])
        elif [new_treenode_y,new_treenode_x+1] in tree:
            node_to_develop_edge.append([new_treenode_y,new_treenode_x+1])
        #print("length of tree_node is",len(node_to_develop_edge))
        if len(node_to_develop_edge) == 1:
            tree_lottery = 0
        else:
            tree_lottery = random.randint(0,len(node_to_develop_edge)-1)
        edge_list.append([node_to_develop_edge[tree_lottery],frontier_to_connect])
        # print("after iteration:")
        # print('current tree nodes:',tree)
        # print('current frontier is',frontier)
    return edge_list

def visualize_edge_list(height,width,edge_list):
    graph_height = height*2 - 1
    graph_width = width*2 - 1
    graph = [[" " for _ in range(graph_width)] for _ in range(graph_height)]
    for i in range(height):
        for j in range(width):
            graph[2*i][2*j] = "▓"

    for edge in edge_list:
        node1_y = edge[0][0]*2
        node1_x = edge[0][1]*2
        node2_y = edge[1][0]*2
        node2_x = edge[1][1]*2
        if node1_y == node2_y:
            graph[node1_y][(node1_x+node2_x)//2] = '█'
        else:
            graph[(node1_y+node2_y)//2][node1_x] = '█'

    for i in range(graph_height):
        for j in range(graph_width):
            if graph[i][j] == '█':
                print("█",end="")
            elif graph[i][j] == '▓':
                print("▓",end="")
            else:
                print("░",end="")
        print('\n',end="")

if __name__ == "__main__":
    edge_list = create_maze(3,6)
    print("maze for size (3,6)")
    visualize_edge_list(3,6,edge_list)
    edge_list2 = create_maze(8,25)
    print("maze for size (8,25)")
    visualize_edge_list(8,25,edge_list2)