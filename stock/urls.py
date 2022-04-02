from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-stocks/', views.add_stock, name='add-stock'),
    path('buy-stocks-rec/', views.stock_recommendation, name='buy-stocks-rec'),
    path('stock-comapany-action/', views.get_action_list, name='action-list'),
    path('stock-edit/<int:pk>/', views.update_stock, name='stock-edit'),
    path('delete-stock/<int:pk>/', views.delete_stock, name='delete-stock'),
    path('delete-news/<int:pk>/', views.delete_news, name='delete-news'),
    path('company-news/', views.corporate_action_list, name='company-news'),
    path('update-scan/', views.update_scan, name='update-scan'),
    path('register/', views.register, name='register'),
    path('verify-otp/', views.verify_phone_receive_sms, name='verify-otp'),
    path('logout/', views.logout_user, name='logout'),
    path('login/', views.login_user, name='login'),
    path('get-quote/', views.get_quote, name='get-quote'),
    # path('check-ann/', views.check_company_ann, name='check-ann'),
    path('refresh/', views.refresh, name='refresh'),
    # path('refresh-select/', views.refresh_select, name='refresh-select'),
    path('refresh-progress/', views.refresh_progress, name='refresh-progress'),
    path('refresh-progress-select/', views.refresh_progress_select, name='refresh-progress-select'),
    # path('refresh-stop/', views.refresh_stop, name='refresh_stop'),
    path('terms-service/', views.terms_service, name='terms-service'),
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),
    path('stock-chart/<str:stock_id>/<str:stock_name>/', views.stock_chart, name='stock-chart'),
]