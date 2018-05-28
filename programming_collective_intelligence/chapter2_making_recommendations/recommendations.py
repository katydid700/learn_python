# coding=utf-8
"""
嵌套字典
寻找一种表达不同人及其偏好的方法
"""
from math import sqrt
"""一个涉及影评者及其对几部电影评分情况的字典"""

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
"""欧几里得距离"""
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

"""皮尔逊算法"""
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

"""为评论者打分
得到一个人员的有序列表
这些人与某个指定人员具有相近的品味
"""
def topMatches(prefs, person, n=5, similarity=sim_pearson):
    scores = [(similarity(prefs,person,other), other)
              for other in prefs if other != person]
    scores.sort()
    scores.reverse()
    return scores[0:n]

print(topMatches(critics,'Toby', n=3))