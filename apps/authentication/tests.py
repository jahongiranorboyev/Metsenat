import requests
from .envv import email, password


class EskizUz:
    """
    send sms to phone number using Eskiz.uz
    """

    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password

    def __request_post(self, url: str, method: str, headers: dict = None, data: dict = None) -> requests.Response:

        if method not in ['get', 'post', 'put', 'delete', 'patch']:
            raise ValueError('Method must be in ["get", "post", "put", "delete", "patch"]')
        if headers is None:
            headers = {
                'Authorization': f'Bearer {self.__get_token()}',
            }

        res = getattr(requests, method)(url=url, json=data, headers=headers)

        res_data = res.json()
        if res.status_code != 200:
            raise ValueError(res_data['message'])

        return res

    def __get_token(self):
        """ get auth token """

        url = 'https://notify.eskiz.uz/api/auth/login'

        data = {
            'email': self.email,
            'password': self.password,
        }
        return "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDE2OTMxNTAsImlhdCI6MTczOTEwMTE1MCwicm9sZSI6InRlc3QiLCJzaWduIjoiNDRjN2NlOTJkN2UzNzFlNzU4YjdiMDU2MDllOGRkMDI0OGVhN2Q4ZTYwNDVmNWVlYTYwMTkxNTUwNWU5OTZhNyIsInN1YiI6Ijk4MjAifQ.SjOEZgGqf__IZEELO3KHikaL64Qse1CeMCVmS7intcg"
        # return res_data['data']['token']

    def register_template(self, template_content: str) -> bool:
        """  returns True  register new template successfully else return False """
        url = "https://notify.eskiz.uz/api/user/template"

        data = {
            'template': template_content,
        }
        self.__request_post(url=url, method='post', data=data)
        return True

    def get_template_list(self):
        """
        get template
        """
        url = "https://notify.eskiz.uz/api/user/template"
        res = self.__request_post(url=url, method='get')

        return res.json()

    def send_message(self, message: str, phone_number: str, alpha_nick: str = '4546') -> bool:
        """ send a message"""

        url = 'https://notify.eskiz.uz/api/message/sms/send'

        data = {
            'mobile_phone': phone_number,
            'message': message,
            'from': alpha_nick,
            'callback_url': 'https://google.com'
        }
        self.__request_post(url=url, method='post', data=data)
        return True


eskiz_uz_service = EskizUz(email=email, password=password)
try:
    pass
except ValueError as e:
    print(e)
