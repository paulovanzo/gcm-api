from django.http import JsonResponse
from .models import Account

def view_balance(request, account_id):
    try:
        account = Account.objects.get(id=account_id)
        balance = account.balance
        return JsonResponse({'saldo': balance})
    except Account.DoesNotExist:
        return JsonResponse({'error': 'Conta não encontrada'}, status=404)
