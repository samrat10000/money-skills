# Renders one engine shot on the Windows GPU box in chunks, sharing the GPU politely, then encodes an mp4.
# Usage (from terror-night\engine\ep1):
#   powershell -ExecutionPolicy Bypass -File ..\..\scripts\run_cut_asus.ps1 -Cut 125 -Frames 120
param([int]$Cut, [int]$Frames, [int]$Chunk = 30, [string]$Res = "1", [string]$Samp = "48", [string]$MB = ".25",
      [string]$Blender = "C:\Users\cross\Downloads\xc\blender501\blender.exe", [string]$OutRoot = "$PWD\..\out")
$env:CUT = "$Cut"; $env:RES = $Res; $env:SAMP = $Samp; $env:MB = $MB; $env:DEVICE = "GPU"; $env:OUTROOT = $OutRoot
New-Item -ItemType Directory -Force "$OutRoot\c$Cut" | Out-Null
for ($a = 1; $a -le $Frames; $a += $Chunk) {
  $b = [Math]::Min($a + $Chunk - 1, $Frames)
  while (Get-Process blender -ErrorAction SilentlyContinue) { Start-Sleep -Seconds 20 }   # another job is rendering: wait, never kill it
  Get-ChildItem "$OutRoot\c$Cut\f*.png" -ErrorAction SilentlyContinue | Where-Object { $_.Length -eq 0 } | Remove-Item   # stale placeholders
  $env:FR = "$a,$b"; $t0 = Get-Date
  & $Blender -b --python shots2.py *> "$OutRoot\r$Cut`_$a.log"
  $n = (Get-ChildItem "$OutRoot\c$Cut\f*.png" | Where-Object { $_.Length -gt 0 }).Count
  $s = ((Get-Date) - $t0).TotalSeconds / [Math]::Max(1, ($b - $a + 1))
  Write-Host ("chunk {0}-{1}: {2:N1} s/frame, {3}/{4} frames on disk" -f $a, $b, $s, $n, $Frames)
  if (-not (Select-String -Path "$OutRoot\r$Cut`_$a.log" -Pattern "CUT DONE" -Quiet)) { Write-Host "ERROR: see $OutRoot\r$Cut`_$a.log"; Get-Content "$OutRoot\r$Cut`_$a.log" -Tail 40; exit 1 }
}
if (Get-Command ffmpeg -ErrorAction SilentlyContinue) {
  ffmpeg -y -loglevel error -framerate 24 -i "$OutRoot\c$Cut\f%04d.png" -c:v libx264 -crf 14 -pix_fmt yuv420p "$OutRoot\$Cut`_frames.mp4"
  Write-Host "encoded $OutRoot\$Cut`_frames.mp4"
}
