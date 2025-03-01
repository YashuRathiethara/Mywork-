
from django.urls import path  
from employee import views  

urlpatterns = [ 
    path('emp/', views.emp, name='emp'),  # Added trailing slash
    path('show/', views.show, name='show'), 
    path('edit/<int:id>/', views.edit, name='edit'),  # Added trailing slash
    path('update/<int:id>/', views.update, name='update'),  # Added trailing slash
    path('delete/<int:id>/', views.destroy, name='delete'),
    path('consume_flask_endpoint/', views.consume_flask_endpoint, name='consume_flask_endpoint'),
    
    ]
