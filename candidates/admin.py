from django.contrib import admin
from .models import Candidate

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'gemini_score', 'created_at')
    search_fields = ('name', 'email')
    ordering = ('-gemini_score',)
