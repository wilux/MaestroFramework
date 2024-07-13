import inspect


def _action(action, text=None, id=None, index=None, point=None, width=None, height=None, tolerance=None,
            enabled=None, checked=None, focused=None, selected=None, optional=None, repeat=None, delay=None,
            custom_text=None):
    sig = inspect.signature(_action)
    bound_args = sig.bind_partial(text, id, index, point, width, height, tolerance,
                                  enabled, checked, focused, selected, optional, repeat, delay, custom_text)

    positional_args = bound_args.args
    with open("template.yaml", "a") as file:
        if len(positional_args) == 0:
            file.write(f'- {action}: "{text}"\n')
            file.close()
        else:
            file.write(f'- {action}: \n')
            file.close()
            _selector(text, id, index, point, width, height, tolerance, enabled, checked, focused, selected,
                      optional, repeat, delay, custom_text)


def _selector(text=None, id=None, index=None, point=None, width=None, height=None, tolerance=None,
              enabled=None, checked=None, focused=None, selected=None, optional=None, repeat=None, delay=None,
              custom_text=None):
    """
     text: "Text"     # (optional) Finds text or accessibility text that matches regexp.
     id: "id"         # (optional) Finds id that matches regexp
     index: 0         # (optional) 0-based index of the view to select among those that match all other criteria
     point: 50%,50%.  # (optional) Relative position on screen. 50%,50%: Middle of screen
     point: 50, 50    # (optional) Exact coordinates on screen, x:50 y:50, in pixels.
     width: 100       # (optional) Finds element of a given width
     height: 100      # (optional) Finds element of a given height
     tolerance: 10    # (optional) Tolerance to apply when comparing width and height
     enabled: true    # (optional) Searches for view with a given "enabled" state
     checked: true    # (optional) Searches for view with a given "checked" state
     focused: true    # (optional) Searches for view with a given "focused" state
     selected: true   # (optional) Searches for view with a given "selected" state
     optional: false  # (default: false) If set to true, test won't fail if view can't be found
     repeat: 3        # In some cases it is desirable to repeat taps. Default 1
     delay: 500       # Delay between taps. Default 100ms
    """
    sig = inspect.signature(_selector)
    bound_args = sig.bind_partial(text, id, index, point, width, height, tolerance,
                                  enabled, checked, focused, selected, optional, repeat, delay)
    params = {k: v for k, v in bound_args.arguments.items()}

    with open("template.yaml", "a") as file:
        for param, value in params.items():
            if value is not None:
                if "text" in param or "id" in param:
                    if custom_text is not None:
                        param = custom_text
                    file.write(f'   {param}: "{value}" \n')
                elif "point" in param:
                    value = ", ".join(map(str, value))
                    file.write(f'   {param}: {value} \n')
                elif "enable" in param or "checked" in param or "focused" in param or "selected" in param or "optional" in param:
                    file.write(f'   {param}: {str(value).lower()} \n')
                else:
                    file.write(f'   {param}: {value} \n')
