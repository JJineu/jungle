# 모든 트럭이 건넜을 때 최소 몇 초인지
# bridge_length 트럭개수이자 거리, weight 이하
# bridge_length 만큼 cnt+
# 다리 위 무게 안에 들어가는지, 1초의 간격은 필요
# 다리의 길이만큼 cnt
# 1. bridge_w 에서 cnt == 거리이면 맨끝 트럭하나 하나 빼주고, bridge_w - truck_w
# 2. 새로 진입하는 트럭 pop, bridge_w + truck_w <= weight 이면 넣어주고 아니면 다시 맨앞에 삽입
# (비교부터 해주고 팝)
# 3. 진입했으면, cnt += 1
# 4. 총 흐른 시간 알아야 되므로 second 변수로 계속 계산


from collections import deque

def solution(bridge_length, weight, truck_weights):
    # truck = deque()

    # for i in truck_weights:
    #     truck.append(i)

        
    bridge_w = 0
    bridge = [[truck_weights[0],1]]
    second = 1
    while 1:
        if not bridge:
            break

        for t,c in bridge:
            c += 1
            bridge.append([t,c])

        if bridge[0][1] == bridge_length:
            bridge_w -= bridge[0][0]
            bridge.pop(0)

        tmp = bridge_w
        tmp += truck_weights[0]
        if weight >= bridge_w:
            truck_w = truck_weights.pop(0)
            bridge_w += truck_w
            bridge.append([truck_w, 0])
            
        
        second += 1
        print(second)
    return second

solution(2,10,[7,4,5,6])
solution(100,100,[10,10,10,10,10,10,10,10,10,10])