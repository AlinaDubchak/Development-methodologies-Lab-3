from fastapi import APIRouter

router = APIRouter()


@router.get('')
def hello_world() -> dict:
    return {'msg': 'You have unlocked a new achievement in docker!'}
