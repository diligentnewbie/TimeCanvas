# '''
# Author: HKini 1778267485@qq.com
# Date: 2024-03-07 16:49:01
# LastEditTime: 2024-03-07 16:49:05
# LastEditors: HKini 1778267485@qq.com
# Description: 相册，以及相册类型得路由
# FilePath: \TimeCanvas\backend\routers\album.py

# '''
from fastapi import APIRouter,Depends,HTTPException
from dependencies import auth_depend, db_depend
from sqlalchemy.orm import Session
from models import orm_models
from schemas import orm_schema
from crud import album_crud, user_crud
from services import baidufile_service
from utils import aes
router = APIRouter()
#获取相册类型
@router.get("/albumtype",tags=["albumtype"])
async def get_album_type(
    db: Session = Depends(db_depend.get_db),
    baidu_uk: str = Depends(auth_depend.verify_jwt_token),
):
    return album_crud.get_album_type(db, baidu_uk)
#创建相册类型
@router.post("/albumtype",tags=["albumtype"])
async def album_type_create(
    album_type: orm_schema.AlbumType,
    db: Session = Depends(db_depend.get_db),
    baidu_uk: str = Depends(auth_depend.verify_jwt_token),
):
    userinfo = user_crud.get_user(db, baidu_uk)
    access_token = aes.decrypt(userinfo.access_token)
    #判断百度网盘是否有项目的总文件夹，如果没有就创建
    if baidufile_service.is_folder_exist(access_token, "TimeGallery/"+album_type.albumtype_name)==True:
        pass
    else:
        baidufile_service.create_project_folder(access_token, "/apps/TimeGallery/"+album_type.albumtype_name)
    return album_crud.album_type_create(db, album_type, baidu_uk)
#删除相册类型
@router.delete("/albumtype",tags=["albumtype"])
async def album_type_delete(
    album_type_id: int,
    db: Session = Depends(db_depend.get_db),
    baidu_uk: str = Depends(auth_depend.verify_jwt_token),
):
    return album_crud.album_type_delete(db, album_type_id, baidu_uk)
#修改相册类型
@router.put("/albumtype",tags=["albumtype"])
async def album_type_update(
    album_type: orm_schema.AlbumTypeUpdate,
    id: int,
    db: Session = Depends(db_depend.get_db),
    baidu_uk: str = Depends(auth_depend.verify_jwt_token),
):
    return album_crud.album_type_update(db, album_type, id, baidu_uk)

#获取相册类型下的相册
@router.get("/album",tags=["album"])
async def get_album(
    album_type_id: int,
    db: Session = Depends(db_depend.get_db),
    baidu_uk: str = Depends(auth_depend.verify_jwt_token),
):
    return album_crud.get_album(db, album_type_id, baidu_uk)
#创建相册
@router.post("/album",tags=["album"])
async def album_create(
    album: orm_schema.AlbumCreate,
    db: Session = Depends(db_depend.get_db),
    baidu_uk: str = Depends(auth_depend.verify_jwt_token),
):
    #先判断相册类型是否存在
    album_type = db.query(orm_models.AlbumType).filter(
        orm_models.AlbumType.id == album.album_type, 
        orm_models.AlbumType.albumtype_owner==baidu_uk
    ).first()
    userinfo = user_crud.get_user(db, baidu_uk)
    access_token = aes.decrypt(userinfo.access_token)
    if not album_type:
        return HTTPException(status_code=404, detail="相册类型不存在")
    #判断百度网盘是存在对应的文件夹，如果没有就创建
    if baidufile_service.is_folder_exist(access_token, "TimeGallery/"+album_type.albumtype_name+"/"+album.album_name)==True:
        pass
    else:
        baidufile_service.create_project_folder(access_token, "/apps/TimeGallery/"+album_type.albumtype_name+"/"+album.album_name)
    return album_crud.album_create(db, album, baidu_uk)
#删除相册
@router.delete("/album",tags=["album"])
async def album_delete(
    album_id: int,
    db: Session = Depends(db_depend.get_db),
    baidu_uk: str = Depends(auth_depend.verify_jwt_token),
):
    return album_crud.album_delete(db, album_id, baidu_uk)
#修改相册
@router.put("/album",tags=["album"])
async def album_update(
    album: orm_schema.AlbumUpdate,
    id: int,
    db: Session = Depends(db_depend.get_db),
    baidu_uk: str = Depends(auth_depend.verify_jwt_token),
):
    return album_crud.album_update(db, album, id, baidu_uk)
#获取每个相册类型下的相册，并从百度网盘提取相册类型封面以及相册封面
@router.get("/albuminfo",tags=["albuminfo"])
async def get_albuminfo(
    db: Session = Depends(db_depend.get_db),
    baidu_uk: str = Depends(auth_depend.verify_jwt_token),
):
    #获取用户的百度access_token
    access_token = user_crud.get_user(db, baidu_uk).access_token
    access_token = aes.decrypt(access_token)
    return album_crud.get_album_with_cover(db, baidu_uk,access_token)

#获取某个目录下的所有图片
@router.get("/albumfiles",tags=["albuminfo"],description="获取某个目录下的所有图片")
async def get_album_files(
    folder_name: str,
    db: Session = Depends(db_depend.get_db),
    baidu_uk: str = Depends(auth_depend.verify_jwt_token),
):
    access_token = user_crud.get_user(db, baidu_uk).access_token
    access_token = aes.decrypt(access_token)
    folder_name="apps/TimeGallery/"+folder_name
    return baidufile_service.get_image(access_token, folder_name)
#级联选择器数据
@router.get("/albumcascade",tags=["albuminfo"],description="级联选择器数据")
async def get_album_cascade(
    db: Session = Depends(db_depend.get_db),
    baidu_uk: str = Depends(auth_depend.verify_jwt_token),
):
    return album_crud.get_album_cascade(db, baidu_uk)