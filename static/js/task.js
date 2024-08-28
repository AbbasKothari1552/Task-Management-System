function show_add_task_modal(event) {
    event.preventDefault()
    document.querySelector('.task_overlay').classList.add('task_show_overlay')
    document.querySelector('.task_form').classList.add('task_show_form')
    document.getElementById('task_btn').innerText = `Add Task`
    // send request to add_task url 
    document.getElementById('TaskForm').setAttribute('action', `/add_task/`);
}

function hide_add_task_modal(event) {
    event.preventDefault()
    document.querySelector('.task_overlay').classList.remove('task_show_overlay')
    document.querySelector('.task_form').classList.remove('task_show_form')
}

function show_edit_task_modal(event) {
    event.preventDefault();
    
    // Ensure `this` refers to the clicked element
    const targetElement = event.currentTarget;
    
    document.querySelector('.task_overlay').classList.add('task_show_overlay');
    document.querySelector('.task_form').classList.add('task_show_form');
    document.getElementById('task_btn').innerText = 'Edit Task';
    
    // Get taskId from the clicked element
    const taskId = targetElement.getAttribute('data-task-id');
    
    // Fetch details of the task from taskId and prefill the form
    fetch(`/get_task/${taskId}/`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('id_title').value = data.title;
            document.getElementById('id_description').value = data.description;
            document.getElementById('id_tag').value = data.tag.name;
            document.getElementById('id_priority').value = data.priority;
            document.getElementById('id_date').value = data.date;
            document.getElementById('id_time').value = data.time;
            document.getElementById('id_repeat').value = data.repeat;
        })
        .catch(error => console.error('Error fetching task data:', error));
    
    document.getElementById('TaskForm').setAttribute('action', `/edit_task/${taskId}/`);
    // console.log('Form action:', document.getElementById('EditTaskForm').getAttribute('action'));

}

function show_delete_task_modal(event) {
    event.preventDefault()
    document.querySelector('.delete_task_overlay').classList.add('delete_task_show_overlay')
    document.querySelector('.delete_task_form').classList.add('delete_task_show_form')

    // Get task details from the clicked element
    const taskName = this.getAttribute('data-task-name');
    const taskId = this.getAttribute('data-task-id');
    
    // Display the task title in the modal
    document.getElementById('modalTaskTitle').innerText = `Are you sure you want to delete the task: "${taskName}"?`;
    
    // Update the form action with the correct task ID
    document.getElementById('deleteTaskForm').setAttribute('action', `/delete_task/${taskId}/`);
}

function hide_delete_task_modal(event) {
    event.preventDefault()
    document.querySelector('.delete_task_overlay').classList.remove('delete_task_show_overlay')
    document.querySelector('.delete_task_form').classList.remove('delete_task_show_form')
}

// Show modal for adding the task.
var show_add_task = document.getElementById('add_task')
show_add_task.addEventListener('click',show_add_task_modal)

// Show modal for editing thhe task.
var edit_task = document.querySelectorAll('.edit-task');

edit_task.forEach(function(button) {
    button.addEventListener('click', show_edit_task_modal);
});

var hide_add_task = document.getElementById('hide_task')
hide_add_task.addEventListener('click',hide_add_task_modal)

// Hide add tadk modal
var hide_add_task = document.getElementById('hide_task')
hide_add_task.addEventListener('click',hide_add_task_modal)

// Select all delete buttons
var deleteButtons = document.querySelectorAll('.delete-task');

// Loop through each delete button and attach event listener
deleteButtons.forEach(function(button) {
    button.addEventListener('click', show_delete_task_modal);
});

var hide_delete_task = document.getElementById('hide_delete_task')
hide_delete_task.addEventListener('click',hide_delete_task_modal)

