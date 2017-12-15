<!DOCTYPE html>

<html>
    <head>
    	<meta charset="utf-8">
	    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
	    <meta name="description" content="">
	    <meta name="author" content="">
        <title>المتنبيء</title>
        <link rel="stylesheet" href="dist/css/bootstrap.min.css" >
    	<link href="dist/css/narrow-jumbotron.css" rel="stylesheet">
		

    </head>
    <body>
	    <div class="container">
		    <header class="header clearfix">
		        <h3 class="text-center">المتنبيء</h3>
		    </header>      	 
	       
	        <?php

				if(isset($_POST['addition'])) {
					chdir('codes');
					$file_open = fopen("files/TN1.txt","w+");
					fwrite($file_open, $_POST['addition']);
					fclose($file_open);
					
					shell_exec('sh ./shell.sh files TN 1 test');
					$output = shell_exec('python predict.py');

					echo "<pre>$output</pre>";
				}
				

			?>
	        <div class="jumbotron">
<!-- 	          	<h1 class="display-3">Jumbotron heading</h1>
 -->	          	<p class="lead">Cras justo odio, dapibus ac facilisis in, egestas eget quam. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.</p>
	          	<form action="" method="POST">
	          	<div class="form-group">
		    		<label for="input" class="d-block text-right">عدد الكلمات: <span  id="wordCount">0</span></label>
		    		<textarea dir="rtl" name="addition" id='text' class="form-control" id="input" rows="10"></textarea>
		  		</div>
	          	  <button type="submit" class="btn btn-lg btn-info Guess">تنبأ</button>

		        </div>
		        </form>

		        <div class="row marketing">
	          <div class="col-lg-6">
	           

	            <h4>Subheading</h4>
	            <p>Maecenas sed diam eget risus varius blandit sit amet non magna.</p>
	          </div>

	          <div class="col-lg-6">
	           

	            <h4>Subheading</h4>
	            <p>Maecenas sed diam eget risus varius blandit sit amet non magna.</p>
	          </div>
	        </div>


	      <footer class="footer">
	        <p>&copy; Company 2017</p>
	      </footer>

	   </div> <!-- /container -->
   </body>

</html>
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.3/umd/popper.min.js" integrity="sha384-vFJXuSJphROIrBnz7yo7oB41mKfc8JzQZiCq4NCceLEaO4IHwicKwpJf9c9IpFgh" crossorigin="anonymous"></script>
<script src="dist/js/bootstrap.min.js"></script>
<script type="text/javascript" src="dist/js/script.js"></script>