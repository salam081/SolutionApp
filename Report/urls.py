from django.urls import path
from .views import *

urlpatterns = [
    path('collectreport/',collect_report, name='collectreport'),
    path('reportform/',create_report, name='report-form'),
    path('updatereport/<str:pk>/',update_report, name='updatereport'),
    path('deletereport/<str:pk>/',delete_report, name='deletereport'),

    # get report history
    path('report/history/<str:pk>/',track_report_history, name='report_history'),

    path('detailview/<pk>/',subunit_reportDetailView.as_view() ,name='detailview'),
    path('reportlistvie/',SubUnitReportListView ,name='reportlistview'),
    path('report/',render_pdf_view, name='report'),
    path('pdf/<pk>/',cittureport_render_pdf_view, name='reportpdf'),
]