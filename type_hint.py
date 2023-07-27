from typing import List, Dict

price: int = 100
tax: float = 1.1

def calu_price_include_tax(price: int, tax: float) -> int:
  return int(price * tax)

if __name__ == '__main__':
  print (f'{calu_price_include_tax(price, tax)}円')


sample_list: List[int] =[1,2,3,4]
sample_dict: Dict[str, str] ={'username': 'abc'}
