from fastapi import APIRouter, Depends
from database.database_connection import get_db
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from wikipediaapi import Wikipedia
from database.schema import Language, Project, Sentence
from utils.utils import responseModel
from model.request_model import project_model, translated_sentence_model

router = APIRouter()

@router.get("/languages")
def getLanguages(db:Session=Depends(get_db)):
    resp = jsonable_encoder(db.query(Language).all())
    return responseModel(200, data=resp, errors= [])


@router.post("/project")
def getLanguages(payload_model:project_model,db:Session=Depends(get_db)):
    print("this request", jsonable_encoder(payload_model))
    payload = jsonable_encoder(payload_model)
    resp  = {}
    new_project_obj = Project(project_title = payload.get("project_title"), project_lang_id = payload.get("target_lang_id"))
    try:
        db.add(new_project_obj)
        db.commit()
        db.refresh(new_project_obj)
        project_id = jsonable_encoder(new_project_obj).get("project_id")
    except Exception as err:
        return responseModel(400, data=[], errors="Choosed Wrong Language")
    summary = Wikipedia().page(payload.get("project_title"))
    if not summary.exists():
        return responseModel(400, data=[], errors="No Wikipwedia page found for given topic, please choose different topic")
    summary_sentences = summary.summary.split('.')
    for sentence in summary_sentences:
        if len(sentence)>0:
            new_project_obj = Sentence(project_id = project_id, original_sentence = sentence)
            db.add(new_project_obj)
            db.commit()
            db.refresh(new_project_obj)
    resp['project_id'] = project_id
    resp["sentences"] = jsonable_encoder(db.query(Sentence.sen_id, Sentence.original_sentence).filter(Sentence.project_id == project_id).all())
    return responseModel(200, data=resp, errors= [])


@router.post("/sentences")
def add_translated_sentence(payload_model:translated_sentence_model,db:Session=Depends(get_db)):
    payload = jsonable_encoder(payload_model)
    tranlated_sentence = payload["sentences"]
    try:
        for sentence in tranlated_sentence:
            sentence_to_update = db.query(Sentence).filter(Sentence.sen_id == sentence["sen_id"])
            sentence_to_update.update({"translated_sentence":sentence["tranlated_sentence"]})
            db.commit()
        return responseModel(201, data="Edited sucessful", errors= [])
    except Exception as err:
        return responseModel(400, data={}, errors= [f"Got this error while updating {err}"])

