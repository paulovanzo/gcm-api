from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Account

def view_balance(request, account_id):
    try:
        account = Account.objects.get(id=account_id)
        balance = account.balance
        return JsonResponse({'saldo': balance})
    except Account.DoesNotExist:
        return JsonResponse({'error': 'Conta não encontrada'}, status=404)

def create_account(request):
    if request.method == 'POST':
        number = request.POST.get('number')
        account = Account.objects.create(number=number)
        return HttpResponse(f'Conta criada com sucesso. Número: {account.number}')
    return render(request, 'account/create_account.html')

def check_balance(request):
    if request.method == 'POST':
        number = request.POST.get('number')
        account = get_object_or_404(Account, number=number)
        return HttpResponse(f'Saldo da conta {account.number}: {account.balance}')
    return render(request, 'account/check_balance.html')
