from django.shortcuts import render, redirect
from .models import PersonalDetails, MedicalHistory
from .forms import PersonalDetailsForm, MedicalHistoryForm
from .models import MedicalHistory
from django.shortcuts import get_object_or_404, redirect

def edit_profile(request):
    profile = PersonalDetails.objects.first()  # Get the first entry

    if request.method == 'POST':
        form = PersonalDetailsForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Go back to profile page
    else:
        form = PersonalDetailsForm(instance=profile)

    return render(request, 'medical_records/edit_profile.html', {'form': form})

def edit_record(request, record_id):
    record = get_object_or_404(MedicalHistory, id=record_id)
    if request.method == 'POST':
        form = MedicalHistoryForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = MedicalHistoryForm(instance=record)
    return render(request, 'medical_records/edit_record.html', {'form': form})

def delete_record(request, record_id):
    record = get_object_or_404(MedicalHistory, id=record_id)
    if request.method == 'POST':
        record.delete()
        return redirect('dashboard')
    return render(request, 'medical_records/confirm_delete.html', {'record': record})
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
