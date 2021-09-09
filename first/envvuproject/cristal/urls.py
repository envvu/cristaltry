from . import views
from django.urls import path

app_name = 'cristal'
urlpatterns = [
    path('', views.index, name='index'),
    path('introduction/',views.introduction,name='introduction'),
    path('management/',views.management,name='management'),
    path('directors-message/', views.directormessage, name='directormessage'),
    path('corecompetence/', views.corecompetence, name='corecompetence'),
    path('our-team/',views.ourteam,name='ourteam'),
    path('classIX/',views.classIX,name='classIX'),
    path('classX/',views.classX,name='classX'),
    path('classXI/', views.classXI, name='classXI'),
    path('classXII/', views.classXII, name='classXII'),
    path('classXII-pass/', views.classXIIpass, name='classXIIpass'),
    path('ibs-bank-coaching/', views.ibsbankcoaching, name='ibsbankcoaching'),
    path('result-19-20/', views.result19_20, name='result19_20'),
    path('result-18-19/', views.result18_19, name='result18_19'),
    path('result-17-18/', views.result17_18, name='result17_18'),
    path('result-16-17/', views.result16_17, name='result16_17'),
    path('result-15-16/', views.result15_16, name='result15_16'),
    path('result-14-15/', views.result14_15, name='result14_15'),
    path('result-13-14/', views.result13_14, name='result13_14'),
    path('result-12-13/', views.result12_13, name='result12_13'),
    path('result-11-12/', views.result11_12, name='result11_12'),
    path('contactus/', views.contactus, name='contactus'),



    path('regnform/', views.regnform, name='regnform'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('online-regnform-tutions/', views.online_regnform_tutions, name='online_regnform_tutions'),
    path('terms-and-conditions/',views.terms_and_conditions,name='terms_and_conditions'),
    path('refund-policy/',views.refund_policy,name='refund_policy'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
]