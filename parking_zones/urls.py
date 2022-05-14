from django.urls import path
from . import views


urlpatterns = [
    path('book/', views.ReservationView.as_view(), name='book'),
    path('ticket/', views.Ticket_Pdf.as_view(), name='ticket'),
    path('all_tickets/', views.Display_Tickets.as_view(), name='all-tickets'),
    path('checkout/', views.check_out, name='checkout')
]
