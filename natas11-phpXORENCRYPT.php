<?php

$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");

function xor_encrypt($in, $key) {
    //$key = '<censored>';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}
$plaintext = json_encode($defaultdata);
echo($plaintext);
echo("\n");
$ciphertext = hex2bin('306c3b242439382d383d3f23392a6a766920276e676c2a2b28212423396c726e68282e2a2d282e6e36');
echo($ciphertext);
echo("\n");

echo(xor_encrypt($plaintext, $ciphertext));
echo("\n");

//so the above yield GAMK and some other junk, GAMK should be our key, so we can do this again with the data we want
$wantedData = array( "showpassword"=>"yes", "bgcolor"=>"#ffffff");
$wantedPlaintext = json_encode($wantedData);
$key = 'KNHL';

$secureCookie = xor_encrypt($wantedPlaintext, $key);
echo($secureCookie);
echo("\n");

$newCookie = base64_encode($secureCookie);
echo($newCookie);
echo("\n");

?>