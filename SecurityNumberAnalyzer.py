class SecurityAnalyzer:

  def __init__(self, num: int):
    self.num = num
    self.digit_count = 0
    self.digit_sum = 0
    self.digit_product = 1
    self.max_digit = 0
    self.min_digit = 9
    self.reversed_num = 0
    self.analyze()

  def analyze(self):
    temp = self.num
    while temp > 0:
      current_digit = temp % 10
      self.digit_count += 1
      self.digit_sum += current_digit
      self.digit_product *= current_digit
      if current_digit > self.max_digit:
        self.max_digit = current_digit
      if current_digit < self.min_digit:
        self.min_digit = current_digit
      self.reversed_num = self.reversed_num * 10 + current_digit
      temp //= 10

  def get_classification(self):
    is_palindrome = self.num == self.reversed_num
    if self.digit_sum > 20 and self.max_digit >= 8 and is_palindrome:
      return "STRONG SECURITY NUMBER"
    else:
      return "NORMAL SECURITY NUMBER"

  def display_results(self):
    print("\n--- Analysis Output ---")
    print(f"Number of Digits : {self.digit_count}")
    print(f"Sum of Digits    : {self.digit_sum}")
    print(f"Product of Digits: {self.digit_product}")
    print(f"Largest Digit    : {self.max_digit}")
    print(f"Smallest Digit   : {self.min_digit}")
    print(f"Reverse          : {self.reversed_num}")
    print(f"\nResult: {self.get_classification()}")


if __name__ == "__main__":
  try:
    user_input = int(input("Enter a positive integer: "))
    if user_input <= 0:
      print("Please enter a positive integer.")
    else:
      analyzer = SecurityAnalyzer(user_input)
      analyzer.display_results()
  except ValueError:
    print("Invalid input. Please enter a valid integer.")