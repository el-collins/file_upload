from fastapi import FastAPI, File, UploadFile, Depends, HTTPException
from fastapi.responses import JSONResponse
from models import UserProfile
from sqlmodel import Session # type: ignore
import shutil
from dependencies import get_session, get_user_agent

app = FastAPI()


# Route to create a user profile
@app.post("/profiles/")
async def create_profile(username: str, phone_number: str, email: str, profile_picture: UploadFile = File(...), session: Session = Depends(get_session), user_agent: str = Depends(get_user_agent)):
        try: 
            # Save profile picture to disk
            file_location = f"profile_pictures/{profile_picture.filename}"
            with open(file_location, "wb") as buffer:
                shutil.copyfileobj(profile_picture.file, buffer)
            
            # Create a new user profile record
            user_profile = UserProfile(username=username, phone_number=phone_number, email=email, profile_picture=file_location)
            session.add(user_profile)
            session.commit()
            session.refresh(user_profile)
            print(user_profile)

            # Convert UserProfile to dictionary to make it a JSON-serializable format before returning it

            return JSONResponse(content={"profile": user_profile.dict(),"headers": {"user_agent": user_agent}})
        except  Exception as e:
            return JSONResponse(status_code=400, content={"message": str(e)})
        # raise HTTPException(status_code=500, detail="Internal Server Error")

# Route to get a profile by ID
@app.get("/profiles/{profile_id}")
def get_profile(profile_id: int, session: Session = Depends(get_session), user_agent: str = Depends(get_user_agent)):
        profile = session.get(UserProfile, profile_id)
        if profile is None:
            raise HTTPException(status_code=404, detail="Profile not found")
        
        # Return the profile and headers
        return JSONResponse(content={"profile": profile.dict(), "headers": {"user_agent": user_agent}})

