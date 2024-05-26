<!--<script>-->
<!--    import {push} from 'svelte-spa-router'-->
<!--    import fastapi from "../lib/api"-->

<!--    let error = {detail:[]}-->
<!--    let due_date = ''-->
<!--    let content = ''-->

<!--    function post_todo(event) {-->
<!--        event.preventDefault()-->
<!--        let url = "/api/todo/create"-->
<!--        let params = {-->
<!--            content: content,-->
<!--            due_date: due_date,-->
<!--        }-->
<!--        fastapi('post', url, params,-->
<!--            (json) => {-->
<!--                push("/")-->
<!--            },-->
<!--            (json_error) => {-->
<!--                // error = json_error-->
<!--            }-->
<!--        );-->
<!--    }-->
<!--</script>-->

<!--<div class="container">-->
<!--    <h5 class="my-3 border-bottom pb-2">질문 등록</h5>-->
<!--    &lt;!&ndash;    <Error error={error} />&ndash;&gt;-->
<!--    <form method="post" class="my-3">-->
<!--        <div class="mb-3">-->
<!--            <label for="subject">제목</label>-->
<!--            <input type="text" class="form-control" bind:value="{content}">-->
<!--        </div>-->
<!--        <div class="mb-3">-->
<!--            <label for="due_date">기한</label>-->
<!--            <input type="date" id="due_date" name="due_date" class="form-control" bind:value={due_date}>-->
<!--        </div>-->
<!--        <button class="btn btn-primary" on:click="{post_todo}">저장하기</button>-->
<!--    </form>-->
<!--</div>-->
<!--<script>-->
<!--    import {push} from 'svelte-spa-router';-->
<!--    import fastapi from "../lib/api";-->

<!--    let error = {detail: []};-->
<!--    let due_date = '';-->
<!--    let content = '';-->

<!--    function post_todo() {-->
<!--        let url = "/api/todo/create";-->
<!--        let params = {-->
<!--            content: content,-->
<!--            due_date: due_date,-->
<!--        };-->
<!--        fastapi('post', url, params,-->
<!--            (json) => {-->
<!--                console.log("Success:", json); // 성공 시 콘솔 로그 추가-->
<!--                push("/");-->
<!--            },-->
<!--            (json_error) => {-->
<!--                console.log("Error:", json_error); // 에러 시 콘솔 로그 추가-->
<!--                error = json_error;-->
<!--            }-->
<!--        );-->
<!--    }-->

<!--    function handleSubmit(event) {-->
<!--        event.preventDefault();-->
<!--        post_todo();-->
<!--    }-->
<!--</script>-->

<!--<div class="container">-->
<!--    <h5 class="my-3 border-bottom pb-2">질문 등록</h5>-->
<!--    &lt;!&ndash;    <Error error={error} />&ndash;&gt;-->
<!--    <form method="post" class="my-3" on:submit={handleSubmit}>-->
<!--        <div class="mb-3">-->
<!--            <label for="subject">제목</label>-->
<!--            <input type="text" class="form-control" bind:value="{content}">-->
<!--        </div>-->
<!--        <div class="mb-3">-->
<!--            <label for="due_date">기한</label>-->
<!--            <input type="datetime-local" id="due_date" name="due_date" class="form-control" bind:value={due_date}>-->
<!--        </div>-->
<!--        <button type="submit" class="btn btn-primary">저장하기</button>-->
<!--    </form>-->

<!--</div>-->

<script>
    import {push} from 'svelte-spa-router';
    import fastapi from "../lib/api";

    let error = {detail: []};
    let due_date = '';
    let content = '';
    let due_time = '';

    function post_todo() {
        let url = "/api/todo/create";
        let params = {
            content: content,
            due_date: `${due_date}T${due_time}`,
        };
        fastapi('post', url, params,
            (json) => {
                console.log("Success:", json); // 성공 시 콘솔 로그 추가
                setNotification(content, params.due_date); // setNotification 함수 호출 추가
                push("/");
            },
            (json_error) => {
                console.log("Error:", json_error); // 에러 시 콘솔 로그 추가
                error = json_error;
            }
        );
    }

    function sendNotification(content) {
        // 알림 권한 요청
        Notification.requestPermission().then(function (permission) {
            if (permission === 'granted') {
                // 알림 보내기
                new Notification('Todo Reminder', {
                    body: content,
                });
            }
        });
    }

    function setNotification(content, due_date) {
        // 알림 권한 요청
        Notification.requestPermission().then(function (permission) {
            if (permission === 'granted') {
                // 사용자가 설정한 시간에 알림을 보냅니다.
                const dueDateTime = new Date(due_date);
                const now = new Date();
                const delay = dueDateTime.getTime() - now.getTime();

                setTimeout(() => {
                    new Notification('Todo Reminder', {
                        body: content,
                    });
                }, delay);
            }
        });
    }

    function handleSubmit(event) {
        event.preventDefault();
        post_todo();
    }
</script>

<div class="container">
    <h5 class="my-3 border-bottom pb-2">질문 등록</h5>
    <form method="post" class="my-3" on:submit={handleSubmit}>
        <div class="mb-3">
            <label for="subject">제목</label>
            <input type="text" class="form-control" bind:value="{content}">
        </div>
        <div class="mb-3">
            <label for="due_date">기한</label>
            <input type="date" id="due_date" name="due_date" class="form-control" bind:value={due_date}>
        </div>
        <div class="mb-3">
            <label for="due_time">시간</label>
            <input type="time" id="due_time" name="due_time" class="form-control" bind:value={due_time}>
        </div>
        <button type="submit" class="btn btn-primary">저장하기</button>
    </form>
</div>