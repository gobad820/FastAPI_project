<script>
    import fastapi from "../lib/api.js";
    import {link} from 'svelte-spa-router';

    function get_todo_list() {
        fastapi('get', '/api/todo/list', {}, (json) => {
            todo_list = json;
        })
    }

    async function handleCheckboxChange(todo) {
        if (todo.completed) {
            await fastapi('delete', `/api/todo/${todo.id}`, {}, () => {
                get_todo_list();
            });
        }
    }

    function isExpired(due_date) {
        const now = new Date();
        const dueDateTime = new Date(due_date);
        return now > dueDateTime;
    }

    get_todo_list();


    let todo_list = [];
    let checked = false;

    let todos_today = [];
    let todos_tomorrow = [];
    let todos_later = [];

    async function get_todos(day) {
        await fastapi('get', `/api/todo/todos/${day}`, {}, (json) => {
            if (day === 'today') {
                todos_today = json;
            } else if (day === 'tomorrow') {
                todos_tomorrow = json;
            } else if (day === 'later') {
                todos_later = json;
            }
        })
    }

    $: get_todos('today');
    $: get_todos('tomorrow');
    $: get_todos('later');
</script>
<style>
    .expired {
        color: red;
    }
</style>
<!--<ul>-->
<!--    {#each todo_list as todo}-->
<!--        <li><a use:link href="/detail/{todo.id}">{todo.content}</a></li>-->
<!--    {/each}-->
<!--</ul>-->


<div class="container my-3">
    <table class="table">
        <thead>
        <tr class="table-dark">
            <th>번호</th>
            <th>제목</th>
            <th>만료날짜</th>
            <th>완료</th>
        </tr>
        </thead>
        <tbody>
        {#each todo_list as todo, i}
            <tr>
                <td>{i + 1}</td>
                <td>
                    <a use:link href="/detail/{todo.id}" class:expired={isExpired(todo.due_date)}>{todo.content}</a>
                </td>
                <td>{todo.due_date}</td>
                <td>
                    <input type="checkbox" bind:checked={todo.completed} on:change={() => handleCheckboxChange(todo)}/>
                </td>
            </tr>
        {/each}
        </tbody>
    </table>
    <a use:link href="/todo-create" class="btn btn-primary">Todo 등록하기</a>
</div>

<div class="container my-3">
    <h2 class="mb-3">Today's Todos</h2>
    <ul class="list-group">
        {#each todos_today as todo}
            <li class="list-group-item">{todo.content} - Due: {todo.due_date}</li>
        {/each}
    </ul>

    <h2 class="mt-5 mb-3">Tomorrow's Todos</h2>
    <ul class="list-group">
        {#each todos_tomorrow as todo}
            <li class="list-group-item">{todo.content} - Due: {todo.due_date}</li>
        {/each}
    </ul>

    <h2 class="mt-5 mb-3">Later Todos</h2>
    <ul class="list-group">
        {#each todos_later as todo}
            <li class="list-group-item">{todo.content} - Due: {todo.due_date}</li>
        {/each}
    </ul>
</div>