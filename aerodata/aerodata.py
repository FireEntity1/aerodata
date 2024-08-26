"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from reflex_motion import motion
from aerodata.components.aircraft_popup import aircraft_popup

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.center(rx.vstack(
            rx.center( rx.heading("AeroData", size="9"), ),
            rx.divider(),
            rx.heading("AIRBUS", size="8"),
            rx.divider(),

            rx.heading("A320 Family", size="6"),
            aircraft_popup("Airbus A319", "150PAX", "3700NMi (CEO/NEO)"),
            aircraft_popup("Airbus A320", "180PAX", "3000NMi (CEO)  |  3700NMi (NEO)"),
            aircraft_popup("Airbus A321", "220PAX", "3000NMi (CEO)  |  4700NMi (XLR)"),

            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        ),
    )


app = rx.App()
app.add_page(index)
