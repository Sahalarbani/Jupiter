#!/usr/bin/python

import random
import requests
from time import sleep
import os, signal, sys
from pyfiglet import figlet_format
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.text import Text
from rich.style import Style

__CHANNEL_USERNAME__ = "CPMNuker"
__GROUP_USERNAME__   = "CPMNukerChat"

def signal_handler(sig, frame):
    print("\n Bye Bye...")
    sys.exit(0)

def gradient_text(text, colors):
    lines = text.splitlines()
    height = len(lines)
    width = max(len(line) for line in lines)
    colorful_text = Text()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != ' ':
                color_index = int(((x / (width - 1 if width > 1 else 1)) + (y / (height - 1 if height > 1 else 1))) * 0.5 * (len(colors) - 1))
                color_index = min(max(color_index, 0), len(colors) - 1)  # Ensure the index is within bounds
                style = Style(color=colors[color_index])
                colorful_text.append(char, style=style)
            else:
                colorful_text.append(char)
        colorful_text.append("\n")
    return colorful_text

def banner(console):
    os.system('cls' if os.name == 'nt' else 'clear')
    brand_name = figlet_format('CPMNuker', font='drpepper')
    colors = [
        "rgb(255,0,0)", "rgb(255,69,0)", "rgb(255,140,0)", "rgb(255,215,0)", "rgb(173,255,47)", 
        "rgb(0,255,0)", "rgb(0,255,255)", "rgb(0,191,255)", "rgb(0,0,255)", "rgb(139,0,255)",
        "rgb(255,0,255)"
    ]
    colorful_text = gradient_text(brand_name, colors)
    console.print(colorful_text, end=None)
    console.print("[bold green]♕ CPMNuker[/bold green]: Car Parking Multiplayer Hacking Tool.")
    console.print(f"[bold green]♕ Telegram[/bold green]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue] or [bold blue]@{__GROUP_USERNAME__}[/bold blue].")
    console.print("[bold red]==================================================[/bold red]")
    console.print("[bold yellow]! Note[/bold yellow]: Logout from CPM before using this tool !.", end="\n\n")

def load_player_data(cpm):
    response = cpm.get_player_data()
    if response.get('ok'):
        data = response.get('data')
        if 'floats' in data and 'localID' in data and 'money' in data and 'coin' in data:
            console.print("[bold][red]================[/red][ PLAYER DETAILS ][red]================[/red][/bold]")
            console.print(f"[bold green]Name   [/bold green]: { (data.get('Name') if 'Name' in data else 'UNDEFINED') }.")
            console.print(f"[bold green]LocalID[/bold green]: { (data.get('localID') if 'localID' in data else 'UNDEFINED') }.")
            console.print(f"[bold green]Money  [/bold green]: { (data.get('money') if 'money' in data else 'UNDEFINED') }.")
            console.print(f"[bold green]Coins  [/bold green]: { (data.get('coin') if 'coin' in data else 'UNDEFINED') }.")
        else:
            console.print("[bold red]! ERROR[/bold red]: new accounts must be signed-in to the game at least once !.")
            exit(1)
    else:
        console.print("[bold red]! ERROR[/bold red]: seems like your login is not properly set !.")
        exit(1)
    
def load_key_data(cpm):
    data = cpm.get_key_data()
    console.print("[bold][red]==================================================[/red][/bold]")
    console.print(f"[bold green]Access Key [/bold green]: { data.get('access_key') }.")
    console.print(f"[bold green]Telegram ID[/bold green]: { data.get('telegram_id') }.")
    console.print(f"[bold green]Balance    [/bold green]: { (data.get('coins') if not data.get('is_unlimited') else 'Unlimited') }.")

def load_client_details():
    response = requests.get("http://ip-api.com/json")
    data = response.json()
    console.print("[bold][red]==================================================[/red][/bold]")
    console.print(f"[bold][green]Location[/bold][/green]: {data.get('city')}, {data.get('regionName')}, {data.get('countryCode')}")
    console.print(f"[bold][green]ISP[/bold][/green]     : {data.get('isp')}")
    console.print("[bold][red]===================[/red][ SERVICES ][red]===================[/red][/bold]")

def prompt_valid_value(content, tag, password=False):
    while True:
        value = Prompt.ask(content, password=password)
        if not value or value.isspace():
            print(f"{tag} cannot be empty or just spaces. Please try again.")
        else:
            return value

def interpolate_color(start_color, end_color, fraction):
    start_rgb = tuple(int(start_color[i:i+2], 16) for i in (1, 3, 5))
    end_rgb = tuple(int(end_color[i:i+2], 16) for i in (1, 3, 5))
    interpolated_rgb = tuple(int(start + fraction * (end - start)) for start, end in zip(start_rgb, end_rgb))
    return "{:02x}{:02x}{:02x}".format(*interpolated_rgb)

def rainbow_gradient_string(customer_name):
    modified_string = ""
    num_chars = len(customer_name)
    start_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    end_color = "{