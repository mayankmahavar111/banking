from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout,password_reset,password_reset_done,password_reset_confirm,password_reset_complete
urlpatterns = [
	url(r'^data/(?P<acc>[a-zA-Z]{1,16})/$',views.data,name='data'),
	url(r'register/$',views.register,name='register'),
	url(r'^feedback/$',views.feedback,name='feeedback'),
	url(r'logout/$',logout,{'template_name':'chkbal/logout.html'}),
	url(r'login/$',login,{'template_name':'chkbal/login.html'}),
	url(r'profile/$',views.profile,name='profile'),
	url(r'^$',views.index, name='index'),
	url(r'^profile/update/$',views.update,name='update'),
	url(r'^profile/enquiry/',views.enquiry,name='enquiry'),
	url(r'^profile/transaction/',views.transaction,name='transaction'),
	url(r'^profile/mini-statement/',views.mini,name='mini'),
	url(r'^profile/account-details/$',views.updateAccount,name='updateAccount'),
	url(r'^change-password/',views.password,name='password'),
	url(r'^reset-password/$',password_reset,name='reset-password'),
	url(r'^reset-password/done/$',password_reset_done,name='password_reset_done'),
	url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, name='password_reset_confirm'),
	url(r'^reset-password/complete/$',password_reset_complete,name="password_reset_complete"),
	url(r'^help/$',views.help,name='help'),
	url(r'^about/$',views.Aboutus,name='about'),
	url(r'^deposite/$',views.deposite,name='deposite'),
	url(r'^fund/(?P<y>[a-zA-Z]{1,10})/$',views.fund,name='fund'),
	url(r'^checkAccount/$',views.checkAccount,name='checkAccount'),
	url(r'^mpin/(?P<y>[a-zA-Z]{1,10})/(?P<bal>[0-9]{1,10})/$',views.mpin,name="mpin")
]