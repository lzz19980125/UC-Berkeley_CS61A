def shifty_shifts(start, goal, limit):
    def records(start, goal, count, limit):
        if (count > limit):
            return limit + 1
        if (len(start) == 1):
            if (len(goal) == 1):
                if (start[0] == goal[0]):
                    return count
                return count + 1
            if (start[0] == goal[0]):
                return count + len(goal[1:])
            return count + 1 + len(goal[1:])
        if (start[0] == goal[0]):
            return records(start[1:], goal[1:], count, limit)
        return records(start[1:], goal[1:], count + 1, limit)
    return records(start, goal, 0, limit)

def final_diff(start, goal, limit):
    return shifty_shifts(start, goal, limit)

def autocorrect(user_word, valid_words, diff_function, limit):
    if (user_word in valid_words):
        return user_word
    smallest , reuslt  = float('inf'),None
    for i in valid_words:
        if(diff_function(user_word,i,limit)<smallest):
            smallest = diff_function(user_word,i,limit)
            result = i
    if(smallest >limit):
        return user_word
    else:
        return result

list = ['apple','banana','grape','orange']
print(autocorrect('an',list,final_diff,10))






