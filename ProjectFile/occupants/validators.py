from django.core.exceptions import ValidationError

def validate_file_extension(value):
	if not value.name.endswith('.csv'):
		print("ERRORROORORO")
		raise ValidationError(u'Not a valid file type. Please upload a csv file containing WiFi Log Data')
