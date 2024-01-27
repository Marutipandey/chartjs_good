from django.shortcuts import render
from django.db.models import Count
from .models import Student

def home(request):
    # Aggregate counts based on gender and year for verified students
    gender_year_counts = Student.objects.filter(verified=True).values('gender', 'dateField__year').annotate(count=Count('id'))

    data = []
    for item in gender_year_counts:
        data.append({
            'gender': item['gender'],
            'year': item['dateField__year'],
            'count': item['count'],
        })

    context = {
        'data': data,
        'gender_list': list(set([item['gender'] for item in data])),
        'year_list': list(set([item['year'] for item in data])),
    }

    return render(request, 'index.html', context)
