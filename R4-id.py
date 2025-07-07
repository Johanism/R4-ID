from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm
from rich.prompt import Prompt
from modules.banner import get_banner
from modules.play import play_music
from modules.core import clear_screen, slow_print, dork_search

console = Console()

def prompt_save_option():
    try:
        save = Confirm.ask("[yellow]Mau simpen hasil pencarian ke file?[/yellow]")
        if save:
            filename = Prompt.ask("[cyan]Masukin nama file (tanpa .txt)[/cyan]")
            return filename + ".txt" if not filename.endswith(".txt") else filename
        return None
    except KeyboardInterrupt:
        console.print("[bold red]\n[!] Lo cabut mendadak... Keluar deh.[/bold red]")
        exit(0)

def main():
    clear_screen()
    play_music()
    console.print(get_banner())  # banner dari banner.py

    # quote keren
    quote = "[italic red]Semua log nunjukin dia gak balik... tapi gue masih nunggu.[/italic red]"
    console.print(Panel(quote, title="[bold white]QUOTE[/bold white]", border_style="red", expand=False))

    console.print()
    filename = prompt_save_option()
    dork_search(filename)

if __name__ == "__main__":
    main()
