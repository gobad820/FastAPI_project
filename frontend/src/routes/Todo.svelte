<script>
    import fastapi from "../lib/api.js";
    import {link} from 'svelte-spa-router';

    let todo_list = [];
    let checked = false;

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
