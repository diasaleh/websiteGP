<!DOCTYPE html>

<html>
    <head>
    	<meta charset="utf-8">
	    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
	    <meta name="description" content="">
	    <meta name="author" content="">
        <title>المتنبىء</title>
        <link rel="stylesheet" href="dist/css/bootstrap.min.css" >
    	<link href="dist/css/narrow-jumbotron.css" rel="stylesheet">
		

    </head>
    <body>
	    <div class="container">
		    <header class="header text-center clearfix">
		    	<div class="text-center">
	        		<img width="320px" class="d-inline-block text-center" src="final2.png"> 
	        	</div>
	        	<h3 class="text-center">تنبأ بعصر نص عربي</h3>

		    </header>      	 
	       
	        <div class="jumbotron">
<!-- 	          	<h1 class="display-3">Jumbotron heading</h1>
	 -->    	     	
 				<p class="lead"></p>
 				<ul dir="rtl" class="text-right">
 					<li>أدخل على الأقل 500 كلمة للحصول على نتيجة دقيقة.</li>
 					<li>كلما زاد عدد الكلمات المدخلة زادت الدقة.</li>
 				</ul>
	          	<form action="predict.php" method="POST">
	          	<div class="form-group">
		    		<label for="input" class="d-block text-right">عدد الكلمات: <span  id="wordCount">0</span></label>
		    		<textarea dir="rtl" name="addition" id='text' class="form-control" id="input" rows="10"></textarea>
		  		</div>
	          	  <button type="submit" class="btn btn-lg btn-outline-info Guess">تنبأ</button>
		        </form>


		        <div class="row marketing ">
	          	
		          	<!-- <div class="col-12">
		          		<h4>كيف يعمل الموقع؟</h4>
		            	<p>Maecenas sed diam eget risus varius blandit sit amet non magna.</p>
		          	</div> -->
		        </div>
		    </div>
 

	            


	      

	   </div> <!-- /container -->
	   	<footer class="footer text-center">
	        <p>&copy; Al-Motanabe 2017</p>
	    </footer>
   </body>

</html>
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.3/umd/popper.min.js" integrity="sha384-vFJXuSJphROIrBnz7yo7oB41mKfc8JzQZiCq4NCceLEaO4IHwicKwpJf9c9IpFgh" crossorigin="anonymous"></script>
<script src="dist/js/bootstrap.min.js"></script>
<script type="text/javascript" src="dist/js/script.js"></script>