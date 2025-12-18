# fix_all_repos.ps1
$basePath = Get-Location
$excludedRepos = @("CLOUD LEARNER")

# Loop through all repos in base path
Get-ChildItem -Directory | Where-Object { $excludedRepos -notcontains $_.Name } | ForEach-Object {
    $repo = $_
    Write-Host "--- Processing repo: $($repo.Name) ---"

    Set-Location $repo.FullName

    # Ensure scripts folder exists
    $scriptsPath = Join-Path $repo.FullName "scripts"
    if (-not (Test-Path $scriptsPath)) {
        New-Item -ItemType Directory -Path $scriptsPath | Out-Null
    }

    # Move Python and PS scripts to scripts/
    Get-ChildItem -File -Include *.py,*.ps1 | ForEach-Object {
        git mv $_.FullName (Join-Path $scriptsPath $_.Name)
    }

    # Remove .terraform directories
    Get-ChildItem -Recurse -Directory -Filter ".terraform" | ForEach-Object {
        Remove-Item -Recurse -Force $_.FullName
        git rm -r --cached $_.FullName
    }

    # Stage everything
    git add .

    # Commit changes
    $commitMsg = "Cloud Support: reorganized scripts, removed .terraform, updated README paths"
    git commit -m $commitMsg

    # Push changes
    git push origin main

    Set-Location $basePath
    Write-Host "--- Finished repo: $($repo.Name) ---`n"
}

Write-Host "✅ All repos processed (except excluded ones)."
