$codes=72,101,108,108,111,44,87,111,114,108,100,33
foreach ($c in $codes){
    $c=[char]$c
    Write-Host -NoNewline $c -ForegroundColor (Get-Random -InputObject "Red","Yellow","Green","Cyan","Magenta","White")
}