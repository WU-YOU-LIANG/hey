password = 'a123456'
i = 3
while i >= 0:
	pwd = input('請輸入你的密碼: ')
	if pwd == password:
		print('登入成功')
		break
	else:
	    if i > 0:
	    	print('密碼錯誤.你還有', i ,'次機會')
	    	i = i - 1
	    else:
	    	print('密碼錯誤.沒機會了可憐哪')
	    	break
	    