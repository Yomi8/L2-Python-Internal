from main.py import encrypt

decrypt_encrypt = input('Do you want to encrypt or decrypt a message?')
if decrypt_encrypt == 'encrypt':
  text_encrypt = input('Enter text for encryption: ')
  shift_encrypt = int(input('Enter shift for encryption: '))
  encrypt(text_encrypt, shift_encrypt)
  print(encrypt)
  file_no_file = input('Do you want to save this to a file?')
  if file_no_file == 'yes':
    to_file()
  else:
    print('Okay, bye!')
if decrypt_encrypt == 'decrypt':
  text_file = input('Do you want to decrypt from a file or text? ')
  if text_file == 'file':
    file_name = input('Enter file name: ')
    file_name = file_name + '.txt'
    file_name = open(file_name, 'r')
    text_file = file_name.read()
    file_name.close()
    print(text_file)
  else:
    text_file = input('Enter text for decryption: ')
    shift_decrypt = int(input('Enter shift for encryption: '))

  