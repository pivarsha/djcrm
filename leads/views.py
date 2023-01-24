from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse

from leads.models import Lead,User,Agent
from .forms import LeadModelForm,LeadForm,CustomUserCreationForm
from django.views.generic import TemplateView,CreateView,ListView,DetailView
from django.views import generic
from django.core.mail import send_mail


#CRUD

#class based View
class SignUpView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
 
    def get_success_url(self):
        return reverse("login")



class LandingPageView(generic.TemplateView):
    template_name = "landing.html"



class LeadCreateView(generic.CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:h")

    def form_valid(self, form):

        send_mail(
        subject = "A lead Has Been Created.",
        message = "Go To The Site To See, The New Lead.",
        from_email = "test@test.com",
        recipient_list = ["test2@gmail.com"]
        )  

        return super(LeadCreateView,self).form_valid(form)




class LeadListView(generic.ListView):
    template_name = "leads/index.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"



class LeadDetailView(generic.DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"

 

class LeadUpdateView(generic.UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:h")



class LeadDeleteView(generic.DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()
     
    def get_success_url(self):
        return reverse("leads:h")


# Create your views here.

def home_page(request): #Retrieve
    leads = Lead.objects.all()
    context = {
        "leads":leads,
    }

    return render(request,"leads/index.html",context)

def lead_create(request): #Create
    form = LeadModelForm()
    if request.method == "POST":
        print("Receiving a post request")
        form = LeadModelForm(request.POST)
        if form.is_valid():
            print("form is valid")
            print(form.cleaned_data)
            form.save()
            print("form data is being saved")
            return redirect("/home")
        
    context = {
        "form":form
    }
    return render(request,"leads/lead_create.html",context)

def landing_page(request):
    return render(request,"landing.html")




def lead_detail(request,pk): #detail
    lead = Lead.objects.get(id = pk)
    print(lead)
    context = {
        "lead":lead
    }
    return render(request,"leads/lead_detail.html",context)



def lead_update(request,pk): # update
    lead = Lead.objects.get(id = pk)
    form = LeadModelForm(instance = lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST,instance=lead)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        "form":form,
        "lead":lead
    }
    return render(request,"leads/lead_update.html",context)


def lead_delete(request,pk): #delete
    lead = Lead.objects.get(id = pk)
    lead.delete()
    return redirect('/home')
