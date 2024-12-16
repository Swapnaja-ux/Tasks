def caesar_cipher(text, shift):
  """Encrypts or decrypts a message using the Caesar cipher.

  Args:
    text: The message to be encrypted or decrypted.
    shift: The number of positions to shift the letters.

  Returns:
    The encrypted or decrypted message.
  """

  result = ""
  for char in text:
    if char.isalpha():
      shift_char = ord(char) + shift
      if char.isupper():
        shift_char = shift_char % 65 + 65
      else:
        shift_char = shift_char % 97 + 97
      result += chr(shift_char)
    else:
      result += char
  return result

def main():
  while True:
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
      text = input("Enter the message to encrypt: ")
      shift = int(input("Enter the shift value: "))
      encrypted_text = caesar_cipher(text, shift)
      print("Encrypted message:", encrypted_text)
    elif choice == 2:
      text = input("Enter the message to decrypt: ")
      shift = int(input("Enter the shift value: "))
      decrypted_text = caesar_cipher(text, -shift)
      print("Decrypted message:", decrypted_text)
    elif choice == 3:
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()