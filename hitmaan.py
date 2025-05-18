# OG CLI Tool - "HitMaan 2.0"
# Built with 💻 Python + Terminal Swagger
# Functions like Postman but feels like Linux

import requests
import json
import os
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, Confirm
from rich.panel import Panel
from urllib.parse import urlparse

console = Console()


def print_header():
    console.rule("[bold blue]🔥 HitMaan 2.0 - Your Terminal API Buddy 🔥")
    console.print("\nDeveloped by Alhan ✦ Inspired by FOSS\n")


def get_method():
    return Prompt.ask("[bold cyan]Choose HTTP Method", choices=["GET", "POST", "PUT", "DELETE"], default="GET")


def get_url():
    return Prompt.ask("[bold yellow]Enter full URL (e.g., https://api.example.com/endpoint)")


def get_headers():
    raw = Prompt.ask("[bold magenta]Enter Headers as JSON (or leave empty)", default="{}")
    try:
        return json.loads(raw)
    except:
        console.print("[red]Invalid JSON for headers. Using empty headers.")
        return {}


def get_body():
    raw = Prompt.ask("[bold green]Enter Request Body as JSON (or leave empty)", default="{}")
    try:
        return json.loads(raw)
    except:
        console.print("[red]Invalid JSON for body. Using empty body.")
        return {}


def get_form_data():
    form_data = {}
    console.print("[bold green]Enter Form Data (press enter to stop):")
    while True:
        key = Prompt.ask("Key", default="").strip()
        if not key:
            break
        val = Prompt.ask("Value", default="").strip()
        form_data[key] = val
    return form_data


def display_response(res):
    console.print(Panel.fit(f"[bold green]Status: {res.status_code}"))

    table = Table(title="Response Headers")
    table.add_column("Key", style="cyan")
    table.add_column("Value", style="magenta")
    for k, v in res.headers.items():
        table.add_row(k, v)
    console.print(table)

    console.print("\n[bold blue]Response Body:")
    try:
        parsed = res.json()
        console.print_json(json.dumps(parsed, indent=2))
    except:
        console.print(res.text)


def run():
    print_header()

    method = get_method()
    url = get_url()
    headers = get_headers()

    use_form = Confirm.ask("[bold cyan]Do you want to send form-data instead of raw JSON?", default=False)

    data = get_form_data() if use_form else get_body()

    try:
        with console.status("[bold green]Sending request..."):
            if method == "GET":
                res = requests.get(url, headers=headers)
            elif method == "POST":
                res = requests.post(url, headers=headers, data=data if use_form else None, json=None if use_form else data)
            elif method == "PUT":
                res = requests.put(url, headers=headers, data=data if use_form else None, json=None if use_form else data)
            elif method == "DELETE":
                res = requests.delete(url, headers=headers)
        display_response(res)

    except Exception as e:
        console.print(f"[bold red]Request Failed: {e}")


if __name__ == "__main__":
    run()
