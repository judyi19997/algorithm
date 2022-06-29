# https://programmers.co.kr/learn/courses/30/lessons/77484
# 프로그래머스 로또의 최고 순위와 최저 순위 - level 1
def solution(lottos, win_nums):
    dict = {0:6,1:6,2:5, 3:4, 4:3, 5:2, 6:1}
    catch = 0
    predict = 0
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            catch +=1
        if lottos[i] == 0:
            predict +=1
    return dict[catch+predict],dict[catch]
