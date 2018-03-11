<!DOCTYPE html>
<html>
  <head>
	<title>Diabetic Spreadsheet</title>
  </head>
  
  <?php
    echo "Day is: " . $_GET["Day"];
    echo "<br>";
    echo "Glucose is: " . $_GET["Glucose"];
    echo "<br>";
    echo "Carb intake is: " . $_GET["CarbIntake"];
    echo "<br>";
    echo "Insulin is: " . $_GET["Insulin"];
    echo "<br>";
    echo "Time since last meal is: " . $_GET["Hours"] . " " .  "Hours," . " " .
                    $_GET["Minutes"] . " " . "Minutes";

    echo "<br>";
    echo "<br>";
    echo "Thank you. Your data has been recorded.";
    echo "<br>";    
    echo "<a href=\"WebPage.html\">Go Back</a>";
  
    $my_file = fopen("dataFile.txt", "a") or die("Unable to open file!");
    $new_line = "\n";
    fwrite($my_file, $_GET["Day"]);
    fwrite($my_file, $new_line);
    fwrite($my_file, $_GET["Glucose"]);
    fwrite($my_file, $new_line);
    fwrite($my_file, $_GET["CarbIntake"]);
    fwrite($my_file, $new_line);
    fwrite($my_file, $_GET["Insulin"]);
    fwrite($my_file, $new_line);
    fwrite($my_file, $_GET["Hours"]);
    fwrite($my_file, $new_line);
    fwrite($my_file, $_GET["Minutes"]);
    fwrite($my_file, $new_line); 

    fclose($my_file); 
   ?>


</body>
</html>

