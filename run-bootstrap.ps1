#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Wrapper script to run Code-Morningstar.ps1 with proper execution policy handling.
.DESCRIPTION
    This script ensures that Code-Morningstar.ps1 can be executed regardless of 
    the current PowerShell execution policy settings.
.NOTES
    Created to fix the PowerShell execution policy issue in CI/CD environments.
#>

$ErrorActionPreference = "Stop"

try {
    # Try to set execution policy for the current process
    try {
        Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force
        Write-Host "✅ Set execution policy to Bypass for current process"
    } catch {
        Write-Warning "Could not set execution policy: $($_.Exception.Message)"
        Write-Host "⚠️  Continuing anyway..."
    }
    
    # Get the directory where this script is located
    $scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
    $bootstrapScript = Join-Path $scriptDir "Code-Morningstar.ps1"
    
    # Check if the bootstrap script exists
    if (-not (Test-Path $bootstrapScript)) {
        throw "Bootstrap script not found at: $bootstrapScript"
    }
    
    Write-Host "🚀 Running Code Morningstar bootstrap script..."
    
    # Execute the bootstrap script
    & $bootstrapScript
    
    Write-Host "✅ Bootstrap script completed successfully!"
    
} catch {
    Write-Error "❌ Bootstrap script failed: $($_.Exception.Message)"
    exit 1
}