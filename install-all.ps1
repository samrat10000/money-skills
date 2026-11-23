# Runs every skill pack's installer (Windows).
Get-ChildItem -Path $PSScriptRoot -Directory | ForEach-Object {
  $i = Join-Path $_.FullName "install\install.ps1"
  if (Test-Path $i) { Write-Host "== $($_.Name)"; & powershell -ExecutionPolicy Bypass -File $i }
}
