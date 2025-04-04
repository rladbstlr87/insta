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
7. imageField 사용 위해서 `pip install pillow`
8. `python manage.py makemigrations`
9. `python manage.py migrate`
---
10. .gitignore 에 image/ 폴더 추가
11. `pip freeze >> requirements.txt`
---
12. 프로젝트 urls에 include 구조 작성 `path('posts/', include('posts.urls')),`
13. 앱폴더 `posts`폴더에도 urls.py 만들어서 중복되는 함수 최소화(이중구조)
---
8. 앱폴더에 urls.py 추가하고 아래 문장 기재
```py
urlpatterns = [
    path('', views.index),
]
```

# 배포
1. AWS를 통해서 컴터 한대 빌리고
2. 빌린 컴터에 python, django 설치하고
3. 프로젝트 옮겨오고
...

## **django pjt**

### **0. settings.py**

- ALLOWED_HOSTS
    - EC2 서버주소를 등록
    - 편하게 배포하기 위하여 `*` 로 등록 후 추후 수정가능
- 
```
# settings.py
ALLOWED_HOSTS = [
    '.compute.amazonaws.com',
    '*',
]
```

### **1. 의존성 저장**

- freeze

```
pip freeze > requirements.txt
```

### **2. git push**

- 원격저장소에 업로드 (add, commit, push)