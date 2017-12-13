$(function(){
	$('#btnSignUp').click(function(){
		
		$.ajax({
			url: '/signUp',
			data: $('form').serialize(),
			/////////////////////////////
                        //data: JSON.stringify({'param':{"hello":"world"}}),
                        dataType: "json",
                        ////////////////////////////
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
