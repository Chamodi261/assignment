from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, EmailStr, validator
import datetime
from typing import List
import email_validator

app = FastAPI()

class Item(BaseModel):
	item_id: str
	quntity: int 
	price: float


class RequsetModel(BaseModel):
	user_id: str 
	email: EmailStr
	timestamp: str 
	items: List[Item]

	@validator("timestamp")
	def check_time(cls, v):
		try:
			pass
		except:
			raise ValueError("Invalid timestamp format")


	@validator("items")
	def check_items_count(cls, v):
		if len(v) < 1:
			raise ValueError("At least one item should be have")
		return v

def authorization(token: str):
	if token != valid_token:
		raise HTTPException(status_code=403, detail="Not Authorized")
	return "read-write"

data_stg = []

@app.post("/upload/")
def upload_data(request_data:RequsetModel,token: str = Depends(authorization)):
	data_stg.append(request_data)
	return {"message": "Data Upload Successfully"}


@app.get("/process/")
def process_data():
	pass

