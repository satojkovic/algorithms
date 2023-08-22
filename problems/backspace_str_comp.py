def backspace_str_comp(s, t):
    def emulate_input_text(s):
        stack = []
        for c in s:
            if c != "#":
                stack.append(c)
            else:
                if stack:
                    stack.pop()
        return "".join(stack)

    return emulate_input_text(s) == emulate_input_text(t)


def test_backspace_str_comp():
    assert backspace_str_comp("ab#c", "ad#c") is True
    assert backspace_str_comp("ab##", "cd##") is True
    assert backspace_str_comp("#", "##") is True
    assert backspace_str_comp("c#d", "cde") is False
    assert backspace_str_comp("ab#cd", "dc#ba") is False
