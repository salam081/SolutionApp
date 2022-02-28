from django.shortcuts import render,  get_object_or_404 ,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView, DetailView
from .models import *
from users.models import UnitHead


# Create your views here.
#=========collect_report start here=================

def collect_report(request):
    collect_report=None
    report_types = ReportType.objects.all()
    profile = UnitHead.objects.all()
    get_report_type = request.GET.get('report_type')
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')

    if request.method == 'GET':
        if not get_report_type:
            messages.info(request, "Please select Report type and specify date range")
        else:
            collect_report = SubUnitReport.objects.filter(
                report_type_id=get_report_type,
                date_from__gte=date_from, date_to__lte=date_to
                )

    context = {'collect_report': collect_report, "report_types":report_types, 'profile':profile}
    return render(request, 'cittureport/reportsummary.html', context)
    #========= collect_report ends here=================

def create_report(request):
    report = ReportType.objects.all()
    user = request.user

    if request.method == 'POST':
        report_type_id = request.POST.get('report_type','')
        report_type = ReportType.objects.get(id=report_type_id)
        introductions = request.POST.get('introductions','')
        achievement = request.POST.get('achievement','')
        challenge = request.POST.get('challenge','')
        conclusion = request.POST.get('conclusion','')
        date_from = request.POST.get('date_from','')
        date_to = request.POST.get('date_to','')
        data = SubUnitReport(report_type=report_type, introductions=introductions, achievement=achievement, challenge=challenge,
                                         date_from=date_from,date_to=date_to, conclusion=conclusion,created_by=user)
        data.save() 
        return redirect('reportlistview')
    context = {'report':report}      
    return render(request, 'cittureport/reportform.html',context) 

#============ update report report views ==========
def update_report(request,pk):
    report = SubUnitReport.objects.get(id=pk)
    report_type = ReportType.objects.all()

    if request.method == 'POST':
        UpdatedSubUnitReport.objects.create(subUnitReport=report,report_type=report.report_type,
                                                introductions=report.introductions,
                                                 achievement=report.achievement,
                                                 challenge=report.challenge,
                                                  conclusion=report.conclusion
                                            )
        report_type_id = request.POST.get('report_type','')
        report_type_instance = ReportType.objects.get(id=report_type_id)
        introductions = request.POST.get('introductions','')
        achievement = request.POST.get('achievement','')
        challenge = request.POST.get('challenge','')
        conclusion = request.POST.get('conclusion','')

        report.introductions = introductions
        report.report_type = report_type_instance
        report.achievement= achievement
        report.challenge = challenge
        report.conclusion = conclusion
        report.save()
        return redirect('reportlistview')
    context = {'report':report, 'report_type':report_type}
    return render(request, 'cittureport/reportformupdate.html',context )

#============ update report report views end ==========

#========== get report history ================
def track_report_history(request, pk):
    sub_unit_report = SubUnitReport.objects.get(id=pk)
    history = UpdatedSubUnitReport.objects.filter(subUnitReport=sub_unit_report).order_by("-id")
    context={"history":history, "current":sub_unit_report }
    return render(request, "cittureport/report_history.html", context)
#========== get report history end ================

#============== SubUnitReportListView start ============
def SubUnitReportListView(request):
    profile = UnitHead.objects.all()
    subunit = SubUnitReport.objects.all()
    context = {'subunit':subunit,'profile':profile}
    return render(request,'cittureport/main.html',context)
#============== SubUnitReportListView end ============

#===========DetailView start ==================
class subunit_reportDetailView(DetailView):
    model = SubUnitReport
    template_name = 'cittureport/detail.html' 
#=========== DetailView end ==================

#=========== delete view for details start =============
def delete_report(request, pk):
    obj = get_object_or_404(SubUnitReport, id = pk)
 
    if request.method =="POST":
        obj.delete()
        return redirect("reportlistview")
    context ={'obj':obj}
    return render(request, "cittureport/delete.html", context)      
#=========== delete view end ================== 
#    
 # ============pdf views start here==============   
def cittureport_render_pdf_view(request,*args, **kwargs):
    pk = kwargs.get('pk')
    report = get_object_or_404(SubUnitReport,pk=pk)

    template_path = 'cittureport/pdf2.html'
    context = {'report':report}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
#======== pdf view end ==============
#     
#======== render pdf view start ==============
def render_pdf_view(request):
    template_path = 'cittureport/pdf1.html'
    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
#========= ends here =================