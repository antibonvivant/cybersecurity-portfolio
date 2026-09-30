param(
    [Parameter(Mandatory=$true)][datetime]$Start,
    [Parameter(Mandatory=$true)][datetime]$End,
    [string]$OutDir = '.\evidence-private\windows-auth'
)
$ErrorActionPreference = 'Stop'
if ($End -le $Start) { throw 'End must be later than Start.' }
if (Test-Path $OutDir) { throw 'Choose a new output directory to preserve existing evidence.' }
New-Item -ItemType Directory -Path $OutDir | Out-Null
# Run on the lab host. Dates are interpreted by PowerShell; supply ISO timestamps with offsets.
$events = @(Get-WinEvent -FilterHashtable @{LogName='Security';Id=4624,4625;StartTime=$Start;EndTime=$End})
$rows = foreach ($ev in $events) {
    [xml]$xml = $ev.ToXml()
    $data = @{}
    foreach ($item in $xml.Event.EventData.Data) { $data[[string]$item.Name] = [string]$item.'#text' }
    $ev.ToXml() | Set-Content -Encoding UTF8 -Path (Join-Path $OutDir ('event-' + $ev.RecordId + '.xml'))
    [pscustomobject]@{
        TimeUTC=$ev.TimeCreated.ToUniversalTime().ToString('o'); EventID=$ev.Id; RecordID=$ev.RecordId
        Host=$ev.MachineName; TargetUser=$data['TargetUserName']; TargetDomain=$data['TargetDomainName']
        LogonType=$data['LogonType']; SourceIP=$data['IpAddress']; Workstation=$data['WorkstationName']
        Status=$data['Status']; SubStatus=$data['SubStatus']; ProcessName=$data['ProcessName']
    }
}
$rows | Sort-Object TimeUTC | Export-Csv -NoTypeInformation -Encoding UTF8 -Path (Join-Path $OutDir 'timeline.csv')
Get-ChildItem -Path $OutDir -File | Get-FileHash -Algorithm SHA256 |
    Select-Object Path,Hash | Export-Csv -NoTypeInformation -Encoding UTF8 -Path (Join-Path $OutDir 'hashes.csv')
Write-Output ('Exported ' + $events.Count + ' events. Review and sanitize before publication.')
