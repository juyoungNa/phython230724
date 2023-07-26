# chatGPT.py

import os
import random
import time

# 게임판의 크기
WIDTH = 60
HEIGHT = 20

# 패들의 크기와 초기 위치
PADDLE_SIZE = 5
PADDLE_POS = HEIGHT-2

# 초기 공 위치 및 속도 벡터
BALL_POS = [WIDTH//2, PADDLE_POS-1]
BALL_VEL = [1, -1]

# 점수
score = 0

# 화면을 지우는 함수
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

# 게임판을 그리는 함수
def draw(paddle_pos, ball_pos, blocks):
    clear()
    # 윗 부분
    print("="*WIDTH)
    for row in range(HEIGHT-1):
        line = "|"
        for col in range(WIDTH-2):
            if row == ball_pos[1] and col == ball_pos[0]:
                line += "o"
            elif row == paddle_pos:
                if col in range(ball_pos[0]-PADDLE_SIZE//2, ball_pos[0]+PADDLE_SIZE//2+1):
                    line += "="
                else:
                    line += " "
            elif [col, row] in blocks:
                line += "#"
            else:
                line += " "
        line += "|"
        print(line)
    # 아래 부분
    print("="*WIDTH)
    print("Score:", score)

# 게임이 종료되었는지 검사하여 결과를 반환하는 함수
def game_over(ball_pos):
    return ball_pos[1] >= PADDLE_POS

# 프로그램 실행 시작
playing = True

# 블록 생성하기
blocks = []
for row in range(3, 10):  # 세로축 범위
    for col in range(1, WIDTH-1):  # 가로축 범위
        blocks.append([col, row])

# 게임 루프
while playing and blocks:
    draw(PADDLE_POS, BALL_POS, blocks)
    time.sleep(0.1)

    # 공을 이동시키기
    BALL_POS[0] += BALL_VEL[0]
    BALL_POS[1] += BALL_VEL[1]

    # 공이 벽에 닿았다면 반사시키기
    if BALL_POS[0] == 0 or BALL_POS[0] == WIDTH-1:
        BALL_VEL[0] *= -1
    if BALL_POS[1] == 0:
        BALL_VEL[1] *= -1

    # 공이 패들에 닿았다면 반사시키기
    if BALL_POS[1] == PADDLE_POS-1 and BALL_POS[0] in range(PADDLE_POS-PADDLE_SIZE//2, PADDLE_POS+PADDLE_SIZE//2+1):
        BALL_VEL[1] *= -1

    # 블록에 닿은 경우 처리
    for i, block in enumerate(blocks):
        if BALL_POS == block:
            blocks.pop(i)
            BALL_VEL[1] *= -1
            score += 1

    # 게임 종료 검사
    if game_over(BALL_POS):
        playing = False

# 게임 종료 화면 출력
draw(PADDLE_POS, BALL_POS, [])
if blocks:
    print("YOU LOSE!")
else:
    print("YOU WIN!")