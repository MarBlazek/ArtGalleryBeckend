from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

# Definiranje OAuth2 sheme za autentifikaciju putem tokena
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class UserInDB(BaseModel):
    username: str
    password: str

# Funkcija za provjeru valjanosti tokena
def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    Provjerava je li token valjan i dohvaća korisnika prema tokenu.
    Ovo je samo primjer, u stvarnoj aplikaciji provjera tokena bi bila složenija.
    """
    # Ovdje biste provodili stvarnu provjeru tokena
    if token != "expected_token":
        raise HTTPException(status_code=401, detail="Invalid token")
    
    # Ako je token valjan, vraća podatke o korisniku
    return {"username": "valid_user"}