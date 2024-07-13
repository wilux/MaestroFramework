from behave import *

from automation import assertion, tap, send_keys, wait


@given("The user open Stori App")
def step_impl(context):
    with open("template.yaml", "a") as file:
        file.write(f"- launchApp:\n")
        file.write('    clearState: true\n')


@step('The user logins with {username} and {password}')
def step_impl(context, username, password):
    wait.until_visible(60, text="Quiero ser cliente")
    tap.on("Inicia sesión")
    tap.long_press_on("Correo electrónico")
    send_keys.text(username)
    tap.on("Iniciar sesión")
    tap.long_press_on("Contraseña")
    send_keys.text(password)
    tap.on("Inicia sesión", index=1)

