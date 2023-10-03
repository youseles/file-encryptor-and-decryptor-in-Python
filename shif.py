import pyAesCrypt

password = input('Введите пароль для шифрования файла: ')

#encryptt
pyAesCrypt.encryptFile('infile', 'outfile', password)