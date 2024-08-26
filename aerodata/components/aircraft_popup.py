import reflex as rx
from reflex_motion import motion

def aircraft_popup(aircraft_name: str, capacity: str, range: str):
    return rx.alert_dialog.root(
        motion(rx.alert_dialog.trigger(
            rx.button(aircraft_name),
        ),
        while_hover={"scale": 1.2},
        while_tap={"scale": 0.9},
        transition={"type": "spring", "stiffness": 400, "damping": 17},),
        rx.alert_dialog.content(
            rx.alert_dialog.title(f"{aircraft_name}"),
            rx.alert_dialog.description(
                rx.text(f"Range: {range}"),
                rx.text(f"Max Capacity: {capacity}")
            ),
            rx.flex(
                rx.alert_dialog.cancel(
                    rx.button("Close"),
                ),
                spacing="3",
            ),
        ),
    )