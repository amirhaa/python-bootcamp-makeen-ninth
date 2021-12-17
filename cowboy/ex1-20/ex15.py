def mean_scores(scores_dict):
    count = 0
    starter = 0
    for score in scores_dict.values() :
        starter += score
        count +=1
    return starter / count