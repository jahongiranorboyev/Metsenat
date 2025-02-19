import uuid

from faker import Faker
from decimal import Decimal

from django.db import transaction
from django.utils.text import slugify
from django.core.management.base import BaseCommand

from apps.appeals.models import Appeal
from apps.users.models import CustomUser
from apps.sponsors.models import StudentSponsor
from apps.general.models import University, PaymentMethod

fake = Faker()

class Command(BaseCommand):
    help = "Creates fake data for testing"

    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Creating fake data..."))

        try:
            # Universities
            universities = [
                University(
                    id=uuid.uuid4(),
                    name=fake.company(),
                    contract_amount=Decimal(fake.random_int(min=5000000, max=50000000)),
                    slug=slugify(fake.company())
                )
                for _ in range(5)
            ]
            University.objects.bulk_create(universities)

            # Payment Methods
            payment_methods = [
                PaymentMethod(
                    id=uuid.uuid4(),
                    name=fake.word(),
                    slug=slugify(fake.word())
                )
                for _ in range(5)
            ]
            PaymentMethod.objects.bulk_create(payment_methods)

            # Custom Users (Students and Sponsors)
            students, sponsors, users = [], [], []
            for _ in range(50):
                role = fake.random_element([CustomUser.UserRole.STUDENT, CustomUser.UserRole.SPONSOR])
                phone_number = f"+998{fake.random_int(900000000, 999999999)}"
                first_name, last_name = fake.first_name(), fake.last_name()
                university = fake.random_element(universities) if role == CustomUser.UserRole.STUDENT else None
                sponsor_type = fake.random_element(["physical", "legal"]) if role == CustomUser.UserRole.SPONSOR else None
                necessary_balance = university.contract_amount if university else Decimal("0")

                user = CustomUser(
                    id=uuid.uuid4(),
                    phone_number=phone_number,
                    first_name=first_name,
                    last_name=last_name,
                    role=role,
                    university=university,
                    sponsor_type=sponsor_type,
                    necessary_balance=necessary_balance
                )
                users.append(user)
                if role == CustomUser.UserRole.STUDENT:
                    students.append(user)
                else:
                    sponsors.append(user)

            CustomUser.objects.bulk_create(users)

            # Appeals
            appeals = [
                Appeal(
                    id=uuid.uuid4(),
                    sponsor_fullname=fake.name(),
                    phone_number=f"+998{fake.random_int(900000000, 999999999)}",
                    amount=Decimal(fake.random_int(min=1000000, max=50000000)),
                    available_balance=Decimal(fake.random_int(min=1000000, max=50000000)),
                    status=fake.random_element([
                        Appeal.AppealStatus.New, Appeal.AppealStatus.Approved,
                        Appeal.AppealStatus.Reviewing, Appeal.AppealStatus.Cancelled
                    ]),
                    sponsor=fake.random_element(sponsors),
                    payment_method=fake.random_element(payment_methods)
                )
                for _ in range(50)
            ]
            Appeal.objects.bulk_create(appeals)

            # Student-Sponsor Relationship
            student_sponsor_relations = [
                StudentSponsor(
                    id=uuid.uuid4(),
                    appeal=fake.random_element(appeals),
                    student=fake.random_element(students),
                    amount=Decimal(fake.random_int(min=1000000, max=50000000))
                )
                for _ in range(50)
            ]
            StudentSponsor.objects.bulk_create(student_sponsor_relations)

            self.stdout.write(self.style.SUCCESS("Successfully created fake data!"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error occurred: {e}"))
            raise
