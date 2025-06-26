import math
import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_clock():
    radius = 10
    while True:
        clear()
        
        canvas = [[' ' for _ in range(2*radius+1)] for _ in range(2*radius+1)]

      
        for angle in range(0, 360, 6):
            rad = math.radians(angle)
            x = int(radius + radius * math.cos(rad))
            y = int(radius + radius * math.sin(rad))
            canvas[y][x] = 'o'

        
        t = time.localtime()
        second = t.tm_sec
        minute = t.tm_min
        hour = t.tm_hour % 12 + minute / 60

        
        def draw_hand(value, length, symbol, max_value):
            angle = math.radians((360 / max_value) * value - 90)
            for i in range(1, length):
                x = int(radius + i * math.cos(angle))
                y = int(radius + i * math.sin(angle))
                canvas[y][x] = symbol

        draw_hand(hour, 5, 'H', 12)
        draw_hand(minute, 7, 'M', 60)
        draw_hand(second, 9, '.', 60)

        
        for row in canvas:
            print(''.join(row))
        time.sleep(1)

draw_clock()
