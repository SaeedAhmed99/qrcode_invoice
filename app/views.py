from email.mime import base
from django.shortcuts import render
from django.http import HttpResponse
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.template.loader import get_template
from .models import image
from io import BytesIO
import qrcode 
from .models import image, Website
import base64


def index(request):
    im = Website.objects.first()
    context = {
        'image': im
    }
    return render(request, 'index01.html', context)


# def pdfreport(request):
#     im = image.objects.get(pk=1)

#     template_path = 'pdfreport.html'

#     context = {
#         'image': im
#     }

#     response = HttpResponse(content_type='application/pdf')

#     response['Content-Disposition'] = 'filename="pdf_report.pdf"'

#     template = get_template(template_path)
#     # print(im.photo)
#     html = template.render(context)

#     # result = BytesIO()

#     # create a pdf
#     pisa_status = pisa.CreatePDF(
#     html, dest=response)
#     # pisa_status = pisa.CreatePDF(html.encode("UTF-8"), result)
#     # if error then show some funy view
#     if pisa_status.err:
#         return HttpResponse('We had some errors <pre>' + html + '</pre>')
#     return response





def pdfreport(request):
    im = Website.objects.first()

    template_path = 'pdfreport.html'

    context = {
        'image': im
    }
    template = get_template(template_path)
    html  = template.render(context)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None



# 2- Generate QR code (TLV):
# - Seller’s name.
# - VAT registration number of the seller.
# - Time stamp of the invoice (date and time).
# - Invoice total (with VAT).
# - VAT total.

def qr(request):
    nameSeller = 'Firoz Ashraf'
    vatRegisterNumber = 1234567891
    dateTime = '2021-11-17 08:30:00'
    totalInvoice = 115.00
    vat = 15.00

    result01 = f'##{nameSeller}##{vatRegisterNumber}##{dateTime}##{totalInvoice:.2f}##{vat:.2f}'
    print(result01)
    b64 = str(base64.b64encode(result01.encode('ascii')))
    print(str(b64))
    # print(type(b64))
    qr = Website.objects.create(value = b64)
    context = {

    }
    return HttpResponse('yes')
