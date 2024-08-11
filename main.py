import pygame as pg
from variables import *
from paddle import Paddle
from ball import Ball
import sys

try:
    class PongGame:
        def __init__(self, game):
            pg.init()
            pg.display.set_caption("Pong Game")

            self.game = game
            self.screen = game.screen
            self.clock = game.clock
            self.score_font = pg.font.Font("resorces/font/font.ttf", SCORE_FONT_SIZE)

            self.left_paddle = Paddle(self,
                                 10,
                                 HEIGHT // 2 - PADDLE_HEIGHT // 2,
                                 PADDLE_WIDTH, PADDLE_HEIGHT)
            self.right_paddle = Paddle(self,
                                  WIDTH - 10 - PADDLE_WIDTH,
                                  HEIGHT // 2 - PADDLE_HEIGHT // 2,
                                  PADDLE_WIDTH, PADDLE_HEIGHT)

            self.ball = Ball(self, WIDTH // 2, HEIGHT // 2, BALL_RADIUS)

            self.left_score = 0
            self.right_score = 0

            self.is_running = True
            self.is_mute = False
            self.is_fullscreen = False
            self.won = False

        def update(self):
            self.draw([self.left_paddle, self.right_paddle])
            self.handle_paddle_movement()
            self.handle_collisions()
            self.ball.move()
            self.update_scores()
            pg.display.flip()

        def handle_paddle_movement(self):
            keys = pg.key.get_pressed()

            if keys[pg.K_w] and self.left_paddle.y - PADDLE_VEL >= 0:
                self.left_paddle.move_up()
            if keys[pg.K_s] and self.left_paddle.y + PADDLE_VEL + self.left_paddle.height <= HEIGHT:
                self.left_paddle.move_down()

            if keys[pg.K_UP] and self.right_paddle.y - PADDLE_VEL >= 0:
                self.right_paddle.move_up()
            if keys[pg.K_DOWN] and self.right_paddle.y + PADDLE_VEL + self.right_paddle.height <= HEIGHT:
                self.right_paddle.move_down()

        def handle_collisions(self):
            if self.ball.y + self.ball.radius >= HEIGHT:
                self.ball.y_vel *= -1
            elif self.ball.y - self.ball.radius <= 0:
                self.ball.y_vel *= -1

            if self.ball.x_vel < 0:
                if self.left_paddle.y <= self.ball.y <= self.left_paddle.y + self.left_paddle.height:
                    if self.ball.x - self.ball.radius <= self.left_paddle.x + self.left_paddle.width:
                        self.adjust_ball_vel()
            else:
                if self.right_paddle.y <= self.ball.y <= self.right_paddle.y + self.right_paddle.height:
                    if self.ball.x + self.ball.radius >= self.right_paddle.x:
                        self.adjust_ball_vel()

        def adjust_ball_vel(self):
            self.ball.x_vel *= -1

            middle_y = self.left_paddle.y + self.left_paddle.height / 2
            difference_in_y = middle_y - self.ball.y
            reduction_factor = (self.left_paddle.height / 2) / MAX_BALL_VEL
            y_vel = difference_in_y / reduction_factor
            self.ball.y_vel = -1 * y_vel

        def update_scores(self):
            if self.ball.x < 0:
                self.right_score += 1
                self.ball.reset()
            elif self.ball.x > WIDTH:
                self.left_score += 1
                self.ball.reset()

            won = False
            win_text = ""

            if self.left_score >= WINNING_SCORE:
                won = True
                win_text = "Left Player Won!"
            elif self.right_score >= WINNING_SCORE:
                won = True
                win_text = "Right Player Won!"

            if won:
                text = self.score_font.render(win_text, 1, TEXT_COLOR)
                self.screen.blit(text, (WIDTH // 2 - text.get_width() //
                                2, HEIGHT // 2 - text.get_height() // 2))
                pg.display.update()
                pg.time.delay(3000)
                self.ball.reset()
                self.left_paddle.reset()
                self.right_paddle.reset()
                self.left_score = 0
                self.right_score = 0

        def draw(self, paddles):
            self.screen.fill(BG_COLOR)

            left_score_text = self.score_font.render(f"{self.left_score}", 1, SCORE_COLOR)
            right_score_text = self.score_font.render(f"{self.right_score}", 1, SCORE_COLOR)
            self.screen.blit(left_score_text,
                             (WIDTH // 4 - left_score_text.get_width()
                              // 2, 20))
            self.screen.blit(right_score_text,
                             (WIDTH * 3 / 4 - right_score_text.get_width()
                              // 2, 20))

            for paddle in paddles:
                paddle.draw()

            for i in range(10, HEIGHT, HEIGHT // 20):
                if i % 2 == 1:
                    continue
                pg.draw.rect(self.screen, LINE_COLOR, (WIDTH // 2 - 5, i, 10, HEIGHT // 20))

                self.ball.draw()

        def handle_events(self):
            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    self.is_running = False
                    break

                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_m:
                        if self.is_mute:
                            self.game.music.play()
                        else:
                            self.game.music.mute()
                        self.is_mute = not self.is_mute

                    elif event.key == pg.K_f:
                        self.game.toggle_fullscreen()

        def run(self):
            while self.is_running:
                self.clock.tick(FPS)
                self.handle_events()
                self.update()
            pg.quit()
            sys.exit(0)

except KeyboardInterrupt:
    print("\nGame terminated.")
