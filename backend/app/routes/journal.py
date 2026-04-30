from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class ActivityInput(BaseModel):
    text: str

@router.post("/generate-entry")
def generate_entry(data: ActivityInput):
    return {
        "my_space": "Worked on backend APIs and explored authentication.",
        "tasks": [
            "Implemented login API",
            "Tested endpoints with Postman"
        ],
        "learnings": [
            "Understanding JWT authentication",
            "Improved debugging skills"
        ],
        "tools": [
            "Node.js",
            "Postman"
        ],
        "achievements": "Successfully created a working authentication route."
    }

@router.post("/generate-week")
def generate_week(data: ActivityInput):
    week_entries = []
    for day in range(1, 6):
        week_entries.append({
            "day": day,
            "tasks": ["Worked on backend development"],
            "learnings": ["Understanding API design"],
            "tools": ["Node.js", "Postman"],
            "achievements": "Improved backend functionality"
        })
    return {"week": week_entries}

@router.post("/generate-logbook")
def generate_logbook(data: ActivityInput):
    entries = []
    for day in range(1, 81):
        entries.append({
            "day": day,
            "tasks": ["Worked on project development"],
            "learnings": ["Improved understanding of backend systems"],
            "tools": ["Node.js", "Express"],
            "achievements": "Completed assigned development tasks"
        })
    return {"entries": entries}
