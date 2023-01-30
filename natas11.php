#!/opt/homebrew/bin/php
<?php

$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");

//default function, we're gonna modify it below
// function xor_encrypt($in) {
//     $key = '<censored>';
//     $text = $in;
//     $outText = '';

//     // Iterate through each character
//     for($i=0;$i<strlen($text);$i++) {
//     $outText .= $text[$i] ^ $key[$i % strlen($key)];
//     }

//     return $outText;
// }

//so our function
//The XOR logic works like this:
//plaintext ^ key = ciphertext
//what we can do is leverage this though: plaintext ^ ciphertext = key
function xor_encrypt($in, $key) {
    //removed the key value from in here AND OH MY GOODNESS IT FIXED HOURS OF ISSUES I can't believe I missed that -_-
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

//original = json_encode($defaultdata);
//renaming
$plaintext = json_encode($defaultdata);

//this outputs what we were getting in python before the .hex() ie: 0l;$$98-8=?#9*jvi 'ngl*+(!$#9lrnh(.*-(.n6
//(ok technicality, we needed to utf-8 the value in python to match 100% but it's more or less the same
$ciphertext = hex2bin('306c3b242439382d383d3f23392a6a766920276e676c2a2b28212423396c726e68282e2a2d282e6e36');
echo "|ciphertext is: " . $ciphertext;

//see logic above, just passing plaintext and ciphertext wihtout key, to get key
//John gets a repeating output of 4 characters...instead my terminal gets all goofy but I do see GAMK first every time
//update: after fixing the xor_encrypt above now this runs just like John's... that makes way more sense, value is KNHL
echo("|key should be: " . xor_encrypt($plaintext, $ciphertext));

$key = 'KNHL';

$good_data = array("show_password"=>'yes', "bgcolor"=>"#ffffff");

$goodplaintext = json_encode($good_data);
$goodciphertext = xor_encrypt( $goodplaintext, $key );
echo("|good ciphertext (xor'd) is: " . $goodciphertext);

$cookie = base64_encode($goodciphertext);
//this should be XOR'd data
echo("|good plaintext is: " . $goodplaintext);

echo("|cookie data: " . $cookie);//this actually returned something proper using terminal itself not in sublime terminal
//it looks like this: R0EWBhwYLRUFTU8UChwXTUhHHVtPQUlMEQgRCghRTkFfTFAJFAMCWFpBGA==
//I've seen similar before, I'm guessing that's what we need over in python without the ==
//I dunno why the php script is gimping out, it made me think this wouldn't work but maybe
// ———————————————————————————————————————
//after fixing the function above, it's not gimping out and I got different cookie data: MGw7JCQ5FzwqPTs7JDwsbnFsMSk4bGRuKSkrIychOm5xbGsqLSguKi1sNQ==
// still had to run in terminal though, in-sublime terminal is goofy



//SDG
?>