# flask-practice1

- 이름: 안세호
- 학번: 23013283

# HW2

- 과제 : Todo 앱에 완료 체크 기능 추가
- 마감 : 10월8일(목) 23:59

- 설명

    todo_app 폴더를 복사하여 HW2 폴더에서 기능 추가
    `/` + 할 일 추가 및 목록 출력
    `/toggle/<int:index>` + 완료 상태 전환
    `/delete/<int:index>` + 할 일 삭제

· 수업에서 만든 todo_app은 그대로 두고 HW2에서만 수정

· 할 일은 `{'text': 입력값, 'done': False}` 형태의 딕셔너리로 저장

· 목록에는 `todo.text`를 출력하고, Delete 링크와 함께 [완료] 링크를 추가

· [완료]를 누르면 done 값을 반대로 바꾸고 목록으로 redirect

· 완료된 할 일의 글자에 취소선을 표시하고, 다시 누르면 취소선이 사라짐

· toggle에도 삭제 기능과 같은 인덱스 범위 확인을 넣고, 기존 삭제 기능은 유지

· 새로고침해도 완료 상태가 유지될 것. 서버를 재시작하면 초기화되는 것은 정상

· 제출 파일은 HW2/app.py, HW2/templates, HW2/static, HW2/README.md이며, 커밋은 3개 이상 필요

· README.md에 실행 화면 캡처 3장 첨부
    ① 할 일 두 개가 있는 목록
    ② 하나를 [완료] 눌러 취소선이 표시된 화면
    ③ 새로고침한 뒤에도 취소선이 남아 있는 화면

 ① <img width="475" height="481" alt="스크린샷 2026-10-08 121707" src="https://github.com/user-attachments/assets/6747fe9e-27d6-4984-9021-8993b978d0d2" />

 ② <img width="485" height="476" alt="스크린샷 2026-10-08 121746" src="https://github.com/user-attachments/assets/01646408-5960-4c01-b562-08d8159cb63c" />

 ③ <img width="486" height="674" alt="스크린샷 2026-10-08 121934" src="https://github.com/user-attachments/assets/c7228400-8f14-410b-bb4c-009896ce7e68" />


