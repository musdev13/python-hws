from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContactForm
from .models import Contact


def contact_list(request):
    query = request.GET.get("q", "").strip()
    contacts = Contact.objects.all()
    if query:
        contacts = contacts.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query)
        )
    return render(request, "contacts/list.html", {
        "contacts": contacts,
        "query": query,
    })


def contact_create(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contact_list")
    else:
        form = ContactForm()
    return render(request, "contacts/form.html", {
        "form": form,
        "title": "Новий контакт",
        "submit_label": "Додати",
    })


def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect("contact_list")
    else:
        form = ContactForm(instance=contact)
    return render(request, "contacts/form.html", {
        "form": form,
        "title": f"Редагувати: {contact}",
        "submit_label": "Зберегти",
        "contact": contact,
    })


def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        contact.delete()
        return redirect("contact_list")
    return render(request, "contacts/delete.html", {"contact": contact})
