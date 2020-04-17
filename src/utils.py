def get_allowed_moves(map):
    coordinates = []
    for i in range(3):
        for j in range(3):
            if map[i][j] == 0:
                coordinates.append([i,j])
    return coordinates

def get_winner(map):
    for k in range(3):
        if map[k][0] == map[k][1] and map[k][0] == map[k][2] and map[k][1] == map[k][2] and map[k][0] != 0:
            return True, map[k][0]
        if map[0][k] == map[1][k] and map[0][k] == map[2][k] and map[1][k] == map[2][k] and map[0][k] != 0:
            return True, map[0][k]

    if map[1][1] != 0:
        if map[0][0] == map[1][1] and map[0][0] == map[2][2] and map[1][1] == map[2][2]:
            return True, map[1][1]
        if map[0][2] == map[1][1] and map[0][2] == map[2][0] and map[1][1] == map[2][0]:
            return True, map[1][1]

    return False, 0

def get_line(map,x):
    return map[x]

def get_column(map,y):
    return [map[0][y],map[1][y],map[2][y]]

def get_first_diag(map):
    return [map[0][0],map[1][1],map[2][2]]

def get_second_diag(map):
    return [map[0][2],map[1][1],map[2][0]]

def first_diag_coord():
    return [[0,0],[1,1],[2,2]]

def second_diag_coord():
    return [[0,2],[1,1],[2,0]]

def get_argmax(list_of_values):
    max = list_of_values[0]
    arg_max = 0
    for i in range(1,len(list_of_values)):
        if list_of_values[i] > max:
            max = list_of_values[i]
            arg_max = i
    return arg_max

def coordinates_to_number(x,y):
    return 3*x+y

def number_to_coordinates(x):
    return int(x/3.0), x%3
