import argparse

parser = argparse.ArgumentParser()

parser.add_argument("text", help="some text",type=str)

parser.add_argument("to_replace", help="text to replace", type=str)

parser.add_argument("replaced", help="text to replace with", type=str)

args = parser.parse_args()

print("The given text: ", args.text)
print("First word: ",args.to_replace)
print("Second word: ",args.replaced)
print("Output string: ",args.text.replace(args.to_replace,args.replaced))
