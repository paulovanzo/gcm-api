from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from decimal import Decimal

from .models import Account

def menu(request):
    return render(request, 'account/menu.html')

def view_balance(request, account_id):
    try:
        account = Account.objects.get(id=account_id)
        balance = account.balance
        return JsonResponse({'saldo': balance})
    except Account.DoesNotExist:
        return JsonResponse({'error': 'Conta não encontrada'}, status=404)

def check_account(request):
    if request.method == 'POST':
        number = request.POST.get('number')
        account = get_object_or_404(Account, number=number)
        return JsonResponse({'saldo': account.balance, 'numero': account.number, 'tipo de conta': account.account_type, 'pontos': account.points})
    return render(request, 'account/check_account.html')

def create_account(request):
    if request.method == 'POST':
        number = request.POST.get('number')
        account_type = request.POST.get('account_type')
        
        initial_balance = request.POST.get('saldo_inicial')
        account = Account.objects.create(number=number, account_type=account_type)
        
        if account.account_type == 'bonus':
            account.points += 10
            account.save()
        
        if Account.objects.filter(number=number).exists():
            return HttpResponse("Essa conta já está cadastrada.")
        
        account.balance = initial_balance
        account.save()

        return HttpResponse(f'Conta criada com sucesso. Número: {account.number}. ' + (f'Pontos: {account.points}' if account.account_type == 'bonus' else ''))

    return render(request, 'account/create_account.html')

def check_balance(request):
    if request.method == 'POST':
        number = request.POST.get('number')
        account = get_object_or_404(Account, number=number)
        return HttpResponse(f'Saldo da conta {account.number}: {account.balance}')
    return render(request, 'account/check_balance.html')

def credit(request):
    if request.method == 'POST':
        number = request.POST.get('number')
        value = Decimal(request.POST.get('value'))
        account = get_object_or_404(Account, number=number)
        if value < 0:
            return JsonResponse({'error': 'Valor inválido'}, status=400)
        account.balance += value

        if account.account_type == 'bonus':
            account.points += int(value / 100)

        account.save()
        return HttpResponse(f'Crédito realizado na conta {account.number}. Novo saldo: {account.balance}')
    return render(request, 'account/credit.html')

def debit(request):
    if request.method == 'POST':
        number = request.POST.get('number')
        value = Decimal(request.POST.get('value'))
        account = get_object_or_404(Account, number=number)

        if value < 0:
            return JsonResponse({'error': 'Valor inválido'}, status=400)

        if account.account_type == 'poupanca':
            if account.balance >= value:
                account.balance -= value
                account.save()
                return HttpResponse(f'Débito realizado na conta {account.number}. Novo saldo: {account.balance}')
            else:
                return JsonResponse({'error': 'Saldo insuficiente'}, status=400)    
        else:
            if account.balance >= value - 1000:
                account.balance -= value
                account.save()
                return HttpResponse(f'Débito realizado na conta {account.number}. Novo saldo: {account.balance}')
            else:
                return JsonResponse({'error': 'Saldo negativo ultrapassa -1000'}, status=400)    

    return render(request, 'account/debit.html')

def transfer(request):
    if request.method == 'POST':
        source_number = request.POST.get('source_number')
        destination_number = request.POST.get('destination_number')
        value = Decimal(request.POST.get('value'))
        source_account = get_object_or_404(Account, number=source_number)
        destination_account = get_object_or_404(Account, number=destination_number)

        if value < 0:
            return JsonResponse({'error': 'Valor inválido'}, status=400)
        if source_account.balance < value:
            return JsonResponse({'error': 'Conta de origem não possui saldo insuficiente'}, status=400)  
        source_account.balance -= value
        destination_account.balance += value

        if destination_account.account_type == 'bonus':
            destination_account.points += int(value / 150)

        source_account.save()
        destination_account.save()

    return render(request, 'account/transfer.html')

def yield_interest(request):
    if request.method == 'POST':
        number = request.POST.get('number')
        interest_rate = Decimal(request.POST.get('interest_rate'))

        account = get_object_or_404(Account, number=number, account_type='poupanca')
        current_balance = account.balance

        interest_amount = current_balance * (interest_rate / 100)
        account.balance += interest_amount
        account.save()

        return HttpResponse(f"Render Juros realizado com sucesso. Saldo atualizado: {account.balance}")

    return render(request, 'account/yield_interest.html')
