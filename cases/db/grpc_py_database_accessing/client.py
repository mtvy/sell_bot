
import grpc, sys, json

from .api.grpc import *


TB = 'ask_tb'
DB_HOST = 'postgres://postgres:postgres@postgres:5433/postgres'

class Database:

    def __init__(self, host: str, dbHost: str) -> None:
        self.host = host
        self.conn = grpc.insecure_channel(host) 
        self.stub = DatabaseStub(self.conn)
        self.dbHost = dbHost
    
    def get(self, columns: str, table: str, condition: str) -> list | str:
        req = self.stub.GetDb(GetDbRequest(
            columns=columns, table=table, condition=condition, db_host=self.dbHost))
        if req.status != "ok":
            return [], req.status
        data = json.loads(req.data.decode("utf-8"))
        return data if data else [], req.status

    def insert(self, table: str, columns: str, values: str) -> InsertDbResponse:
        return self.stub.InsertDb(InsertDbRequest(
            table=table, columns=columns, values=values, db_host=self.dbHost))

    def delete(self, table: str, condition: str) -> DeleteDbResponse:
        return self.stub.DeleteDb(DeleteDbRequest(
            table=table, condition=condition, db_host=self.dbHost))

    def update(self, table: str, to_set: str, condition: str) -> UpdateDbResponse:
        return self.stub.UpdateDb(UpdateDbRequest(
            table=table, to_set=to_set, condition=condition, db_host=self.dbHost))
    

def run(host, dbhost):

    db = Database(host, dbhost)
    
    print(db.get(columns="*", table=TB, condition="WHERE url='Hello'"))


if __name__ == "__main__":
    host = sys.argv[1].split('=')[1] # localhost:808...
    print(host)
    run(host, DB_HOST)