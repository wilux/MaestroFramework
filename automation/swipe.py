from automation.selector import _selector


def direction_reference(direction="UP", duration=400):
    with open("template.yaml", "a") as file:
        file.write(f'- swipe: \n')
        file.write(f'   direction: {direction}\n')
        file.write(f'   duration: {duration}\n')


def direction_relative(s1=90, s2=50, e1=10, e2=50, duration=400):
    with open("template.yaml", "a") as file:
        file.write(f'- swipe: \n')
        file.write(f'   start: {s1}, {s2}\n')
        file.write(f'   end: {e1}, {e2}\n')
        file.write(f'   duration: {duration}\n')


def direction_coordinate(s1=90, s2=50, e1=10, e2=50, duration=400):
    with open("template.yaml", "a") as file:
        file.write(f'- swipe: \n')
        file.write(f'   start: {s1}%, {s2}%\n')
        file.write(f'   end: {e1}%, {e2}%\n')
        file.write(f'   duration: {duration}\n')


def to_element(text=None, id=None, index=None, point=None, width=None, height=None, tolerance=None,
               enabled=None, checked=None, focused=None, selected=None, optional=None, repeat=None,
               delay=None, direction="DOWN"):
    with open("template.yaml", "a") as file:
        file.write(f'- swipe: \n')
        file.write(f'   from: \n')
        _selector(text, id, index, point, width, height, tolerance, enabled, checked, focused, selected,
                  optional, repeat, delay)
        file.write(f'   {direction}: \n')

