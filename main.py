import saves
import player
import printer
import utils
def game(type:str,company_dict:dict,snow_dict:dict,used_type_company:str,used_type_snow:str,counts=1,coins=0):
    snow=100
    stopSnow=200
    if type=="company":
        snowCompany=player.Player(company_dict,used_type_company,1,0)
        snowWeather=player.Player(snow_dict,used_type_snow,counts,coins)
    elif type=="snow":
        snowCompany=player.Player(company_dict,used_type_company,counts,coins)
        snowWeather=player.Player(snow_dict,used_type_snow,1,0)
    while snow>0 and snowCompany.isLive() and snowWeather.isLive() and snow<stopSnow:
        utils.clear_console()
        printer.printInfoTable(type,
                                    snowCompany.ask("used_type"),
                                    snowWeather.ask("used_type"),
                                    snowCompany.ask("effect"),
                                    snowWeather.ask("effect"),
                                    snowCompany.ask("strength"),
                                    snowWeather.ask("strength"),
                                    snowCompany.ask("coins"),
                                    snowWeather.ask("coins"),
                                    snowCompany.ask("count"),
                                    snowWeather.ask("count")
                                    )
        printer.printCostTable(type,
                                snowCompany.ask("cost"),
                                snowWeather.ask("cost"),
                                snowCompany.ask("boost_cost"),
                                snowWeather.ask("boost_cost")
                                )
        printer.printActionTable(type)
        ans=input("Write here: ")
        if type=="company":
                if ans=="" or ans.lower()=="Enter":
                    snow-=snowCompany.do()
                elif ans=="0":
                    snowCompany.boost()
                elif ans=="1":
                    snowCompany.buy()
                elif ans=="2":
                    saves.makeSave("company",
                                snowCompany.ask("used_type"),
                                snowCompany.ask("count"),
                                snowCompany.ask("coins")
                                )
                else:
                    print(f"Command {ans} is not found")
                    input()
                snow+=snowWeather.bot()
        elif type=="snow":
            if ans=="" or ans.lower()=="Enter":
                snow+=snowWeather.do()
            elif ans=="0":
                snowWeather.boost()
            elif ans=="1":
                snowWeather.buy()
            elif ans=="2":
                saves.makeSave("snow",
                            snowWeather.ask("used_type"),
                            snowWeather.ask("count"),
                            snowWeather.ask("coins")
                            )
            else:
                print(f"Command {ans} is not found")
                input()
            snow-=snowCompany.bot()
    if type=="company":
        if snow<=0 or not(snowWeather.isLive()):
            printer.youWin()
        elif snow>=stopSnow or not(snowCompany.isLive()):
            printer.youLose()
    elif type=="snow":
        if snow<=0 or not(snowCompany.isLive()):
            printer.youLose()
        elif snow>=stopSnow or not(snowWeather.isLive()):
            printer.youWin()
       
    
                
if __name__ == "__main__":
    clean=saves.getDict("company")
    snow=saves.getDict("snow")
    type=printer.chooseMode()
    utils.clear_console()
    if type=="snow" or type=="company":
        game(type,
             clean,
             snow,
             "shovel",
             "rare snow"
             )     
    if type == "save":
        save_tuple=saves.readSave()
        if save_tuple[0]=="company":
            game("snow",
             clean,
             snow,
             save_tuple[1],
             "rare snow",
             save_tuple[2],
             save_tuple[3]
             ) 
        elif save_tuple[0]=="snow":
            game("company",
             clean,
             snow,
             "shovel",
             save_tuple[1],
             save_tuple[2],
             save_tuple[3]
            ) 