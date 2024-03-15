'''
  Name: Amanda Henderson and Cameron Labes
  James Hargest College
  Programming Internal Python for 2.7 & 2.8 ~ 10 credits
  Due Date: 12 April
'''

# Functons
def encrypt(message, shift):
  output = []
  for character in message:
    if character.isalpha():
      if character.isupper():
        output.append(chr((ord(character) + shift - 65) % 26 + 65))
      else:
        output.append(chr((ord(character) + shift - 97) % 26 + 97))
    else:
      output.append(character)
  output = ''.join(output)
  return output

def decrypt(message, shift):
  return encrypt(message, -shift)

def file_write(file_name, message):
  with open(file_name, 'w') as file:
    file.write(message)
    file.close()
    
def file_read(file_name):
  with open(file_name, 'r') as file:
    message = file.readline()
    file.close()
  return message