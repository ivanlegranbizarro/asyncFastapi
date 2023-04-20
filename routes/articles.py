from typing import List

from fastapi import Depends, status
from fastapi.exceptions import HTTPException
from fastapi.routing import APIRouter

from database.db import Article, database
from helpers.jwt_fastapi import get_current_user
from schemas.articles import ArticleSchema

router = APIRouter(
    prefix="/articles",
    tags=["Articles"],
)


@router.get("/", response_model=List[ArticleSchema], status_code=200)
async def get_all_articles():
    query = Article.select()
    return await database.fetch_all(query)


@router.post("/", response_model=ArticleSchema, status_code=201, dependencies=[Depends(get_current_user)])
async def create_article(article: ArticleSchema):
    try:
        query = Article.insert().values(
            **article.dict()
        )
        last_record_id = await database.execute(query)
        return {**article.dict(), "id": last_record_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get('/{article_id}', response_model=ArticleSchema, status_code=200)
async def get_article(article_id: int):
    query = Article.select().where(Article.c.id == article_id)
    article = await database.fetch_one(query)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article


@router.put('/{article_id}', response_model=ArticleSchema, status_code=status.HTTP_202_ACCEPTED, dependencies=[Depends(get_current_user)])
async def update_article(article_id: int, article: ArticleSchema):
    article = await get_article(article_id)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    query = Article.update().where(Article.c.id == article_id).values(
        **article.dict()
    )
    await database.execute(query)
    return await get_article(article_id)


@router.delete('/{article_id}', status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(get_current_user)])
async def delete_article(article_id: int):
    old_article = await get_article(article_id)
    if not old_article:
        raise HTTPException(status_code=404, detail="Article not found")
    query = Article.delete().where(Article.c.id == article_id)
    await database.execute(query)
    return {"message": "Article deleted successfully"}
