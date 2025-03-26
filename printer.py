import rich
import utils
from rich.console import Console
from rich.table import Table
console=Console()
def printCostTable(type:str,
                   buying_cost_company:str,
                   buying_cost_snow:str,
                   boost_cost_company:str,
                   boost_cost_snow:str
                   )->None:
    table=Table(show_header=True,show_lines=True,header_style="bold #f92672")
    table.add_column("Type of price")
    table.add_column("Coins")
    if type=="company":
        table.add_row("Buying",buying_cost_company)
        table.add_row("Boost",boost_cost_company)
    if type=="snow":
        table.add_row("Buying",buying_cost_snow)
        table.add_row("Boost",boost_cost_snow)
    console.print(table)
def printActionTable(type):
    table=Table(show_header=True,show_lines=True,header_style="bold green")
    table.add_column("Action")
    table.add_column("Command")
    if type=="company":
        table.add_row("Clean","Enter")
    elif type=="snow":
        table.add_row("Snow","Enter")
    table.add_row("Boost","0")
    table.add_row("Buy","1")
    table.add_row("Make save for battle","2")
    table.add_row("Exit","exit")
    console.print(table)
def printInfoTable(type:str,
                   used_type_company:str,
                   used_type_snow:str,
                   effect_company:str,
                   effect_snow:str,
                   strength_company:str,
                   strength_snow:str,
                   coins_company:str,
                   coins_snow:str,
                   count_company:str,
                   count_snow:str
                   )->None:
    table=Table(show_header=True,show_lines=True,header_style="bold magenta")
    table.add_column("Entity")
    table.add_column("Tool")
    table.add_column("Effective")
    table.add_column("Strength")
    table.add_column("Coins")
    table.add_column("Count of tool")
    if type=="company":
        table.add_row("You",
                      used_type_company,
                      str(int(effect_company)*int(count_company)),
                      strength_company,
                      coins_company,
                      count_company
                      )
        table.add_row("Enemy",
                      used_type_snow,
                      str(int(effect_snow)*int(count_snow)),
                      strength_snow,
                      coins_snow,
                      count_snow
                      )
    elif type=="snow":
        table.add_row("You",
                      used_type_snow,
                      str(int(effect_snow)*int(count_snow)),
                      strength_snow,
                      coins_snow,
                      count_snow
                      )
        table.add_row("Enemy",
                      used_type_company,
                      str(int(effect_company)*int(count_company)),
                      strength_company,
                      coins_company,
                      count_company
        )
    console.print(table)
def chooseMode()->str:
    utils.clear_console()
    type=None
    table=Table(show_header=True,show_lines=True,header_style="bold blue")
    table.add_column("Mode")
    table.add_column("Command")
    table.add_row("Fight with bot for [bold cyan]snow clean company[/bold cyan]","company")
    table.add_row("Fight with bot for [bold cyan]snow weather[/bold cyan]","snow")
    table.add_row("Fight against save","save")
    console.print(table)
    type=input("Write here: ")
    while True:
        if type.lower()!="company" or type.lower()!="snow":
            break
        utils.clear_console()
        console.print(table)
        print("Try again")
        type=input("Write here: ")
    return type
def youWin()->str:
    utils.clear_console()
    console.rule(":tada: [bold #ffd700]Congratulations, you’ve won! :trophy: [/bold #ffd700]")
    console.print("Your efforts and strategic thinking have paid off! You’ve defeatead your enemy and achieved victory! ")
    console.print("Let this be a step towards new adventures!")
def youLose()->str:
    utils.clear_console()
    console.rule(":disappointed:[bold #ff0000] Unfortunately, you've lost...[/bold #ff0000] :crossed_swords:  ",style="#ff0000")
    console.print("Your enemy was stronger, and luck wasn't on your side today")
    console.print("Don’t despair!  ")
    console.print("It’s time to train harder and come back with renewed strength!  ",style="bold")