from typing import List
from fastapi import APIRouter, Depends
from pydantic import BaseModel

favorites_router = APIRouter(prefix="/api/v1/favorites")


class Favorite(BaseModel):
    title: str
    rank: int
    url: str
    thumbnail: str


class FavoritesResponse(BaseModel):
    favorites: List[Favorite]


@favorites_router.get("/")
async def favorites() -> FavoritesResponse:
    return FavoritesResponse(
        favorites=[
            Favorite(title="title1", rank=1, url="url1", thumbnail="thumbnail1"),
            Favorite(title="title2", rank=2, url="url2", thumbnail="thumbnail2"),
            Favorite(title="title3", rank=3, url="url3", thumbnail="thumbnail3"),
        ]
    )
    # model로부터 데이터를 받아옴
