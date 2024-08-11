import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
BUTTON_WIDTH, BUTTON_HEIGHT = 250, 70  # Increase button size
BUTTON_MARGIN = 30  # Increase margin between buttons
FONT_SIZE = 40  # Increase font size for better readability

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Fonts
FONT = pygame.font.Font(None, FONT_SIZE)
INSTRUCTION_FONT = pygame.font.Font(None, 24)  # Smaller font for instructions


class Buttons:
    def __init__(self, text, position):
        self.text = text
        self.position = position
        self.rect = pygame.Rect(position[0], position[1], BUTTON_WIDTH, BUTTON_HEIGHT)
        self.color = WHITE

    def draw(self, screen):
        # Draw button rectangle
        pygame.draw.rect(screen, self.color, self.rect)

        # Render the text
        text_surface = FONT.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.title_font = pygame.font.Font(None, 48)
        self.title_text = "Game Menu"
        self.show_buttons = True  # Flag to show/hide buttons
        self.instruction_text = None  # Placeholder for instruction text

        # Create buttons
        self.buttons = [
            Buttons("Play", (SCREEN_WIDTH // 2 - BUTTON_WIDTH // 2, 200)),
            Buttons("Instructions", (SCREEN_WIDTH // 2 - BUTTON_WIDTH // 2, 200 + BUTTON_HEIGHT + BUTTON_MARGIN)),
            Buttons("Quit", (SCREEN_WIDTH // 2 - BUTTON_WIDTH // 2, 200 + 2 * (BUTTON_HEIGHT + BUTTON_MARGIN)))
        ]

    def draw(self):
        # Fill the screen with black background
        self.screen.fill(BLACK)

        # Draw the title
        title_surface = self.title_font.render(self.title_text, True, WHITE)
        title_rect = title_surface.get_rect(center=(SCREEN_WIDTH // 2, 100))
        self.screen.blit(title_surface, title_rect)

        # Draw the buttons if they should be shown
        if self.show_buttons:
            for button in self.buttons:
                button.draw(self.screen)
        # Otherwise, draw the instructions text
        elif self.instruction_text:
            self.draw_instructions()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if self.show_buttons:
                for button in self.buttons:
                    if button.is_clicked(mouse_pos):
                        if button.text == "Play":
                            print("Play")
                        elif button.text == "Instructions":
                            self.instructions()
                        elif button.text == "Quit":
                            print("Quit")
                            pygame.quit()
                            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if self.show_buttons:
                    pygame.quit()
                    sys.exit()
                else:
                    self.show_buttons = True  # Show buttons again (return to main menu)

    def instructions(self):
        # Hide the buttons
        self.show_buttons = False

        # Instruction text
        self.instruction_text = (
            "Pong is a simple yet iconic video game that simulates table tennis. The objective is straightforward: "
            "players aim to score points by getting the ball past their opponent's paddle. The game is typically "
            "played by two players, each controlling a paddle on either side of the screen. Player 1 usually controls "
            "the left paddle using the up and down arrow keys, while Player 2 controls the right paddle using the "
            '"W" and "S" keys. The game starts with the ball in the center of the screen, and it moves in a random '
            "direction to begin play.\n\n"
            "As the game progresses, players move their paddles up and down to hit the ball back and forth across the "
            "screen. The ball bounces off the paddles and walls, changing direction based on where it hits. If a player "
            "fails to return the ball and it passes their paddle, the opponent scores a point. The first player to reach "
            "a set number of points, typically 11 or 21, wins the game.\n\n"
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
        # Wrap the instruction text to fit the screen
        y_offset = 150
        words = self.instruction_text.split(" ")
        lines = []
        current_line = ""

        for word in words:
            test_line = f"{current_line} {word}".strip()
            if INSTRUCTION_FONT.size(test_line)[0] < SCREEN_WIDTH - 40:  # 40 pixels padding
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word

        lines.append(current_line)

        # Render each line of the instruction text
        for line in lines:
            text_surface = INSTRUCTION_FONT.render(line, True, WHITE)
            self.screen.blit(text_surface, (20, y_offset))
            y_offset += INSTRUCTION_FONT.get_height() + 5  # Add some space between lines


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Game Menu")

    menu = Menu(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            menu.handle_event(event)

        menu.draw()
        pygame.display.flip()


if __name__ == "__main__":
    main()

