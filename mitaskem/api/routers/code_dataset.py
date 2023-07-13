import os
import sys

from fastapi import APIRouter,status
from fastapi.responses import JSONResponse

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)
from src.connect import code_dataset_connection

router = APIRouter()


@router.post("/run", tags=["Code-to-format"])
def run_code_dataset(input_code: str, input_dataset: str, gpt_key: str):

    s, success = code_dataset_connection(code=input_code, schema=input_dataset, gpt_key=gpt_key)

    if not success:
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content=s)

    return s
