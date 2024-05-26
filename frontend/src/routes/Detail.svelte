<script>
    import fastapi from "../lib/api"
    export let params = {}
    let todo_id = params.todo_id
    let todo = {};
    let error = {detail: []};
    let content = "";

    function get_todo(){
        fastapi("get","/api/todo/detail/"+todo_id,{},(json)=>{
            todo=json
        })
    }

    get_todo()
</script>

<h1>Todo</h1>
<div>
    {todo.content} : {todo.due_date}
</div>
