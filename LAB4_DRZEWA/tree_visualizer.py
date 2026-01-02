
def display_tree(tree):
    if not tree.root:
        print("Empty tree.")
        return

    lines, *_ = _display_aux(tree.root)
    for line in lines:
        print(line)

def _display_aux(node):
    """Funkcja pomocnicza generująca ASCII-art."""
    if node.right is None and node.left is None:
        line = str(node.key)
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    if node.right is None:
        lines, n, p, x = _display_aux(node.left)
        s = str(node.key)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * ' ' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

    if node.left is None:
        lines, n, p, x = _display_aux(node.right)
        s = str(node.key)
        u = len(s)
        first_line = s + x * ' ' + (n - x) * ' '
        second_line = (u) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

    left, n, p, x = _display_aux(node.left)
    right, m, q, y = _display_aux(node.right)
    s = str(node.key)
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * ' ' + s + y * ' ' + (m - y) * ' '
    second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)
    zipped_lines = zip(left, right)
    lines = [a + u * ' ' + b for a, b in zipped_lines]
    return [first_line, second_line] + lines, n + m + u, max(p, q) + 2, n + u // 2
