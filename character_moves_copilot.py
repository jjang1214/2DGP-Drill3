from pico2d import *
import math

open_canvas(800, 600)

# 이미지 로드
grass = load_image('grass.png')
character = load_image('character.png')

grass_x, grass_y = 400, 30

# 사각형 궤적: (400,90) → (780,90) → (780,560) → (20,560) → (20,90) → (400,90)
rect_points = [
    (400, 90), (780, 90), (780, 560), (20, 560), (20, 90), (400, 90)
]
# 삼각형 궤적: (400,90) → (700,500) → (100,500) → (400,90)
tri_points = [
    (400, 90), (700, 500), (100, 500), (400, 90)
]
# 원 궤적: 중심(400,300), 반지름 210, 시작 각도 -90도(즉, (400,90)에서 시작)
circle_cx, circle_cy, circle_r = 400, 300, 210
circle_start_angle = -90

state = 0  # 0=사각, 1=삼각, 2=원

# 사각형 이동 인덱스 및 진행률
rect_idx = 0
rect_t = 0.0
# 삼각형 이동 인덱스 및 진행률
tri_idx = 0
tri_t = 0.0
# 원 이동 각도
circle_angle = circle_start_angle

RECT_FRAMES = 100
TRI_FRAMES = 100
CIRCLE_FRAMES = 360

running = True
while running:
    clear_canvas()
    grass.draw(grass_x, grass_y)

    if state == 0:  # 사각형 운동
        x1, y1 = rect_points[rect_idx]
        x2, y2 = rect_points[rect_idx + 1]
        char_x = (1 - rect_t) * x1 + rect_t * x2
        char_y = (1 - rect_t) * y1 + rect_t * y2
        character.draw(char_x, char_y)
        rect_t += 1.0 / RECT_FRAMES
        if rect_t >= 1.0:
            rect_t = 0.0
            rect_idx += 1
            if rect_idx == len(rect_points) - 1:
                # (400,90) 도달, 삼각형 운동으로 전환
                rect_idx = 0
                state = 1
    elif state == 1:  # 삼각형 운동
        x1, y1 = tri_points[tri_idx]
        x2, y2 = tri_points[tri_idx + 1]
        char_x = (1 - tri_t) * x1 + tri_t * x2
        char_y = (1 - tri_t) * y1 + tri_t * y2
        character.draw(char_x, char_y)
        tri_t += 1.0 / TRI_FRAMES
        if tri_t >= 1.0:
            tri_t = 0.0
            tri_idx += 1
            if tri_idx == len(tri_points) - 1:
                # (400,90) 도달, 원 운동으로 전환
                tri_idx = 0
                state = 2
    elif state == 2:  # 원 운동 (반시계방향)
        angle = math.radians(circle_angle)
        char_x = circle_cx + circle_r * math.cos(angle)
        char_y = circle_cy + circle_r * math.sin(angle)
        character.draw(char_x, char_y)
        circle_angle -= 360.0 / CIRCLE_FRAMES  # 반시계방향
        if circle_angle <= circle_start_angle - 360:  # -90도에서 한 바퀴(-450도)
            circle_angle = circle_start_angle
            state = 0

    update_canvas()
    delay(0.01)

    # 이벤트 처리
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            running = False
        elif e.type == SDL_KEYDOWN and e.key == SDLK_ESCAPE:
            running = False

close_canvas()

# copilot의 코딩