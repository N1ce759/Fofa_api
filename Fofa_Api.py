import base64
import requests

def banner():
	print(r"""
	 ______   ______   ______   ________            ________   ______   ________     
	/_____/\ /_____/\ /_____/\ /_______/\          /_______/\ /_____/\ /_______/\    
	\::::_\/_\:::_ \ \\::::_\/_\::: _  \ \         \::: _  \ \\:::_ \ \\__.::._\/    
	 \:\/___/\\:\ \ \ \\:\/___/\\::(_)  \ \         \::(_)  \ \\:(_) \ \  \::\ \     
	  \:::._\/ \:\ \ \ \\:::._\/ \:: __  \ \  _______\:: __  \ \\: ___\/  _\::\ \__  
	   \:\ \    \:\_\ \ \\:\ \    \:.\ \  \ \/______/\\:.\ \  \ \\ \ \   /__\::\__/\ 
	    \_\/     \_____\/ \_\/     \__\/\__\/\__::::\/ \__\/\__\/ \_\/   \________\/ """)
	print("\n\t\t\t\t\t\t\t\t\t" + "-----By N1ce")
def Search():
	email = r'xxx@xxx.com'
	api_key = r'xxxx'
	api = r'https://fofa.info/api/v1/search/all?email={}&key={}&qbase64={}&size=10000'
	arg = input('输入正则：')
	print("开始查询：" + arg)
	flag = base64.b64encode(arg.encode()).decode()
	try:
		response = requests.get(api.format(email,api_key,flag))
		results = response.json()["results"]
		print("共搜索到{}条记录！".format(len(results)))
		# 保存结果
		#file_name = r"{}.txt".format(arg)
		f = open("Result.txt","a+")
		for addr in results:
			f.write(addr[0]+'\n')
		f.close()
		print("已保存至Result.txt中！")
	except Exception as e:
		print("查询失败，请检查email和api_key是否正确！")

if __name__ == '__main__':
	banner()
	Search()