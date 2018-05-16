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
