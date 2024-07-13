from automation.selector import _action


def visible(text=None, id=None, index=None, point=None, width=None, height=None, tolerance=None,
            enabled=None, checked=None, focused=None, selected=None, optional=None, repeat=None, delay=None):
    _action("assertVisible", text, id, index, point, width, height, tolerance, enabled, checked, focused, selected,
            optional,
            repeat, delay)


def not_visible(text=None, id=None, index=None, point=None, width=None, height=None, tolerance=None,
                enabled=None, checked=None, focused=None, selected=None, optional=None, repeat=None, delay=None):
    _action("assertNotVisible", text, id, index, point, width, height, tolerance, enabled, checked, focused, selected,
            optional,
            repeat, delay)
