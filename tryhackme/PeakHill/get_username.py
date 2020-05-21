import textwrap
import pickle
import re
from Crypto.Util.number import bytes_to_long, long_to_bytes

# with open('.creds') as handler:
# 	data = handler.read()

# data = textwrap.wrap(data, 8)
# # print(data)


# byte = []

# with open('new', 'wb+') as writer:
# 	for d in data:
# 		b = int(d, 2).to_bytes(len(d) // 8, byteorder='big')
# 		print(b)
# 		writer.write(b)

def atoi(text):
	return int(text) if text.isdigit() else text

def natural_keys(text):
	text = text[0]
	return [ atoi(c) for c in re.split(r'(\d+)', text) ]

pickle_off = open("new", "rb")
creds = pickle.load(pickle_off)
pickle_off.close()


ssh_user = []
ssh_pass = []
for cred in creds:
	if 'user' in cred[0]:
		ssh_user.append(cred)
	else:
		ssh_pass.append(cred)

ssh_user.sort()
ssh_pass.sort(key=natural_keys)

ssh_user = [user[1] for user in ssh_user]
print('Username: ', ''.join(ssh_user))
ssh_pass = [passwd[1] for passwd in ssh_pass]
print('Password: ', ''.join(ssh_pass))

username = long_to_bytes(1684630636)
password = long_to_bytes(2457564920124666544827225107428488864802762356L)

print(username, password)