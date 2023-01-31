import os
import sys

from fastapi import APIRouter,status
from fastapi.responses import JSONResponse

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)
from src.gen_petri import *

router = APIRouter()


@router.post("/get_places", tags=["Code-2-Petri-net"])
def run_places(code: str, gpt_key: str):
    s, success = get_places(text=code, gpt_key=gpt_key)

    if not success:
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content=s)

    return s

@router.post("/get_parameters", tags=["Code-2-Petri-net"])
def run_places(code: str, gpt_key: str):
    s, success = get_parameters(text=code, gpt_key=gpt_key)

    if not success:
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content=s)

    return s

@router.post("/get_transitions", tags=["Code-2-Petri-net"])
def run_transitions(code: str, gpt_key: str):
    s, success = get_transitions(text=code, gpt_key=gpt_key)

    if not success:
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content=s)

    return s

#@router.post("/match_place_to_text", tags=["Code-2-Petri-net"])
def run_match_place_to_text(text: str, place: str, gpt_key: str):
    s, success = match_place_to_text(text=text, place=place, gpt_key=gpt_key)

    if not success:
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content=s)

    return s

#@router.post("/init_param_from_text", tags=["Code-2-Petri-net"])
def run_init_param_from_text(text: str, param: str, gpt_key: str):
    s, success = init_param_from_text(text=text, param=param, gpt_key=gpt_key)

    if not success:
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content=s)

    return s

#@router.post("/match_place_and_text_to_columns", tags=["Code-2-Petri-net"])
def run_match_place_and_text_to_columns(text: str, place: str, columns: str, gpt_key: str):
    s, success = match_place_and_text_to_columns(text=text, place=place, columns=columns, gpt_key=gpt_key)

    if not success:
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content=s)

    return s