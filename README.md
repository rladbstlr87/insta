# Board

1. 가상환경 활성화
2. .gitignore
3. Django 설치
---
4. `django-admin startproject insta .`
---
5. `django-admin startapp posts`
6. `settings.py`에서 앱폴더 등록
base.html 구조 작성
---
7. 앱폴더 `articles`폴더에도 urls.py 만들어서 중복되는 함수 최소화(이중구조)
---
8. 앱폴더에 urls.py 추가하고 아래 문장 기재
```py
urlpatterns = [
    path('', views.index),
]
```