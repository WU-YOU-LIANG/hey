password = 'a123456'
i = 3
while i >= 0:
	pwd = input('請輸入你的密碼: ')
	if pwd == password:
		print('登入成功')
		break
	elif i == 0:
		print('登入失敗')
		break
	else:
	    print('你還有', i ,'次機會')
	    i = i - 1