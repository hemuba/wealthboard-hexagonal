import oracledb as odb

class OracleConnectionProvider:
    def __init__(self, usr:str, pwd:str, dsn:str):
        
        self._usr = usr
        self._pwd = pwd
        self._dsn = dsn
        self._pool = None
        
        
    def init_pool(self, min: int=1, max: int=5, increment: int=1):
        """Creates a pool connection at the application startup"""
        self._pool = odb.create_pool(
            user=self._usr,
            password=self._pwd,
            dsn=self._dsn,
            min=min,
            max=max,
            increment=increment
        )
        
    def get_oracledb_connection(self):
        """Returns the connection from the pool if it exists"""
        if self._pool:
            self._pool.acquire()
        return odb.connect(user=self._usr, password=self._pwd, dsn=self._dsn)
        