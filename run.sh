python manage.py makemigrations store
python manage.py migrate
python manage.py shell

from django.contrib.auth.models import User
from store.models import FoodProduct, Order, OrderItem

p1 = FoodProduct.objects.create(name="Apple", price=5.99, description="Fresh apples")
p2 = FoodProduct.objects.create(name="Banana", price=3.50, description="Ripe bananas")
p3 = FoodProduct.objects.create(name="Orange", price=4.00, description="Citrus fruits")
p4 = FoodProduct.objects.create(name="Bread", price=2.50, description="Whole grain bread")
p5 = FoodProduct.objects.create(name="Milk", price=1.80, description="Fresh dairy milk")
p6 = FoodProduct.objects.create(name="Cheese", price=7.49, description="Cheddar cheese")
p7 = FoodProduct.objects.create(name="Eggs", price=2.99, description="Farm eggs (dozen)")
p8 = FoodProduct.objects.create(name="Coffee", price=9.99, description="Ground coffee beans")
p9 = FoodProduct.objects.create(name="Chocolate", price=6.75, description="Dark chocolate bar")
p10= FoodProduct.objects.create(name="Yogurt", price=1.50, description="Natural yogurt")

python manage.py collectstatic