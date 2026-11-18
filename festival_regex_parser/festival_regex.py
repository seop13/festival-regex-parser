import re
import os

# 로그 파일을 열어서 전체 내용을 문자열로 읽기
f = open('festival_log.txt', 'r', encoding='utf-8')
data = f.read()
f.close()


# 1. 유효한 이메일: @ 바로 뒤가 영문/숫자여야 함
email_pattern = re.compile(r'[a-zA-Z0-9._]+@[a-zA-Z0-9]+[a-zA-Z0-9.]*\.[a-zA-Z]+')
emails = email_pattern.findall(data)

print('1. 유효한 이메일')
for email in emails:
    print('  ', email)
print()


# 2. 휴대폰 번호: 010 + 4자리 + 4자리 (구분자 - . 공백)
phone_pattern = re.compile(r'010[-. ]\d{4}[-. ]\d{4}')
phones = phone_pattern.findall(data)

print('2. 휴대폰 번호')
for phone in phones:
    print('  ', phone)
print()


# 3. 재학생 학번/학과: [202로 시작하는 9자리 / 한글 학과] → (학번, 학과) 튜플
student_pattern = re.compile(r'\[(202\d{6})\s*/\s*([가-힣]+)\]')
students = student_pattern.findall(data)

print('3. 본교 재학생 (학번, 학과)')
for student in students:
    print('  ', student)
print()


# 4-1. GitHub 저장소: http(s)://github.com/ 으로 시작하는 주소만
github_pattern = re.compile(r'https?://github\.com/[a-zA-Z0-9_./-]+')
githubs = github_pattern.findall(data)

print('4-1. GitHub 저장소 URL')
for url in githubs:
    print('  ', url)
print()


# 4-2. 유효 쿠폰: FEST-2026- 뒤에 대문자/숫자 4자리
coupon_pattern = re.compile(r'FEST-2026-[A-Z0-9]{4}')
coupons = coupon_pattern.findall(data)

print('4-2. 2026년 유효 쿠폰')
for coupon in coupons:
    print('  ', coupon)
print()


# 5. 부스별 매출: '- 부스명 매출: 금액원' 줄에서 부스명과 금액만 꺼내기
sales_pattern = re.compile(r'^-\s(.+)\s매출:\s([0-9,]+)원', re.MULTILINE)

print('5. 부스별 총 매출액')
total = 0
for m in sales_pattern.finditer(data):
    booth = m.group(1)                           # 부스 이름
    amount_text = m.group(2)                     # 금액 문자열 (예: '1,350,000')
    amount = int(amount_text.replace(',', ''))   # 쉼표 제거 후 정수로 변환
    total = total + amount                       # 합계에 더하기
    print('   %s : %s원' % (booth, amount_text))

print('   ----------------------------')
print('   전체 매출 합계 : {:,}원'.format(total))