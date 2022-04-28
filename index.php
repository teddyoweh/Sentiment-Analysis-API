
<?php
# -*- coding=utf-8 -*-
# Name: teddy oweh
# Email: teddyoweh@teddyoweh.com
# Message: Feel Free To Contact Me on Enquires or Questions.



$host = '10.119.137.245';
$port = 5000;

$conn = 'http://'.$host.':'.$post;

$show ='none';
$name = $_POST['submit'];
$loc = array(
  "Text" => "null",
  "Sentiment" => "null",
  "Sentiment Level" => "null",
  "Polarity" => "null",
  "Subjectivity" => "null",
  
  
);
if(isset($name)){
  if(empty($name))
      {
          die("contact name is empty");
      }
      else
      {
        $text = $_POST['text'];
        $uri = $conn.'/?text='.urlencode($text);
        $url = file_get_contents($uri);
        $loc = json_decode($url, true); 
        $show = 'block';
      }   
    
}
?>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
<form style='padding:11px;'method="post">
    <div class="container">
        <div class="row">
            <input style='width:max-content;'name='text' class="form-control form-control-lg" type="text" placeholder="Enter a sentence" aria-label=".form-control-lg example">
            <input style='width:max-content;' name='submit'type="submit" class="btn btn-primary" value='Analyze'>
        </div>
    </div>

</form>
<div style='display:<?php echo $show?>;padding: 0px 126px;'> 
<table style='width:max-content;'class="table">
   
  <tbody>
  <tr>
      <th scope="row">  Text</th>
      <td><span style='font-family:monospace'><?php echo $loc['Text']?></span></td>
   
    </tr>
    <tr>
      <th scope="row">Sentiment</th>
      <td><span style='font-family:monospace'><?php echo $loc['Sentiment']?></span></td>
   
    </tr>
    <tr>
      <th scope="row">Sentiment Level</th>
      <td><span style='font-family:monospace'><?php echo $loc['Sentiment Level']?></span></td>
       
    </tr>
    <tr>
      <th scope="row">Polarity</th>
      
      <td><span style='font-family:monospace'><?php echo $loc['Polarity']?></span></td>
    </tr>
    <tr>
      <th scope="row">Subjectivity</th>
      
      <td><span style='font-family:monospace'><?php echo $loc['Subjectivity']?></span></td>
    </tr>
  </tbody>
</table>
</div>