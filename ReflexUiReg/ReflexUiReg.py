"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

@rx.page("/","Auth")
def render_auth_page():
    return rx.center(
                rx.vstack(
                    rx.hstack(
                        rx.color_mode.button(position="top-right"),
                        justify="center",
                        width="100%"
                    ),
                    width="100%",
                    max_width="10%",
                    height="100%",
                    justify="center",
                    align="center"
                ),
        width="100",
        height="100vh"
    )

app = rx.App(
        theme=rx.theme(
        appearance="light",
        has_background=True,
        radius="large",
        accent_color="teal",
    )
)
