# osnovna FastAPI aplikacija; provjera: uvicorn main:app --reload
from fastapi import FastAPI
from user_models import User, Artwork, Gallery
from crud_operations import create_user, create_gallery, get_gallery, update_gallery, delete_gallery, create_artwork, get_artwork, update_artwork, delete_artwork

app = FastAPI()

# Korisnici - endpoint koji omogućuje dodavanje novog korisnika
@app.post("/users/")
async def add_user(user: User):
    response = create_user(user.dict())
    return response

# Galerije
@app.post("/galleries/")
async def add_gallery(gallery: Gallery):
    response = create_gallery(gallery.dict())
    return response

@app.get("/galleries/{gallery_id}")
async def read_gallery(gallery_id: str):
    response = get_gallery(gallery_id)
    return response

@app.put("/galleries/{gallery_id}")
async def update_gallery_data(gallery_id: str, gallery: Gallery):
    response = update_gallery(gallery_id, gallery.dict())
    return response

@app.delete("/galleries/{gallery_id}")
async def delete_gallery_data(gallery_id: str):
    response = delete_gallery(gallery_id)
    return response

# Umjetnička djela
@app.post("/artworks/")
async def add_artwork(artwork: Artwork):
    response = create_artwork(artwork.dict())
    return response

@app.get("/artworks/{artwork_id}")
async def read_artwork(artwork_id: str):
    response = get_artwork(artwork_id)
    return response

@app.put("/artworks/{artwork_id}")
async def update_artwork_data(artwork_id: str, artwork: Artwork):
    response = update_artwork(artwork_id, artwork.dict())
    return response

@app.delete("/artworks/{artwork_id}")
async def delete_artwork_data(artwork_id: str):
    response = delete_artwork(artwork_id)
    return response


