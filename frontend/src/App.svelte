<script>
    import Router from 'svelte-spa-router';
    import Home from "./routes/Home.svelte";
    import Detail from "./routes/Detail.svelte"
    import Todo from "./routes/Todo.svelte";
    import TodoCreate from "./routes/TodoCreate.svelte";
    import Weather from './components/Weather.svelte';

    const routes = {
        "/": Todo,
        "/detail/:todo_id": Detail,
        '/todo-create': TodoCreate
    }
</script>
<Weather/>
<Router {routes}/>