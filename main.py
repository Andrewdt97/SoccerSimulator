import random
from table import League
from team import Team




if __name__ == '__main__':
    prem = League('Premier League')
    prem.addTeam(Team('Chelsea', 90))
    prem.addTeam(Team('Spurs', 95))
    prem.addTeam(Team('Arsenal', 75))
    prem.addTeam(Team('Liver', 85))
    prem.addTeam(Team('ManCity', 87))
    prem.addTeam(Team('Man Utd', 85))
    prem.addTeam(Team('Everton', 78))
    prem.addTeam(Team('WBA', 70))
    prem.addTeam(Team('WHU', 68))
    prem.addTeam(Team('Watford', 67))
    prem.addTeam(Team('Stoke', 66))
    prem.printTable()
    
 
            