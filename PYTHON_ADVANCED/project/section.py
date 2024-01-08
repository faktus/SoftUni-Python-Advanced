from project.task import Task

class Section:
    

    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        
        self.tasks.append(new_task)
        return f"Task {new_task} is added to the section"

    def complete_task(self, task_name: str):

        if task_name not in self.tasks:
            return f"Could not find task with the name {task_name}"
        Task.completed = True
        return f"Completed task {task_name}"

    def clean_section(self):

        count = 0
        for task in self.tasks:
            if Task(*task).completed:
                count += 1
                self.tasks.remove(task)
        return f'Cleared {count} tasks.'

    def view_section(self):
        return f'Section {self.name}, {Task.details()}'
    

task = Task("Make bed", "27/05/2020")

print(task.change_name("Go to University"))

print(task.change_due_date("28.05.2020"))

task.add_comment("Don't forget laptop")

print(task.edit_comment(0, "Don't forgetlaptop and notebook"))

print(task.details())