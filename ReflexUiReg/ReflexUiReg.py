"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

@rx.page("/","Auth")
def render_auth_page():
    return rx.center(
                rx.vstack(
                    rx.hstack(
                        rx.color_mode.button(),
                        justify="center",
                        width="100%"
                    ),
                    rx.vstack(
                        rx.heading("Creer un Compte",size="6",weight="regular"),
                        rx.text(
                            "Entrer votre email",
                            font_size="10px",
                            weight="medium",
                            color_scheme="amber"
                            ),
                        width="100%",
                        spacing="1",
                        align="center"
                    ),
                    rx.input(
                        width="100%",
                        placeholder="myemail@domaine.com"  
                    ),
                    rx.button(
                        "Se Connecter avec votre Email",
                        width="100%",
                        cursor="pointer",
                        variant="surface",
                        color_scheme="bronze"
                    ),
                    rx.hstack(
                        rx.divider(width="20%"),
                        rx.text("Ou Continuer avec : ",font_size="10px",weight="bronze",color_scheme="gray"),
                        rx.divider(width="20%"),
                        width="100%",
                        align="center",
                        justify="center"    
                    ),
                    rx.button(
                        rx.icon(tag="twitter",size=15),
                        "twitter",
                        width="100%",
                        variant="surface",
                        cursor="pointer",
                        color_scheme="bronze"
                    ),
                    rx.button(
                        rx.icon(tag="linkedin",size=15),
                        "linkedin",
                        width="100%",
                        variant="surface",
                        cursor="pointer",
                        color_scheme="bronze"
                    ),
                    rx.button(
                        rx.icon(tag="Github",size=15),
                        "Github",
                        width="100%",
                        variant="surface",
                        cursor="pointer",
                        color_scheme="bronze"
                    ),
                    width="100%",
                    max_width="50%",
                    height="100%",
                    justify="center",
                    align="center"
                ),
        width="100%",
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
