from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Plataforma, Ip, Sw, Hw, Departamento, Modulo, Responsable, ResponsableSistema, Sistema, Submodulo
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db import connection
import pandas as pd
from environment_app.export_csv import DataFrameCreator
import xlsxwriter
""" from .export_csv import export_to_excel """
#For HwDetailView
""" from django.views.generic import DetailView """

# Create your views here.
import logging
logger = logging.getLogger(__name__)

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def exit(request):
  logout(request)
  return redirect('main')

@login_required
def plataformas(request):
    plataformas = Plataforma.objects.select_related('id_sistema').all()
    context = {
        'plataformas': plataformas,
    }
    return render(request, 'all_ambientes.html', context)


@login_required
def detalles(request, id_plataforma):
    myplatform = Plataforma.objects.get(id_plataforma=id_plataforma)

    sw = myplatform.sw_set.all()
    hw = myplatform.hw_set.all()

    # Obtener la información de la dirección IP
    ips = []
    for s in sw:
        if s.ip_set.exists():
            ips.extend(s.ip_set.all())

    for x in sw:
        sw_ips = x.ip_set.all()
        ip_list = []
        for ip in sw_ips:
            ip_list.append(ip.ip)
        x.ip_sw = ", ".join(ip_list)

    template = loader.get_template('detalles.html')
    context = {
        'myplatform': myplatform,
        'sw': sw,
        'hw': hw,
    }
    return HttpResponse(template.render(context, request))


def download_excel(request):
    departamentos = DataFrameCreator.create_dataframe(Departamento)
    hws = DataFrameCreator.create_dataframe(Hw)
    ips = DataFrameCreator.create_dataframe(Ip)
    modulos = DataFrameCreator.create_dataframe(Modulo)
    plataformas = DataFrameCreator.create_dataframe(Plataforma)
    responsables = DataFrameCreator.create_dataframe(Responsable)
    responsables_sistema = DataFrameCreator.create_dataframe(ResponsableSistema)
    sistemas = DataFrameCreator.create_dataframe(Sistema)
    submodulos = DataFrameCreator.create_dataframe(Submodulo)
    sws = DataFrameCreator.create_dataframe(Sw)

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="data.xlsx"'
    writer = pd.ExcelWriter(response, engine='xlsxwriter')

    departamentos.to_excel(writer, sheet_name='Departamentos', index=False)
    hws.to_excel(writer, sheet_name='Hw', index=False)
    ips.to_excel(writer, sheet_name='Ip', index=False)
    modulos.to_excel(writer, sheet_name='Modulos', index=False)
    plataformas.to_excel(writer, sheet_name='Plataformas', index=False)
    responsables.to_excel(writer, sheet_name='Responsables', index=False)
    responsables_sistema.to_excel(writer, sheet_name='ResponsablesSistema', index=False)
    sistemas.to_excel(writer, sheet_name='Sistemas', index=False)
    submodulos.to_excel(writer, sheet_name='Submodulos', index=False)
    sws.to_excel(writer, sheet_name='Sws', index=False)

    writer.save()
    return response








