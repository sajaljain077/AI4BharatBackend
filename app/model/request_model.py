from pydantic import BaseModel
from fastapi import APIRouter, Body, Depends, HTTPException, Request,Query
from typing import List, Optional
from datetime import date



class project_model(BaseModel):
    target_lang_id : int
    project_title : str

class tranlated_submodule(BaseModel):
    sen_id : int
    tranlated_sentence: str

class translated_sentence_model(BaseModel):
    sentences : list[tranlated_submodule]