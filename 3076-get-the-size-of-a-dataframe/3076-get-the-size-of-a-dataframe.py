import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    lsit=[]
    a,b=players.shape
    lsit.append(a)
    lsit.append(b)
    return lsit
    