# 被测类：计算器
class Calculator:
    def add(self, a, b):
        return a + b

    def div(self, a, b):
        try:
            return a / b
        except:
            ZeroDivisionError
            print("程序出现异常，异常信息：除数为0")
