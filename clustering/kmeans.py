from collections import defaultdict
from math import inf
import random
import csv
import math

"""
Name: Xiaoyan Su
BUID: U70449420
Assignment: CS506 Extra Credit
"""

def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)
    
    Returns a new point which is the center of all the points.
    """

    ret = [0] * len(points[0])


    for each in points:
        for i in range(len(each)):
           # print(len(ret))
           # print(len(each))
            ret[i] += int(each[i])

    return [sum_/len(points) for sum_ in ret]


    #raise NotImplementedError()


def update_centers(data_set, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    #raise NotImplementedError()

    dic = {}
    for i in range(len(data_set)):
        if assignments[i] not in dic:
            dic[assignments[i]] = [data_set[i]]

        else:
            dic[assignments[i]].append(data_set[i])
    ret = []
    dic_lst = list(dic.keys())

    for each in dic_lst:
        ret.append(point_avg(dic[each]))
    

    return ret





def assign_points(data_points, centers):
    """
    """
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):
    """
    Returns the Euclidean distance between a and b
    """

    #print(zip(a,b))
    #print([(x,y) for x,y in zip(a,b)])

    ret = sum([(int(x) - int(y)) ** 2 for x, y in zip(a, b)])


    return math.sqrt(ret)


def generate_k(data_set, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    return random.sample(data_set,k)

print(generate_k([[2,3,4,],[4,5,6]], 1))

def get_list_from_dataset_file(dataset_file):
    
    ret = []

    with open(dataset_file,'r') as f:
        data = csv.reader(f)
        for point in data:
            ret.append(point)
    return ret


def cost_function(clustering):
    
    cost = 0
    for each in clustering.keys():
        center = point_avg(clustering[each])
        for each_point in clustering[each]:
            cost += distance(each_point, center)

    return cost


def k_means(dataset_file, k):
    dataset = get_list_from_dataset_file(dataset_file)
    k_points = generate_k(dataset, k)
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    return clustering
