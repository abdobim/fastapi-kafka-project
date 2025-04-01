from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Dummy role logic for illustration


def get_current_user_role(token: str = Depends(oauth2_scheme)) -> str:
    # In a real case, decode the token and extract the role
    if token == "admin-token":
        return "admin"
    elif token == "user-token":
        return "user"
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")


def role_required(required_role: str):
    def dependency(role: str = Depends(get_current_user_role)):
        if role != required_role:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access denied")
    return dependency