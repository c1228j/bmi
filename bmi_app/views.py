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

        context = self.get_context_data(your_bmi=bmi)

        return self.render_to_response(context)

