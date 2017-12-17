 <?php

	if(isset($_POST['addition'])) {
		chdir('codes');
		$str = $_POST['addition'];
		$wordsC = count(preg_split('/\s+/', $str));
		 
		$file_open = fopen("files/TN1.txt","w+");
		fwrite($file_open, $str);
		fclose($file_open);
		
		shell_exec('sh ./shell.sh files TN 1 test');
		chdir('codes');
		// $output = shell_exec("python predict.py '".$wordsC."'");
		$output = "hi";
		echo "<pre>$output</pre>";
	}
	

?>