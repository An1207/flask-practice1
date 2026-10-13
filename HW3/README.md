# flask-practice1

- 이름: 안세호
- 학번: 23013283

# HW3

- 과제 : Todo 앱에 수정 기능 더하기
- 마감 : 10월 13일(화) 23:59

- 설명

    `todo_app` 폴더의 Todo 앱을 `HW3` 폴더로 복사하고 Flask-SQLAlchemy와 SQLite를 사용하도록 구성

    `/` + 할 일과 설명 추가 및 데이터베이스 목록 조회

    `/toggle/<int:id>` + 완료 상태 전환

    `/edit/<int:id>` + 할 일과 설명 수정

    `/delete/<int:id>` + 할 일 삭제

· `Todo` 모델에 `id`, `text`, `note`, `done` 필드를 정의

· 추가, 수정, 삭제 후 `db.session.commit()`을 실행하여 변경 내용을 SQLite에 저장

· 수정 화면의 입력칸에는 `todo.text`, `todo.note`의 현재 값이 표시됨

· 목록 화면에서 [수정] 링크를 눌러 수정 화면으로 이동하고, [저장] 후 목록으로 돌아옴

· 서버를 종료하고 다시 실행해도 할 일, 설명, 완료 상태가 유지됨

· SQLite 파일은 `HW3/instance/todo.db`에 자동 생성되며 저장소에는 올리지 않음

· 제출 파일은 `HW3/app.py`, `HW3/templates`, `HW3/static/style.css`, `HW3/README.md`이며 HW3 변경 커밋은 3개 이상 필요

## 실행 화면

### ① 목록 화면

<img width="434" height="450" alt="스크린샷 2026-10-13 212113" src="https://github.com/user-attachments/assets/edf4ced4-5fbc-4719-9df5-20702ea40286" />


### ② 수정 화면

<img width="433" height="377" alt="스크린샷 2026-10-13 212156" src="https://github.com/user-attachments/assets/c17808d9-c074-49d9-ba49-3b97177d29b6" />


### ③ 서버를 껐다 켠 뒤에도 그대로인 목록

<img width="673" height="683" alt="스크린샷 2026-10-13 212340" src="https://github.com/user-attachments/assets/3ac4337c-0b2f-4cd3-9ce9-d375ec1c7bdb" />


