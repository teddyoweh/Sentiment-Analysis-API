<?php
use GuzzleHttp;

$word = 'Im a developer';
$url = "https://sentiment-analytics-api.herokuapp.com/?text=$word";
$client = new \GuzzleHttp\Client();
$response = $client->request('GET', $url);
$data = json_decode($response->getBody(), true);

print_r($data);

foreach($data as $key => $item) {
    echo $key . ": " . $item . "\n";
}

?>