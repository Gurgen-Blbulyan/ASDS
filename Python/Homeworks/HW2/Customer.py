import sys
sys.path.append("/Users/gurgenblbulyan/Desktop/ASDS/PYTHON/HW/HW2")
import argparse


from Productcheck import check

def buy(product,num,price):
    if check(product, num):
        print(f"You bought {product} and spent {num*price}")
    else:
        print("Sorry! We are out of this product.")
        
parser = argparse.ArgumentParser()

parser.add_argument("product", help="product type",type=str)

parser.add_argument("num", help="number of product", type=int)

parser.add_argument("price", help="price of product", type=int)

args = parser.parse_args()

def main():
    buy(args.product,args.num,args.price)

if __name__ == '__main__':
    main()
    