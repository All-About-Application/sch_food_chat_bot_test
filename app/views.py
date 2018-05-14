from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app.my_module.button import *
from app.my_module.repdic import *
from app.my_module.scheduleparser import *
from pytz import timezone
import requests, datetime, json

# 데이터 목록
# menu/SnowFlowerOne.json     향설1 생활관
# menu/SnowFlowerTwo.json     향설2 생활관
# menu/SnowFlowerThree.json   향설3 생활관
# menu/StudentUnion.json      학생 회관
# menu/FacultyRestaurant.json 교직원 식당

# 개발자 정보 메세지
dev_info = '''[*] 컴퓨터소프트웨어공학과
[*] 17학번 김민수
[*] Github : alstn2468
[*] KakaoTalk : alstn2468
[*] 새로운 기능 문의 환영
[*] 에러 발견 문의 환영'''

# 선택한 버튼이 학식 메뉴일 경우 메세지 포매팅
select_button = '[*] 선택한 버튼 : {0}\n[*] {1}의\n[*] {0} 메뉴입니다.\n'

# 데이터를 보기 좋게 출력하기 위한 문자열 처리 함수
def char_replace(meal) :

	for key, value in trans_dic.items() :

		meal = meal.replace(key, value)

	return meal

# 결과를 출력하고 다시 입력을 받기 위한 함수
def re_process(output) :

    return JsonResponse (
		{
            'message':
			{
                'text': output
            },
            'keyboard':
			{
                'type': 'buttons',
                'buttons' : basic_button
            }
        }
	)

# 학식 버튼을 눌렀을 때 세부 버튼을 받기 위한 함수
def food_sel_process() :

	return JsonResponse (
		{
			'message' :
			{
				'text' : '어느 곳의 메뉴가 궁금하신가요?'
			},
			'keyboard' :
			{
				'type' : 'buttons',
				'buttons' : food_sel_process_button
			}
		}
	)

def keyboard(request) :

	return JsonResponse (
		{
		'type' : 'buttons',
		'buttons' : basic_button
		}
	)

@csrf_exempt
def answer(request) :

	json_str = (request.body).decode('utf-8')
	received_json = json.loads(json_str)
	content_name = received_json['content']
	type_name = received_json['type']
	user_key = received_json['user_key']

	# 오늘
	today = datetime.datetime.now()
	today_info = today.strftime('%Y년 %m월 %d일')
	today_weekday = today.weekday()

	if content_name == '학식' :
		return food_sel_process()

	elif content_name == '향설1 생활관' :

		try :
			with open('app/menu/SnowFlowerOne.json', 'rb') as f :
				datas = json.load(f)

			if today_weekday == 0 :
				meal = str(datas.get('월'))
				meal = char_replace(meal)

			elif today_weekday == 1 :
				meal = str(datas.get('화'))
				meal = char_replace(meal)

			elif today_weekday == 2 :
				meal = str(datas.get('수'))
				meal = char_replace(meal)

			elif today_weekday == 3 :
				meal = str(datas.get('목'))
				meal = char_replace(meal)

			elif today_weekday == 4 :
				meal = str(datas.get('금'))
				meal = char_replace(meal)

			elif today_weekday == 5 :
				meal = str(datas.get('토'))
				meal = char_replace(meal)

			else :
				meal = '\n일요일에 ' + content_name + ' 식당은\n운영하지 않습니다.'

		except Exception as e:
			meal = str(e) + '\n에러메세지가 보이면 관리자에게 알려주세요.'

		send_message = select_button.format(content_name, today_info) + meal

		return re_process(send_message)

	elif content_name == '향설2 생활관' :

		try :
			with open('app/menu/SnowFlowerTwo.json', 'rb') as f :
				datas = json.load(f)

			if today_weekday >= 0 or today_weekday <= 4  :
				meal = str(datas.get('향2'))
				meal = char_replace(meal)

			else :
				meal = '\n주말에 ' + content_name + ' 식당은\n운영하지 않습니다.'

		except Exception as e:
			meal = str(e) + '\n에러메세지가 보이면 관리자에게 알려주세요.'

		send_message = select_button.format(content_name, today_info) + meal

		return re_process(send_message)

	elif content_name == '향설3 생활관' :

		try :
			with open('app/menu/SnowFlowerThree.json', 'rb') as f :
				datas = json.load(f)

			if today_weekday == 0 :
				meal = str(datas.get('월'))
				meal = char_replace(meal)

			elif today_weekday == 1 :
				meal = str(datas.get('화'))
				meal = char_replace(meal)

			elif today_weekday == 2 :
				meal = str(datas.get('수'))
				meal = char_replace(meal)

			elif today_weekday == 3 :
				meal = str(datas.get('목'))
				meal = char_replace(meal)

			elif today_weekday == 4 :
				meal = str(datas.get('금'))
				meal = char_replace(meal)

			else :
				meal = str(datas.get('주말'))
				meal = char_replace(meal)

		except Exception as e:
			meal = str(e) + '\n에러메세지가 보이면 관리자에게 알려주세요.'

		send_message = select_button.format(content_name, today_info) + meal

		return re_process(send_message)

	elif content_name == '학생회관' :

		try :
			with open('app/menu/StudentUnion.json', 'rb') as f :
				datas = json.load(f)

			if today_weekday == 0 :
				meal = str(datas.get('월'))
				meal = char_replace(meal)

			elif today_weekday == 1 :
				meal = str(datas.get('화'))
				meal = char_replace(meal)

			elif today_weekday == 2 :
				meal = str(datas.get('수'))
				meal = char_replace(meal)

			elif today_weekday == 3 :
				meal = str(datas.get('목'))
				meal = char_replace(meal)

			elif today_weekday == 4 :
				meal = str(datas.get('금'))
				meal = char_replace(meal)

			else :
				meal = '\n주말에 ' + content_name + ' 식당은\n운영하지 않습니다.'

		except Exception as e:
			meal = str(e) + '\n에러메세지가 보이면 관리자에게 알려주세요.'

		send_message = select_button.format(content_name, today_info) + meal

		return re_process(send_message)

	elif content_name == '교직원 식당' :

		try :
			with open('app/menu/FacultyRestaurant.json', 'rb') as f :
				datas = json.load(f)

			if today_weekday == 0 :
				meal = str(datas.get('월'))
				meal = char_replace(meal)

			elif today_weekday == 1 :
				meal = str(datas.get('화'))
				meal = char_replace(meal)

			elif today_weekday == 2 :
				meal = str(datas.get('수'))
				meal = char_replace(meal)

			elif today_weekday == 3 :
				meal = str(datas.get('목'))
				meal = char_replace(meal)

			elif today_weekday == 4 :
				meal = str(datas.get('금'))
				meal = char_replace(meal)

			else :
				meal = '\n주말에 '+ content_name + '은\n운영하지 않습니다.'

		except Exception as e:
			meal = str(e) + '\n에러메세지가 보이면 관리자에게 알려주세요.'

		send_message = select_button.format(content_name, today_info) + meal

		return re_process(send_message)

	elif content_name == '처음으로' :

		return keyboard()

	elif content_name == '종강' :

		# 종강 일
		finish = datetime.datetime(2018, 6, 22)
		finish_info = finish.strftime('%Y년 %m월 %d일')
		date_dif = finish - today

		send_message = '[*] 선택한 버튼 : ' + content_name + '\n[*] 오늘 : ' + today_info + '\n[*] 종강 : ' + finish_info + '\n[*] 종강까지 %d일 남았습니다.' % date_dif.days

		return re_process(send_message)

	elif content_name == '학사 일정' :

		result_message = parser()

		send_message = '[*] 선택한 버튼 : ' + content_name + '\n[*] ' + today_info + result_message

		return re_process(send_message)

	elif content_name == '개발자 정보' :

		send_message = '[*] 선택한 버튼 : ' + content_name + '\n' + dev_info

		return re_process(send_message)

	else :

		error_message = '[*] 심각한 오류입니다.\n[*] 개발자에게 알려주세요'

		if type_name == 'photo' :
			error_message = '[*] 사진을 보내도 기능이 없네요.\n[*] 버튼을 눌러주세요!'

		elif type_name == 'video' :
			error_message = '[*] 영상을 보내도 기능이 없네요.\n[*] 버튼을 눌러주세요!'

		elif type_name == 'audio' :
			error_message = '[*] 녹음 파일을 보내도 기능이 없네요.\n[*] 버튼을 눌러주세요!'

		return re_process(error_message)
