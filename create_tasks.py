# create_tasks.py
 
"""def main():
    tasks = TaskList.objects.all()
    print(f"There are {tasks.count()} tasks in the database")
"""

def main():
    fake: Faker = Faker()
 
    for i in range(30):
        task = TaskList.objects.create(
            name=fake.paragraph(nb_sentences=1),
            status=random.choice(TaskList.StatusChoice.choices)[0],
        )
        print(f"Created todo. Name: {task.name}  Status: {task.status}")
 
    task_count = TaskList.objects.count()
 
    print(f"There are {task_count} todos in the database")
 
if __name__ == "__main__":
    import os
 
    from django.core.wsgi import get_wsgi_application
 
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    application = get_wsgi_application()

    import random
    
    from faker import Faker
    from todolist.models import TaskList
 
    main()