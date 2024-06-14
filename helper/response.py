from typing import Optional, Any, List, Generic,TypeVar, Union

from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel

T = TypeVar('T')


class PaginationMeta(BaseModel):
    total: int
    page: int
    size: int
    pages: Optional[int] = None  # Optional: Total number of pages (can be calculated)


class PaginationResponse(BaseModel):
    status_code: int
    message: str
    result: list[Any]
    meta: Optional[PaginationMeta] = None


class ResponseModel(BaseModel, Generic[T]):
    status_code: Optional[int] = status.HTTP_200_OK
    message: Optional[str] = "OK"
    result : Union[T, List[T], None]
    
    
class ListResponseModel(BaseModel, Generic[T]):
    status_code: Optional[int] = status.HTTP_200_OK
    message: Optional[str] = "OK"
    result : Union[List[T], None]



def SuccessfulResponseModel(message: Optional[str] = "OK", result: Optional[T | List[T]] = None):
    if isinstance(result, list):
        return ListResponseModel(
            message=message,
            result=result
        )
    else:
        return ResponseModel(
            message=message,
            result=result
        )


def CreateResponseModel(message: Optional[str] = "created successfully.", result: Optional[T | List[T]] = None):
    return ResponseModel(
        status_code=status.HTTP_201_CREATED,
        message=message,
        result=result
    )


def ErrorResponseModel(message: Optional[str] = "Internal Server Error", result: Optional[T | List[T]] = None):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "message": message,
            "result": result
        }
    )


def NotFoundResponseModel(message: Optional[str] = "data not found", result: Optional[T | List[T]] = None):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "status_code": status.HTTP_404_NOT_FOUND,
            "message": message,
            "result": result
        }
    )


def UnauthorizedResponseModel(message: Optional[str] = "not authenticated", result: Optional[T | List[T]] = None):
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={
            "status_code": status.HTTP_401_UNAUTHORIZED,
            "message": message,
            "result": result
        }
    )
    

def ForbiddenResponseModel(message: Optional[str] = "forbidden", result: Optional[T | List[T]] = None):
    return JSONResponse(
        status_code=status.HTTP_403_FORBIDDEN,
        content={
            "status_code": status.HTTP_403_FORBIDDEN,
            "message": message,
            "result": result
        }
    )


def BadRequestResponseModel(message: Optional[str] = "bad request", result: Optional[T | List[T]] = None):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "status_code": status.HTTP_400_BAD_REQUEST,
            "message": message,
            "result": result
        }
    )


def UnprocessableResponseModel(message: Optional[str] = "unprocessable content", result: Optional[T | List[T]] = None):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "status_code": status.HTTP_422_UNPROCESSABLE_ENTITY,
            "message": message,
            "result": result
        }
    )
