from team import *
import random

class League:
    
    def __init__(self, name):
        
        self._name = name
        self._numTeams = 0
        
        self._teamsList = []
        
        
    def addTeam(self, team):
        self._teamsList.append(team)
        self._numTeams += 1
        
    def printTable(self):
        teamsListCopy = self._teamsList[:]
        print(self._name + '\nName\t\t\tGP\tW\tD\tL\tPts\tGF\tGA\tGD')
        for i in range(1, len(self._teamsList)+1):
            team = max(teamsListCopy)
            if len(team.getName()) > 12:
                print(str(i) +'. ' + team.getName() + "\t" + str(team.getGamesPlayed()) + '\t' + str(team.getWins()) + "\t" + str(team.getDraws()) + "\t" + str(team.getLoses()) + "\t" + str(team.getPoints()) + "\t" + str(team.getGoalsFor()) + "\t" + str(team.getGoalsAgainst()) + "\t" + str(team.getGoalDiff()))
            elif len(team.getName()) < 4:
                print(str(i) +'. ' + team.getName() + "\t\t\t" + str(team.getGamesPlayed()) + '\t' + str(team.getWins()) + "\t" + str(team.getDraws()) + "\t" + str(team.getLoses()) + "\t" + str(team.getPoints()) + "\t" + str(team.getGoalsFor()) + "\t" + str(team.getGoalsAgainst()) + "\t" + str(team.getGoalDiff()))
            else:
                print(str(i) +'. ' + team.getName() + "\t\t" + str(team.getGamesPlayed()) + '\t' + str(team.getWins()) + "\t" + str(team.getDraws()) + "\t" + str(team.getLoses()) + "\t" + str(team.getPoints()) + "\t" + str(team.getGoalsFor()) + "\t" + str(team.getGoalsAgainst()) + "\t" + str(team.getGoalDiff()))
            teamsListCopy.remove(team)
            
    def matchDay(self):
        teamsListCopy = self._teamsList[:]
        matchDaySchedule = []
        for i in range(0, self._numTeams):
            matchDaySchedule.append(teamsListCopy.pop(random.randint(0, len(teamsListCopy)-1)))
        for i in range(0, len(matchDaySchedule), 2):
            self.playMatch(matchDaySchedule[i], matchDaySchedule[i+1])

            
    def playMatch(self, team1, team2, debug=False):
        team1RunningOvr = team1.getOvr()
        team1RunningOvr += random.randint(-15,10)
        if team1RunningOvr > 100:
            team1RunningOvr = 100
            
        team2RunningOvr = team2.getOvr()
        team2RunningOvr += random.randint(-15,10)
        if team2RunningOvr > 100:
            team2RunningOvr = 100
    
        team1ScoreChance = 22 + ((team1RunningOvr - team2RunningOvr) // 2)
        if team1ScoreChance < 5:
            team1ScoreChance = 5
        if team1ScoreChance > 90:
            team1ScoreChance = 90
            
        team2ScoreChance = 22 + ((team2RunningOvr - team1RunningOvr) // 2)
        if team2ScoreChance < 5:
            team2ScoreChance = 5
        if team2ScoreChance > 90:
            team2ScoreChance = 90
            
        
        team1Goals = 0
        team2Goals = 0
        
        for tick in range(0,6):
            if random.randint(0,100) < team1ScoreChance:
                team1Goals += 1
            if random.randint(0, 100) < team2ScoreChance:
                team2Goals += 1
                
        print(team1.getName() +' ' + str(team1Goals) + ' - ' + str(team2Goals) + ' ' + team2.getName())
        
        if team1Goals == team2Goals:
            team1.addDraw(team1Goals, team2Goals)
            team2.addDraw(team2Goals, team1Goals)
            
        elif team1Goals>team2Goals:
            team1.addWin(team1Goals, team2Goals)
            team2.addLoss(team2Goals, team1Goals)
            
        else:
            team2.addWin(team2Goals, team1Goals)
            team1.addLoss(team1Goals, team2Goals)
        
        
        if debug:
            print(team1.getName() +' running overal: ' + str(team1RunningOvr))
            print(team1.getName() + ' scoring chance: ' +str(team1ScoreChance))
            print(team2.getName() + ' running overal: ' + str(team2RunningOvr))
            print(team2.getName() + ' scoring change: ' +str(team2ScoreChance))
            
    def playSeason(self):
        for team1 in self._teamsList:
            for team2 in self._teamsList:
                if team1 != team2:
                    self.playMatch(team1, team2)
    
if __name__ == '__main__':
    prem = League('Premier League')
    prem.addTeam(Team('Chelsea', 90))
    prem.addTeam(Team('Spurs', 95))
    prem.addTeam(Team('Arsenal', 75))
    prem.addTeam(Team('Liverpool', 85))
    prem.addTeam(Team('Manchester City', 87))
    prem.addTeam(Team('Man Utd', 85))
    prem.addTeam(Team('Everton', 78))
    prem.addTeam(Team('WBA', 70))
    prem.addTeam(Team('WHU', 68))
    prem.addTeam(Team('Watford', 67))
    prem.addTeam(Team('Stoke', 66))
    prem.addTeam(Team('Burnley', 65))
    prem.addTeam(Team('KimAFC', 75))
    prem.addTeam(Team('AndrewFC', 82))
    prem.addTeam(Team('ShionFC', 80))
    prem.addTeam(Team('KaiFC', 78))
    prem.addTeam(Team('QuistFC', 69))
    prem.addTeam(Team('IanFC', 88))
    prem.addTeam(Team('Theron FC', 87))
    prem.addTeam(Team('DrewFC', 86))
    prem.printTable()
    
    prem.playSeason()
    prem.printTable()
        
    