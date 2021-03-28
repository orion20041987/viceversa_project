from django.shortcuts import render

def home(request):
	return render(request, 'home.html')


def tryit(request):
	return render(request, 'tryit.html')

def revers(request):
	user_text = request.GET['usertext']
	user_text_word_list = [x for x in user_text.split()]
	user_text_len = len(user_text_word_list)
	reversed_text = user_text[::-1]
	return render(request, 'reverse.html', {'usertext':user_text, 'usertextlen':user_text_len, 'reversedtext':reversed_text})
