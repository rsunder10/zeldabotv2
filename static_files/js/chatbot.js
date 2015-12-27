// $(document).ready(function(e){


// $('#text').keyup(function(e){
//     if(e.keyCode == 13)
//     {
//        var msg =$(this).val();
//        if (msg!=''){
//        	$('#send').click();
//        }
//     }
// });
// $('#send').click(function(e){
// 	var msg = $('#text').val()
// 	var html = '<div class="chat-box-right">'+msg+'</div><div class="chat-box-name-right"><img src="assets/img/user.gif" alt="bootstrap Chat box user image" class="img-circle" />- Romin Royeelin</div><hr class="hr-clas" />'
// });

	// if(user != ''){
	// 	$('#upvote_review').click(function(e){

	// 		var upvote = 'True';
	// 		var data = {
	// 			'upvote':upvote
	// 		} 
				// $.ajax({
				// 	  	method: "GET",
				// 	  	url: url,
				// 	  	data:data,
				// 	  	success:function(data){
				// 	  		console.log(data);
				// 	  		$('#upcount').text(data.upvote);
				// 	  		$('#downcount').text(data.downvote);
				// 	  		$('#downvote_review').removeAttr('disabled');
				// 	  		$('#upvote_review').attr('disabled','disabled');

				// 	  	},
				// 	  	error: function(response,error){
				// 	  		console.log(response);
				// 	  		console.log(error);
				// 	  	}
				// 	});
	// 	});

	// 	$('#downvote_review').click(function(e){
	// 		var downvote = 'True';

	// 		var data = {
	// 			'downvote':downvote
	// 		} 
	// 			$.ajax({
	// 				  	method: "GET",
	// 				  	url: url,
	// 				  	data:data,
	// 				  	success:function(data){
	// 				  		console.log(data);
	// 				  		$('#upcount').text(data.upvote);
	// 				  		$('#downcount').text(data.downvote);
	// 				  		$('#upvote_review').removeAttr('disabled');
	// 				  		$('#downvote_review').attr('disabled','disabled');

	// 				  	},
	// 				  	error: function(response,error){
	// 				  		console.log(response);
	// 				  		console.log(error);
	// 				  	}
	// 				});
	// 	});


	// 		$('#cupvote').click(function(e){

	// 		var upvote = 'True';
	// 		var comment_id = $(this).attr('comment-id');
	// 		var data = {
	// 			'cupvote':upvote,
	// 			'comment_id':comment_id
	// 		} 
	// 			$.ajax({
	// 				  	method: "GET",
	// 				  	url: url,
	// 				  	data:data,
	// 				  	success:function(data){
	// 				  		console.log(data);
	// 				  		$('#cupcount').text(data.cupvote);
	// 				  		$('#cdowncount').text(data.cdownvote);
	// 				  		$('#cdownvote').removeAttr('disabled');
	// 				  		$('#cupvote').attr('disabled','disabled');
					  		
	// 				  	},
	// 				  	error: function(response,error){
	// 				  		console.log(response);
	// 				  		console.log(error);
	// 				  	}
	// 				});
	// 	});

	// 	$('#cdownvote').click(function(e){
	// 		var downvote = 'True';
	// 		var comment_id = $(this).attr('comment-id');
	// 		var data = {
	// 			'cdownvote':downvote,
	// 			'comment_id':comment_id
	// 		} 
	// 			$.ajax({
	// 				  	method: "GET",
	// 				  	url: url,
	// 				  	data:data,
	// 				  	success:function(data){
	// 						console.log(data);				  		
	// 				  		$('#cupcount').text(data.cupvote);
	// 				  		$('#cdowncount').text(data.cdownvote);
	// 				  		$('#cupvote').removeAttr('disabled');
	// 				  		$('#cdownvote').attr('disabled','disabled');
	// 				  	},
	// 				  	error: function(response,error){
	// 				  		console.log(response);
	// 				  		console.log(error);
	// 				  	}
	// 				});
	// 	});

	// }
// });

