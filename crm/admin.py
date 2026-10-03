from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple

from crm.models import Anket, TypeOperations, Candidate, Doctor, MedCard


class TypeOperationsInline(admin.StackedInline):
    model = TypeOperations
    extra = 3


@admin.register(MedCard)
class MedCardAdmin(admin.ModelAdmin):
    formfield_overrides = {models.ManyToManyField: {'widget': CheckboxSelectMultiple}, }
    list_display = ('date_oper', 'anket_id', 'phone', 's_name', 'name', 'm_name')
    search_fields = ('anket_id', 'phone', 's_name', 'name', 'm_name')
    #list_editable = ('anket_id',)
    

@admin.register(Anket)
class AnketAdmin(admin.ModelAdmin):
    list_display = ('date_filling', 'external_id', 'state',)
    list_editable = ('external_id', 'state',)
    search_fields = ['date_filling', 'external_id', 'state']


@admin.register(TypeOperations)
class TypeOperationsAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'duration',  )
    list_display_links = ('code', 'name',)
    list_editable = ('duration', )


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    formfield_overrides = {models.ManyToManyField: {'widget': CheckboxSelectMultiple}, }
    search_fields = ['Sname', 'phoneNumber']
    date_hierarchy = 'date_oper'
    list_display = ('date_oper', 'phoneNumber', 'Sname', 'Name', 'Mname', 'Doctor', 'Surgeon')
    list_display_links = ('date_oper', 'Sname', 'Name', 'Mname')
    list_editable = ('Doctor',)


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('F_name', 'L_name', 'S_name', 'position', 'specialty')
    list_display_links = ('F_name', 'L_name', 'S_name', 'position', 'specialty',)
    # list_editable = ('plan_oper', 'opis_oper',)