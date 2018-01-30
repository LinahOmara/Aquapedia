# howdy/urls.py
from django.conf.urls import url
from howdy import views

urlpatterns = [
	#customer APIs
    url(r'^bill/$', views.Latest_bill.as_view()),
    url(r'^history/$', views.History.as_view()),
    url(r'^expectedbill/$', views.Expected_bill.as_view()),
    url(r'^getdate/$', views.Bill_date.as_view()),
    url(r'^ActualVsExpected/$', views.ActualVsExpected.as_view()),
    url(r'^Actualtillnow/$', views.Actualtillnow.as_view()),
    url(r'^tier/$', views.Tier.as_view()),
    url(r'^tierupdates/$', views.TierUpdates.as_view()),
    url(r'^msg/$', views.Msg.as_view()),
    url(r'^leakage/$', views.Leakage.as_view()),
    url(r'^lastUpdate/$', views.LastUpdate.as_view()),
    url(r'^comparison/$', views.Comparison.as_view()),
    #company APIs
    url(r'^users_count/$', views.UsersCount.as_view()),
    url(r'^alerts/$', views.Alterts.as_view()),
    url(r'^geographic/$', views.Geographic.as_view()),
    url(r'^predict/$', views.Predict.as_view()),
    url(r'^analysis/$', views.Analysis.as_view()),
]
