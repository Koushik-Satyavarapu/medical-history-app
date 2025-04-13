from django.shortcuts import render, redirect
from .models import PersonalDetails, MedicalHistory
from .forms import PersonalDetailsForm, MedicalHistoryForm

def dashboard(request):
    recent_records = MedicalHistory.objects.order_by('-date')[:5]
    profile = PersonalDetails.objects.first()
    return render(request, 'medical_records/dashboard.html', {
        'recent_records': recent_records,
        'profile': profile
    })

def profile(request):
    person = PersonalDetails.objects.first()
    return render(request, 'medical_records/profile.html', {'person': person})

def add_profile(request):
    if request.method == 'POST':
        form = PersonalDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = PersonalDetailsForm()
    return render(request, 'medical_records/add_profile.html', {'form': form})

def view_history(request):
    records = MedicalHistory.objects.all()
    return render(request, 'medical_records/view_history.html', {'records': records})

def add_record(request):
    if request.method == 'POST':
        form = MedicalHistoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_history')
    else:
        form = MedicalHistoryForm()
    return render(request, 'medical_records/add_record.html', {'form': form})
