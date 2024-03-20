while True:
  options = '''
  1. Encrypt Message
  2. Decrypt Message
  3. Exit
  '''

  print(options)

  user_selection = input("Your selection (1/2/3): ")

  if user_selection == '1':

    text_encrypt = input('Enter text for encryption: ')
    shift_encrypt = get_shift('Enter shift for encryption: ')

    encrypted = encrypt(text_encrypt, shift_encrypt)

    print(f"\nEncrypted Text: {encrypted}")

    file_no_file = input('\nDo you want to save this to a file? ')

    if file_no_file == 'yes':
      file_write("encoded.txt", encrypted)
    else:
      print('Okay, bye!')

  elif user_selection == '2':

    text_file = input('Do you want to decrypt from a file or text? ')

    if text_file == 'file':

      file_name = input('Enter file name: ')
      message = file_read(file_name)

      print(f"Encrypted message: {message}")



      decrypted = decrypt(message, get_shift('Enter shift for decryption: '))
      print(f"Decrypted message: {decrypted}")

    else:
      text_file = input('Enter text for decryption: ')
      shift_decrypt = get_shift('Enter shift for decryption: ')

      result = decrypt(text_file, shift_decrypt)
      print(f"Decrypted text: {result}")

  elif user_selection == '3':
    print('Exiting...')
    sleep(1)
    exit()

