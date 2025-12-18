# Navigate to repo root before running
# cd C:\path\to\your/next/repo

$scenarios = Get-ChildItem -Path .\scenarios -Directory

Write-Host "CloudFormation Template Validation Results:`n"

foreach ($scenario in $scenarios) {
    $templatePath = Join-Path $scenario.FullName "cloudformation.yaml"
    if (Test-Path $templatePath) {
        try {
            $result = aws cloudformation validate-template --template-body "file://$templatePath" 2>&1
            if ($result -like "*Parameters*") {
                Write-Host "✅ [$($scenario.Name)] CloudFormation template valid"
            } else {
                Write-Host "❌ [$($scenario.Name)] CloudFormation template validation returned unexpected output"
            }
        } catch {
            Write-Host "❌ [$($scenario.Name)] CloudFormation template validation failed"
            Write-Host "Error: $_"
        }
    } else {
        Write-Host "❌ [$($scenario.Name)] No cloudformation.yaml found"
    }
}

Write-Host "`nValidation complete. Screenshot being captured..."

# --- Screenshot Section ---
Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

$bounds = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds
$bitmap = New-Object System.Drawing.Bitmap $bounds.Width, $bounds.Height
$graphics = [System.Drawing.Graphics]::FromImage($bitmap)
$graphics.CopyFromScreen($bounds.Location, [System.Drawing.Point]::Empty, $bounds.Size)

# Save screenshot in repo root
$screenshotPath = Join-Path (Get-Location) ("CloudFormation_Validation_" + (Get-Date -Format "yyyyMMdd_HHmmss") + ".png")
$bitmap.Save($screenshotPath, [System.Drawing.Imaging.ImageFormat]::Png)

Write-Host "✅ Screenshot saved to $screenshotPath"
