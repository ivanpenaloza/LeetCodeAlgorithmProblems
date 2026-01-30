from typing import List, Union, Collection, Mapping, Optional, Dict


class Table:

    def __init__(self, name:str, columns: int, rows: Dict, row_count: int = 0):
        self.name = name 
        self.columns = columns
        self.rows = rows 
        self.row_count = row_count

class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        """
        two string arrays, names and columns, both of size n.

        The ith table is represented by the name names[i] and contains columns[i] number of columns
        """
        self.names = names 
        self.columns = columns
        self.data = {}

        for i in range(0, len(self.names)):
            self.data[self.names[i]] = Table(
                name = self.names[i],
                columns=self.columns[i],
                rows={}
            )

        return 
        

    def ins(self, name: str, row: List[str]) -> bool:
        """
        Inserts row into the table name and returns true.
        If row.length does not match the expected number of columns, or name is not a valid table,
        returns false without any insertion.
        """        
        table: Table = self.data.get(name)
        if table is None:
            return False 
        if len(row) != table.columns:
            return False 
        table.row_count += 1
        table.rows[table.row_count] = row

        return True 
        

    def rmv(self, name: str, rowId: int) -> None:
        """
        Removes the row rowId from the table name.
        If name is not a valid table or there is no row with id rowId, no removal is performed.
        """        
        table: Table = self.data.get(name, None)
        if table is None:
            return 
        
        if rowId in table.rows:
            del table.rows[rowId]

        return 
        

    def sel(self, name: str, rowId: int, columnId: int) -> str:
        """
        Returns the value of the cell at the specified rowId and columnId in the table name.
        If name is not a valid table, or the cell (rowId, columnId) is invalid, returns "<null>".
        """        
        null = "<null>"
        table: Table = self.data.get(name, None)
        if table is None:
            return null
        
        if rowId not in table.rows:
            return null
        
        try:
            return table.rows[rowId][columnId - 1]
        except Exception:
            return null
        

    def exp(self, name: str) -> List[str]:
        """
        Returns the rows present in the table name.
        If name is not a valid table, returns an empty array.
        Each row is represented as a string, with each cell value (including the row's id) separated by a ",".
        """
        table: Table = self.data.get(name, None)
        if table is None:
            return []
        
        result = []

        for row_id, row in table.rows.items():
            row_str = ",".join(row)
            result.append(f"{row_id},{row_str}")
        
        return result
        


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# param_1 = obj.ins(name,row)
# obj.rmv(name,rowId)
# param_3 = obj.sel(name,rowId,columnId)
# param_4 = obj.exp(name)