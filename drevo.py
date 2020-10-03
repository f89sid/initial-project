import os

path = input("Введите директорию:")

for root, dirs, files in os.walk(path):
	print(root)