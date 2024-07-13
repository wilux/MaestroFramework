def key(key_option):
    """
        home - home button

        lock - button to lock the device screen

        enter - enter button

        backspace - backspace button

        volume up and volume down - control the volume

        back - back button (Android only)

        power - power button (Android only)

        tab - tab button (Android only)
    """
    with open("template.yaml", "a") as file:
        file.write(f'- pressKey: {key_option}\n')