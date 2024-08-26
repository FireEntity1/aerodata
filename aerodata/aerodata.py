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
                aircraft_popup("A319", "150PAX", "3700NMi (CEO/NEO)"),
                aircraft_popup("A320", "180PAX", "3000NMi (CEO)  |  3700NMi (NEO)"),
                aircraft_popup("A321", "220PAX", "3000NMi (CEO)  |  4700NMi (XLR)"),

            rx.divider(),
                rx.heading("Airbus A330 Family",size="6"),
                aircraft_popup("A330ceo", "400PAX (-200) | 440PAX (-300)", "7260NMi (-200) | 6340NMi (-300)"),
                aircraft_popup("A330neo", "400PAX (-800) | 440PAX (-900)", "8100NMi (-800) | 7200NMi (-900)"),
            rx.divider(),
                rx.heading("Airbus A340 Family", size="6"),
                aircraft_popup("A340-300","440PAX","7400NMi"),
                aircraft_popup("A340-500/600", "440PAX (-500) | 475PAX (-600)", "9000NMi (-500) | 7800NMi (-600)"),
            rx.divider(),
                rx.heading("Airbus A350 Family", size="6"),
                aircraft_popup("A350-900", "440PAX", "9300NMi (standard) | 9700NMi (ULR)"),
                aircraft_popup("A350-1000","480PAX","8700NMi"),
            rx.divider(),
                rx.heading("Airbus A380"),
                aircraft_popup("A380-800", "840PAX", "8200NMi"),

            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        ),
    )


app = rx.App()
app.add_page(index)
