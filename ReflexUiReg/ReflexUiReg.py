"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

@rx.page("/","Auth")
def render_auth_page():
    return rx.center(
        width="100",
        height="100vh"
    )

app = rx.App(theme=rx.theme( appearance="light", accent_color="crimson"))
