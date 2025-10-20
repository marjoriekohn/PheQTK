from shutil import get_terminal_size
import textwrap


def terminal_width(default: int = 80) -> int:
    try:
        return get_terminal_size().columns
    except Exception:
        return default


def rule(title: str = "", char: str = "─") -> None:
    width = terminal_width()
    if title:
        pad = f" {title} "
        side = (width - len(pad)) // 2
        print(char * max(side, 0) + pad + char * max(width - len(pad) - side, 0))
    else:
        print(char * width)


def para(text: str, indent: int = 0) -> None:
    # Wrap long paragraphs to the terminal width with optional indentation
    width = max(terminal_width() - indent, 40)
    print(textwrap.fill(text, width=width, subsequent_indent=" " * indent, initial_indent=" " * indent))


def bullet(text: str) -> None:
    para(f"• {text}")


def step(n: int, title: str) -> None:
    rule(f"Step {n}: {title}")
