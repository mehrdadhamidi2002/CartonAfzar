import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm  # Import your ContactForm
from .models import Contact
from django.views.decorators.http import require_GET
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from django.http import HttpResponse
from weasyprint import HTML
from .models import Contact
from django.template.loader import render_to_string
import tempfile
from django.db.models import Count
from xhtml2pdf import pisa
from io import StringIO, BytesIO
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


def home(request):
    if request.method == 'POST':
        print(request.user)
        user = request.user
        context = {'user': user}
    if request.method == 'GET':
        context = {'user': None}

    return render(request, 'tss/index.html', context)

def subscribe(request):
    #return HttpResponse('<div style="color:blue">Subscribed</div>')
    return render(request,'partial.html', {})

def create_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the data to the database
           # return redirect('/')  # Redirect to a success page
    else:
        form = ContactForm()

    #return render(request, 'contact_form.html', {'form': form})
    return HttpResponse('ok')

def sitemessages_grid_view(request):
    print(request)
    print(request.POST)
    print(request.GET)
    site_messages = Contact.objects.all()
    return render(request, 'sitemessages.html', {'sitemessages': site_messages})

def filter_messages(request):
    print('Filtering messages')
    print(request)
    print(request.POST)
    print(request.GET)
    search_query = request.GET.get('search', 'nooooo')
    
    print(search_query)
    if search_query:
        sitemessages = Contact.objects.filter(name__icontains=search_query)
    else:
        sitemessages = Contact.objects.all()
    return render(request, 'sitemessagespartial.html', {'sitemessages': sitemessages})


def fetch_resources(uri, rel):
    path = os.path.join(settings.STATIC_ROOT,
                        uri.replace(settings.STATIC_URL, ""))
    return path


def print_invoice(request):

    pdfmetrics.registerFont(TTFont('MarkaziText', 'C:\\Users\\mehrdad\\CartonAfzar\\tss\\static\\fonts\\MarkaziText-Bold.ttf'))

    template_path = 'tss/sitemessagesRep.html'
    sitemessages = Contact.objects.all()
    msgcounts = sitemessages.aggregate(msg_count=Count('id'))
    context = {'sitemessages': sitemessages, 'total': msgcounts}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; attachment; filename="invoice'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(BytesIO(html.encode("UTF-8")), dest=response, link_callback=fetch_resources)

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

    # response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'inline; attachment; filename="invoice.pdf"'
    # response['Content-Transfer-Encoding'] = 'binary'

    # sitemessages = Contact.objects.all()
    # msgcounts = sitemessages.aggregate(msg_count=Count('id'))
    # html_string = render_to_string('sitemessagesRep.html', {'sitemessages':sitemessages, 'total': msgcounts})    
    # html = HTML(string=html_string)
    # result = html.write_pdf()

    # with tempfile.NamedTemporaryFile(delete=False) as f:
    #     f.write(result)
    #     f.flush()
    #     response.write(open(f.name, 'rb').read())
    #     f.close()
    #     return response
    