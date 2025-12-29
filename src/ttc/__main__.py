import arcade

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
WINDOW_TITLE = "Triple Triad: Console"

SQUARE_WIDTH = 5
SQUARE_HEIGHT = 5
SQUARE_SPACING = 10


class GameView(arcade.View):
    def __init__(self):
        super().__init__()

        self.background_color = arcade.color.DARK_SLATE_GRAY

    def on_draw(self):
        self.clear()

        for x in range(0, WINDOW_WIDTH, SQUARE_SPACING):
            for y in range(0, WINDOW_HEIGHT, SQUARE_SPACING):
                arcade.draw_rect_filled(
                    arcade.rect.XYWH(x, y, SQUARE_WIDTH, SQUARE_HEIGHT),
                    arcade.color.DARK_BLUE,
                )


def main():
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
    game = GameView()
    window.show_view(game)
    arcade.run()


if __name__ == "__main__":
    main()
