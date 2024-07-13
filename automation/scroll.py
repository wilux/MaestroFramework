from automation.selector import _selector


def up():
    with open("template.yaml", "a") as file:
        file.write(f'- scroll: \n')


def until_visible_element(text=None, id=None, index=None, point=None, width=None, height=None, tolerance=None,
                          enabled=None, checked=None, focused=None, selected=None, optional=None, repeat=None,
                          delay=None, direction="DOWN", timeout=20000, speed=40, visibilityPercentage=100, centerElement=False):
    with open("template.yaml", "a") as file:
        file.write(f'- scrollUntilVisible: \n')
        file.write(f'   element: \n')
        _selector(text, id, index, point, width, height, tolerance, enabled, checked, focused, selected,
                  optional, repeat, delay)
        file.write(f'   {direction}: \n')
        file.write(f'   {timeout}: \n')
        file.write(f'   {speed}: \n')
        file.write(f'   {visibilityPercentage}: \n')
        file.write(f'   {str(centerElement).lower()}: \n')


