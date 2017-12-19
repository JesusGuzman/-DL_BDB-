/*$(function(){
	$('#btnSignUp').click(function(){
		
		$.ajax({
			url: '/signUp',
			data: $('form').serialize(),
                        dataType: "json",
			type: 'POST',
			success: function(response){
				console.log(response);
			
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});
*/
$(function(){
        $("#formuploadajax").on("submit", function(e){
            e.preventDefault();
            var f = $(this);
            var formData = new FormData(document.getElementById("formuploadajax"));
            formData.append("dato", "valor");
            //formData.append(f.attr("name"), $(this)[0].files[0]);
            $.ajax({
                url: "/upload_image",
                type: "post",
                dataType: "json",
                data: formData,
                cache: false,
                contentType: false,
	     processData: false
            })
                .done(function(res){
                    $("#mensaje").html("Respuesta: " );
                });
        });
    });
