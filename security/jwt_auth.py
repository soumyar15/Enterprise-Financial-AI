from datetime import datetime, timedelta
import jwt

SECRET_KEY = "finance_ai_secret"

ALGORITHM = "HS256"


class JWTManager:

    def create_token(self, username):

        payload = {

            "sub": username,

            "exp": datetime.utcnow() + timedelta(hours=8)

        }

        return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)