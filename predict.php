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
	       
	        <div class="jumbotron2">
<!-- 	          	<h1 class="display-3">Jumbotron heading</h1>
	 -->    
	 	          	<form action="index.php" method="POST">

	 		<button type="submit" id ="back" class="btn btn-outline-info Guess">الرجوع</button>

 				<p class="lead"></p>
 				
	          
		        </form>


		        <div class="row marketing ">
	          	
		          	<div class="col-12 text-center">
		          		 <?php
		          		 function clean($string) {
						   $string = str_replace(' ', '-', $string); // Replaces all spaces with hyphens.

						   return preg_replace('/[^A-Za-z0-9\-]/', '', $string); // Removes special chars.
						}
							if(isset($_POST['addition'])) {
								chdir('codes');
								$str = $_POST['addition'];
								$wordsC = count(preg_split('/\s+/', $str));
								$date = date_create();
								$ti = date_timestamp_get($date);
								shell_exec("sh ./shsh.sh '".$ti."' ");
								$dirname = "".$ti."/T1.txt";
								$file_open = fopen($dirname,"w+");
								fwrite($file_open, $str);
								fclose($file_open);
								
								shell_exec("sh ./shell.sh '".$ti."' TN 1 '".$ti."'");
								chdir('codes');
								$output = shell_exec("python predict.py  '".$ti."' '".$wordsC."'");
								$dirname2 = "".$ti."_P.txt";

								$handle = fopen($dirname2, "r");
								$i=0;

								if ($handle) {
								    while (($line = fgets($handle)) !== false) {

								    	if($i==0){
								    		echo "التنبؤ هو";
								       	 	echo "<h1 style='font-size: 70px'>هـ $line </h1>";
								       	 	$line = (int)$line;
								       	 	if ($line == "1400" ) {
											   echo "<p style='font-size: 50px'>نص حديث</p>";
											} elseif ($line == "1000" ) {
												echo "<p style='font-size: 50px'>عصر ازدهار اللغة</p>";
											} 
											elseif ($line == "100" ) {
												echo "<p style='font-size: 50px'>نص قديم</p>";
											} 
								    	}
								    	if($i==1){
								    	echo "<hr>";
								    	$line = (float)$line;
								    	$line = round($line,1, PHP_ROUND_HALF_UP);
								    	echo "نسبة النص القديم - 100هـ";
								       	 echo "<p style='font-size: 30px'>$line%</p>";
								    	}
								    	if($i==2){
								    	$line = (float)$line;
								    	$line = round($line,1, PHP_ROUND_HALF_UP);
								    	echo "نسبة النص متوسط الحداثة  - 1000هـ";
								       	 echo "<p style='font-size: 30px'>$line%</p>";
								    	}
								    	if($i==3){
								    	$line = (float)$line;
								    	$line = round($line,1, PHP_ROUND_HALF_UP);
								    	echo "نسبة النص الحديث - 1400هـ";
								       	 echo "<p style='font-size: 30px'>$line%</p>";
								    	}
								    	$i++;
								    }

								    fclose($handle);
								} else {
								    // error opening the file.
								} 
								


							}else{
							echo "error";
						}
							

						?>
					
		          	</div>
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

