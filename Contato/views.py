from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

def Contato(request):
    assunto = 'Consultas da DentiCare'
    
    if request.method == 'POST':
        # Recopilar dados do formulario
        context = {
            'nome': request.POST['txtnome'],
            'sobrenome': request.POST['txtsobrenome'],
            'celular': request.POST['txtcelular'],
            'email': request.POST['txtemail'],
            'mensagem': request.POST['txtmensagem']
        }
        
        # Renderizar o template HTML
        html_content = render_to_string('Contato/email_template.html', context)
        text_content = strip_tags(html_content)  # Versao texto plano do HTML
        
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['mpaucarporras@gmail.com']
        
        # Criar o email com conteudo alternativo (HTML e texto plano)
        email = EmailMultiAlternatives(
            subject=assunto,
            body=text_content,
            from_email=email_from,
            to=recipient_list
        )
        
        email.attach_alternative(html_content, "text/html")
        email.send()
        
        return render(request, 'Contato/obrigado.html')
    
    return render(request, "Contato/contato.html")