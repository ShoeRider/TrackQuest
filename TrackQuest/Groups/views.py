from django.shortcuts import render

# Create your views here.

def CreateGroup(request):
    #if !groupname:
    if (request.method == 'GET'):
        form = GroupForm()
        fields = ['name','about']
        return render(request, 'group/Group_Create.html', {"From": form, "field": fields})
    if (request.method == 'POST'):
        form = GroupForm(request.POST)
        context = request.POST.dict()
        print(context['name'])
        alreadyExists = Group.objects.filter(name = context['name'])
        print(alreadyExists.count())
        if (alreadyExists.count()):
            return render(request, 'friend/FormFill_FriendRequest.html', {"from": " Group already exists !"})
        if form.is_valid():
            Grouper = Group.make_group(name=context['name'],about=context['about'],user= request.user)
            Forum.objects.create(topic_name=str(Grouper.name) + " Forum", description="The forum of the group " + str(Grouper.name), group = Grouper)
            return render(request, 'group/Group_CreatedRedirect.html', {"Message": "Group: "+ context['name']+" Created !", "group":context['name']})

            #return render(request, 'friend/FormFill_FriendRequest.html', {"from": "You just submitted an invalid Group Form !"})
    return render(request, '404.html',{"Message": "Experienced group doesnt exist!"})

def searchGroup_Form(request):
    return render(request, 'group/searchGroup_Form.html')

def searchGroup_Results(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        groups = Group.objects.filter(name__contains=q)
        return render(request, 'group/searchGroup_Results.html',
                      {'groups': groups, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')

class GroupDelete(DeleteView):
    model = Group
    context_object_name = "Group" #use this in the template
    success_url = reverse_lazy('MyGroups')
    template_name = 'group/Group_confirm_delete.html'
