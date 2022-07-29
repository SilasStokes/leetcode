#! /usr/bin/env python3


def func(x: list):
	x[0] = 1
	return x



def main():
	x = [0]
	print(x)
	print(hex(id(x)))


	y = func(x)
	print(x)
	print(hex(id(x)))
	print(y)
	print(hex(id(y)))

	return None


if __name__ == "__main__":
	main()