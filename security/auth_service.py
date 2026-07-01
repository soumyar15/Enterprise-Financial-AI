from security.jwt_auth import JWTManager


jwt_manager = JWTManager()


class AuthService:

    def login(self, username):

        return {

            "token": jwt_manager.create_token(username)

        }