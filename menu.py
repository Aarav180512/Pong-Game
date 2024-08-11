import pygame as pg
from variables import *
from buttons import Buttons
from main import PongGame
from music import Music
import sys

try:
    class Menu:
        def __init__(self):
            pg.init()
            pg.display.set_caption("Pong Game Menu")

            self.screen = pg.display.set_mode(WIN_SIZE)
            self.clock = pg.time.Clock()
            self.title_text = "Pong Game"

            self.button_font = pg.font.Font("resorces/font/font.ttf", BUTTON_FONT_SIZE)
            self.title_font = pg.font.Font("resorces/font/font.ttf", TITLE_FONT_SIZE)
            self.instruction_font = pg.font.Font("resorces/font/font.ttf", INSTRUCTION_FONT_SIZE)

            self.buttons = [
                Buttons(self, self.button_font,
                        "Play",
                        (WIDTH // 2 - BUTTON_WIDTH // 2, 200)
                        ),
                Buttons(self, self.button_font,
                        "Instructions",
                        (WIDTH // 2 - BUTTON_WIDTH // 2, 200 + BUTTON_HEIGHT + BUTTON_MARGIN)
                        ),
                Buttons(self, self.button_font,
                        "Quit",
                        (WIDTH // 2 - BUTTON_WIDTH // 2, 200 + 2 * (BUTTON_HEIGHT + BUTTON_MARGIN))
                        )
            ]

            self.pong_game = PongGame(self)
            self.music = Music("resorces/music/pong-pong-193380.mp3")

            self.instruction_text = None

            self.is_running = True
            self.show_buttons = True
            self.is_mute = False
            self.is_fullscreen = False

        def update(self):
            self.draw()
            pg.display.flip()

        def play_music(self):
            self.music.play_music()

        def toggle_fullscreen(self):
            if self.is_fullscreen:
                self.screen = pg.display.set_mode(WIN_SIZE)
            else:
                self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
            self.is_fullscreen = not self.is_fullscreen

        def title(self):
            title_surface = self.title_font.render(self.title_text, True, TITLE_COLOR)
            title_rect = title_surface.get_rect(center=(WIDTH // 2, 80))
            self.screen.blit(title_surface, title_rect)

        def play(self):
            self.pong_game.run()

        def instructions(self):
            self.show_buttons = False

            self.instruction_text = (
                "Pong is a simple yet iconic video game that simulates table tennis. The objective is straightforward: "
                "players aim to score points by getting the ball past their opponent's paddle. The game is typically "
                "played by two players, each controlling a paddle on either side of the screen. Player 1 controls the "
                "right paddle using the up and down arrow keys, while Player 2 controls the right paddle using the 'W' "
                "and 'S' keys. The game starts with the ball in the center of the screen, and it moves in a random "
                "direction to begin play.\n\n"
                
                "As the game progresses, players move their paddles up and down to hit the ball back and forth across the "
                "screen. The ball bounces off the paddles and walls, changing direction based on where it hits. If a player "
                "fails to return the ball and it passes their paddle, the opponent scores a point. The first player to reach "
                f"a set number of points, {WINNING_SCORE} points, wins the game.\n\n"
                
                "The dynamics of Pong make it more challenging as the game continues. The ball often increases in speed, "
                "requiring quicker reactions and more precise movements. Additionally, the angle at which the ball bounces "
                "off the paddle can be controlled by hitting the ball with different parts of the paddle, adding a layer of "
                "strategy to the game. Players must not only react quickly but also think ahead to outmaneuver their opponent.\n\n"
                
                "To excel in Pong, players should focus on anticipating the ball’s trajectory and positioning their paddle "
                "accordingly. Controlling the ball's bounce by using the paddle’s edges can help create difficult angles for "
                "the opponent to return. Staying calm and focused, especially as the ball's speed increases, is key to "
                "maintaining control and ultimately winning the game. With practice and strategic play, players can master "
                "the timing and precision needed to dominate in Pong."
            )

        def draw_instructions(self):
            paragraphs = self.instruction_text.split("\n\n")
            y_offset = 165

            for paragraph in paragraphs:
                words = paragraph.split(" ")
                lines = []
                current_line = ""

                for word in words:
                    test_line = f"{current_line} {word}".strip()
                    if self.instruction_font.size(test_line)[0] < WIDTH - 40:
                        current_line = test_line
                    else:
                        lines.append(current_line)
                        current_line = word

                lines.append(current_line)

                for line in lines:
                    text_surface = self.instruction_font.render(line, True, (255, 255, 255))
                    self.screen.blit(text_surface, (20, y_offset))
                    y_offset += self.instruction_font.get_height() + 5

                y_offset += self.instruction_font.get_height()

        def draw(self):
            self.screen.fill(BG_COLOR)
            self.title()
            if self.show_buttons:
                for button in self.buttons:
                    button.draw()
            elif self.instruction_text:
                self.draw_instructions()


        def handle_events(self):
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.is_running = False
                    break

                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE and not self.show_buttons:
                        if self.show_buttons:
                            pg.quit()
                            sys.exit()
                        else:
                            self.show_buttons = True

                    elif event.key == pg.K_m:
                        if self.is_mute:
                            self.music.play()
                        else:
                            self.music.mute()
                        self.is_mute = not self.is_mute

                    elif event.key == pg.K_f:
                        self.toggle_fullscreen()

                elif event.type == pg.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    for button in self.buttons:
                        if button.is_clicked(mouse_pos):
                            if self.show_buttons:
                                if button.text == "Instructions":
                                    self.instructions()
                                elif button.text == "Play":
                                    self.play()
                                elif button.text == "Quit":
                                    pg.quit()
                                    sys.exit()

        def run(self):
            while self.is_running:
                self.clock.tick(FPS)
                self.handle_events()
                self.update()
            pg.quit()
            sys.exit()


    if __name__ == "__main__":
        menu = Menu()
        menu.play_music()
        menu.run()

except KeyboardInterrupt:
    print("\nGame terminated.")
