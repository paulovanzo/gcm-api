from django.apps import AppConfig

class ApiConfig(AppConfig):
    name = "account"
    
    def __str__(self):
        return str(self.number)