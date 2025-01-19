import pygame
import os
import pandas as pd

# Ініціалізація Pygame
pygame.init()

# Параметри екрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Меню вибору карт")

# Основні кольори
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)

# Шрифт
font = pygame.font.Font(None, 36)

# Шлях до папки з картами
MAPS_FOLDER = "maps"

# Завантаження списку карт
maps = [f for f in os.listdir(MAPS_FOLDER) if f.endswith(".vox")]

# Створення DataFrame для карт
data = {
    "Map Name": maps,
    "Path": [os.path.join(MAPS_FOLDER, m) for m in maps]
}
maps_df = pd.DataFrame(data)

# Функція для відображення тексту на екрані
def draw_text(text, x, y, color=BLACK):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Функція для відображення меню вибору
selected_index = 0
def draw_menu():
    screen.fill(WHITE)
    draw_text("Виберіть карту:", 50, 50)

    for i, row in maps_df.iterrows():
        color = BLUE if i == selected_index else BLACK
        draw_text(row["Map Name"], 100, 100 + i * 40, color)

# Основний цикл гри
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected_index = (selected_index - 1) % len(maps_df)
            elif event.key == pygame.K_DOWN:
                selected_index = (selected_index + 1) % len(maps_df)
            elif event.key == pygame.K_RETURN:
                selected_map = maps_df.iloc[selected_index]
                print(f"Вибрана карта: {selected_map['Map Name']} ({selected_map['Path']})")

    draw_menu()
    pygame.display.flip()

pygame.quit()
