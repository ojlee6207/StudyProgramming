import re

def smart_cast(number_str):
    if '.' in number_str:
        return float(number_str)
    else:
        return int(number_str)

def parse_expression(command):
    match = re.match(r'\s*(\d+(\.\d+)?)(\s*)([+\-*/])(\s*)(\d+(\.\d+)?)\s*', command)
    if not match:
        raise ValueError("올바른 수식이 아닙니다!")
    num1 = smart_cast(match.group(1))
    operator = match.group(4)
    num2 = smart_cast(match.group(6))
    return num1, operator, num2

def calculate(num1, operator, num2):
    if operator == '+':
        return num1+num2
    elif operator == '-':
        return num1-num2
    elif operator == '*':
        return num1*num2
    elif operator == '/':
        return num1/num2 if num2 != 0 else "0으로 나눌 수 없습니다."
    else:
        return "연산자 오류 발생! 다시 입력하세요"
    
# def main():
#     while True:
#         command = input("계산식을 입력하세요 (탈출 : exit 입력)")
#         if command.lower() == 'exit':
#             print("계산기를 종료합니다.")
#             break
#         try:
#             # num1, operator, num2 = command.split()
#             num1, operator, num2 = parse_expression(command)
#             result = calculate(num1,operator,num2)
#             print(f"결과 : {result}")
#         except ValueError as ve:
#             print(ve)
#         except Exception as e:
#             print(f"예기치 못한 에러 발생 : {e}")

# if __name__ == "__main__":
#     main()
