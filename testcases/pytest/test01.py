# -*- coding:utf-8 -*-
import pytest


class TestLoginCase:
    def test01(self):
        print('测试01')

    def test02(self):
        print('测试01')


if __name__ == '__main__':
    pytest.main(['-sv', 'test01.py'])
