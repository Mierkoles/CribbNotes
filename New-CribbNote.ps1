<#
.SYNOPSIS
  Scaffold a new Cribb Notes issue from the template.

.DESCRIPTION
  Creates notes/<slug>/index.qmd from _templates/note-template.qmd with the title,
  date, and categories filled in. The new note starts as a draft so it won't publish
  until you remove `draft: true`.

.EXAMPLE
  ./New-CribbNote.ps1 -Title "What a Token Actually Is"

.EXAMPLE
  ./New-CribbNote.ps1 -Title "RAG, Without the Hand-Waving" -Categories AI,Demystified -WhatIf
#>
[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [Parameter(Mandatory)] [string]   $Title,
    [string]   $Slug,
    [string[]] $Categories = @('AI'),
    [datetime] $Date = (Get-Date)
)

$ErrorActionPreference = 'Stop'
$root = $PSScriptRoot

if (-not $Slug) {
    $Slug = ($Title.ToLower() -replace "[^a-z0-9\s-]", "" -replace "\s+", "-").Trim('-')
}

$dir  = Join-Path $root "notes/$Slug"
$file = Join-Path $dir 'index.qmd'

if (Test-Path $file) { throw "A note already exists at: $file" }

$cats  = ($Categories -join ', ')
$front = @"
---
title: "$Title"
subtitle: "Note — one-line hook."
description: "The one-sentence promise: what the reader walks away knowing."
date: $($Date.ToString('yyyy-MM-dd'))
categories: [$cats]
author: "Mark Cribb"
draft: true
---

Open with the question, the moment, or the misconception that made this worth writing.

## The one idea



## Why it matters



## Show the gears



*Feels like magic. It's math.*

— Mark
"@

if ($PSCmdlet.ShouldProcess($file, 'Create new Cribb Note')) {
    New-Item -ItemType Directory -Path $dir -Force | Out-Null
    Set-Content -Path $file -Value $front -Encoding utf8
    Write-Host "Created $file" -ForegroundColor Green
    Write-Host "Preview the site with:  quarto preview" -ForegroundColor DarkGray
    Write-Host "When ready, delete the 'draft: true' line to publish." -ForegroundColor DarkGray
}
