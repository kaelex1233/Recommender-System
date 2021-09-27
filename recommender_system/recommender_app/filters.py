import django_filters
from django_filters import DateFilter, CharFilter

class StudentInfoFilter(django_filters.FilterSet):
	name = CharFilter(field_name='name', lookup_expr='icontains')
	job_description = CharFilter(field_name='job_description', lookup_expr='icontains')
	skills = CharFilter(field_name='skills', lookup_expr='icontains')


	class Meta:
		model = Student
		fields = '__all__'
		exclude = ['phone', 'email', 'profile_picture', 'date_created']
