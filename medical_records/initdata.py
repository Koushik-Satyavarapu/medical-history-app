from .models import PersonalDetails, MedicalHistory
from datetime import date

def load_default_data():
    if not PersonalDetails.objects.exists():
        PersonalDetails.objects.create(
            name="John Doe",
            age=30,
            gender="Male",
            contact="1234567890"
        )

    if not MedicalHistory.objects.exists():
        MedicalHistory.objects.create(
            title="Flu Treatment",
            description="Visited doctor for flu symptoms. Prescribed rest and medication.",
            date=date(2023, 3, 15)
        )
        MedicalHistory.objects.create(
            title="Allergy Checkup",
            description="Tested positive for dust allergy. Given antihistamines.",
            date=date(2023, 6, 20)
        )
        MedicalHistory.objects.create(
            title="COVID Vaccination",
            description="Received second dose of COVID-19 vaccine.",
            date=date(2021, 9, 10)
        )
