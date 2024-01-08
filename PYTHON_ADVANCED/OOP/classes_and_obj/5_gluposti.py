class Section:
    tasks = []

    def __int__(self, name: str):
        self.name = name


    def add_task(self, new_task: str):
        if new_task in Section.tasks:
            return f"Task is already in the section {self.name}"
        Section.tasks.append(new_task)
        return f"Task {new_task} is added to the section"

    def complete_task(self, task_name: str):

        if task_name not in Section.tasks:
            return f"Could not find task with the name {task_name}"
        Task.completed = True
        return f"Completed task {task_name}"

    def clean_section(self):

        result = f"Cleared {len(Section.tasks)} tasks."
        for task in Section.tasks:
            Section.tasks.remove(task)
        return result

    def view_section(self):
        return f'Section {self.name}, {Task.details()}'




section = Section("neshto")
