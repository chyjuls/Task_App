from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []
tasks_id_counter = 1

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/tasks')
def tasks_page():
    return render_template('tasks.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    global tasks_id_counter
    task_description = request.form.get('task')
    if task_description:
        tasks.append({'id': tasks_id_counter, 'description': task_description})
        tasks_id_counter += 1
    return redirect(url_for('tasks_page'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return redirect(url_for('tasks_page'))

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if request.method == 'POST':
        task['description'] = request.form.get('task')
        return redirect(url_for('tasks_page'))
    return render_template('edit.html', task=task)

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        task['completed'] = True
    return redirect(url_for('tasks_page'))


if __name__ == '__main__':
    app.run(debug=True)
