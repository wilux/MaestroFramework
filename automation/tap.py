from automation.selector import _action


def on(text=None, id=None, index=None, point=None, width=None, height=None, tolerance=None,
       enabled=None, checked=None, focused=None, selected=None, optional=None, repeat=None, delay=None):
    _action("tapOn", text, id, index, point, width, height, tolerance, enabled, checked, focused, selected, optional,
            repeat, delay)


def long_press_on(text=None, id=None, index=None, point=None, width=None, height=None, tolerance=None,
                  enabled=None, checked=None, focused=None, selected=None, optional=None, repeat=None, delay=None):
    _action("longPressOn", text, id, index, point, width, height, tolerance, enabled, checked, focused, selected,
            optional,
            repeat, delay)


def double_on(text=None, id=None, index=None, point=None, width=None, height=None, tolerance=None,
              enabled=None, checked=None, focused=None, selected=None, optional=None, repeat=None, delay=None):
    _action("doubleTapOn", text, id, index, point, width, height, tolerance, enabled, checked, focused, selected,
            optional,
            repeat, delay)
