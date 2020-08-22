import os 
import random


arr = [ i for i in range(9) ]
matches = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [2,4,6]
]

user = []
comp = []

def match (l):
    global matches
    n = 0
    for comb in matches:
        c = 0
        n += 1
        for index in comb:
            if index  in l:
                c += 1
        if c == 3:
            return True, n
    return False, None





def row_col(x,y):
    if  60 <= x < 365:
        col = 0
    elif 365 <= x < 773:
        col = 1
    elif 773 <= x <= 1108:
        col = 2

    if 300 <= y < 530 :
        row = 0
    elif 530 <= y < 788:
        row = 1
    elif  788 <= y <= 980 :
        row = 2

    return row,col

def comp_turn(combs):
    global arr, comp, user, matches
    print('list of concern :',combs)
    if comp == [] and user[0] in [0,2,6,8]:
        if user[0] == 0:
            index = 2
        if user[0] == 2:
            index = 8
        if user[0] == 8:
            index = 6
        if user[0] == 6:
            index = 0
        arr.remove(index)
        comp.append(index)
        return index
        
    if go_computer_win():
        index =  comp_win()
        print('comp try :', index)
        return index



    if combs != []: 
        for comb in combs:
            for i in comb:
                if i not in comp and i not in user:
                    index = i 
                    arr.remove(index)
                    comp.append(index)
                    return index

    if 4 in user and  medium()[0]:
        index = medium()[1]
        arr.remove(index)
        comp.append(index)
        return index

    return hard()


def empty(row,col):
    global arr 
    index = row*3 + col
    if index in arr:
        arr.remove(index)
        user.append(index)
        return True
    else:
        return False

def initial():
    global arr, user, comp
    arr[:] = [0,1,2,3,4,5,6,7,8]
    user[:] = []
    comp[:] = []

def get_combs(opp,me):
    global arr, matches
    list_of_concern = []
    print('user :', user , 'comp :', comp)
    for comb in matches:
        c_in_user = 0
        c_in_comp = 0 
        for index in comb:
            if index in opp :
                c_in_user += 1
            if index in me  :
                c_in_comp += 1
        #print('comb :',comb, 'c in user :', c_in_user, 'c in comp :', c_in_comp)
        if c_in_comp == 0 and c_in_user == 2:
            list_of_concern.append(comb)
    return list_of_concern


def medium():
    global arr, comp, user
    fatals = [[0,6],[2,0],[8,2], [6,8]]
    for fatal in fatals:
        if fatal[0] in user  and fatal[1] in arr:
            return True,fatal[1]
    return False,None
def hard():
    global arr, comp
    priority = [4,0,2,6,8,1,3,5,7]
    for i in priority:
        if i in arr:
            arr.remove(i)
            comp.append(i)
            return i 
def comp_win():
    global arr, user, comp
    combinations = get_combs(comp, user)
    print('combinations :', combinations)
   
    for comb in combinations:
        for index in comb:
            if index not in comp:
                comp.append(index)
                arr.remove(index)
                return  index 

def go_computer_win():
    global arr, user, comp
    combinations = get_combs(comp, user)
    print('combinations :', combinations)
    if combinations == []:
        return False
    return True