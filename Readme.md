## 2020.08.20
* 회원가입 API 완료
* 게시판 글 목록 불러오기 + CRUD API 완료


# 오류
```
django.db.migrations.exceptions.InconsistentMigrationHistory: Migration admin.0001_initial is applied before its dependency accounts.0001_initial on database 'default'.
```
* User model 커스터마이징 과정에서 이런 오류가 발생했는데 postgresql 테이블을 전부 삭제한 후 migrations에 0001_initial을 삭제하고 다시 migrations을 진행하니 잘 된다.
* 데이터베이스에 있는 migrations 테이블(처음 migrate했을때 생긴 테이블인듯?)이 커스터마이징하는 과정에서 불일치가 일어나서 제대로 작동하지 않는다고 한다.
[stack over flow](https://stackoverflow.com/questions/44651760/django-db-migrations-exceptions-inconsistentmigrationhistory)