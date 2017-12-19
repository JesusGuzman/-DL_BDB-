$(function(){
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
