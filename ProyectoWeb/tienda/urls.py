from django.urls import path

from  .import views


urlpatterns = [
    
    path('',views.tienda, name="Tienda"),
    path('categoria/<int:categorias_id>', views.productos_por_categoria, name="productos_por_categoria"),
    
    # path('productos/', views.lista_todos_los_productos, name="todos_los_productos"),

   ]

