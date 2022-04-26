from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .forms import YourDataForm

class IndexView(generic.FormView):
    template_name = 'bmi_app/index.html'
    form_class = YourDataForm
    success_url = reverse_lazy('bmi_app:index')

    def form_valid(self, form):
        weight = form.cleaned_data['weight']
        height = form.cleaned_data['height']

        if height < 100:
            height = height / 10
        else:
            height = height / 100

        bmi = weight / (height ** 2)

        message = ''

        if bmi < 18.5:
            message = 'やせ'
        elif bmi >= 18.5 or bmi < 25.5:
            message = "標準"
        elif bmi >= 25:
            message = "肥満"
        elif bmi >= 30:
            message = "高度肥満"
        else:
            message = "エラー"

        context = self.get_context_data(your_bmi=bmi, message=message)

        return self.render_to_response(context)

