import os
import time
import random
from collections import deque

class SnakeGame:
    def __init__(self):
        self.width = 30
        self.height = 15
        self.speed = 0.2

    def main(self):
        print("=== 贪吃蛇游戏 ===")
        print(f"游戏区域: {self.width} x {self.height}")
        print("方向键控制: w=上 a=左 s=下 d=右 q=退出\n")

        # 初始化蛇的位置（头部）
        snake_x = self.width // 2
        snake_y = self.height // 2
        snake_direction = 's'
        snake_body = deque([(snake_x, snake_y)])

        # 生成食物位置
        food_x = random.randint(0, self.width - 1)
        food_y = random.randint(0, self.height - 1)

        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"分数: {len(snake_body)}")

            # 绘制游戏地图
            for y in range(self.height):
                row = ''
                for x in range(self.width):
                    if (x, y) in snake_body:
                        row += 'O'
                    elif (x == food_x and y == food_y):
                        row += '*'
                    else:
                        row += '.'
                print(row)

            # 获取用户输入（简化版）
            try:
                key = input(f"方向 (w/a/s/d/q): ").lower()
            except EOFError:
                break

            if key == 'q':
                break
            elif key == 'w' and snake_direction != 's':
                snake_direction = 'w'
            elif key == 'a' and snake_direction != 'd':
                snake_direction = 'a'
            elif key == 's' and snake_direction != 'w':
                snake_direction = 's'
            elif key == 'd' and snake_direction != 'a':
                snake_direction = 'd'

            # 计算新位置
            if snake_direction == 'w':
                new_x, new_y = snake_body[-1][0], snake_body[-1][1] - 1
            elif snake_direction == 's':
                new_x, new_y = snake_body[-1][0], snake_body[-1][1] + 1
            elif snake_direction == 'a':
                new_x, new_y = snake_body[-1][0] - 1, snake_body[-1][1]
            elif snake_direction == 'd':
                new_x, new_y = snake_body[-1][0] + 1, snake_body[-1][1]

            # 检测是否吃到食物
            if (new_x, new_y) == (food_x, food_y):
                food_x = random.randint(0, self.width - 1)
                food_y = random.randint(0, self.height - 1)
            else:
                # 移动蛇头
                snake_body.append((new_x, new_y))
                snake_body.popleft()

            # 检测碰撞（撞墙）
            if new_x < 0 or new_x >= self.width or new_y < 0 or new_y >= self.height or (new_x, new_y) in snake_body:
                print(f"游戏结束！最终得分: {len(snake_body)}")
                break

            time.sleep(self.speed)

if __name__ == '__main__':
    game = SnakeGame()
    try:
        game.main()
    except KeyboardInterrupt:
        print("\n游戏已退出！")