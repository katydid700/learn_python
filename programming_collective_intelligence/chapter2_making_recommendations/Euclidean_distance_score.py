# coding=utf-8
"""欧几里得距离评价
用来计算人们在品味方面的相似程度
"""
from math import sqrt
critics = {
    'Lisa Rose': {'Lady in the water ': 2.5, 'Snakes on a Plane': 3.5, 'Just My luck ': 3.0, 'Superman Returns ': 3.5,
                  'You, me and Dupree': 2.5, 'The night Listener': 3.0},
    'Gene Seymour': {'Lady in the water': 3.0, 'Snakes on a Plane': 3.5, 'Just My luck ': 1.5, 'Superman Returns ': 5.0,
                   'The night Listener': 3.0, 'You, me and Dupree': 3.5},
    'Michael Phillips': {'Lady in the water': 2.5, 'Snakes on a Plane': 3.0,  'Superman Returns ': 3.5,
                   'The night Listener': 4.0},
    'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My luck ': 3.0, 'The night Listener': 4.5,
                     'Superman Returns ': 4.0, 'You, me and Dupree': 2.5 },
    'Mick LasSalle': {'Lady in the water': 3.0, 'Snakes on a Plane': 4.0,  'Just My luck ': 2.0, 'Superman Returns ': 3.0,
                   'The night Listener': 3.0, 'You, me and Dupree': 2.0},
    'Jack Matthews': {'Lady in the water': 3.0, 'Snakes on a Plane': 4.0, 'The night Listener': 3.0, 'Superman Returns ': 5.0,
                      'You, me and Dupree': 3.0},
    'Toby': {'Snakes on a Plane': 4.5,  'You, me and Dupree': 1.0, 'Superman Returns ': 4.0}

}

def sim_distance(prefs, person1, person2):
    si = { }
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1
    if len(si) == 0:
        return 0
    sum_of_squares = sum([pow(prefs[person1][item]-prefs[person2][item], 2)
                          for item in prefs[person1] if item in prefs[person2]])
    return 1/(1 + sqrt(sum_of_squares))

print sim_distance(critics, 'Lisa Rose', 'Gene Seymour')

