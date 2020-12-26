<?php
$res = file_get_contents("https://www.europages.cn/%E5%90%84%E4%BC%81%E4%B8%9A/pg-2/jieguo.html?ih=01505B;21810C");

preg_match_all("/alt=\"([^\"]*)\" id=\"([^\"]*)\"/i", $res, $res2);

var_dump($res2);
