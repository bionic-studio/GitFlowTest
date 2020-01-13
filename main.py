import video
import mail


def func_video():
	video.fast()
	video.slowly()

def func_mail():
	mail.send_msg()
	mail.receive_msg()
	mail.auto_send()

def main():
	func_video()
	func_mail()

if __name__ == '__main__':
	main()
