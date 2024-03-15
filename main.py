from functions import encrypt, decrypt, file_write, file_read

decrypt_encrypt = input('Do you want to encrypt or decrypt a message? ')
if decrypt_encrypt == 'encrypt':

  text_encrypt = input('Enter text for encryption: ')
  shift_encrypt = int(input('Enter shift for encryption: '))

  encrypted = encrypt(text_encrypt, shift_encrypt)

  print(encrypted)

  file_no_file = input('Do you want to save this to a file? ')

  if file_no_file == 'yes':
    file_write("encoded.txt", encrypted)
  else:
    print('Okay, bye!')

elif decrypt_encrypt == 'decrypt':

  text_file = input('Do you want to decrypt from a file or text? ')

  if text_file == 'file':

    file_name = input('Enter file name: ')
    message = file_read(file_name)

    print(f"Encrypted message: {message}")
    shift_file = int(input('Enter shift for decryption: '))

    decrypted = decrypt(message, shift_file)
    print(f"Decrypted message: {decrypted}")

  else:
    text_file = input('Enter text for decryption: ')
    shift_decrypt = int(input('Enter shift for decryption: '))

    result = decrypt(text_file, shift_decrypt)
    print(f"Decrypted text: {result}")

  