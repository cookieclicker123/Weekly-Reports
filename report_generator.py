import datetime

def get_input(prompt):
    return input(prompt)

def create_markdown_file(week_data, notes):
    date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    filename = f"Weekly_Report_{date_str}.md"
    
    content = f"""## Weekly Plan vs Progress Report - {date_str}

### Review of Last Week's Progress

| Task | Description | Why | Planned Status | Actual Status |
| --- | --- | --- | --- | --- |\n"""
    
    for task in week_data['last_week']:
        content += f"| {task['task']} | {task['description']} | {task['why']} | {task['planned']} | {task['actual']} |\n"
    
    content += "\n### Plan for This Week\n\n| Task | Description | Why | Planned Status |\n| --- | --- | --- | --- |\n"
    
    for task in week_data['this_week']:
        content += f"| {task['task']} | {task['description']} | {task['why']} | {task['planned']} |\n"
    
    content += "\n### Notes and Comments\n\n"
    
    for note in notes:
        content += f"- {note}\n"
    
    with open(filename, 'w') as file:
        file.write(content)
    
    print(f"Weekly report {filename} created successfully.")

def main():
    # Collect input from user
    last_week_tasks = []
    this_week_tasks = []
    notes = []

    num_last_week = int(get_input("How many tasks to review from last week? "))
    for _ in range(num_last_week):
        task = {
            'task': get_input("Task: "),
            'description': get_input("Description: "),
            'why': get_input("Why: "),
            'planned': get_input("Planned Status: "),
            'actual': get_input("Actual Status: ")
        }
        last_week_tasks.append(task)
    
    num_this_week = int(get_input("How many tasks planned for this week? "))
    for _ in range(num_this_week):
        task = {
            'task': get_input("Task: "),
            'description': get_input("Description: "),
            'why': get_input("Why: "),
            'planned': get_input("Planned Status: ")
        }
        this_week_tasks.append(task)

    num_notes = int(get_input("How many notes/comments? "))
    for _ in range(num_notes):
        note = get_input("Note/Comment: ")
        notes.append(note)
    
    # Create the markdown file
    week_data = {
        'last_week': last_week_tasks,
        'this_week': this_week_tasks
    }
    create_markdown_file(week_data, notes)

if __name__ == "__main__":
    main()
