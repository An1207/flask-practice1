# HW6

안세호 · 23013283

## 실행방법

`.venv` 환경에서 Jupyter로 `hw6.ipynb`를 열고 `Restart Kernel → Run All`을 실행한 뒤 출력과 함께 저장합니다.
`sales_clean.csv`는 노트북과 같은 폴더에 두며, 실행하면 `sales_model.pkl`이 생성됩니다.

새 환경에서는 HW6 폴더에서 다음 순서로 준비합니다.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install pandas==3.1.0 scikit-learn==1.9.1 joblib==1.6.0 Flask==3.1.3 flask-restx==1.3.2 jupyter==1.1.1 ipykernel==7.4.0
jupyter notebook hw6.ipynb
```

Jupyter에서 `.venv` 커널을 선택해 전체 실행합니다. 이미 준비된 `data_analysis/.venv` 커널을 사용해도 됩니다.
API는 HW6 폴더에서 다음 명령으로 실행합니다.

```powershell
flask --app app run
```

http://127.0.0.1:5000/api/docs 에서 `POST /sales/predict`를 펼치고 `Try it out → Execute`를 누릅니다.
수량 `40`, 단가 `200000`을 보내면 HTTP 200과 `{"total_sales": 8000000}`을 반환합니다. `docs.png`는 이 응답을 캡처한 화면입니다.
5000번 포트를 다른 실습 서버가 사용 중이면 해당 서버를 종료한 뒤 실행합니다.

## 단계③답

총액은 수량 × 단가인데, linear regression은 a × 수량 + b × 단가 + c 형태라 두 입력의 곱을 직접 표현하지 못해 test R²가 0.862에 그친다.  
수량 × 단가인 `qp`를 추가하면 그 열의 계수가 1, 나머지 계수와 절편이 0에 가까워져 총액 공식을 그대로 표현하므로 test R²가 1.0이 된다.

## 단계⑤결정과이유

max_depth는 8로 선택한다. 교차검증 평균 R²가 0.992로 높고, 잎 250개인 depth 8에서 잎 781개인 depth 12로 늘려도 평균 R²는 0.995로 0.003만 높아져 더 단순한 쪽을 선택했다.  
총액 = 수량 × 단가라는 규칙이 실제로 있으므로, 제한 없는 트리의 training R² 1.000과 test R² 0.994의 차이도 작다.

## 단계⑦답

API에는 linear regression + qp를 사용한다. 수량 40, 단가 200,000원일 때 예측한 8,000,000원이 실제 곱인 8,000,000원과 일치한다.  
depth 8 트리는 7,362,301원을 예측하므로, test R²가 1.0이며 총액 공식을 정확히 표현하는 linear regression + qp를 선택했다.  
서버에서도 `qp = quantity × unit_price`를 만들어 입력해야 하며, 실제 서비스에서는 공식이 있으므로 모델 없이 두 값을 곱하는 방법도 가능하다.
