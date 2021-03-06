from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from qa.models import Question, Answer

# Create your views here.
def test(request, *args, **kwargs):
	return HttpResponse('OK')

def new_questions(request):
	quests = Question.objects.new()
	limit = 10
	page = request.GET.get('page', 1)
	paginator = Paginator(quests, limit)
	paginator.baseurl = "/?page="
	page = paginator.page(page)
	return render(request, 'main.html', {
		'q': page.object_list,
		'paginator': paginator,
		'page': page})

def popular(request):
	pops = Question.objects.popular()
	limit = 10
	page = request.GET.get('page', 1)
	paginator = Paginator(pops, limit)
	paginator.baseurl = "/popular/?page="
	page = paginator.page(page)
	return render(request, 'popular.html', {
		'q': page.object_list,
		'paginator': paginator,
		'page': page})

def question_page(request, id):
	q = get_object_or_404(Question, pk=id)
	a = Answer.objects.filter(question = id)
	return render(request, 'question.html', {'q': q, 'a': a})
