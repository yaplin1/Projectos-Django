from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from carro.carro import Carro
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from .models import Producto
from pedidos.models import LineaPedido, Pedido


# Create your views here.

@login_required(login_url="/autenticacion/logear")
def procesar_pedido(request):
    pedido=Pedido.objects.create(user=request.user)
    carro=Carro(request)
    lineas_pedido=list()
    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedido(
            #producto_id=Producto.objects.get(pk=key), otra manera de interrelacionar
            producto_id=key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedido
        ))

    LineaPedido.objects.bulk_create(lineas_pedido)

    enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombreusuario=request.user.username,
        emailusuario=request.user.email
    )
    aviso="El pedido se ha creado correctamente<br>se envio a su correo, !Gracia!"
    messages.success(request, aviso)

    return redirect("../tienda")


def enviar_mail(**kwargs):

    asunto="Gracias por el pedido"
    mensaje=render_to_string("emails/pedido.html", {
        "pedido": kwargs.get("pedido"),
        "lineas_pedido": kwargs.get("lineas_pedido"),
        "nombreusuario": kwargs.get("nombreusuario")

    })

    mensaje_texto=strip_tags(mensaje)
    # from_email="cortezhenryp@gmail.com"
    to=kwargs.get("emailusuario")
    to="ryssoftperu@gmail.com"

    nombre_remitente = "Surtido Ya"
    from_email_con_alias = f'"{nombre_remitente}" <cortezhenryp@gmail.com>'

    send_mail(asunto,mensaje_texto,from_email_con_alias,[to],html_message=mensaje)


