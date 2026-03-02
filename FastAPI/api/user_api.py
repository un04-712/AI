
from fastapi import APIRouter

# 创建子路由
router = APIRouter()

@router.get('/users')
def read_users():
    return "read_users test"

@router.get('/auth/login/')
def login():
    return "login test"

@router.get('/auth/register/')
def register():
    return "register test"