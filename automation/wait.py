from automation.selector import _action, _selector


def until_visible(seconds, text=None, id=None, index=None, point=None, width=None, height=None, tolerance=None,
                  enabled=None, checked=None, focused=None, selected=None, repeat=None):
    seconds = seconds * 1000
    _visibility(seconds, text, id, index, point, width, height, tolerance,
                enabled, checked, focused, selected, repeat, "visible")


def until_not_visible(seconds, text=None, id=None, index=None, point=None, width=None, height=None, tolerance=None,
                      enabled=None, checked=None, focused=None, selected=None, repeat=None):
    seconds = seconds * 1000
    _visibility(seconds, text, id, index, point, width, height, tolerance,
                enabled, checked, focused, selected, repeat, "notVisible")


def _visibility(seconds, text=None, id=None, index=None, point=None, width=None,
                height=None,
                tolerance=None,
                enabled=None, checked=None, focused=None, selected=None, repeat=None, type_visibili=""):
    type_visibili = type_visibili.lower()
    _action("extendedWaitUntil", text, id, index, point, width, height, tolerance, enabled, checked, focused,
            selected, repeat, custom_text=type_visibili)
    with open("template.yaml", "a") as file:
        file.write(f"   timeout: {seconds}\n")


def for_animation_to_end(seconds=10):
    seconds = seconds * 1000
    with open("template.yaml", "a") as file:
        file.write(f'- waitForAnimationToEnd: \n')
        file.write(f'   timeout: {seconds}\n')
