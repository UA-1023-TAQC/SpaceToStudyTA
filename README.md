# SpaceToStudyTA

Create a `.env` file in the root of your project:

```dosini
BASE_URL=base_url

STUDENT_EMAIL=student@test.com
STUDENT_PASSWORD=student_password
STUDENT_FIRST_NAME=student
STUDENT_LAST_NAME=student

TUTOR_EMAIL=tutor@test.com
TUTOR_PASSWORD=tutor_password
TUTOR_FIRST_NAME=tutor
TUTOR_LAST_NAME=tutor
```
run pylint
```shell
pylint ./SpaceToStudy
```


## Run tests
```shell
pytest --alluredir=./my_allure_results ./tests
```

