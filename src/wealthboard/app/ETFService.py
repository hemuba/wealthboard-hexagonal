from wealthboard.driven.adapters.OracleETFRepository import OracleETFRepository

class ETFService:
    
    def __init__(self, repo:OracleETFRepository):
        self._repo = repo
        
    def fetchAll(self):
        return self._repo.fetchAll()