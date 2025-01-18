from pydantic import BaseModel
from typing import List, Optional

# Model za korisnika
class User(BaseModel):
    id: str
    name: str
    email: str
    date_registered: str

# Model za djelo
class Artwork(BaseModel):
    id: str
    title: str
    description: Optional[str]
    date_created: str
    artist_id: str

# Model za galeriju
class Gallery(BaseModel):
    id: str
    title: str
    description: Optional[str]
    date_created: str
    artworks: List[Artwork]
    creator_id: str