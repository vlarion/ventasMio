from django.contrib import admin
from django.urls import path
from . import views
from mantenedor.views import ComunaListado  , ComunaDetalle, ComunaCrear, ComunaActualizar, ComunaEliminar, ProveedorCombo, ProductoMirar, ProdCombo, ProdList
from mantenedor.views import PersonaListado,ProductoListado, ProdListado,ProductoDetalle, PersonaFrm, ProductoLeer, ProductoActualizar, ProductoEliminar, ProductoCrear
from mantenedor.views import Imagen

urlpatterns = [

    path('imagen', views.Imagen, name='image'),

##***********************************
    
    path('prodCombo', views.ProdCombo, name='prod_combo'),
    path('productoActualizar', views.ProductoActualizar),
    path('productoEliminar', views.ProductoEliminar),
    path('productoCrear', views.ProductoCrear),    
    path('productoMirar', views.ProductoMirar),
    path('productoListado/', views.ProductoListado ,name='producto_list'),
    path('prodListado/', views.ProdListado ,name='prod_list'),
    path('prodList/', views.ProdList ,name='produ_list'),
    path('proveedorCombo/', views.ProveedorCombo, name='Proveedor_combo'),
    path('comuna/detalle/<int:pk>', ProductoDetalle.as_view(template_name = "mantenedor/comuna/detalles.html"), name='detalles'),
    path('personaListado/', views.PersonaListado ,name='persona_list'),
    path('personaFrm/', views.PersonaFrm     ,name='persona_frm'),

##***********************************
    # La ruta 'leer' en donde listamos todos los registros o postres de la Base de Datos
    #path('comuna/', ComunaListado.as_view(template_name = "mantenedor/Comuna/index.html"), name='leer'),
    path('comunaFrm/', views.ComunaFrm     ,name='comuna_frm'),
    path('comunaListado/', views.ComunaListado ,name='comuna_list'),


    # La ruta 'detalles' en donde mostraremos una página con los detalles de un postre o registro 
    path('comuna/detalle/<int:pk>', ComunaDetalle.as_view(template_name = "mantenedor/comuna/detalles.html"), name='detalles'),

    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo postre o registro  
    path('comuna/crear', ComunaCrear.as_view(template_name = "mantenedor/Comuna/crear.html"), name='crear'),

    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un postre o registro de la Base de Datos 
    path('comuna/editar/<int:pk>', ComunaActualizar.as_view(template_name = "mantenedor/comuna/actualizar.html"), name='actualizar'), 

    # La ruta 'eliminar' que usaremos para eliminar un postre o registro de la Base de Datos 
    path('comuna/eliminar/<int:pk>', ComunaEliminar.as_view(), name='eliminar'),   

##***********************************

    path('index/', views.index, name='index'),
    path('', views.index, name='index'),
    path('marca', views.marca),
    path('modelo', views.modelo),
    path('producto', views.producto),
    path('productoLeer', views.ProductoLeer),

    path('busxx', views.bus),

    path('error/<int:question_id>', views.detailError),


    # ex: /polls/5/
    path('<int:preNro>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),    
]
