class Team:
    
    def __init__(self, name='No name given', ovr=50):
        self._name = name
        self._ovr = ovr
        
        self._gamesPlayed = 0
        self._wins = 0
        self._draws = 0
        self._loses = 0
        self._points = 0
        
        self._goalsFor = 0 
        self._goalsAgainst = 0
        self._goalDiff = 0
        
    def getName(self):
        return self._name
    
    def getOvr(self):
        return self._ovr
        
    def getGamesPlayed(self):
        return self._gamesPlayed
    
    def getWins(self):
        return self._wins
    
    def getDraws(self):
        return self._draws
    
    def getLoses(self):
        return self._loses
    
    def getPoints(self):
        return self._points
    
    def getGoalsFor(self):
        return self._goalsFor
    
    def getGoalsAgainst(self):
        return self._goalsAgainst
    
    def getGoalDiff(self):
        return self._goalDiff
        
    def addWin(self, gf, ga):
        self._gamesPlayed += 1
        self._wins += 1
        self._points += 3
        self._goalsFor += gf
        self._goalsAgainst += ga
        self.calcGD()
    
    def addDraw(self, gf, ga):
        self._gamesPlayed += 1
        self._draws += 1
        self._points += 1
        self._goalsFor += gf
        self._goalsAgainst += ga
    
    def addLoss(self, gf, ga):
        self._gamesPlayed += 1
        self._loses += 1
        self._goalsFor += gf
        self._goalsAgainst += ga
        self.calcGD()
    
    
    
    def calcGD(self):
        self._goalDiff = self._goalsFor - self._goalsAgainst
        
    def __gt__(self, other):
        if self.getPoints() != other.getPoints():
            return self.getPoints() > other.getPoints()
        elif self.getGoalDiff() != other.getGoalDiff():
            return self.getGoalDiff() > other.getGoalDiff()
        elif self.getGoalsFor() != other.getGoalsFor():
            return self.getGoalsFor() > other.getGoalsFor()
        else:
            return False
    
    
if __name__ == '__main__':
    tottenham = Team('Spurs', 100)
    assert tottenham.getGamesPlayed() == 0
    assert tottenham._name == 'Spurs'
    