import random
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import (
    PhysicalBook,
    ElectronicBook,
    AudioBook,
    Author,
    Translator,
    Teller,
    Publisher,
    Category,
)

# Create your views here.
class AllBook(TemplateView):

    def get(self, request, **kwargs):
        all_book = []

        physicalbook = PhysicalBook.objects.all()
        electronicbook = ElectronicBook.objects.all()
        audiobook = AudioBook.objects.all()

        for book in physicalbook:
            all_book.append({
                'picture': book.picture,
                'title': book.title,
                'show_author': book.show_author,
                'show_translator': book.show_translator,
                'show_category': book.show_category,
                'show_publisher': book.show_publisher,
                'show_user_rate': book.show_user_rate,
                'status': book.get_read_status_display(),
                'platform': book.get_platform_display(),
                'type': 'فیزیکی',
                'update_url': reverse('book:physicalbook_update', kwargs={'pk':book.pk}),
                'delete_url': reverse('book:physicalbook_delete', kwargs={'pk':book.pk}),
            })
        
        for book in electronicbook:
            all_book.append({
                'picture': book.picture,
                'title': book.title,
                'show_author': book.show_author,
                'show_translator': book.show_translator,
                'show_category': book.show_category,
                'show_publisher': book.show_publisher,
                'show_user_rate': book.show_user_rate,
                'status': book.get_read_status_display(),
                'platform': book.get_platform_display(),
                'type': 'الکترونیکی',
                'update_url': reverse('book:electronicbook_update', kwargs={'pk':book.pk}),
                'delete_url': reverse('book:electronicbook_delete', kwargs={'pk':book.pk}),
            })

        for book in audiobook:
            all_book.append({
                'picture': book.picture,
                'title': book.title,
                'show_author': book.show_author,
                'show_translator': book.show_translator,
                'show_category': book.show_category,
                'show_publisher': book.show_publisher,
                'show_user_rate': book.show_user_rate,
                'status': book.get_listen_status_display(),
                'platform': book.get_platform_display(),
                'type': 'صوتی',
                'update_url': reverse('book:audiobook_update', kwargs={'pk':book.pk}),
                'delete_url': reverse('book:audiobook_delete', kwargs={'pk':book.pk}),
            })

        random.shuffle(all_book)
        context = {
            'all_book': all_book
        }

        return render(request, 'book/index.html', context)


class PhysicalBookList(ListView):
    model = PhysicalBook
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ElectronicBookList(ListView):
    model = ElectronicBook

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AudioBookList(ListView):
    model = AudioBook

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AuthorList(ListView):
    model = Author
    template_name = 'book/person_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_title'] = "نویسندگان"
        context['update_url'] = 'book:author_update'
        context['delete_url'] = 'book:author_delete'
        return context


class TranslatorList(ListView):
    model = Translator
    template_name = 'book/person_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_title'] = "مترجمین"
        context['update_url'] = 'book:translator_update'
        context['delete_url'] = 'book:translator_delete'
        return context


class TellerList(ListView):
    model = Teller
    template_name = 'book/person_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_title'] = "گویندگان"
        context['update_url'] = 'book:teller_update'
        context['delete_url'] = 'book:teller_delete'
        return context


class PublisherList(ListView):
    model = Publisher

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CategoryList(ListView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PhysicalBookCreate(CreateView):
    model = PhysicalBook
    fields = ['picture', 'title', 'author', 'translator', 'language_book', 'user_rate', 'category', 'price', 'price_unit', 'user_description', 'book_url', 'publisher', 'pages_readed', 'pages', 'read_status', 'platform']
    template_name = 'book/physicalbook_create_update.html'


class PhysicalBookUpdate(UpdateView):
    model = PhysicalBook
    fields = ['picture', 'title', 'author', 'translator', 'language_book', 'user_rate', 'category', 'price', 'price_unit', 'user_description', 'book_url', 'publisher', 'pages_readed', 'pages', 'read_status', 'platform']
    template_name = 'book/physicalbook_create_update.html'


class PhysicalBookDelete(DeleteView):
    model = PhysicalBook
    success_url = reverse_lazy('book:physicalbook')
    template_name = 'book/book_confirm_delete.html'

class ElectronicBookCreate(CreateView):
    model = ElectronicBook
    fields = ['picture', 'title', 'author', 'translator', 'language_book', 'user_rate', 'category', 'price', 'price_unit', 'user_description', 'book_url', 'publisher', 'pages_readed', 'pages', 'read_status', 'platform', 'book_file']
    template_name = 'book/electronicbook_create_update.html'


class ElectronicBookUpdate(UpdateView):
    model = ElectronicBook
    fields = ['picture', 'title', 'author', 'translator', 'language_book', 'user_rate', 'category', 'price', 'price_unit', 'user_description', 'book_url', 'publisher', 'pages_readed', 'pages', 'read_status', 'platform', 'book_file']
    template_name = 'book/electronicbook_create_update.html'


class ElectronicBookDelete(DeleteView):
    model = ElectronicBook
    success_url = reverse_lazy('book:electronicbook')
    template_name = 'book/book_confirm_delete.html'


class AudioBookCreate(CreateView):
    model = AudioBook
    fields = ['picture', 'title', 'author', 'translator', 'language_book', 'user_rate', 'category', 'price', 'price_unit', 'user_description', 'book_url', 'publisher',  'teller', 'episode', 'season', 'listen_status', 'platform', 'book_file']
    template_name = 'book/audiobook_create_update.html'


class AudioBookUpdate(UpdateView):
    model = AudioBook
    fields = ['picture', 'title', 'author', 'translator', 'language_book', 'user_rate', 'category', 'price', 'price_unit', 'user_description', 'book_url', 'publisher',  'teller', 'episode', 'season', 'listen_status', 'platform', 'book_file']
    template_name = 'book/audiobook_create_update.html'


class AudioBookDelete(DeleteView):
    model = AudioBook
    success_url = reverse_lazy('book:audiobook')
    template_name = 'book/book_confirm_delete.html'


class AuthorCreate(CreateView):
    model = Author
    fields = ['avatar', 'first_name', 'middle_name', 'last_name']
    template_name = 'book/person_create_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = Author._meta.verbose_name
        return context


class TranslatorCreate(CreateView):
    model = Translator
    fields = ['avatar', 'first_name', 'middle_name', 'last_name']
    template_name = 'book/person_create_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = Translator._meta.verbose_name
        return context


class TellerCreate(CreateView):
    model = Translator
    fields = ['avatar', 'first_name', 'middle_name', 'last_name']
    template_name = 'book/person_create_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = Teller._meta.verbose_name
        return context


class AuthorUpdate(UpdateView):
    model = Author
    fields = ['avatar', 'first_name', 'middle_name', 'last_name']
    template_name = 'book/person_create_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = Author._meta.verbose_name
        return context


class TranslatorUpdate(UpdateView):
    model = Translator
    fields = ['avatar', 'first_name', 'middle_name', 'last_name']
    template_name = 'book/person_create_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = Translator._meta.verbose_name
        return context


class TellerUpdate(UpdateView):
    model = Translator
    fields = ['avatar', 'first_name', 'middle_name', 'last_name']
    template_name = 'book/person_create_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = Teller._meta.verbose_name
        return context