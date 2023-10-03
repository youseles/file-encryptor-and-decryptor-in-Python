import pyAesCrypt

password = input('Введите пароль для файла: ')

#decryptt
pyAesCrypt.decryptFile('outfile', 'infile', password)