import os


def is_valid_number(text):
  """Checks if the text is a valid non-negative number up to 200 digits."""
  if not text.isdigit():
    return False
  if len(text) > 200:
    return False
  return True


def add_numbers(num1, num2):
  """Adds two large numbers digit by digit from right to left."""
  # Make both strings the same length by padding with leading zeros
  max_len = max(len(num1), len(num2))
  num1 = num1.zfill(max_len)
  num2 = num2.zfill(max_len)

  carry = 0
  result = []

  # Loop from right to left (end of string to start)
  for i in range(max_len - 1, -1, -1):
    digit1 = int(num1[i])
    digit2 = int(num2[i])

    total = digit1 + digit2 + carry
    carry = total // 10  # Carry over for the next column
    result.append(str(total % 10))  # Keep the last digit

  # If there is a leftover carry at the very end, add it
  if carry > 0:
    result.append(str(carry))

  # Reverse the list back to correct order and join into a string
  result.reverse()
  return "".join(result)


def multiply_numbers(num1, num2):
  """Multiplies two large numbers using standard long multiplication."""
  # Handle special case if any number is 0
  if num1 == "0" or num2 == "0":
    return "0"

  # Initialize a list of zeros to hold the product digits
  n1 = len(num1)
  n2 = len(num2)
  result = [0] * (n1 + n2)

  # Reverse strings to work from right to left easily
  s1 = num1[::-1]
  s2 = num2[::-1]

  for i in range(n1):
    for j in range(n2):
      digit1 = int(s1[i])
      digit2 = int(s2[j])

      # Multiply digits and add existing value at this position
      product = (digit1 * digit2) + result[i + j]

      # Store the single digit and carry the rest over
      result[i + j] = product % 10
      result[i + j + 1] += product // 10

  # Remove any leading zeros at the end of our reversed list
  while len(result) > 1 and result[-1] == 0:
    result.pop()

  # Reverse back to normal and join into a string
  result.reverse()
  return "".join(str(d) for d in result)


def main():
  filename = input("Enter the filename: ")

  # 1. Check if file exists
  if not os.path.exists(filename):
    print(f"Error: The file '{filename}' was not found.")
    return

  # 2. Read the numbers from the file
  with open(filename, "r") as file:
    lines = file.readlines()

  if len(lines) < 2:
    print("Error: The file must contain at least two lines.")
    return

  num1 = lines[0].strip()
  num2 = lines[1].strip()

  # 3. Validate inputs
  if not is_valid_number(num1) or not is_valid_number(num2):
    print("Error: Numbers must be non-negative integers up to 200 digits.")
    return

  # 4. Calculate sum and product
  total_sum = add_numbers(num1, num2)
  total_product = multiply_numbers(num1, num2)

  # 5. Display results
  print("=== Large Number Operations ===")
  print(f"Number 1: {num1}")
  print(f"Number 2: {num2}")
  print("-" * 30)
  print(f"Sum:     {total_sum}")
  print(f"Product: {total_product}")


if __name__ == "__main__":
  main()