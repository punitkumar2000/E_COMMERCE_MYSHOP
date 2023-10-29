import jwt
from functools import wraps
from datetime import datetime
from django.http.response import JsonResponse

# from my_shop.helpers.utils import PRIVATE_KEY
PRIVATE_KEY = """
MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCu+3hU65jUp2qi
+fRJDmjm2hUcNaq6FUH+QqhX/kZ8DXxAaorqs0BHzbpGUyizM01hxB5DeolbfBoB
ZWTnGw6UZqo1JUpxJKfqRy4zh8i3kfr3WnOHan2fJPtF470MihDgA1PgGK1IAddZ
25XIX1lmMRvTdWbUP0KsSz6dIeV7Al5CKAsD5sUI749k/J+6hROe8tDZGsliSt1N
8LVUqPwarfBhbnPYX5AetFspUB7hopjwDlhgL79ttSBtqpLYkSUqHteIe5t4yWld
402sYhCWtOO3PeqLlarzRBvfDr6tij/wUVlxFip/ZWBwVZN7c4KIeER3al64YOpb
i8A7TYW3AgMBAAECggEADqZxQbLj/dHyhKimwkMZl1Jk+BKqM6A6AT61d4CLiDFc
2MvSy6msVRatZNvriW1fKjNQUVf+DhHK35kMpKjIRLZ/w6lWnThzcpL5FElnDa+E
Mpd5GrpYwC1JeGWD23vnw8mjiRynzWKSFCzlUnxhMMQlz0OCE30kaOZ33JIM84pw
qWcrkZpKnhvwSD/Q3GVd9VcO+FvotKztsUQLv6BCvphq1LjAtlzC+tSESJTHmhkm
5ixXxdbtwCvrmE3uxXX1n0FqKMpT1UfAwBcNjwQf3B0A9BUALRyuNl6Fv10KUkCj
yXXdurpv+o/uXWMiZx/X9SRpOF6Yj454AJoNsnoY2QKBgQDldmhOcajaSP+G4GKj
zcJd1WTcOA8zi0/Jgt3866BeyjRVZTZa1AqakfWa8505uNvxC3ZOO6V03d0sLXCa
u/lq7NAk0ZSLgsap5h+nErDcjMonLbws3uRfomRd5tpo6A/XJqhiV9nzy40T6eoF
BUVz5ghKD84nNY/GdRc/UKBYxQKBgQDDOBdnb2WEdjIUXBmJJFEiLqgdbvFQqzAn
hQIoKoO4wTAOW74qgegwTvMj0K+q2GZP1qHu4ySN4aV7xnoeBkHUlwZQ0jharNPD
oKTT5lzDHusbSnofvVr3SV/yUpYj4fyTtNIzNcfeMlUzISdm+pPPOuQiTjzy93R0
tGQRGtW0SwKBgCR6zZxi/3gskMstkyD9jkACs/U6yFfmdvnPX2FdSHKpbOaCn8CS
41iticFnp4BMvlK1AsrvOp+4wffLBZLj/YQdP/4Kf7YqRVEvb6rNEucNTvopkDgF
+4Kku5YeJGz3L8WBtNVlqBXVL4mR7416yA7j7D9yAdFD96aSaO6877ENAoGAYIMK
jwhzl9kXSRl/Rl29/rgyRNrkUo1PcTpAprreBCj+KRsSGNHAiKF/cuVo832oly/1
PrTtDXfQ6DBnjxBo20EOzkYftjRbPQvecSQiGBThBsz7M1XZ8wdDd/l8YKEIzb1H
binYdfFMTcrGQBMBoCHtR0iGuVe9KzVDg3FQ1aECgYAF/5JQq9V2bPzauGqdMKIS
ce1JqVkuw8dansid7XejdVwH6QmgMrkt4elk5zV74vqOJs0D057cwVvW7bPj6dd6
DLSj0gTEvd97D8X8xMc/CeIifO8M16SwuoqDf5xdtOVDjnFFvc1y+25Pl9Z2Xkud
w3O4APa3T59+oY5XeyqfSg==
"""


def validate_token(token):
    try:
        payload = jwt.decode(token, PRIVATE_KEY, algorithms=["HS256"])
        if datetime.utcnow() > datetime.fromtimestamp(payload["exp"]):
            return False
        return payload
    except jwt.ExpiredSignatureError as e:
        return False
    except jwt.DecodeError as e:
        return False


def token_required(func):
    @wraps(func)
    def middleware(request):
        token = request.headers.get("Authorization", "")
        x_api_key = request.headers.get("x-api-key", "")

        if not token:
            return JsonResponse({"message": "Authorization Token missing!"}, status=401, safe=False)

        if not x_api_key:
            return JsonResponse({"message": "x-api-key missing!"}, status=401, safe=False)

        payload = validate_token(token)
        print("payload", payload)
        if not payload:
            return JsonResponse({"message": "Invalid or expired token"}, status=401, safe=False)

        if payload["XApiKey"] != x_api_key:
            email = payload["Email"]
            return JsonResponse({"message": f"Invalid x_api_key or This x_api_key Doesn't belong to the User {email}"}, status=401, safe=False)
        request.user = payload

        return func(request)

    return middleware

