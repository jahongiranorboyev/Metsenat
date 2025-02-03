# from rest_framework.settings import api_settings
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework_simplejwt.exceptions import InvalidToken, AuthenticationFailed
# from rest_framework_simplejwt.tokens import Token
#
# from django.utils.translation import gettext_lazy as _
#
#
# class CustomJWTAuthentication(JWTAuthentication):
#     def get_user(self, validated_token: Token):
#         print(validated_token)
#         """
#         Attempts to find and return a user using the given validated token.
#         """
#         try:
#             user_id = validated_token[api_settings.USER_ID_CLAIM]
#         except KeyError:
#             raise InvalidToken(_("Token contained no recognizable user identification"))
#
#         try:
#             user = self.user_model.objects.get(**{api_settings.USER_ID_FIELD: user_id})
#         except self.user_model.DoesNotExist:
#             raise AuthenticationFailed(_("User not found"), code="user_not_found")
#
#         if api_settings.CHECK_USER_IS_ACTIVE and not user.is_active:
#             raise AuthenticationFailed(_("User is inactive"), code="user_inactive")
#
#         return user