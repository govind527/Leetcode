class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res=[]
        rowMin=rStart
        rowMax=rStart+1
        colMin=cStart
        colMax=cStart+1
        while len(res)!=rows*cols:
            
            for col in range(colMin,colMax):
                if 0<=col<cols and 0<=rowMin<rows: res.append([rowMin,col])
            
            for row in range(rowMin,rowMax):
                if 0<=colMax<cols and 0<=row<rows: res.append([row,colMax])
            
            colMin-=1
            
            for col in range(colMax,colMin,-1):
                if 0<=col<cols and 0<=rowMax<rows: res.append([rowMax,col])
            
            rowMin-=1
            
            for row in range(rowMax,rowMin,-1):
                if 0<=colMin<cols and 0<=row<rows: res.append([row,colMin])
            
            colMax+=1
            rowMax+=1
        
        return res
        