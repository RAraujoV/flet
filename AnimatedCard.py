from flet import (
    flet,
    Page,
    UserControl,
    Column,
    Card,
    Container,
    Row,
    alignment,
    colors,
    animation,
    border,
    Text,
    transform,
)


# Class  set up
class AnimatedCard(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        self._icon_container_ = Container(
            visible=False,
            width=120,
            height=35,
            bgcolor=colors.BLUE_800,
            border_radius=25,
            animate_opacity=200,
            offset=transform.Offset(0, 0.25),
            animate_offset=animation.Animation(duration=900, curve="ease"),
            content=Row(
                alignment="center",
                controls=[
                    Text("More info", size=12, weight="w600"),
                ],
            ),
        )

        self._cara = Container(
            width=280,
            height=380,
            bgcolor=colors.WHITE,
            border_radius=12,
            on_hover=lambda e: self.AnimateCardFunction(e),
            animate=animation.Animation(600, "ease"),
            border=border.all(2, colors.WHITE24),
            content=Column(
                alignment="center",
                horizontal_alignment="center",
                spacing=0,
                controls=[
                    Container(
                        padding=20,
                        alignment=alignment.bottom_center,
                        content=Text(
                            "Card Title", color=colors.BLACK, size=28, weight="w800"
                        ),
                    ),
                    Container(
                        padding=20,
                        alignment=alignment.top_center,
                        content=Text(
                            "Card details", color=colors.BLACK, size=14, weight="w500"
                        ),
                    ),
                ],
            ),
        )

        self._carta = Card(
            elevation=0,
            content=Container(
                content=Column(
                    spacing=0,
                    horizontal_alignment="center",
                    controls=[
                        self._cara,
                    ],
                )
            ),
        )
        self._tablero = Column(
            spacing=0,
            horizontal_alignment="center",
            controls=[
                self._carta,
                self._icon_container_,
            ],
        )
        return self._tablero

    def AnimateCardFunction(self, e):
        self._icon_container_.visible = True
        self._icon_container_.update()
        if e.data == "true":
            for __ in range(20):
                self._carta.elevation += 1
                self._carta.update()
            self._cara.border = border.all(4, colors.BLUE_800)
            self._cara.update()
            self._icon_container_.offset = transform.Offset(0, -0.75)
            self._icon_container_.opacity = 1
            self._icon_container_.update()

        else:
            for __ in range(20):
                self._carta.elevation -= 1
                self._carta.update()
            self._cara.border = border.all(4, colors.WHITE24)
            self._cara.update()
            self._icon_container_.offset = transform.Offset(0, 0.5)
            self._icon_container_.opacity = 0
            self._icon_container_.update()


def main(page: Page):
    page.bgcolor = colors.WHITE60
    app = AnimatedCard()
    page.add(app)
    page.update()


if __name__ == "__main__":
    flet.app(target=main)
