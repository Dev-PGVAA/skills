# Check if all phases in the active task_plan.md are complete
# Always exits 0 -- uses stdout for status reporting
# Used by Stop hook to report task completion status
#
# Plan resolution (mirror of resolve-plan-dir.sh):
#   1. Explicit -PlanFile argument, if given
#   2. $env:PLAN_ID -> ./.planning/<id>/
#   3. ./.planning/.active_plan
#   4. Newest ./.planning/<dir>/ containing task_plan.md
#   5. Legacy ./task_plan.md at project root

param(
    [string]$PlanFile = ""
)

if (-not $PlanFile) {
    $PlanFile = "task_plan.md"
    $PlanRoot = Join-Path (Get-Location) ".planning"
    $Candidate = $null

    if ($env:PLAN_ID -and (Test-Path (Join-Path $PlanRoot $env:PLAN_ID))) {
        $Candidate = Join-Path $PlanRoot $env:PLAN_ID
    } elseif (Test-Path (Join-Path $PlanRoot ".active_plan")) {
        $Id = (Get-Content (Join-Path $PlanRoot ".active_plan") -Raw).Trim()
        if ($Id -and (Test-Path (Join-Path $PlanRoot $Id))) {
            $Candidate = Join-Path $PlanRoot $Id
        }
    }

    if (-not $Candidate -and (Test-Path $PlanRoot)) {
        $Newest = Get-ChildItem $PlanRoot -Directory |
            Where-Object { Test-Path (Join-Path $_.FullName "task_plan.md") } |
            Sort-Object LastWriteTime -Descending |
            Select-Object -First 1
        if ($Newest) { $Candidate = $Newest.FullName }
    }

    if ($Candidate -and (Test-Path (Join-Path $Candidate "task_plan.md"))) {
        $PlanFile = Join-Path $Candidate "task_plan.md"
    }
}

if (-not (Test-Path $PlanFile)) {
    Write-Host '[planning-with-files] No task_plan.md found -- no active planning session.'
    exit 0
}

# Read file content
$content = Get-Content $PlanFile -Raw

# Count total phases
$TOTAL = ([regex]::Matches($content, "### Phase")).Count

# Check for **Status:** format first
$COMPLETE = ([regex]::Matches($content, "\*\*Status:\*\* complete")).Count
$IN_PROGRESS = ([regex]::Matches($content, "\*\*Status:\*\* in_progress")).Count
$PENDING = ([regex]::Matches($content, "\*\*Status:\*\* pending")).Count

# Fallback: check for [complete] inline format if **Status:** not found
if ($COMPLETE -eq 0 -and $IN_PROGRESS -eq 0 -and $PENDING -eq 0) {
    $COMPLETE = ([regex]::Matches($content, "\[complete\]")).Count
    $IN_PROGRESS = ([regex]::Matches($content, "\[in_progress\]")).Count
    $PENDING = ([regex]::Matches($content, "\[pending\]")).Count
}

# Report status -- always exit 0, incomplete task is a normal state
if ($COMPLETE -eq $TOTAL -and $TOTAL -gt 0) {
    Write-Host ('[planning-with-files] ALL PHASES COMPLETE (' + $COMPLETE + '/' + $TOTAL + '). If the user has additional work, add new phases to task_plan.md before starting.')
} else {
    Write-Host ('[planning-with-files] Task in progress (' + $COMPLETE + '/' + $TOTAL + ' phases complete). Update progress.md before stopping.')
    if ($IN_PROGRESS -gt 0) {
        Write-Host ('[planning-with-files] ' + $IN_PROGRESS + ' phase(s) still in progress.')
    }
    if ($PENDING -gt 0) {
        Write-Host ('[planning-with-files] ' + $PENDING + ' phase(s) pending.')
    }
}
exit 0
