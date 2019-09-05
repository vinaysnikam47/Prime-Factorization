# Program to find out happy numbers

# Function to check whether number is happy number or not
def is_happy_num(num):

	while True:

		add = 0
		list_num = list(num)

		for i in list_num:
			n = int(i)
			add += (n**2)

		if add == 1:
			return True
		elif add != 1 and len(str(add)) == 1:
			return False
		else:
			num = str(add)
			continue

# Function to find out first 8 happy numbers
def main():
	
	happy_numbers = []

	for num in range(100):

		if is_happy_num(str(num)):
			happy_numbers.append(num)
			if len(happy_numbers) == 8:
				break
			continue

		else:
			pass

	print(f"First 8 happy numbers are : {happy_numbers}")

if __name__ == '__main__':
	main()