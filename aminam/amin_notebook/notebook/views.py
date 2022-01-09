from django.shortcuts import render,redirect
from notebook.models import Notebook
from notebook.forms import NotebookForm
from django.contrib import messages

def index(request):
    notebook = Notebook.objects.all()
    return render(request, 'index.html', {'notebook': notebook})

def new_note(request):
    form = NotebookForm()
    if request.method == 'POST':
        form = NotebookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'update.html', {'form': form})

def  note_detail(request, pk):
    note = Notebook.objects.get(id=pk)
    form = NotebookForm(instance=Notebook)
    if request.method == 'POST':
        form = NotebookForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(request, "update.html", {"note": note, "form": form})


def delete_note(request, pk):
    note = Notebook.objects.get(id=pk)
    form = NotebookForm(instance=note)
    if request.method == 'POST':
        note.delete()
        messages.info(request, "The note has been deleted")
    return render(request, "delete.html", {"note": note, "form": form})

def search_page(request):
    if request.method == 'POST':
        search_text = request.POST['search']
        notes = Notebook.objects.filter(heading__icontains = search_text) |Notebook.objects.filter(text__icontains = search_text)
        if notes is None:
            messages.info(request, "Note not found")
        return render(request, "search.html", {"notes": notes})
       
    
  

