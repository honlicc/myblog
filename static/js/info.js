$(function () {
    $('#btn').on('click', function () {
        var comment = $('#comment').val()
        var csrf = $('input[name="csrfmiddlewaretoken"]').val()
        var blog_id = $('#respond').attr('blog_id')

        if (comment.replace(/(^s*)|(s*$)/g, "").length == 0) {
            alert('评论内容不可为空')
        } else {

            params = {'comment': comment, 'csrfmiddlewaretoken': csrf, 'blog_id': blog_id}
            $.post('/comment', params, function (data) {
                if (data.res == 1) {
                    alert(data.msg)
                    location.reload();
                }
                else {
                    alert(data.msg)
                }
            })
        }
    })
})

