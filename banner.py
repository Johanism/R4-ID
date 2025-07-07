from rich.panel import Panel
from rich.align import Align
from rich.text import Text

def get_banner():
    ascii_art = r"""
     ____  __ __  ________
    / __ \/ // / /  _/ __ \
   / /_/ / // /_ / // / / /
  / _, _/__  __// // /_/ /
/_/ |_|  /_/ /___/_____/

    """
    author = "Recon for Information Dorking by yallism."
    full_text = f"{ascii_art}\n{author}"

    return Panel(
        Align.center(Text(full_text, justify="center", style="bold cyan")),
        title="[bold red]yallism[/bold red]",
        border_style="bold red",
        expand=False
    )
