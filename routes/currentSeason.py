from fastapi import FastAPI,HTTPException,status,Response,Depends
from typing import Optional,Any
from model import Driver

app = FastAPI(title="F1 Drivers in 2025 Season", version="0.0.1",description="Api for learning")

def fake_db():
    try:
        print("Conecting database")
    except:
        print("Desconecting databse")
drivers = {
    1:{
    "name": "Max Verstappen",
    "team": "Red Bull Racing",
    "country": "Netherlands",
    "podiums": 113,
    "wdc": 4,
    "wins": 63 
    },
    2:{
    "name": "Lewis Hamilton",
    "team": "Ferrari",
    "country": "United Kingdom",
    "podiums": 202,
    "wdc": 7,
    "wins": 105 
    },
    3:{
    "name": "Charles Leclerc",
    "team": "Ferrari",
    "country": "Mônaco",
    "podiums": 43,
    "wdc": 0,
    "wins": 8 
    },
    4:{
    "name": "Lando Norris",
    "team": "McLaren F1 team",
    "country": "United Kingdom",
    "podiums": 28,
    "wdc": 0,
    "wins": 5 
    },
    5:{
    "name": "George Russell",
    "team": "Mercedes ",
    "country": "United Kingdom",
    "podiums": 17,
    "wdc": 0,
    "wins": 3 
    },
    6:{
    "name": "Alexander Albon",
    "team": "Williams",
    "country": "Thailand",
    "podiums": 2,
    "wdc": 0,
    "wins": 0 
    },
    7:{
    "name": "Lance Stroil",
    "team": "Aston Martin",
    "country": "Canada",
    "podiums": 3,
    "wdc": 0,
    "wins": 0 
    },
    8:{
    "name": "Oscar Piastri",
    "team": "McLaren F1 team",
    "country": "Australia",
    "podiums": 11,
    "wdc": 0,
    "wins": 3 
    },
    9:{
    "name": "Andrea Kimi Antonelli",
    "team": "Mercedes",
    "country": "Italy",
    "podiums": 0,
    "wdc": 0,
    "wins": 0 
    },
    10:{
    "name": "Nicolas Hülkenberg",
    "team": "Kick Sauber",
    "country": "Germany",
    "podiums": 0,
    "wdc": 0,
    "wins": 0
    },
    11:{
    "name": "Esteban Ocon",
    "team": "Hass",
    "country": "France",
    "podiums": 4,
    "wdc": 0,
    "wins": 1 
    },
    12:{
    "name": "Olive Bearman",
    "team": "Hass",
    "country": "United Kingdom",
    "podiums": 0,
    "wdc": 0,
    "wins": 0
    },
    13:{
    "name": "Yuki Tsunoda",
    "team": "Red Bull Racing",
    "country": "Japan",
    "podiums": 0,
    "wdc": 0,
    "wins": 0
    },
    14:{
    "name": "Carlos Sainz ",
    "team": "Williams",
    "country": "Spain",
    "podiums": 27,
    "wdc": 0,
    "wins": 4
    },
    15:{
    "name": "Isack Hadjar",
    "team": "Racing Bulls",
    "country": "France",
    "podiums": 0,
    "wdc": 0,
    "wins": 0
    },
    16:{
    "name": "Pierre Gasly",
    "team": "Alpine",
    "country": "France",
    "podiums": 5,
    "wdc": 0,
    "wins": 1 
    },
    17:{
    "name": "Liam Lawson",
    "team": "Racing Bulls",
    "country": "Mew Zealand",
    "podiums": 0,
    "wdc": 0,
    "wins": 0 
    },
    18:{
    "name": "Gabirel Bortoleto",
    "team": "Kick Sauber",
    "country": "Brazil",
    "podiums": 0,
    "wdc": 0,
    "wins": 0 
    },
    19:{
    "name": "Jack Doohan",
    "team": "Alpine",
    "country": "Australia",
    "podiums": 0,
    "wdc": 0,
    "wins": 0 
    },
    20:{
    "name": "Fernando Alonso",
    "team": "Aston Martin",
    "country": "Spain",
    "podiums": 106,
    "wdc": 2,
    "wins": 32 
    },
}


@app.get('/drivers',description="Return all drivers")
async def get_drivers(db: Any = Depends(fake_db)):
    return drivers

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0", port="8000", log_level="info", reload=True)
