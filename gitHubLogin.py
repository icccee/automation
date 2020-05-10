from webbot import Browser

# run automation to login github automaticly 
# without typing usrname and psw

# webbot is super easy to do the automation
# only down side is only supporting google chrome
def openUrl(url):
	try:
		
		web = Browser()
		web.go_to(url)
		return web

	except:
		return "Not valid website" 

def loginCredencial(usrname,psw,bot):
	# find usr name area
	bot.click('Sign in')
	bot.type(usrname,into='Email')
	bot.click('NEXT', tag ='span')
	bot.type(psw, into ='Password', id= 'passwordFieldId')
	bot.click('Sign in', tag ='span')



if __name__ == "__main__":
	# url github
	url = "github.com"

	# login info
	usrName ='username'
	psw = 'password'
	bot = openUrl(url)
	loginCredencial(usrName,psw,bot)
	#bot.close_current_tab()
