import os
import sys
import time
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.progress import track
from googlesearch import search
from modules.logger import logger

console = Console()

# Bersihin layar
def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

# Efek ketik
def slow_print(text, color="white", delay=0.0025):
    for char in text:
        console.print(char, style=color, end="")
        time.sleep(delay)
    print()

# Nanya mau simpen atau nggak
def prompt_save_option():
    try:
        save = Confirm.ask("[yellow][?] Mau simpen hasil pencarian ke file?[/yellow]")
        if save:
            filename = Prompt.ask("[cyan][+] Masukkan nama file (tanpa .txt)[/cyan]")
            return filename
        return None
    except KeyboardInterrupt:
        console.print("\n[bold red][!] Lo ngapain cabut kocak..[/bold red]")
        sys.exit(0)

# Fungsi utama buat cari dork
def dork_search(filename=None):
    try:
        console.print(Panel("[bold cyan]Masukin Dork pencarian lo di bawah ini[/bold cyan]", title="Dork Input", expand=False))
        dork = Prompt.ask("[green]Masukin Dork[/green]")
        limit = Prompt.ask("[green]Jumlah hasil yang mau ditampilkan[/green]", default="10")

        if not limit.isdigit():
            console.print("[bold red][!] Input harus angka, puki![/bold red]")
            return

        console.print(Panel("[yellow]Sedang mencari hasil... sabar ya...[/yellow]", expand=False))
        results = list(search(dork, num_results=int(limit)))

        console.print(Panel(f"[bold green][✓] Hasil ditemukan: {len(results)}[/bold green]", title="Result", expand=False))

        for i, result in enumerate(track(results, description="Menampilkan hasil...")):
            line = f"[{i+1}] {result}"
            console.print(f"[cyan]{line}[/cyan]")
            if filename:
                logger(filename, line)

        console.print(Panel("[bold green]Pencarian selesai bro![/bold green]", title="✔ Done", expand=False))

    except KeyboardInterrupt:
        console.print("\n[bold red][!] Lo cancel di tengah jalan. Gapapa, besok bisa lanjut lagi.[/bold red]")
        sys.exit(1)
