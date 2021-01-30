import sys
import pytest
import yaml
from pythoncode.Calculator import Calculator

def get_datas1():
    with open("datas/calc_add.yml") as f:
        datas1 = yaml.safe_load(f)
    return (datas1['add']['datas'], datas1['add']['ids'])

def get_datas2():
    with open("datas/calc_div.yml") as f:
        datas2 = yaml.safe_load(f)
    return (datas2['div']['datas'], datas2['div']['ids'])

# 测试计算类
class TestCalc:
    datas1: list = get_datas1()
    datas2: list = get_datas2()

    # 前置条件
    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()

    # 后置条件
    def teardown_class(self):
        print("结束计算")

    #测试相加功能
    @pytest.mark.parametrize("a, b, result", datas1[0], ids=datas1[1])
    def test_add(self, a, b, result):
        print(f"a={a} , b ={b} ,result={result}")
        assert result == self.calc.add(a, b)

    #测试相除功能
    @pytest.mark.parametrize("a, b, result", datas2[0], ids=datas2[1])
    def test_div(self, a, b, result):
        print(f"a={a} , b={b}, result={result}")
        assert result == self.calc.div(a, b)



