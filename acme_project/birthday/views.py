from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import BirthdayForm
from .models import Birthday
from .utils import calculate_birthday_countdown


class BirthdayCreateView(CreateView):
    model = Birthday
    form_class = BirthdayForm


class BirthdayDeleteView(DeleteView):
    model = Birthday


class BirthdayDetailView(DetailView):
    model = Birthday
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['birthday_countdown'] = calculate_birthday_countdown(
            self.object.birthday
        )
        return context


class BirthdayListView(ListView):
    model = Birthday
    ordering = 'id'
    paginate_by = 3


class BirthdayUpdateView(UpdateView):
    model = Birthday
    form_class = BirthdayForm
