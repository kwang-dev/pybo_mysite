from inspect import classify_class_attrs
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views import generic
from .models import Question

# from django.http import HttpResponse
# Create your views here.

def index(request):
     """
     pybo 목록 출력
     """
     question_list = Question.objects.order_by('-create_date')
     context = {'question_list': question_list}
     return render(request, 'pybo/question_list.html', context)

# class IndexView(generic.ListView):
#     """
#     pybo 목록 출력
#     """
#     def get_queryset(self):
#         return Question.objects.order_by('-create_date')


def detail(request, question_id):
     """
     pybo 내용 출력
     """
 #    question = Question.objects.get(id=question_id)
     question = get_object_or_404(Question, pk=question_id)
     context = {'question': question}
     return render(request, 'pybo/question_detail.html', context)

# class DetailView(generic.DetailView):
#     """
#     pybo 내용 출력
#     """
#     model = Question

def answer_create(request, question_id):
     """
     pybo 답변 등록
     """
     question = get_object_or_404(Question, pk=question_id)
     question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
     return redirect('pybo:detail', question_id=question_id)
