# ABC226 - A

'''
組み込み関数のround()では0.5のような値の場合、四捨五入した値(1)ではなく切り捨て値(0)が出力されてしまう
したがって、四捨五入処理を実装するためには別途専用の標準モジュールを利用する必要がある
pythonの場合はdecimalモジュールのDecimalクラスを用いて四捨五入処理を実装することができる
'''

from decimal import Decimal, ROUND_HALF_UP

N = input()
print(Decimal(N).quantize(Decimal("1"),rounding=ROUND_HALF_UP))