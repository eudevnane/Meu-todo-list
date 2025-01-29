// Função para adicionar uma nova tarefa
async function addTask() {
    let taskInput = document.getElementById("task-input");
    let taskText = taskInput.value.trim();  // Remove espaços extras

    if (taskText === "") return;  // Se estiver vazio, não faz nada

    let response = await fetch("/add", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ task: taskText })
    });

    if (response.ok) {
        taskInput.value = ""; // Limpa o campo
        loadTasks(); // Atualiza a lista
    }
}

// Função para carregar todas as tarefas
async function loadTasks() {
    let response = await fetch("/tasks");
    let tasks = await response.json();

    let taskList = document.getElementById("task-list");
    taskList.innerHTML = "";

    tasks.forEach(task => {
        let li = document.createElement("li");
        li.innerHTML = `${task.text} <button onclick="deleteTask(${task.id})">X</button>`;
        taskList.appendChild(li);
    });
}

// Função para remover uma tarefa
async function deleteTask(taskId) {
    await fetch(`/delete/${taskId}`, { method: "DELETE" });
    loadTasks();
}

// Carrega as tarefas ao abrir a página
window.onload = loadTasks;
