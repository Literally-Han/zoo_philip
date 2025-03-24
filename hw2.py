Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def get_integer():
...     return int(input("동전으로 교환하고자 하는 금액은? "))
... 
... amount = get_integer()
... 
... coin_types = [500, 100, 50, 10]  
... for coin in coin_types:
...     num = amount // coin      
...     print(f"{coin}원 동전의 개수: {num}")
