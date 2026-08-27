from django.shortcuts import render, redirect, get_object_or_404
from .models import Ticket

def list_tickets(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        email = request.POST.get('email')
        priority = request.POST.get('priority')
        desc = request.POST.get('description')
        Ticket.objects.create(title=title, email=email, priority=priority, description=desc)
        return redirect('ticket_list')

    tickets = Ticket.objects.order_by('-created_at')
    return render(request, 'tickets/index.html', {'tickets': tickets})

def toggle_status(request, pk):
    ticket = get_object_or_404(Ticket, id=pk)
    ticket.status = 'RESOLVED' if ticket.status == 'OPEN' else 'OPEN'
    ticket.save()
    return redirect('ticket_list')
