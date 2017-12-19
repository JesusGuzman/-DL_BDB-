$(function(){
	$('#btnSignUp').click(function(){
		
		$.ajax({
			//url: '/signUp',
			url: '/upload_image',
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
