from django.shortcuts import render
# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, permissions
from .models import DietPlan
from .serializers import DietPlanSerializer

class SSMember(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="Member").exists()

class DietPlanViewSet(viewsets.ModelViewSet):
    queryset = DietPlan.objects.all()
    serializer_class = DietPlanSerializer
    permission_classes = [permissions.IsAuthenticated, SSMember]

    def get_queryset(self):
        return DietPlan.objects.filter(user=self.request.user)
    


from .models import DietPlan
from .serializers import DietPlanSerializer
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.

def Tweet_list(request):
   tweets = DietPlan.objects.all().order_by('-created_at')
   return render(request, 'DietPlanApp/tweet_list.html',{'tweets': tweets})

@login_required()
def Tweet_create(request):
   if request.method == "POST":
     form = DietPlan(request.POST, request.FILES)
     if form.is_valid():
        Tweet = form.save(commit=False)
        Tweet.user = request.user
        Tweet.save()
        return redirect('Tweet_list')
   else:
      form = DietPlan()
   return render(request, 'DietPlanApp/tweetForm.html', {'form': form})

@login_required()
def tweet_edit(request, tweet_id ):
   tweet = get_object_or_404(DietPlan, pk=tweet_id, user =request.user)
   if request.method =='POST':
      form = DietPlan(request.POST, request.FILES, instance=tweet)
      if form.is_valid():
         tweet = form.save(commit=False)
         tweet.user = request.user
         tweet.save()
         return redirect('Tweet_list')
   else:
      form = DietPlan(instance=tweet)
   return render(request, 'DietPlanApp/tweetForm.html', {'form': form})
   
@login_required()
def tweet_delete(request, tweet_id):
  tweet=  get_object_or_404(DietPlan, pk=tweet_id, user=request.user)
  if request.method == 'POST':
     tweet.delete()
     return redirect('Tweet_list')
  return render(request,'DietPlanApp/confirm_delete.html',{'tweet': tweet})


