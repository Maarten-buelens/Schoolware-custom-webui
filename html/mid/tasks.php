<!DOCTYPE html>
<title>punten</title>

<?php
$time = microtime();
$time = explode(' ', $time);
$time = $time[1] + $time[0];
$start = $time;
?>
<html style="overflow: scroll;">

<link rel="stylesheet" href="/util/css.css">
<script type="text/javascript" src="/util/js.js"></script>
<div>


<?php
ini_set('display_startup_errors', 1);
ini_set('display_errors', 1);
error_reporting(-1);

$command = escapeshellcmd('/usr/bin/python3 ../main.py --taken');
$output = shell_exec($command);
echo $output;

?>

</div>
</html>
<?php
ini_set('display_startup_errors', 1);
ini_set('display_errors', 1);
error_reporting(-1);
$time = microtime();
$time = explode(' ', $time);
$time = $time[1] + $time[0];
$finish = $time;
$total_time = round(($finish - $start), 2);
#$time = number_format(($total_time)$foo, 2, '.', '');
echo 'time to load '.$total_time.' seconds.';
?>
