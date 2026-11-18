# 대동제 & 해커톤 운영 로그 정리 프로그램

파이썬기초실습 **07. 람다와 정규 표현식** 실습 과제입니다.
`festival_log.txt`에서 정규 표현식(`re` 모듈)으로 필요한 정보만 추출합니다.

## 기능
1. 유효한 이메일 추출
2. 010 휴대폰 번호 추출
3. 본교 재학생 (학번, 학과) 추출
4. GitHub 저장소 URL과 2026년 유효 쿠폰 추출
5. 부스별 매출액 추출 및 합계 계산

## 실행 방법
`festival_regex.py`와 `festival_log.txt`를 같은 폴더에 두고 실행합니다.
```bash
python festival_regex.py
```

## 파일 구조
```
├── festival_regex.py   # 메인 프로그램
├── festival_log.txt    # 운영 로그 데이터
└── README.md
```
