# coding=utf-8
"""皮尔逊相关度评价
用来计算人们在品味方面的相似程度
判断两组数与某一直线的拟合程度
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

def sim_pearson(prefs, p1, p2):
    si = {}
    sp = []
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1
    n = len(si)
    if n == 0:
        return 1
    # 求所有偏好之和
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])
    #求平方和
    sum1Sq = sum([pow(prefs[p1][it], 2) for it in si])
    sum2Sq = sum([pow(prefs[p2][it], 2) for it in si])
    # 求乘积之和
    for it in si:
        sp.append(prefs[p1][it] * prefs[p2][it])
    pSum = sum(sp)
    # 计算皮尔逊
    num = pSum - (sum1 * sum2 / n)
    den = sqrt((sum1Sq - pow(sum1, 2)/n) * (sum2Sq - pow(sum2, 2)/n))
    if den == 0 : return 0

    r =num/den
    return r

print sim_pearson (critics, 'Lisa Rose', 'Gene Seymour')