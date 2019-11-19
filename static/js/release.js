function update_table(k, v) {
    $('#opt').after("<option value='" + k + "'>" + v + "</option>");
}

$(function () {
    $('#tag').change(function () {
        var val = $('#tag option:selected').val();
        var csrf = $('input[name="csrfmiddlewaretoken"]').val();
        params = {"val": val, "csrfmiddlewaretoken": csrf}
        $.post('/release/', params, function (data) {
            if (data.res == 0) {
                $('#opt').nextAll().remove()
                $.each(data.data, function (k, v) {
                    update_table(k, v)
                })
            } else {
                $('#opt').nextAll().remove()
            }
        })
    })
})


$(function () {
    $('#btn').on('click', function () {
        var courseched = $('#course:checked').val()
        var csrf = $('input[name="csrfmiddlewaretoken"]').val();

        var blog_tag = null
        var blog_table = null

        if (courseched) {
            blog_tag = $('#tag option:selected').val();
            blog_table = $('#table option:selected').val();
        }

        var blog_title = $('#author').val()
        var blog_text = $('#editor').text()

        var file = document.getElementById("test-image-file").files;
        if (file.length != 0) {
            var blog_img = new FileReader()
            blog_img.readAsDataURL(file[0])
            blog_img.onload = function () {
                var blog_str = blog_img.result

                console.log(typeof(blog_str))

                params = {
                    "blog_tag": blog_tag,
                    "blog_table": blog_table,
                    "blog_title": blog_title,
                    "blog_text": blog_text,
                    "blog_img": blog_str,
                    "csrfmiddlewaretoken": csrf
                }

                $.post('/creatblog/', params, function (data) {
                    console.log(params)
                })
            };
        }
        else {
            blog_img = null
        }

    })
})
