#####################################################
# Computer Project #7
# Neil Kim
# Algorithms
# Open CSV file
# Make definitions for different types of functions
# Asks to input text
# Prompt for inputs
# Using the text spits out information
# Calculations of State and Population
#####################################################

import math

#This function takes no arguments, prompts for a file name and returns the file pointer to
#that file. The function will keep asking until a file is found. Use try-except
#and FileNotFoundError.
def open_file():
    try:
        input_file = input("Enter filename: ")
        fp = open(input_file, 'r')
        return fp
    except:
        FileNotFoundError
    pass

#This function accepts no arguments and returns a list of multipliers, each calculated as
#1⁄sqrt(𝑛𝑛(𝑛𝑛 − 1))
#for values of n from 2 to 60 in that order (the list will have 59 values).
def calc_multipliers():
    result = []
    for n in range (2,61):
        i = (1/(n*(n-1))**0.5)
        result.append(i)
    return result
    pass

#This function accepts three arguments, a state (str), the state’s population (int),
#and a list of floats (the multipliers calculated by the calc_multipliers function), and
#returns a list of priorities for the state, each is a tuple with the priority value and the state
#name: (priority value, state name)
def calc_priorities(s, p, m):
    lists = []
    num = 0
    i = 0
    while i != len(m):
        priority = p * m[num]
        priority = int(priority)
        tuple = (priority, s)
        lists.append(tuple)
        num += 1
        i += 1
    lists.sort(reverse=True)
    return lists
    pass

#This function accepts a file pointer and a list of floats (returned from the
#calc_multipliers function) and returns two lists. It reads each state and its
#population from the file and creates two lists
def read_file_make_priorities(fp, multipliers):
    fp.readline()
    reps = []
    priority = []
    for i in fp:
        i = i.split(',')
        state = i[1].replace('"', '')
        population = i[2]
        if state != 'District of Columbia' and state != 'Puerto Rico':
            x = float(population)
            lists = calc_priorities(state, x, multipliers)
            count = 1
            list_of_states = [state, count]
            reps.append(list_of_states)
            for t in lists:
                priority.append(t)
    priority.sort()
    priority.sort(reverse=True)
    reps.sort()
    z = priority[:(386-1)]
    return reps, z
    pass

#This function accepts as parameters a state (str) and the list of lists where each list is of the
#form [state, count], representing a state’s name and a count of its representatives.
def add_to_state(state, states):
    for i in states:
        if i[0] == state:
            i[1] += 1
    pass

#This function accepts as parameters a list of lists where each list is of the form [state,
#count], representing a state’s name and a count of its representatives.
def display(states):
    x = 'State'
    y = 'Representatives'
    print("{:<15s}{:>4s}".format(x, y))
    for l in states:
        i = l[0].strip()
        print("{:<15s}{:>4d}".format(i, l[1]))
    pass

#This function calls the above functions, first to calculate multipliers , open the file and read the
#data, then calculate the priority list.
def main():
    mult = calc_multipliers()
    fp = open_file()
    i = read_file_make_priorities(fp, mult)
    priority = i[1]
    reps = i[0]
    x = [priority, reps]
    print()
    for states in x[0]:
        add_to_state(states[1], x[1])
    display(x[1])
    pass


if __name__ == "__main__":
    main()