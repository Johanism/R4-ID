from rich.console import Console

console = Console()

def logger(filename, line):
    try:
        with open(f"{filename}.txt", "a", encoding="utf-8") as file:
            file.write(str(line) + "\n")
    except Exception as e:
        console.print(f"[bold red][!] Gagal nyimpen log ke file {filename}.txt: {e}[/bold red]")
