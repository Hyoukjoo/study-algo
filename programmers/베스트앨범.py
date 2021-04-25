import collections

def solution(genres, plays):
    answer = []
    dic = collections.defaultdict(int)
    musics = collections.defaultdict(list)
    n = len(plays)

    for i in range(n):
        dic[genres[i]] += plays[i]
        musics[genres[i]].append((i, plays[i]))
        
    genre_list = sorted(dic.keys(), key=lambda x: dic[x], reverse=True)
    
    for genre in genre_list:
        musics[genre].sort(key=lambda x: (-x[1], x[0]))
        answer.extend([i for i, p in musics[genre][:2]])

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 500, 2500]))