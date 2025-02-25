from django.shortcuts import render, redirect
from .models import Food, Consume, HealthGoal
from .forms import FoodForm, HealthGoalForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

def index(request):
    return render(request, "app/index.html")

@login_required
def add_food(request):
    if request.method == "POST":
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = FoodForm()
    return render(request, "app/add_food.html", {"form": form})

@login_required
def update_goals(request):
    goal, created = HealthGoal.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = HealthGoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = HealthGoalForm(instance=goal)
    return render(request, "app/update_goals.html", {"form": form})

@login_required
def chart_data(request):
    consumed = Consume.objects.filter(user=request.user)
    goal, _ = HealthGoal.objects.get_or_create(user=request.user)

    data = {
        "labels": [c.food_consumed.name for c in consumed],
        "carbs": [c.food_consumed.carbs for c in consumed],
        "proteins": [c.food_consumed.proteins for c in consumed],
        "fats": [c.food_consumed.fats for c in consumed],
        "calories": [c.food_consumed.calories for c in consumed],
        "goal_carbs": goal.carb_goal,
        "goal_proteins": goal.protein_goal,
        "goal_fats": goal.fat_goal,
        "goal_calories": goal.daily_calorie_goal,
    }
    return JsonResponse(data)