
plays =  [400 , 150 , 600 , 500, 50  , 500 , 100 , 100]

answer = list(filter(lambda x: plays[x] == 500, range(len(plays))))
print(answer)